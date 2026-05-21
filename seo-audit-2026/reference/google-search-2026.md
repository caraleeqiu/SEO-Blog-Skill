# Google Search 2026 — Audit Rule Source

Condensed from the *Google Search Live 2026* memo. This is the rule source the
`seo-audit-2026` skill audits against. Each section maps to an audit category.

---

## 0. The core shift

Google's search system was not replaced by AI — it evolved on top of the same
pipeline (Crawling -> Indexing -> Serving). AI Overview / AI Mode add grounding,
reasoning, and query fanout at the serving layer.

The decisive change for content: **content written purely to satisfy ranking
algorithms loses its advantage.** Google explicitly rewards genuinely useful
content with real experience and a creator perspective.

---

## 1. Content quality — `content`

**Commodity vs Non-Commodity content** is the central distinction.

- Commodity (de-prioritized): generic, templated, "anyone could write it."
  - e.g. "Top 10 Things to Consider When Buying Running Shoes", "2024 Kitchen Trends"
- Non-Commodity (rewarded): writing only someone who actually did the work could produce.
  - e.g. "Why This Customer's Shoes Collapsed After 400 Miles"
  - e.g. "Why I Refused Marble Countertops for a Family of Five"

Rules:
- Flag titles that match commodity patterns ("Top N", "N Tips/Things/Ways",
  "Ultimate/Complete Guide", "<year> Trends") for manual review.
- Reward first-hand observation, real cases, specific decisions, depth.
- AI-assisted content is fine. Low-effort / commodity / fake-expertise AI content is not.
- Google does not penalize a whole site for a few low-quality or empty pages —
  it judges whether the site is *genuinely useful* overall. But a low-quality
  section acts as a "bad apple" and should be cut, not kept.

## 2. E-E-A-T & authenticity — `eeat`

E-E-A-T (Experience, Expertise, Authoritativeness, Trust) is not a single
ranking factor, but it is core to Google's quality evaluation. In AI Search,
**Experience (first-hand)** matters more than before.

Rules:
- An author / byline signal should be present.
- `datePublished` and `dateModified` (freshness) should be detectable.
- Quality dimensions Google names: effort, originality, talent/skill, accuracy.
- **Hard red line:** 100% AI content that *pretends* to be human experience —
  faking real cases, faking professional history — is "fake authenticity" and
  sharply lowers quality scores. Audit this as a manual judgment check.

## 3. Technical SEO — `technical`

Fundamentals still matter and must be audited continuously.

Rules:
- Title: 50-60 chars, includes the primary keyword, unique.
- Meta description: ~120-160 chars, compelling.
- Exactly one `<h1>`; sequential heading levels (no skipped levels).
- `canonical` present and correct — indexing deduplicates and keeps one
  canonical version, so duplicate / lightly-rewritten pages lose value.
- Return correct HTTP status codes; manage redesigns with 301 redirects.
- Crawl frequency depends on site speed, quality, and absence of server errors —
  technical stability is itself an SEO signal.
- New pages need internal links — orphan pages are discovered slowly or not at all.
- Do not obsess over link sculpting; improving actual content quality matters more.

## 4. Keyword & intent — `keyword`

Google understands whole sentences, context, and intent (BERT, RankBrain, MUM) —
not just keyword matches.

Rules:
- Primary keyword should appear in title, first ~100 words, at least one H2,
  meta description, and URL.
- Density is a loose guardrail (~1-3%); over-stuffing is a spam signal.
- Priority is semantic relevance, topical authority, and intent matching.

## 5. Structured data — `schema`

Structured data is the machine-readable layer that tells Google what a piece of
content *is*. It does not directly affect ranking and does not guarantee a rich
result, but it enables rich results and strengthens semantic completeness.

Rules:
- `Article` / `BlogPosting`: headline, author, datePublished, dateModified, image.
- `VideoObject` when a video is embedded (see section 7).
- `FAQPage` for FAQ sections — helps page understanding and context.
- Site Name, author identity, and source trust carry rising weight — Google
  Search increasingly behaves like a recommendation engine; brand matters.
- Keep schema fields consistent with the visible content and maintain them.

## 6. Image SEO — `images`

Search is becoming multi-modal; image SEO weight is rising.

Rules:
- Use `<img>` or `<picture>`. Images referenced **only** via CSS
  `background-image` cannot be reliably indexed.
- `<picture>` must contain an `<img>` fallback.
- `alt` is an important signal — clear, accurate, descriptive.
- `title` attribute is weak — far less weight than `alt`.
- Surrounding text / captions help Google understand the image.
- Prefer AVIF / WebP (best quality/compression/performance balance).
- Set width/height to prevent layout shift.
- Provide an Image Sitemap for large or JS-loaded image sets.

## 7. Video SEO — `video`

Video is increasingly integrated into Search; logic resembles YouTube SEO.

Rules:
- Video should be on a dedicated watch page (own URL, title, description, metadata).
- Video must be clearly visible — not hidden embeds, not buried low on the page.
- Surrounding descriptive text helps indexing.
- `VideoObject` JSON-LD: name, description, thumbnailUrl, uploadDate, duration.
  - `duration` must be ISO 8601 (e.g. `PT2M15S`).
  - `contentUrl` (real file) and `embedUrl` should be correct.
- Thumbnail quality drives CTR and snippet display.
- Provide a Video Sitemap — embedded videos especially depend on it.
- Recommended format: MP4 + H.264.

## 8. Internationalization — `intl`

Applies to multilingual sites only.

Rules:
- Each language version on its own URL; subdirectory (`example.com/ja/`) preferred.
- `hreflang` with bidirectional return links — EN points to JA *and* JA back to EN.
- Correct language/region codes (en-US, en-GB, zh-CN, zh-TW).
- Specify language *and* region (same language, different region = different intent).
- Google determines page language mainly from visible content, not just hreflang.
- Localization is not translation — machine-translated SEO pages lose value.

## 9. Spam signals — `spam`

Explicit spam Google actively targets:

- Cloaking
- Doorway pages
- Scraped content (especially sensitive in the AI era — rewrites, AI aggregation,
  reposts with no added value)
- Link spam
- Hacked content

---

## Severity mapping

| Severity  | Meaning                                              |
|-----------|------------------------------------------------------|
| critical  | Blocks indexing or risks a penalty — fix immediately |
| high      | Significantly impacts rankings — fix within 1 week   |
| medium    | Optimization opportunity — fix within 1 month        |
| low       | Nice to have — backlog                               |
| pass      | Check satisfied                                      |

## Judgment-only checks (not automatable — Claude must assess)

- Commodity vs non-commodity: does the article carry real, differentiated experience?
- Fake authenticity: does AI-written content pretend to be lived human experience?
- Real-experience evidence: are examples / tips / mistakes backed by real results?
- Intent match: does the page format match the searcher's intent?
