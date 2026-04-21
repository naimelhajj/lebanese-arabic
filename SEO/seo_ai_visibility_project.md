# SEO and AI Visibility Project

## Purpose
This project exists to improve the organic SEO performance of `lebanese-arabic.com` and increase the site's AI search visibility, especially as tracked in Ubersuggest AI Visibility reports.

The goal is not only to improve rankings in traditional search, but also to improve the likelihood that the brand and pages are surfaced in AI-generated recommendations, answer engines, and prompt-based discovery systems.

This project should use real exported data as its source of truth. At the moment, the core datasets are:

- Google Search Console exports under [`site-health/gsc/`](C:\Development\lebanese-arabic\SEO\site-health\gsc)
- Ubersuggest exports under [`ubersuggest/exports/`](C:\Development\lebanese-arabic\SEO\ubersuggest\exports)
- Ubersuggest AI Visibility exports under [`ubersuggest-ai-visibility/`](C:\Development\lebanese-arabic\SEO\ubersuggest-ai-visibility)
- Local page source snapshots under [`pages/`](C:\Development\lebanese-arabic\SEO\pages)

Later, free exports from Semrush and Ahrefs will also be added and should be treated as additional evidence sources, not replacements. Future work should incorporate those exports into the same decision framework.

## Operating Goal
All SEO work should be prioritized according to this order:

1. Fix technical issues that block crawling, indexing, canonicals, or redirects.
2. Improve pages that are already close to ranking better or already have clear demand.
3. Improve page-to-intent alignment so each important keyword cluster has one clear best page.
4. Improve AI visibility by making entity, offer, and topical relevance more explicit on the best matching pages.
5. Expand content only when existing pages cannot realistically satisfy the query intent.

## Current Data-Driven View
### What Ubersuggest currently suggests
- The site already has many tracked keywords in strong positions.
- The best near-term SEO opportunities are mostly near-win rankings, not major technical emergencies.
- AI Visibility currently rewards explicit, commercial-intent language on the right pages.
- Competitor data suggests strong opportunity in educational/reference content, but that should come after higher-confidence page upgrades.

### Latest AI Visibility Snapshot (April 11, 2026 export)
- Source folder reviewed: [`ubersuggest-ai-visibility/11-04-2026/`](C:\Development\lebanese-arabic\SEO\ubersuggest-ai-visibility\11-04-2026)
- Brand-level movement:
  - `Lebanese Arabic with Hiba` improved from `Visibility 10` to `Visibility 25`
  - mentions increased from `2` to `5`
  - average rank improved from `4.0` to `3.2`
- Prompt-level status:
  - visible in 3 prompts (`beginners`, `group classes`, `immersive experiences`)
  - zero visibility in 7 prompts
- Most important zero-visibility prompts that match current offer:
  - live tutoring with native speakers
  - private lessons tailored to adults
  - flexible scheduling for lessons
  - lessons with cultural context
- Offer-fit rule:
  - prioritize prompts that match existing services first
  - avoid overclaiming on prompts like `certified programs`, `apps`, or `subscription services` unless the offer actually exists

### Highest-value current workstreams
- Preserve and improve the service/commercial page at [`/lebanese-lessons/`](https://lebanese-arabic.com/lebanese-lessons/) for tutoring and booking prompts.
- Improve near-win tracked lesson pages that already rank on page 1 but not yet in the top 3.
- Reduce page-intent ambiguity between similar pages so Google and AI systems have one obvious canonical answer page per topic.

## Current Page-Intent Map
This is the working canonical map for the most important currently identified topics.

### Commercial and AI-visibility pages
- Homepage [`/`](https://lebanese-arabic.com/)
  - Brand/entity page
  - Broad brand trust
  - Learn Lebanese Arabic brand discovery
- Lessons landing page [`/lebanese-lessons/`](https://lebanese-arabic.com/lebanese-lessons/)
  - Private online Lebanese Arabic lessons
  - Native-speaker tutoring
  - Adult learners
  - Live online classes
  - Cultural-context teaching
  - AI prompts around tutors, private lessons, native speakers, and providers
- Books page [`/books/`](https://lebanese-arabic.com/books/)
  - Textbooks
  - Self-study resources
  - Book-related prompts
  - Should evolve from a single long article into a reusable books landing page that can support multiple books and possible future direct sales
  - Must satisfy both informational intent (`Lebanese Arabic books`) and transactional/comparison intent (which book to buy, what is inside, where to buy, who it is for)
- Videos page [`/videos/`](https://lebanese-arabic.com/videos/)
  - Video learning
  - Channel/resource discovery

### Lesson and informational pages
- [`/lesson1/`](https://lebanese-arabic.com/lesson1/)
  - Hello / hi in Lebanese
  - Introductory greetings
  - `marhaba meaning`
- [`/lesson2/`](https://lebanese-arabic.com/lesson2/)
  - `afwan`
  - `afwan meaning`
  - Excuse me / pardon usage in Lebanese travel and everyday conversation
- [`/lesson4/`](https://lebanese-arabic.com/lesson4/)
  - Numbers in Lebanese Arabic
  - Counting money in Lebanese
  - Lebanese lira and banknotes in a numbers-first lesson format
  - Should stay numbers-first unless future data justifies a separate dedicated money article
- [`/lesson12/`](https://lebanese-arabic.com/lesson12/)
  - Grandmother / grandfather / family words
  - Family-tree visual should use a first-party asset plus crawlable HTML support text
- [`/lesson15/`](https://lebanese-arabic.com/lesson15/)
  - Lebanese words / phrases
  - Broader language-intro queries
- [`/lesson40/`](https://lebanese-arabic.com/lesson40/)
  - Thank you in Lebanese
  - Manners / polite expressions
  - Courtesy-language support page
- Planned blog post [`/closest-arabic-dialect-to-msa/`](https://lebanese-arabic.com/closest-arabic-dialect-to-msa/)
  - Which Arabic dialect is closest to MSA / Modern Standard Arabic
  - Informational comparison page about dialect proximity by perception, structure, and vocabulary
  - Should use an answer-first summary and comparison framing
  - Should reinforce Lebanese / Levantine topical authority without overselling Lebanese as the answer to every criterion
  - Should support internal linking toward Lebanese learning resources and classes

## Important Intent Split: Lesson 2 vs Lesson 40
These two pages should support each other, not compete.

### Lesson 2 should own
- `afwan`
- `afwan meaning`
- `excuse me in Lebanese Arabic`
- Travel and situational uses of `afwan`

### Lesson 40 should own
- `thank you in Lebanese`
- `how to say thank you in Lebanese`
- Lebanese manners and polite phrases
- Supportive context around responses, courtesy, and related expressions

### Cannibalization rule
- Do not turn Lesson 40 into the primary `afwan meaning` page unless rankings clearly move there and outperform Lesson 2.
- Do not turn Lesson 2 into the main `thank you in Lebanese` page.
- Cross-link the two pages explicitly where relevant.

## Current Ubersuggest-Driven Priority List
These are the current practical SEO priorities derived from Ubersuggest exports and local page inventory.

### Priority 1: Near-win tracked pages
- Completed current optimization pass on:
  - [`/lesson2/`](https://lebanese-arabic.com/lesson2/) for `afwan` and `afwan meaning`
  - [`/lesson1/`](https://lebanese-arabic.com/lesson1/) for the hello/hi cluster
  - [`/lesson12/`](https://lebanese-arabic.com/lesson12/) for family-word terms
  - [`/lesson4/`](https://lebanese-arabic.com/lesson4/) for `money in lebanese`
- Next untouched tracked near-win:
  - [`/books/`](https://lebanese-arabic.com/books/) for `lebanese arabic books`
- Practical rule:
  - let the recently updated lesson pages settle and gather movement
  - use the next optimization cycle on the remaining tracked page-1-near-win pages that have not yet been sharpened

### Priority 2: Commercial and AI-visibility pages
- [`/lebanese-lessons/`](https://lebanese-arabic.com/lebanese-lessons/) for tutoring and booking prompts
- [`/books/`](https://lebanese-arabic.com/books/) for textbook / self-study prompts
- [`/videos/`](https://lebanese-arabic.com/videos/) for video-learning and YouTube/channel-related prompts

### Immediate AI-visibility priority from latest export
- Run a focused prompt-coverage pass on [`/lebanese-lessons/`](https://lebanese-arabic.com/lebanese-lessons/) for these exact intent clusters:
  - `live tutoring` + `native speakers`
  - `private lessons` + `adults`
  - `flexible scheduling`
  - `cultural context`
- Keep this pass explicit and answer-first (short Q&A/FAQ style blocks) to improve LLM retrieval and prompt matching.

### Books page design rule
- Treat [`/books/`](https://lebanese-arabic.com/books/) as a commercial catalog / landing page, not as a blog-style article.
- The page should:
  - surface the books immediately above the fold
  - make format, audience, level, and buying options explicit
  - support future direct website checkout without redesigning the page structure from scratch
  - reduce long unstructured text in favor of scannable product sections, proof, FAQs, and clear CTAs
- Branding rule:
  - use `Lebanese Arabic with Hiba` consistently as the page-level and product-brand identity
  - avoid `Hiba Najem` in visible sales copy, metadata, and page framing unless a third-party marketplace listing legally requires that personal name elsewhere

### Priority 3: Larger content gap opportunities
- Lebanese pronunciation
- Grammar explanations
- Free resources hub
- Best books / best apps / best videos / best channels pages
- At-home immersion and practice resources

These should be pursued after near-win and page-intent fixes, unless newer Semrush or Ahrefs data materially changes the priority.

## Fresh Content Queue
These are the best current candidates for new blog posts when publishing freshness-oriented informational content between page-optimization workstreams.

### Priority 1: Strongest next fresh post
- `What Language Do Lebanese Speak?`
  - Supported by Ubersuggest demand around:
    - `what language lebanon speak`
    - `what language do lebanese speak`
    - `what language does lebanon speak`
    - `what is language of lebanon`
  - Distinct from the existing Lebanese language-vs-dialect post
  - Strong top-of-funnel informational topic with broad answer-engine relevance
- `Which Arabic Dialect Should You Learn?`
  - Supported by Ubersuggest demand for `which arabic dialect to learn`
  - Strong answer-engine fit
  - Broad decision-making intent that can support Lebanese / Levantine topical authority without forcing a commercial angle

### Priority 2: Strong follow-up explainers
- `Can Different Arabic Dialects Understand Each Other?`
  - Clean informational intent
  - Strong fit with dialect-continuum authority
  - Good answer-engine topic
- `Does Anyone Speak Modern Standard Arabic in Daily Life?`
  - Natural companion to the closest-to-MSA post
  - Clarifies spoken dialects vs formal Arabic
- `What Is the Difference Between Modern Standard Arabic and Arabic Dialects?`
  - Foundational explainer topic
  - Useful as an internal-link hub between dialect, MSA, and Lebanese-focused posts

### Priority 3: Good but needs tighter differentiation
- `Which Arabic Dialect Is Closest to Classical Arabic?`
  - Only worth publishing if clearly differentiated from the existing closest-to-MSA post
  - Must focus on classical / conservative structural features rather than repeat the MSA framing

### Lower-priority or cautious topics
- `Which Arabic Dialect Is Closest to the Quran?`
  - There is query demand, but the topic is more sensitive and easier to mishandle
  - Not the best immediate next fresh post

### Cannibalization guardrail for fresh posts
- Do not create a new post that substantially overlaps with:
  - [`/blog/is-lebanese-a-language-or-dialect/`](https://lebanese-arabic.com/blog/is-lebanese-a-language-or-dialect/)
  - [`/closest-arabic-dialect-to-msa/`](https://lebanese-arabic.com/closest-arabic-dialect-to-msa/)
- New dialect / MSA posts should answer a distinct user question, not restate the same conclusion with a slightly different title.

### Split rule for Lebanese-language posts
- Treat `what language do lebanese speak` as a practical, top-of-funnel query with an answer-first format.
- If maintaining a separate technical linguistics post, retarget that technical post to specialist query intent instead of the practical query:
  - dialect features
  - Levantine classification
  - diglossia in Lebanon
  - code-switching and sociolinguistics in Lebanese speech
- Practical post and technical post should cross-link, but each must keep a distinct title, intro, and heading structure to avoid cannibalization.

## AI Visibility Principles
To improve AI search visibility, pages should:

- Use explicit language instead of implied language.
- Clearly state who the page is for.
- Clearly state what the page helps with.
- Use direct answer blocks for common prompt-style queries.
- Include supporting entity/trust details where relevant.
- Make the site’s offer, expertise, and content scope easy for AI systems to infer.

For commercial pages, this means clearly stating:
- format
- audience
- teacher type
- delivery method
- booking path
- differentiators

For informational pages, this means clearly stating:
- the term
- the meaning
- the usage
- the context
- examples
- how the page differs from related pages

For educational visuals, this means:
- prefer first-party SVG or image assets over embedded third-party widgets or exports
- keep the important vocabulary and relationships available in crawlable HTML near the visual

## Future Data Sources
When Semrush and Ahrefs exports are added later, they should be used to refine:

- keyword prioritization
- backlink prioritization
- competitor gap analysis
- page-to-query alignment
- topical authority opportunities

Those exports should be incorporated into this document as new evidence, not treated as a separate process.

## Working Rule For Future SEO Tasks
Before editing any page for SEO or AI visibility:

1. Check this document for the intended role of the page.
2. Check [`seo_project_history.md`](C:\Development\lebanese-arabic\SEO\seo_project_history.md) to avoid repeating work or causing cannibalization.
3. Use live data from GSC, Ubersuggest, and local page sources.
4. Prefer small, high-confidence improvements before major rewrites.
