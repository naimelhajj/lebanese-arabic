# Home V2 CRO/SEO Report — Drive Organic Visitors to `/lebanese-lessons/` While Preserving Exploration

Date: 2025-11-09

Audience: Stakeholders, content, and implementation (Gutenberg/GTM) teams

Goal: Optimize `/home-v2/` to respectfully channel organic visitors from top queries toward `/lebanese-lessons/` and purchases, without harming the homepage’s exploration role or inquiry conversions.

Top Queries Context (from GSC)
- learn lebanese arabic — 230 clicks | 1,145 impressions | pos 1.9
- lebanese arabic lessons — 72 | 414 | pos 1.2
- learn lebanese — 42 | 264 | pos 2.1
- how to learn lebanese arabic — 35 | 372 | pos 2.8
- learning lebanese arabic — 26 | 183 | pos 2.1
- lebanese arabic course — 22 | 942 | pos 3.2


## Key Findings (Current Pages)

- Titles/H1s
  - `/home-v2/` HTML title reads “home-v2”; no clear H1 detected. This weakens query alignment and clarity.
  - Root homepage also lacks a clear, extractable H1.
- Messaging & Offer Signals
  - “Risk‑free”, “$15”, and “trial” are present across pages, which is good; however, the homepage doesn’t explicitly frame choices by user intent.
- CTAs to `/lebanese-lessons/`
  - `/home-v2/` has ~7 links to `/lebanese-lessons/` with mixed labels (Lessons, Online Classes, Book Trial, etc.). Inconsistent labels dilute clarity; too many similar CTAs can feel noisy.
- Exploration vs Purchase Balance
  - Exploration modules (free lessons) exist but lack soft, consistent hand‑offs to the spear page.


## Strategy Overview

- Align the homepage to searcher intent with an “intent router” design: one clear path to purchase, one clear path to explore.
- Keep the exploration experience prominent; do not bury or remove inquiry paths.
- Normalize the language that points to the spear page and reduce CTA label variety.
- Add compact trust/proof cues early for reassurance, not pressure.


## Proposed `/home-v2/` Structure and Order

1) Hero (Two‑Lane Choice)
- H1: “Learn Lebanese Arabic Online with a Native Teacher”
- Subhead: “Beginner foundations or advanced conversation. Start free—or try a $15 risk‑free trial.”
- Primary CTA: “Book Your $15 Trial” → `/lebanese-lessons/`
- Secondary CTA (link style): “Explore Free Lessons” → `/#popular-lessons`
- Micro‑reassurance: “Trial credited toward packages • Live 1:1 or small group”

2) Proof Snapshot (compact, above the fold)
- 2–3 chips you can support credibly, e.g.: “500+ learners”, “Native Lebanese teacher”, “4.9★ avg rating”.

3) Guided Pathways (Intent Router, 3 Cards)
- “I’m a complete beginner” → `/lebanese-lessons/` (anchor to beginner section if available)
- “I want conversation practice” → `/lebanese-lessons/` (anchor)
- “I’m exploring free lessons” → `/#popular-lessons`
- Each card includes a subtle inline text link: “Try a $15 risk‑free trial” → `/lebanese-lessons/`

4) Popular Free Lessons (Exploration Preserved)
- Feature 6–8 posts including Lesson 15, Lesson 1, and Lebanese Love Phrases.
- Each card: Title + “Learn” button; small footer micro‑link: “→ Try a $15 trial” → `/lebanese-lessons/`

5) How It Works (Short, Conversion‑Oriented)
- 1) Book $15 trial → 2) Meet your teacher live → 3) Pick a package (trial credited)
- Button: “Book Your $15 Trial” → `/lebanese-lessons/`

6) Pricing Snapshot (Skimmable, Not a Paywall)
- Show starting price and “trial credit applies” reassurance.
- Button: “See Packages & Book Trial” → `/lebanese-lessons/`

7) Testimonials (Faces + Quotes)
- 3–5 testimonials; keep it light and visual.
- Button: “Book Your $15 Trial” → `/lebanese-lessons/`

8) Safety Net
- “Not sure? Ask a question” → Inquiry/Contact (protect lead flow that currently works).


## Copy & SEO Alignment

- Page Title (replace “home‑v2”):
  - “Learn Lebanese Arabic Online | Native Teacher | $15 Risk‑Free Trial”
- Meta Description:
  - “Live online Lebanese Arabic lessons with a native teacher. Beginner foundations and advanced conversation. Start free or book a $15 risk‑free trial—credited toward packages.”
- H1:
  - “Learn Lebanese Arabic Online with a Native Teacher”
- Hero Subhead:
  - “Beginner or advanced—learn live, the practical way. Explore free lessons or try a $15 risk‑free trial.”

Why this fits top queries
- “learn lebanese arabic”, “learn lebanese”, “how to learn lebanese arabic”, “learning lebanese arabic”: H1 + subhead + Explore lane honor discovery intent without pushiness.
- “lebanese arabic lessons”, “lebanese arabic course”: primary CTA, pricing snapshot, and how‑it‑works offer a short credible path to the spear page.


## CTA Normalization

- Primary CTA (site‑wide for purchase intent): “Book Your $15 Trial” → `/lebanese-lessons/`
- Secondary CTA (exploration): “Explore Free Lessons” → `/#popular-lessons`
- Inline micro‑links: “Try a $15 risk‑free trial” → `/lebanese-lessons/`
- Avoid mixing “Lessons / Online Classes / Online Lessons” as spear labels; pick the two above to reduce cognitive load.


## Implementation Snippets (Gutenberg‑ready)

Hero (Two‑Lane)
```html
<section class="home-hero" style="text-align:center;padding:40px 16px;background:#f8f9fa;border:1px solid #dee2e6;border-radius:12px;">
  <h1 style="margin:0 0 8px;font-size:clamp(28px,5vw,40px);color:#0f172a;">Learn Lebanese Arabic Online with a Native Teacher</h1>
  <p style="margin:0 0 16px;color:#334155;font-size:18px;">
    Beginner foundations or advanced conversation. Start free—or try a <strong>$15 risk‑free trial</strong>.
  </p>
  <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
    <a href="/lebanese-lessons/" style="display:inline-block;background:#368D83;color:#fff;padding:12px 20px;border-radius:8px;font-weight:700;text-decoration:none;">Book Your $15 Trial</a>
    <a href="#popular-lessons" style="display:inline-block;color:#0f172a;padding:12px 16px;text-decoration:underline;">Explore Free Lessons</a>
  </div>
  <div style="margin-top:12px;color:#475569;font-size:14px;">Trial credited toward packages • Live 1:1 or small group</div>
  <div aria-hidden="true" style="margin-top:8px;color:#64748b;font-size:12px;">Secure checkout • Cancel anytime before your slot</div>
  <link rel="prefetch" href="/lebanese-lessons/" />
  <link rel="prerender" href="/lebanese-lessons/" />
  <script>try{var l=document.querySelector('a[href="/lebanese-lessons/"]');if(l){l.addEventListener('click',function(){window.dataLayer=window.dataLayer||[];dataLayer.push({event:'home_to_spear_click',section:'hero',link_text:'Book Your $15 Trial',position:1});});}}catch(e){}</script>
  <noscript><div style="font-size:12px;color:#64748b;">JavaScript is disabled; you can still <a href="/lebanese-lessons/">book your $15 trial here</a>.</div></noscript>
</section>
```

Popular Lessons Grid (footer micro‑link)
```html
<section id="popular-lessons" class="popular-lessons" style="padding:24px 0;">
  <!-- your existing cards here -->
  <div style="font-size:13px;margin-top:6px;color:#475569;">
    Not ready yet? <a href="/lebanese-lessons/" style="text-decoration:underline;color:#0f172a;">Try a $15 trial</a>
  </div>
</section>
```

How It Works (short)
```html
<section class="how-it-works" style="padding:24px 0;">
  <ol style="max-width:720px;margin:0 auto;color:#334155;line-height:1.6;">
    <li><strong>Book a $15 trial</strong> at a time that suits you.</li>
    <li><strong>Meet your teacher live</strong> for a tailored lesson.</li>
    <li><strong>Pick a package</strong>—your $15 is credited toward it.</li>
  </ol>
  <div style="text-align:center;margin-top:12px;">
    <a href="/lebanese-lessons/" style="display:inline-block;background:#368D83;color:#fff;padding:12px 20px;border-radius:8px;font-weight:700;text-decoration:none;">Book Your $15 Trial</a>
  </div>
</section>
```

Pricing Snapshot (skimmable)
```html
<section class="pricing-snapshot" style="padding:24px 0;">
  <div style="max-width:760px;margin:0 auto;text-align:center;color:#334155;">
    <p style="margin:0 0 8px;">Packages from <strong>$X/session</strong>. Your trial fee is <strong>credited</strong> if you continue.</p>
    <a href="/lebanese-lessons/" style="display:inline-block;background:#368D83;color:#fff;padding:12px 20px;border-radius:8px;font-weight:700;text-decoration:none;">See Packages &amp; Book Trial</a>
  </div>
</section>
```

Testimonials Strip (faces + quotes)
```html
<section class="testimonials-strip" style="padding:24px 0;background:#f8fafc;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0;">
  <!-- 3–5 testimonials; keep concise -->
  <div style="text-align:center;margin-top:12px;">
    <a href="/lebanese-lessons/" style="display:inline-block;background:#368D83;color:#fff;padding:12px 20px;border-radius:8px;font-weight:700;text-decoration:none;">Book Your $15 Trial</a>
  </div>
</section>
```


## Navigation and Footer

- Header nav: expose a single “Lessons” item → `/lebanese-lessons/` (don’t duplicate synonyms that fragment attention).
- Keep “Contact/Inquiry” visible to protect lead conversions.
- Footer: repeat the two primary links (“Book Trial”, “Explore Free Lessons”) + trust badges if available.


## Micro‑Tweaks That Pay Off

- Keep hero assets light to protect LCP; avoid heavy sliders.
- Use one button color (dark teal `#368D83`) for all primary CTAs.
- Only one primary button above the fold to avoid choice paralysis.
- Consider a subtle, dismissible mobile sticky bar after ~12s: “Book $15 Trial | Explore Free Lessons”.


## Tracking & Safety

- GA4 events on `/home-v2/`: `home_to_spear_click` with parameters `{link_text, section, position}`.
- Ensure purchase events carry `home_variant: 'v2'` (cookie or URL param) for attribution.
- Guardrail: monitor homepage “Lesson Inquiry” CVR; if it drops >10% vs 7‑day baseline, roll back hero changes first.


## Rationale Mapping to Queries

- Learn‑intents (“learn lebanese arabic”, “learn lebanese”, “how to learn lebanese arabic”, “learning lebanese arabic”):
  - H1 explicitly matches; Explore lane maintains discovery; soft micro‑links seed the trial option.
- Lesson/course‑intents (“lebanese arabic lessons”, “lebanese arabic course”):
  - Primary CTA + pricing snapshot + how‑it‑works offer a concise, credible route to `/lebanese-lessons/`.


## Rollout Notes

- Implement in Gutenberg using the snippets; reuse existing styles where possible.
- Do not remove existing inquiry paths; we’re adding, not replacing.
- After publishing, validate: LCP in PageSpeed, GA4 click events, and that all spear CTAs resolve to `/lebanese-lessons/`.
