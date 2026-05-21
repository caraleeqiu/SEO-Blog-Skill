#!/usr/bin/env python3
"""
Fetch a web page for SEO auditing.

Adapted from the claude-seo project (MIT). Keeps SSRF protection and
redirect tracking; trimmed to what the seo-audit-2026 skill needs.

Usage:
    python fetch_page.py https://example.com
    python fetch_page.py https://example.com --output page.html
"""

import argparse
import ipaddress
import socket
import sys
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("Error: requests required. Install with: pip install -r requirements.txt",
          file=sys.stderr)
    sys.exit(1)

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 SeoAudit2026/1.0"
)

HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
}


def _blocks_private_ip(hostname: str):
    """Return an error string if the hostname resolves to a private/internal IP."""
    try:
        resolved = socket.gethostbyname(hostname)
        ip = ipaddress.ip_address(resolved)
        if ip.is_private or ip.is_loopback or ip.is_reserved or ip.is_link_local:
            return f"Blocked: {hostname} resolves to a private/internal IP ({resolved})"
    except (socket.gaierror, ValueError, TypeError):
        return None  # DNS failures surface through requests below
    return None


def fetch_page(url: str, timeout: int = 30, max_redirects: int = 5) -> dict:
    """Fetch a URL and return {url, status_code, content, headers, redirect_chain, error}."""
    result = {
        "url": url, "status_code": None, "content": None,
        "headers": {}, "redirect_chain": [], "error": None,
    }

    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        result["error"] = f"Unsupported URL scheme: {parsed.scheme}"
        return result

    ssrf = _blocks_private_ip(parsed.hostname)
    if ssrf:
        result["error"] = ssrf
        return result

    try:
        session = requests.Session()
        session.max_redirects = max_redirects
        response = session.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        result["url"] = response.url
        result["status_code"] = response.status_code
        result["content"] = response.text
        result["headers"] = dict(response.headers)
        if response.history:
            result["redirect_chain"] = [
                {"url": r.url, "status_code": r.status_code} for r in response.history
            ]
    except requests.exceptions.Timeout:
        result["error"] = f"Request timed out after {timeout}s"
    except requests.exceptions.TooManyRedirects:
        result["error"] = f"Too many redirects (max {max_redirects})"
    except requests.exceptions.SSLError as e:
        result["error"] = f"SSL error: {e}"
    except requests.exceptions.ConnectionError as e:
        result["error"] = f"Connection error: {e}"
    except requests.exceptions.RequestException as e:
        result["error"] = f"Request failed: {e}"
    return result


def main():
    parser = argparse.ArgumentParser(description="Fetch a web page for SEO auditing")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--output", "-o", help="Write HTML to this file instead of stdout")
    parser.add_argument("--timeout", "-t", type=int, default=30, help="Timeout in seconds")
    args = parser.parse_args()

    result = fetch_page(args.url, timeout=args.timeout)
    if result["error"]:
        print(f"Error: {result['error']}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result["content"] or "")
        print(f"Saved to {args.output}", file=sys.stderr)
    else:
        print(result["content"])

    print(f"\nURL: {result['url']}", file=sys.stderr)
    print(f"Status: {result['status_code']}", file=sys.stderr)
    for hop in result["redirect_chain"]:
        print(f"  {hop['status_code']} -> {hop['url']}", file=sys.stderr)


if __name__ == "__main__":
    main()
