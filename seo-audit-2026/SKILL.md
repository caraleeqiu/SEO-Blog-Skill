---
name: seo-audit-2026
description: >
  Audit a page or blog article against Google Search 2026 standards (from the
  Google Search Live 2026 memo): non-commodity content, real-experience E-E-A-T,
  structured data, image SEO, video SEO, internationalization, and anti-spam
  signals. Runs an automated checker and outputs a scored, prioritized issue
  list with concrete fixes. Use when the user says audit, SEO check, check this
  page/article, score this content, or provides a URL or HTML file to review.
user-invokable: true
argument-hint: "[url or html-file] [--keyword \"...\"]"
license: MIT
metadata:
  version: "1.0.0"
  category: seo
  source: "Google Search Live 2026 MEMO"
  base: "structure adapted from github.com/AgriciDaniel/claude-seo (MIT)"
---

# SEO Audit 2026

Audit a single page or blog article against Google's 2026 search direction and
return a scored report with prioritized, actionable fixes.

The rule source is `reference/google-search-2026.md` — a condensed, audit-ready
version of the *Google Search Live 2026* memo. Read it before judging the
manual-review items.

## When to use

The user provides a URL or a local HTML file and wants to know whether the
content will hold up under 2026 Google Search — or asks to "audit", "SEO check",
or "score" a page/article.

## Process

1. **Get the input.** A URL, or a local HTML file path. For a file, ask for the
   canonical URL too (`--url`) so URL-based checks run.
2. **Run the automated audit:**
   ```
   pip install -r requirements.txt          # first run only
   python scripts/audit.py <url-or-file> --keyword "<primary keyword>" --format md
   ```
   - `--keyword` enables keyword placement + density checks (skip if unknown).
   - `--type how-to|model-launch|article|page` sharpens schema recommendations.
   - `--format json` for machine-readable output; `--format md` for a report.
3. **Do the judgment-only checks** the script cannot automate — it emits these
   as `[REVIEW]` findings. Read the page content and assess each against
   `reference/google-search-2026.md`:
   - **Commodity vs non-commodity** — does the article carry real, differentiated
     first-hand experience, or is it generic "anyone could write it" content?
   - **Fake authenticity** — does AI-written content pretend to be lived human
     experience (fake cases, fake expertise)? This is a hard red line.
   - **Real-experience evidence** — are examples / tips / mistakes backed by real
     results (screenshots, real prompts, real data)?
   - **Intent match** — does the page format match the searcher's intent?
4. **Merge** the automated findings and your judgment calls into one report.
5. **Present** the scored report and offer to fix the top issues.

## What gets checked

| Category | Automated | Judgment |
|----------|-----------|----------|
| Content Differentiation | thin content, commodity-title patterns | commodity vs non-commodity, real experience |
| E-E-A-T & Authenticity | author signal, publish/update dates | fake authenticity red line |
| Technical SEO | title, meta, H1, heading hierarchy, canonical, robots | — |
| Keyword & Intent | placement (5 spots), density / stuffing | intent match |
| Structured Data | Article/VideoObject/FAQPage/HowTo presence + fields | — |
| Image SEO | alt text, format, dimensions, CSS-background usage | — |
| Video SEO | VideoObject, ISO 8601 duration, thumbnail | watch page, visibility |
| Internationalization | hreflang codes | bidirectional return links |
| Spam Signals | doorway-like pattern | scraped / rewritten content |

## Scoring

Each category is `100 - penalties` (critical -25, high -15, medium -8, low -3),
floored at 0. The overall score is a weighted average over the categories that
apply (keyword, video, and internationalization are scored only when relevant):

| Category | Weight |
|----------|--------|
| Content Differentiation | 20% |
| Technical SEO | 16% |
| E-E-A-T & Authenticity | 14% |
| Structured Data | 14% |
| Keyword & Intent | 10% |
| Image SEO | 10% |
| Video SEO | 10% |
| Internationalization | 3% |
| Spam Signals | 3% |

## Priority definitions

- **Critical** — blocks indexing or risks a penalty. Fix immediately.
- **High** — significantly impacts rankings. Fix within 1 week.
- **Medium** — optimization opportunity. Fix within 1 month.
- **Low** — nice to have. Backlog.
- **Review** — manual judgment required; not automatable.

## Output

Present, in this order:

1. **Score line** — overall score + finding counts by severity.
2. **Category table** — per-category score.
3. **Findings** — grouped by category, ordered Critical -> High -> Medium ->
   Low -> Review, each with a concrete fix.
4. **Top fixes** — the 3-5 highest-impact actions.

Then offer to apply the fixes.

## Error handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS, connection refused) | Report the error. Do not guess page content. Ask the user to verify the URL. |
| Page requires authentication (401/403) | Report it. Ask for the rendered HTML or a public URL. |
| JavaScript-rendered page (near-empty HTML) | Note that content may be client-side rendered; results may be incomplete. Suggest providing a rendered HTML snapshot. |
| Dependencies missing | Run `pip install -r requirements.txt`. |
| HTTP >= 400 | `audit.py` exits with the status code; report it and stop. |

## Notes

- The audit reads raw HTML — it cannot measure Core Web Vitals or verify
  cross-page signals (hreflang return links, site-wide duplication). It flags
  these for manual follow-up.
- This skill is standalone. It does not modify or depend on the Drama.Land
  blog generator in `skill.md`.
