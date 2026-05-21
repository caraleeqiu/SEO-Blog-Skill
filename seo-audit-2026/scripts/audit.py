#!/usr/bin/env python3
"""
Audit a page or blog article against Google Search 2026 standards.

Encodes the automatable rules from reference/google-search-2026.md:
technical SEO, keyword placement, structured data, image SEO, video SEO,
internationalization, and spam signals — plus heuristic flags for
commodity content and E-E-A-T signals.

Judgment-only checks (commodity vs non-commodity, fake authenticity) are
left to the skill's caller; this script flags candidates for review.

Usage:
    python audit.py https://example.com/blog/post
    python audit.py page.html --url https://example.com/blog/post
    python audit.py https://example.com/post --keyword "ai music video"
    python audit.py https://example.com/post --type how-to --format md
"""

import argparse
import json
import os
import re
import sys
from urllib.parse import urlparse

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 required. Install with: pip install -r requirements.txt",
          file=sys.stderr)
    sys.exit(1)

try:
    import lxml  # noqa: F401
    _PARSER = "lxml"
except ImportError:
    _PARSER = "html.parser"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

WEIGHTS = {
    "content":   0.20,
    "eeat":      0.14,
    "technical": 0.16,
    "keyword":   0.10,
    "schema":    0.14,
    "images":    0.10,
    "video":     0.10,
    "intl":      0.03,
    "spam":      0.03,
}

CATEGORY_LABELS = {
    "content":   "Content Differentiation",
    "eeat":      "E-E-A-T & Authenticity",
    "technical": "Technical SEO",
    "keyword":   "Keyword & Intent",
    "schema":    "Structured Data",
    "images":    "Image SEO",
    "video":     "Video SEO",
    "intl":      "Internationalization",
    "spam":      "Spam Signals",
}

SEVERITY_PENALTY = {"critical": 25, "high": 15, "medium": 8, "low": 3, "pass": 0, "info": 0}
SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4, "pass": 5}

ISO8601_DURATION = re.compile(
    r"^P(?!$)(?:\d+Y)?(?:\d+M)?(?:\d+W)?(?:\d+D)?(?:T(?!$)(?:\d+H)?(?:\d+M)?(?:\d+S)?)?$"
)
HREFLANG_CODE = re.compile(r"^(x-default|[a-z]{2,3}(-[A-Za-z]{2,4})?)$")

COMMODITY_PATTERNS = [
    r"\btop\s+\d+\b",
    r"\b\d+\s+(tips|things|ways|reasons|ideas|tricks|hacks|mistakes|steps)\b",
    r"\bultimate guide\b",
    r"\bcomplete guide\b",
    r"\beverything you need to know\b",
    r"\b(19|20)\d{2}\s+trends\b",
    r"\bbest\s+\d+\b",
]

GOOD_IMAGE_FORMATS = {"webp", "avif"}
LEGACY_IMAGE_FORMATS = {"jpg", "jpeg", "png"}
ARTICLE_TYPES = {"Article", "BlogPosting", "NewsArticle", "TechArticle"}
THIN_CONTENT_WORDS = 600

# --------------------------------------------------------------------------
# HTML extraction helpers
# --------------------------------------------------------------------------


def visible_word_count(html: str) -> int:
    soup = BeautifulSoup(html, _PARSER)
    for el in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        el.decompose()
    text = soup.get_text(separator=" ", strip=True)
    return len(re.findall(r"\b\w+\b", text))


def visible_text(html: str) -> str:
    soup = BeautifulSoup(html, _PARSER)
    for el in soup(["script", "style", "noscript"]):
        el.decompose()
    return soup.get_text(separator=" ", strip=True)


def extract_schema(soup) -> list:
    items = []
    for tag in soup.find_all("script", type="application/ld+json"):
        raw = tag.string or tag.get_text()
        if not raw:
            continue
        try:
            data = json.loads(raw)
        except (json.JSONDecodeError, TypeError, ValueError):
            continue
        for candidate in (data if isinstance(data, list) else [data]):
            if not isinstance(candidate, dict):
                continue
            if "@graph" in candidate and isinstance(candidate["@graph"], list):
                items.extend(x for x in candidate["@graph"] if isinstance(x, dict))
            else:
                items.append(candidate)
    return items


def schema_types(items) -> list:
    types = []
    for item in items:
        t = item.get("@type")
        if isinstance(t, list):
            types.extend(str(x) for x in t)
        elif t:
            types.append(str(t))
    return types


def find_schema(items, wanted: set):
    for item in items:
        t = item.get("@type")
        names = t if isinstance(t, list) else [t]
        if any(str(n) in wanted for n in names):
            return item
    return None


def extension_of(src: str) -> str:
    path = urlparse(src or "").path.lower()
    match = re.search(r"\.([a-z0-9]+)$", path)
    return match.group(1) if match else ""


def has_embedded_video(soup) -> bool:
    if soup.find("video"):
        return True
    for iframe in soup.find_all("iframe"):
        src = (iframe.get("src") or "").lower()
        if any(d in src for d in ("youtube.com/embed", "youtu.be",
                                  "youtube-nocookie.com", "player.vimeo.com")):
            return True
    return False


# --------------------------------------------------------------------------
# Audit
# --------------------------------------------------------------------------


def audit(html: str, url: str = None, keyword: str = None, page_type: str = None) -> dict:
    soup = BeautifulSoup(html, _PARSER)
    findings = []

    def add(category, check, severity, message, recommendation=""):
        findings.append({
            "category": category, "check": check, "severity": severity,
            "message": message, "recommendation": recommendation,
        })

    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    word_count = visible_word_count(html)
    schema_items = extract_schema(soup)
    s_types = schema_types(schema_items)
    video_present = has_embedded_video(soup)

    # ---- Technical SEO ----------------------------------------------------
    title = soup.title.get_text(strip=True) if soup.title else None
    if not title:
        add("technical", "title", "critical", "Missing <title> tag",
            "Add a unique 50-60 character title containing the primary keyword.")
    else:
        n = len(title)
        if n < 30:
            add("technical", "title", "high", f"Title too short ({n} chars): \"{title}\"",
                "Expand to 50-60 characters.")
        elif n > 65:
            add("technical", "title", "medium", f"Title long ({n} chars), may truncate in SERP",
                "Trim to 50-60 characters.")
        else:
            add("technical", "title", "pass", f"Title length OK ({n} chars)")

    desc_tag = soup.find("meta", attrs={"name": "description"})
    description = desc_tag.get("content", "").strip() if desc_tag else None
    if not description:
        add("technical", "meta-description", "high", "Missing meta description",
            "Add a compelling 120-160 character meta description.")
    else:
        n = len(description)
        if n < 80:
            add("technical", "meta-description", "medium", f"Meta description short ({n} chars)",
                "Expand to 120-160 characters.")
        elif n > 170:
            add("technical", "meta-description", "low", f"Meta description long ({n} chars)",
                "Trim to 120-160 characters to avoid truncation.")
        else:
            add("technical", "meta-description", "pass", f"Meta description length OK ({n} chars)")

    h1_count = sum(1 for h in headings if h.name == "h1")
    if h1_count == 0:
        add("technical", "h1", "high", "No <h1> on the page",
            "Add exactly one <h1> describing page intent.")
    elif h1_count > 1:
        add("technical", "h1", "medium", f"{h1_count} <h1> tags found",
            "Use exactly one <h1> per page.")
    else:
        add("technical", "h1", "pass", "Exactly one <h1>")

    levels = [int(h.name[1]) for h in headings]
    skipped = any(
        levels[i] > levels[i - 1] + 1 for i in range(1, len(levels))
    )
    if skipped:
        add("technical", "heading-hierarchy", "low",
            "Heading levels skip (e.g. H2 -> H4)",
            "Use sequential heading levels for a clear outline.")
    elif levels:
        add("technical", "heading-hierarchy", "pass", "Heading hierarchy is sequential")

    canonical = soup.find("link", rel="canonical")
    if not canonical or not canonical.get("href"):
        add("technical", "canonical", "medium", "No canonical link",
            "Add a self-referencing <link rel=\"canonical\"> to prevent duplicate-content "
            "deduplication from picking the wrong page.")
    else:
        add("technical", "canonical", "pass", f"Canonical set: {canonical.get('href')}")

    robots = soup.find("meta", attrs={"name": "robots"})
    if robots and "noindex" in robots.get("content", "").lower():
        add("technical", "robots", "critical", "Page is set to noindex",
            "Remove noindex if this page should rank.")

    # ---- Content differentiation -----------------------------------------
    if word_count < THIN_CONTENT_WORDS:
        add("content", "word-count", "high",
            f"Thin content: only {word_count} visible words",
            f"Aim well above {THIN_CONTENT_WORDS} words with substantive, original material.")
    else:
        add("content", "word-count", "pass", f"Word count OK ({word_count} words)")

    if title:
        hits = [p for p in COMMODITY_PATTERNS if re.search(p, title, re.I)]
        if hits:
            add("content", "commodity-title", "medium",
                f"Title matches a commodity-content pattern: \"{title}\"",
                "Google de-prioritizes generic 'anyone could write it' content. "
                "Rewrite around first-hand experience or a differentiated angle, "
                "then judge the body the same way (manual review).")
        else:
            add("content", "commodity-title", "pass",
                "Title does not match common commodity patterns")
    add("content", "differentiation", "info",
        "Manual review: does the article carry real, differentiated first-hand "
        "experience, or is it generic commodity content?",
        "See reference/google-search-2026.md section 1.")

    # ---- E-E-A-T ----------------------------------------------------------
    author_schema = any(item.get("author") for item in schema_items)
    author_meta = soup.find("meta", attrs={"name": "author"})
    author_markup = soup.find(attrs={"rel": "author"}) or soup.find(
        class_=re.compile(r"author|byline", re.I))
    if author_schema or author_meta or author_markup:
        add("eeat", "author", "pass", "Author / byline signal present")
    else:
        add("eeat", "author", "medium", "No author or byline signal found",
            "Add an author with visible credentials (and schema author).")

    article = find_schema(schema_items, ARTICLE_TYPES)
    has_dates = bool(
        (article and (article.get("datePublished") or article.get("dateModified")))
        or soup.find("meta", attrs={"property": "article:published_time"})
        or soup.find("meta", attrs={"property": "article:modified_time"})
        or soup.find("time")
    )
    if has_dates:
        add("eeat", "freshness", "pass", "Publish/update date signal present")
    else:
        add("eeat", "freshness", "low", "No publish/update date detected",
            "Expose datePublished and dateModified for freshness signals.")
    add("eeat", "authenticity", "info",
        "Manual review: AI-assisted content is fine, but content that fakes "
        "lived human experience (fake cases, fake expertise) is a hard red line.",
        "See reference/google-search-2026.md section 2.")

    # ---- Keyword & intent (only when --keyword is given) ------------------
    if keyword:
        kw = keyword.lower().strip()
        text_lower = visible_text(html).lower()
        in_title = bool(title) and kw in title.lower()
        in_desc = bool(description) and kw in description.lower()
        first_100 = " ".join(text_lower.split()[:100])
        in_intro = kw in first_100
        in_h2 = any(kw in h.get_text(" ", strip=True).lower()
                    for h in headings if h.name == "h2")
        in_url = bool(url) and kw.replace(" ", "-") in (url or "").lower()

        placed = sum([in_title, in_desc, in_intro, in_h2, in_url])
        missing = [name for name, ok in [
            ("title", in_title), ("meta description", in_desc),
            ("intro", in_intro), ("an H2", in_h2), ("URL", in_url)] if not ok]
        if placed >= 4:
            add("keyword", "placement", "pass",
                f"Primary keyword placed in {placed}/5 key locations")
        else:
            add("keyword", "placement", "medium",
                f"Primary keyword missing from: {', '.join(missing)}",
                "Place the primary keyword in title, intro, an H2, meta description, and URL.")

        occurrences = len(re.findall(re.escape(kw), text_lower))
        density = (occurrences / word_count * 100) if word_count else 0
        if density > 3.5:
            add("keyword", "density", "high",
                f"Possible keyword stuffing ({density:.1f}% density, {occurrences}x)",
                "Reduce repetition; rely on semantic variations and intent matching.")
        else:
            add("keyword", "density", "pass",
                f"Keyword density OK ({density:.1f}%)")

    # ---- Structured data --------------------------------------------------
    if not schema_items:
        add("schema", "presence", "high", "No JSON-LD structured data found",
            "Add Article/BlogPosting schema at minimum.")
    else:
        add("schema", "presence", "pass",
            f"Structured data present: {', '.join(sorted(set(s_types))) or 'unknown types'}")

        if article:
            required = ["headline", "author", "datePublished", "dateModified", "image"]
            missing = [f for f in required if not article.get(f)]
            if missing:
                add("schema", "article", "medium",
                    f"Article schema missing fields: {', '.join(missing)}",
                    "Populate all core Article fields and keep them consistent with the page.")
            else:
                add("schema", "article", "pass", "Article schema has all core fields")
        else:
            add("schema", "article", "medium", "No Article/BlogPosting schema",
                "Add Article or BlogPosting JSON-LD.")

    faq_present = any(
        re.search(r"\bfaq\b|frequently asked", h.get_text(" ", strip=True), re.I)
        for h in headings
    )
    if faq_present and "FAQPage" not in s_types:
        add("schema", "faqpage", "low", "FAQ section present but no FAQPage schema",
            "Add FAQPage schema — it strengthens semantic completeness and context.")

    is_howto = (page_type == "how-to") or (bool(title) and title.lower().startswith("how to"))
    if is_howto and "HowTo" not in s_types:
        add("schema", "howto", "low", "How-to content but no HowTo schema",
            "Add HowTo schema mapping each tutorial step.")

    # ---- Image SEO --------------------------------------------------------
    images = soup.find_all("img")
    if not images:
        add("images", "presence", "low", "No <img> elements found",
            "Search is multi-modal — add relevant, indexable images.")
    else:
        missing_alt = [i for i in images if not (i.get("alt") or "").strip()]
        if missing_alt:
            add("images", "alt", "high",
                f"{len(missing_alt)}/{len(images)} images missing alt text",
                "Add clear, accurate, descriptive alt text to every image.")
        else:
            add("images", "alt", "pass", f"All {len(images)} images have alt text")

        legacy = [i for i in images
                  if extension_of(i.get("src", "")) in LEGACY_IMAGE_FORMATS]
        if legacy:
            add("images", "format", "low",
                f"{len(legacy)} image(s) use legacy JPEG/PNG",
                "Prefer AVIF/WebP for better quality/compression/performance.")
        else:
            add("images", "format", "pass", "No legacy raster formats detected")

        no_dims = [i for i in images if not (i.get("width") and i.get("height"))]
        if no_dims:
            add("images", "dimensions", "low",
                f"{len(no_dims)}/{len(images)} images missing width/height",
                "Set width and height to prevent layout shift (CLS).")

    bg_count = sum(
        1 for el in soup.find_all(style=True)
        if "background-image" in (el.get("style") or "").lower()
    )
    for style_tag in soup.find_all("style"):
        if style_tag.string:
            bg_count += len(re.findall(r"background-image", style_tag.string, re.I))
    if bg_count:
        add("images", "css-background", "medium",
            f"{bg_count} CSS background-image reference(s) detected",
            "Content images set only via CSS background-image cannot be reliably "
            "indexed. Use <img> or <picture> for images that should rank.")

    # ---- Video SEO (only when a video is embedded) -----------------------
    if video_present:
        video_schema = find_schema(schema_items, {"VideoObject"})
        if not video_schema:
            add("video", "schema", "high",
                "Video embedded but no VideoObject schema",
                "Add VideoObject JSON-LD: name, description, thumbnailUrl, "
                "uploadDate, duration.")
        else:
            required = ["name", "description", "thumbnailUrl", "uploadDate"]
            missing = [f for f in required if not video_schema.get(f)]
            if missing:
                add("video", "schema", "medium",
                    f"VideoObject missing fields: {', '.join(missing)}",
                    "Populate all core VideoObject fields.")
            else:
                add("video", "schema", "pass", "VideoObject has core fields")

            duration = video_schema.get("duration")
            if duration and not ISO8601_DURATION.match(str(duration)):
                add("video", "duration", "medium",
                    f"VideoObject duration not ISO 8601: \"{duration}\"",
                    "Use ISO 8601, e.g. PT2M15S for 2 min 15 sec.")
            elif duration:
                add("video", "duration", "pass", "VideoObject duration is ISO 8601")

            if not video_schema.get("thumbnailUrl"):
                add("video", "thumbnail", "medium", "VideoObject has no thumbnailUrl",
                    "Add a high-quality thumbnail — it drives CTR.")

    # ---- Internationalization (only when hreflang exists) ----------------
    hreflang_links = [
        l for l in soup.find_all("link", rel="alternate") if l.get("hreflang")
    ]
    if hreflang_links:
        bad = [l.get("hreflang") for l in hreflang_links
               if not HREFLANG_CODE.match(l.get("hreflang", ""))]
        if bad:
            add("intl", "hreflang-codes", "medium",
                f"Invalid hreflang code(s): {', '.join(bad)}",
                "Use valid language/region codes, e.g. en-US, zh-CN, or x-default.")
        else:
            add("intl", "hreflang-codes", "pass",
                f"{len(hreflang_links)} hreflang link(s), codes valid")
        add("intl", "hreflang-return", "info",
            "Manual check: hreflang return links must be bidirectional — every "
            "alternate must point back. Not verifiable from a single page.")

    # ---- Spam signals -----------------------------------------------------
    if url:
        internal = external = 0
        host = urlparse(url).netloc
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("#") or href.startswith("javascript:"):
                continue
            netloc = urlparse(href).netloc
            if netloc and netloc != host:
                external += 1
            else:
                internal += 1
        if word_count < 300 and external > 20:
            add("spam", "doorway", "high",
                f"Doorway-like pattern: {word_count} words, {external} external links",
                "Thin pages with many outbound links resemble doorway pages.")
        else:
            add("spam", "doorway", "pass", "No doorway-like pattern detected")
    add("spam", "originality", "info",
        "Manual check: scraped / lightly-rewritten / AI-aggregated content with no "
        "added value is explicit spam in the AI era.")

    # ---- Scoring ----------------------------------------------------------
    cat_findings = {}
    for f in findings:
        cat_findings.setdefault(f["category"], []).append(f)

    category_scores = {}
    for cat, fs in cat_findings.items():
        penalty = sum(SEVERITY_PENALTY.get(f["severity"], 0) for f in fs)
        category_scores[cat] = max(0, 100 - penalty)

    applicable = {c: WEIGHTS[c] for c in category_scores if c in WEIGHTS}
    total_weight = sum(applicable.values()) or 1
    overall = round(
        sum(category_scores[c] * w for c, w in applicable.items()) / total_weight
    )

    summary = {sev: 0 for sev in SEVERITY_PENALTY}
    for f in findings:
        summary[f["severity"]] = summary.get(f["severity"], 0) + 1

    return {
        "url": url,
        "overall_score": overall,
        "word_count": word_count,
        "categories": {
            cat: {
                "label": CATEGORY_LABELS.get(cat, cat),
                "score": category_scores[cat],
                "weight": WEIGHTS.get(cat),
                "findings": sorted(
                    fs, key=lambda f: SEVERITY_ORDER.get(f["severity"], 9)),
            }
            for cat, fs in cat_findings.items()
        },
        "summary": summary,
    }


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

_SEV_TAG = {
    "critical": "[CRITICAL]", "high": "[HIGH]", "medium": "[MEDIUM]",
    "low": "[LOW]", "info": "[REVIEW]", "pass": "[OK]",
}


def to_markdown(report: dict) -> str:
    lines = []
    lines.append("# SEO Audit 2026 — Report")
    lines.append("")
    if report.get("url"):
        lines.append(f"**URL:** {report['url']}")
    lines.append(f"**Overall score:** {report['overall_score']}/100")
    lines.append(f"**Visible words:** {report['word_count']}")
    s = report["summary"]
    lines.append(
        f"**Findings:** {s.get('critical',0)} critical · {s.get('high',0)} high · "
        f"{s.get('medium',0)} medium · {s.get('low',0)} low · "
        f"{s.get('info',0)} manual-review · {s.get('pass',0)} passed"
    )
    lines.append("")
    lines.append("## Category scores")
    lines.append("")
    lines.append("| Category | Score | Weight |")
    lines.append("|----------|-------|--------|")
    for cat, data in report["categories"].items():
        weight = f"{int(data['weight']*100)}%" if data.get("weight") else "-"
        lines.append(f"| {data['label']} | {data['score']}/100 | {weight} |")
    lines.append("")
    lines.append("## Findings")
    for cat, data in report["categories"].items():
        actionable = [f for f in data["findings"] if f["severity"] != "pass"]
        if not actionable:
            continue
        lines.append("")
        lines.append(f"### {data['label']} — {data['score']}/100")
        for f in actionable:
            lines.append(f"- {_SEV_TAG.get(f['severity'],'')} **{f['check']}** — {f['message']}")
            if f.get("recommendation"):
                lines.append(f"  - Fix: {f['recommendation']}")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Audit a page/article against Google Search 2026 standards")
    parser.add_argument("target", help="URL to fetch, or path to a local HTML file")
    parser.add_argument("--url", help="Canonical URL (when target is a local file)")
    parser.add_argument("--keyword", help="Primary keyword to check placement/density")
    parser.add_argument("--type", dest="page_type",
                        choices=["article", "how-to", "model-launch", "page"],
                        help="Page type hint (improves schema recommendations)")
    parser.add_argument("--format", choices=["json", "md"], default="json",
                        help="Output format (default: json)")
    args = parser.parse_args()

    url = args.url
    if os.path.isfile(args.target):
        with open(os.path.realpath(args.target), "r", encoding="utf-8") as f:
            html = f.read()
    else:
        try:
            from fetch_page import fetch_page
        except ImportError:
            print("Error: fetch_page.py must sit next to audit.py", file=sys.stderr)
            sys.exit(1)
        result = fetch_page(args.target)
        if result["error"]:
            print(f"Error fetching {args.target}: {result['error']}", file=sys.stderr)
            sys.exit(1)
        if result["status_code"] and result["status_code"] >= 400:
            print(f"Error: {args.target} returned HTTP {result['status_code']}",
                  file=sys.stderr)
            sys.exit(1)
        html = result["content"] or ""
        url = url or result["url"]

    report = audit(html, url=url, keyword=args.keyword, page_type=args.page_type)

    if args.format == "md":
        print(to_markdown(report))
    else:
        print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
