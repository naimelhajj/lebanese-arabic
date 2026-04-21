# SEO Project History

## Purpose
This file is the running history of SEO and AI-visibility work done on `lebanese-arabic.com`.

Every meaningful SEO investigation, technical fix, page-intent decision, or AI-visibility improvement should be logged here. The goal is to preserve context, avoid repeating work, and make future decisions cumulative.

## 2026-03-19
### GSC coverage triage
- Reviewed exported Google Search Console indexing reports under [`site-health/gsc/coverage/`](C:\Development\lebanese-arabic\SEO\site-health\gsc\coverage).
- Determined that much of the exclusion noise was normal WordPress-style junk:
  - comment pages
  - feeds
  - reply parameters
  - old AMP variants
  - duplicate canonical variants
- Identified the highest-value issues as:
  - `Redirect error`
  - `Server error (5xx)`
  - a small set of meaningful `404` URLs

### Redirect normalization work
- Added and tested redirect normalization for:
  - malformed double-slash URLs
  - `//1000` malformed variants
  - `?nonamp=1`
  - old `/amp/` URLs
- Validated fixes in GSC for:
  - `Redirect error`
  - `Server error (5xx)`

### Legacy page redirects
- Added and tested important legacy redirects for:
  - old video category URLs to current equivalents
  - `/interactive-time-clock` to [`/lebanese-arabic-clock/`](https://lebanese-arabic.com/lebanese-arabic-clock/)
- Validated the relevant `404` fixes in GSC.

### Intentional 404 decisions
- Decided that some URLs should remain `404` or `410` when they were:
  - mistaken internal links
  - junk/plugin artifacts
  - obsolete pages with no meaningful replacement

## 2026-03-19 to 2026-03-20
### Lebanese lessons page improvement for AI visibility
- Audited [`/lebanese-lessons/`](https://lebanese-arabic.com/lebanese-lessons/) using the local source in [`pages/lebanese-lessons/`](C:\Development\lebanese-arabic\SEO\pages\lebanese-lessons).
- Preserved the existing conversion-focused structure instead of redesigning the page.
- Improved semantic alignment for AI-visibility prompts around:
  - private Lebanese Arabic lessons
  - adults
  - native Lebanese speakers
  - live online tutoring
  - cultural context
- Updated title, meta description, hero-support copy, and supporting copy so the page is a stronger target for commercial and AI-driven queries.
- Confirmed the outdated `Skype` wording was removed from metadata.

## 2026-03-20
### Ubersuggest export review
- Audited all exports under [`ubersuggest/exports/`](C:\Development\lebanese-arabic\SEO\ubersuggest\exports).
- Concluded that there was no immediate technical emergency in Ubersuggest exports.
- Determined that the highest-value next work is:
  - near-win tracked pages
  - page-intent clarity
  - AI-visibility improvements on matching pages

### Current strategic interpretation
- Position tracking shows many strong rankings already.
- The best next SEO tasks are incremental lifts, not major sitewide restructuring.
- Competitor exports suggest larger content opportunities later, especially in educational/reference content, but those are secondary to current near-win pages.

### Lesson 2 vs Lesson 40 intent split
- Reviewed local source files in [`pages/`](C:\Development\lebanese-arabic\SEO\pages) to determine the best canonical intent split.
- Decision:
  - [`/lesson2/`](https://lebanese-arabic.com/lesson2/) remains the primary page for:
    - `afwan`
    - `afwan meaning`
    - excuse-me / pardon usage
  - [`/lesson40/`](https://lebanese-arabic.com/lesson40/) remains the better page for:
    - thank-you language
    - manners / polite expressions
    - courtesy context
- Rationale:
  - `lesson2` already ranks for the `afwan` cluster
  - `lesson40` is thematically broader but should not replace `lesson2` for `afwan` without clear evidence
  - both pages should support each other with clearer internal linking

### Lesson 2 implementation review
- Reviewed the updated WordPress/source state of [`/lesson2/`](https://lebanese-arabic.com/lesson2/) after the `afwan` optimization work.
- Confirmed that `lesson2` is now materially better aligned to:
  - `afwan`
  - `afwan meaning`
  - excuse-me / pardon usage intent
- Confirmed the preferred split still holds:
  - [`/lesson2/`](https://lebanese-arabic.com/lesson2/) for `afwan` meaning and usage
  - [`/lesson40/`](https://lebanese-arabic.com/lesson40/) for `thank you`, manners, and broader polite expressions
- Confirmed the next near-win target should be [`/lesson1/`](https://lebanese-arabic.com/lesson1/) for the hello/hi cluster.
- Additional opportunity identified from tracked rankings:
  - `marhaba meaning` is currently not ranked and should be captured on [`/lesson1/`](https://lebanese-arabic.com/lesson1/) without turning that page into a broad pronunciation page.

### Lesson 1 implementation review
- Reviewed the updated WordPress/source state of [`/lesson1/`](https://lebanese-arabic.com/lesson1/) after the hello-cluster optimization work.
- Confirmed the page metadata is now strongly aligned to:
  - `hello in lebanese`
  - `hello lebanese`
  - `how to say hi in lebanese`
  - `marhaba meaning`
- Confirmed this remains the correct target page for the hello / `marhaba` cluster.
- Ongoing guardrail:
  - do not broaden [`/lesson1/`](https://lebanese-arabic.com/lesson1/) into the main page for broad `lebanese pronunciation`
  - keep broader greeting variants such as `good morning` associated with their more specific pages

### Lesson 12 targeting review
- Reviewed [`/lesson12/`](https://lebanese-arabic.com/lesson12/) against current tracked near-win keywords.
- Confirmed the page is already the ranking URL for:
  - `grandpa in lebanese`
  - `grandfather in lebanese`
  - `grandmother in lebanese`
  - `lebanese for grandmother`
- Identified the main issue as page-intent breadth:
  - current title and description are broad family-tree language
  - tracked demand is more specific around grandmother / grandfather / grandpa query phrasing
- Next action:
  - keep [`/lesson12/`](https://lebanese-arabic.com/lesson12/) as the ranking page
  - make the top of the page answer those family-term queries more directly

### Lesson 12 implementation review
- Reviewed the updated WordPress/source state of [`/lesson12/`](https://lebanese-arabic.com/lesson12/) after the family-term optimization work.
- Confirmed the page metadata is now much better aligned to:
  - `grandmother in lebanese`
  - `grandfather in lebanese`
  - `grandpa in lebanese`
  - `lebanese for grandmother`
- Confirmed [`/lesson12/`](https://lebanese-arabic.com/lesson12/) remains the correct target page for this cluster.

### Lesson 12 family-tree asset review
- Reviewed the local Family Echo export at [`pages/lesson12/My-Family-21-Mar-2026-075054905.html`](C:\Development\lebanese-arabic\SEO\pages\lesson12\My-Family-21-Mar-2026-075054905.html).
- Confirmed the export is large, script-heavy, branded as Family Echo, and includes Family Echo title/description metadata.
- Confirmed the export file's embedded license text says it must not be modified or used to create derivative works.
- SEO / GEO recommendation:
  - do not embed the Family Echo HTML directly in [`/lesson12/`](https://lebanese-arabic.com/lesson12/)
  - use it only as a private reference
  - recreate the family tree as a first-party asset (preferably custom SVG or a clean image) and pair it with crawlable HTML text on the page

### Lesson 12 family-tree SVG build
- Built a first-party SVG asset at [`pages/lesson12/lesson12-family-tree.svg`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree.svg).
- Added a local generator script at [`pages/lesson12/generate_family_tree_svg.py`](C:\Development\lebanese-arabic\SEO\pages\lesson12\generate_family_tree_svg.py) so the asset can be regenerated from the exported data later.
- Used:
  - [`pages/lesson12/My-Family-21-Mar-2026-134318836.csv`](C:\Development\lebanese-arabic\SEO\pages\lesson12\My-Family-21-Mar-2026-134318836.csv) for the relationship graph and labels
  - [`pages/lesson12/My-Family-21-Mar-2026-134326526.txt`](C:\Development\lebanese-arabic\SEO\pages\lesson12\My-Family-21-Mar-2026-134326526.txt) as a sanity check against the exported people list
- Current limitation:
  - photos were intentionally not embedded because the CSV/TXT exports do not provide stable publishable photo references
- Current recommendation:
  - use the SVG as the visual asset
  - still keep the key family terms and relationships available in crawlable HTML on the lesson page

### Lesson 12 screenshot-style SVG variant
- Built a second SVG variant at [`pages/lesson12/lesson12-family-tree-screenshot-style.svg`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.svg).
- Purpose:
  - move closer to the user-provided screenshot direction
  - use a single connected tree layout instead of the earlier panel-based infographic layout
  - mimic the green background plus red/white card treatment while still staying first-party
- Current tradeoff:
  - this variant is visually closer to the screenshot
  - it still does not embed real photos, because the CSV/TXT exports do not provide stable publishable photo references

### Lesson 12 screenshot-style connector and photo support update
- Fixed the screenshot-style SVG generator so:
  - grandparent spouse connectors are visibly rendered on both sides
  - the `Khayyeh` / `Mart Khayyeh` spouse connector is horizontal
  - blood relationships render slightly thicker than spouse/non-blood relationships
- Added optional local photo support to the generator:
  - create [`pages/lesson12/family-tree-photos/`](C:\Development\lebanese-arabic\SEO\pages\lesson12\family-tree-photos)
  - add files named by person ID such as `EPTAW.jpg`, `MDG4X.png`, `UW810.webp`, etc.
  - regenerate the SVG and those featured cards will embed the image directly into the output SVG as base64 data

### Lesson 12 hand-edited SVG backup and all-node photo slots
- Created a backup of the current hand-adjusted screenshot-style SVG at [`pages/lesson12/lesson12-family-tree-screenshot-style.backup-before-all-photo-slots-2026-03-22.svg`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.backup-before-all-photo-slots-2026-03-22.svg).
- Added an in-place transformation script at [`pages/lesson12/add_all_photo_slots_to_svg.py`](C:\Development\lebanese-arabic\SEO\pages\lesson12\add_all_photo_slots_to_svg.py).
- Applied that script to the live screenshot-style SVG so all 34 nodes now have a visible photo slot while preserving the hand-adjusted connector geometry.

### Lesson 12 Khayyeh photo crop fix
- Fixed the `Khayyeh` photo placement in [`pages/lesson12/lesson12-family-tree-screenshot-style.svg`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.svg).
- Added a one-off local repair script at [`pages/lesson12/fix_khayyeh_photo_crop.py`](C:\Development\lebanese-arabic\SEO\pages\lesson12\fix_khayyeh_photo_crop.py).
- The fix:
  - removed the stray standalone imported image node
  - added a dedicated SVG `clipPath` for the Khayyeh avatar circle
  - embedded the image inside the `Khayyeh` card group and clipped it to the circular photo area
  - kept the visible avatar border ring so the card styling stays consistent with the rest of the tree

### Lesson 12 title-based family-tree photo import workflow
- Added [`pages/lesson12/embed_family_tree_photos_by_title.py`](C:\Development\lebanese-arabic\SEO\pages\lesson12\embed_family_tree_photos_by_title.py).
- Purpose:
  - let photos be embedded into the hand-edited screenshot-style SVG based on each visible family-member title
  - support both small and large avatar slots without changing the current node or connector layout
- Naming rule:
  - photo filenames should use slugged title names such as `khayyeh`, `emmeh`, `mart-3ammeh`, etc.
  - duplicate titles are numbered, so the two grandparents must be named `sitteh-1`, `sitteh-2`, `jeddeh-1`, and `jeddeh-2`
- Expected photo folder:
  - [`pages/lesson12/family-tree/`](C:\Development\lebanese-arabic\SEO\pages\lesson12\family-tree)

### Lesson 12 centered-photo card conversion
- Created a backup of the pre-conversion SVG at [`pages/lesson12/lesson12-family-tree-screenshot-style.backup-before-promote-all-cards-2026-03-22.svg`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.backup-before-promote-all-cards-2026-03-22.svg).
- Added [`pages/lesson12/promote_compact_cards_to_centered_photo_layout.py`](C:\Development\lebanese-arabic\SEO\pages\lesson12\promote_compact_cards_to_centered_photo_layout.py).
- Applied it to the live screenshot-style SVG so the remaining compact nodes now use the same tall centered-photo card treatment as the larger highlighted family members.
- Also increased the SVG canvas height to keep the bottom-row cards visible after the conversion.

### Lesson 12 avatar size increase and generation-row normalization
- Added [`pages/lesson12/normalize_family_tree_rows_and_avatar_sizes.py`](C:\Development\lebanese-arabic\SEO\pages\lesson12\normalize_family_tree_rows_and_avatar_sizes.py).
- Applied it to [`pages/lesson12/lesson12-family-tree-screenshot-style.svg`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.svg) so:
  - avatar photo circles are larger across the tree
  - third-generation cards now share the same row
  - top-row, parent-row, and spouse connectors were moved to the visual centers of their updated cards
  - the SVG canvas height was increased again to preserve bottom-row visibility after the size change

### Lesson 12 maternal-vs-paternal branch color variant
- Created a backup of the pre-color-variant SVG at [`pages/lesson12/lesson12-family-tree-screenshot-style.backup-before-maternal-paternal-colors-2026-03-22.svg`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.backup-before-maternal-paternal-colors-2026-03-22.svg).
- Added [`pages/lesson12/apply_maternal_paternal_branch_colors.py`](C:\Development\lebanese-arabic\SEO\pages\lesson12\apply_maternal_paternal_branch_colors.py).
- Applied a branch-color variant to the live screenshot-style SVG with this rule:
  - maternal branch and the left-side sibling branch use the red card fill
  - paternal branch and the right-side sibling branch use the white card fill
  - the central self / own-children branch was left unchanged

### Lesson 12 finalized tree backup
- Created a frozen backup of the user-finalized tree at [`pages/lesson12/lesson12-family-tree-screenshot-style.backup-finalized-2026-03-23.svg`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.backup-finalized-2026-03-23.svg).
- User note:
  - the tree colors, portraits, and connections have now been manually finalized
  - do not modify the tree layout further unless explicitly requested in a future task

### Lesson 12 title, branding, and HTML embed support
- Created a new safety backup before adding presentation-layer branding at [`pages/lesson12/lesson12-family-tree-screenshot-style.backup-before-title-footer-2026-03-23.svg`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-screenshot-style.backup-before-title-footer-2026-03-23.svg).
- Added [`pages/lesson12/add_tree_title_and_branding.py`](C:\Development\lebanese-arabic\SEO\pages\lesson12\add_tree_title_and_branding.py).
- Applied it to the live SVG so the graphic now includes:
  - an updated accessible SVG title
  - a visible in-graphic title
  - a small branded footer using [`pages/lesson12/cropped-hiba-logo-without-najem-white.png`](C:\Development\lebanese-arabic\SEO\pages\lesson12\cropped-hiba-logo-without-najem-white.png)
- Added a WordPress-ready page embed block at [`pages/lesson12/lesson12-family-tree-html-snippet.html`](C:\Development\lebanese-arabic\SEO\pages\lesson12\lesson12-family-tree-html-snippet.html) so the page can include a proper HTML heading and descriptive copy above the SVG.
- Replaced the subtitle sentence inside the SVG with a compact color legend matching the finalized tree categories:
  - immediate family
  - extended family
  - non-blood
  - me

### Lesson 12 social-image verification
- Reviewed the refreshed local source snapshot after the new family tree block and lightbox were added.
- Confirmed the visible on-page asset now uses:
  - SVG on page
  - PNG in lightbox, embed code, and custom `ImageObject` schema
- Confirmed the page still emits the old 2015 JPG in server-side metadata:
  - Yoast schema `primaryimage`
  - `thumbnailUrl`
  - `og:image`
  - `twitter:image`
- Conclusion:
  - this is no longer just a cache issue
  - the old JPG is still configured as the page's primary/social image somewhere upstream, most likely via featured image and/or another metadata layer such as Hubbub

### Lesson 12 social-image propagation fix
- Reviewed the next refreshed source snapshot after the featured/social image was updated again.
- Confirmed the page now emits the new 2026 family-tree PNG in:
  - Yoast schema `primaryimage`
  - `og:image`
  - `twitter:image`
  - `thumbnailUrl`

## 2026-03-25
### Published review: closest Arabic dialect to MSA post
- Reviewed the published source at [`blogposts/closest-dialect-source-code.txt`](C:\Development\lebanese-arabic\SEO\blogposts\closest-dialect-source-code.txt) after the post went live.
- Confirmed the main publish-state items are now correct:
  - final canonical URL is live at [`/closest-arabic-dialect-to-msa/`](https://lebanese-arabic.com/closest-arabic-dialect-to-msa/)
  - title, meta description, canonical, and social metadata are aligned
  - Yoast schema now uses the correct published headline and featured image
  - the new featured/social image is [`blogposts/images/closest-dialect-to-msa-featured.png`](C:\Development\lebanese-arabic\SEO\blogposts\images\closest-dialect-to-msa-featured.png)
  - answer-first introduction and FAQ schema are present
  - an internal CTA link to [`/lebanese-lessons/`](https://lebanese-arabic.com/lebanese-lessons/) is present
- Remaining issues after publish:
  - comments are still enabled on the post, which may reintroduce avoidable comment-feed / reply-url noise
  - the visible H2s still include extra `Section 1/2/3` framing that could be simplified later
  - the local saved source shows some mojibake in a few strings, so the live rendered page should be visually checked to confirm whether that is only a local export artifact
- Conclusion:
  - the post is publish-ready and materially improved for SEO, AI retrieval, and social sharing
  - only minor cleanup remains unless live rendering reveals real encoding issues

### Closest-dialect post indexing and internal-link follow-up
- Reviewed the published source again to determine immediate post-publish actions.
- Confirmed the page is strong enough to move into indexing workflow:
  - final canonical URL is live
  - answer-first structure is present
  - FAQ schema is present
  - featured and social image metadata are correct
- Recommended next GSC flow:
  - inspect the exact canonical URL
  - run a live test once
  - if the live test is clean, request indexing
- Identified the strongest current internal-link source as the newer dialect explainer post:
  - [`blogposts/is-lebanese-a-language-or-dialect-source-code.txt`](C:\Development\lebanese-arabic\SEO\blogposts\is-lebanese-a-language-or-dialect-source-code.txt)
  - usable existing anchor/theme phrases include:
    - `Modern Standard Arabic`
    - `Levantine Arabic`
    - `Levantine dialect continuum`
    - `dialect or regional variety of Levantine Arabic`
- Secondary supporting internal-link candidates exist in broader Arabic-background posts, but they are weaker than the dialect explainer because their existing phrasing is less directly aligned to the new post's intent.
  - `thumbnailUrl`
  - `og:image`
  - `twitter:image`
- Remaining metadata mismatch:
  - Yoast `Article.headline` and breadcrumb item still use the old historical title `Decoding Lebanese Family Terms: From Parents to Cousins`
  - visible title, SEO title, description, and social image are otherwise aligned

### Draft blog post review: closest Arabic dialect to MSA
- Reviewed the unpublished preview source at [`blogposts/closest-dialect-source-code.txt`](C:\Development\lebanese-arabic\SEO\blogposts\closest-dialect-source-code.txt).
- Confirmed the preview contains normal draft-only noise that should not be treated as publish blockers:
  - preview canonical and preview URL
  - WordPress admin bar and Query Monitor assets
  - draft `datePublished` anomalies in Yoast schema
- Found real pre-publish issues to fix before publishing:
  - no custom Yoast meta description is set
  - no featured/social image is evident in metadata
  - the page has no internal links in the article body
  - the article opens with a conversational intro instead of an answer-first summary
  - section headings are conceptually good but not yet phrased for strongest search / AI retrievability
  - comments appear enabled on the draft, which should be reviewed given prior indexing cleanup around comment URLs
- Established intended page role:
  - informational comparison page for `which Arabic dialect is closest to MSA`
  - should clarify that the answer changes by criterion: perception, structure, or vocabulary
  - should support Lebanese / Levantine topical authority and the classes funnel without creating misleading overclaims

### Draft blog post keyword and prompt research: closest Arabic dialect to MSA
- Reviewed the Ubersuggest exports in [`blogposts/closest-dialect-keyword-research/`](C:\Development\lebanese-arabic\SEO\blogposts\closest-dialect-keyword-research).
- Confirmed the main keyword target should remain:
  - `which arabic dialect is closest to msa`
- Secondary supportive keyword targets from the export:
  - `which arabic dialect is closest to fusha`
  - `closest dialect to fusha`
  - `which dialect is closest to modern standard arabic`
- Important adjacent keyword to avoid using as the main target for this post:
  - `which arabic dialect to learn`
  - reason: broader decision-intent and stronger candidate for a separate recommendation/comparison page
- Prompt export confirms useful AI-answer angles for this article:
  - vocabulary overlap with MSA
  - structural closeness to classical Arabic
  - mutual intelligibility / similarity framing
  - easiest dialect framing for MSA learners
- Practical decision:
  - publish this post as an answer-first informational comparison page
  - structure the page around criterion-based answers rather than one oversimplified verdict

### Draft blog post publish package: closest Arabic dialect to MSA
- Final recommended publish target:
  - title/H1: `Which Arabic Dialect Is Closest to MSA?`
  - preferred slug: `/closest-arabic-dialect-to-msa/`
  - Yoast focus keyphrase: `which arabic dialect is closest to msa`
- Recommended secondary phrase coverage:
  - `closest dialect to fusha`
  - `which dialect is closest to modern standard arabic`
- Recommended publishing structure:
  - answer-first summary immediately after the opening
  - H2s phrased around dialect closeness by perception, structure, and vocabulary
  - short FAQ covering MSA, Fusha, vocabulary overlap, and Lebanese/Levantine relevance
- Publish blockers that still need manual WordPress action:
  - add a real meta description
  - set a featured/social image
  - review comments setting before publishing

### Draft blog post featured image: closest Arabic dialect to MSA
- Created a first-party 1200x630 featured/social image for the draft post at:
  - [`blogposts/images/closest-dialect-to-msa-featured.png`](C:\Development\lebanese-arabic\SEO\blogposts\images\closest-dialect-to-msa-featured.png)
- Added the reproducible generator script at:
  - [`blogposts/images/generate_closest_dialect_featured.py`](C:\Development\lebanese-arabic\SEO\blogposts\images\generate_closest_dialect_featured.py)
- Visual direction chosen:
  - match the established March 2026 blogpost featured-image style
  - concise title card plus criterion-based answer framing
  - branded first-party asset suitable for featured image, `og:image`, and `twitter:image`

## 2026-03-26
### Fresh content queue prioritization
- Reviewed the current content inventory under [`blogposts/`](C:\Development\lebanese-arabic\SEO\blogposts) and relevant Ubersuggest exports under:
  - [`blogposts/closest-dialect-keyword-research/`](C:\Development\lebanese-arabic\SEO\blogposts\closest-dialect-keyword-research)
  - [`ubersuggest/exports/`](C:\Development\lebanese-arabic\SEO\ubersuggest\exports)
- Confirmed that the recently published posts already cover:
  - Lebanese language vs dialect classification
  - closest Arabic dialect to MSA
- Established the best next fresh-post candidates as:
  - `What Language Do Lebanese Speak?`
  - `Which Arabic Dialect Should You Learn?`
  - `Can Different Arabic Dialects Understand Each Other?`
  - `Does Anyone Speak Modern Standard Arabic in Daily Life?`
  - `What Is the Difference Between Modern Standard Arabic and Arabic Dialects?`
- Broader Ubersuggest export confirms a strong unfilled informational cluster around:
  - `what language lebanon speak`
  - `what language do lebanese speak`
  - `what language does lebanon speak`
  - `what is language of lebanon`
- Distinction decision:
  - this should be treated as separate from the existing Lebanese language-vs-dialect post
  - it targets the practical country/language question, not the classification debate
- Lower-priority or cautionary topics identified:
  - `Which Arabic Dialect Is Closest to Classical Arabic?`
  - `Which Arabic Dialect Is Closest to the Quran?`
- Practical decision:
  - the strongest next fresh-content posts are:
    - `What Language Do Lebanese Speak?`
    - `Which Arabic Dialect Should You Learn?`
  - future dialect / MSA posts should be kept distinct from the existing two published posts to avoid cannibalization
  - lesson-page near-win work still remains the main operational SEO track, with [`/lesson4/`](https://lebanese-arabic.com/lesson4/) still next in the page-optimization queue

### Lesson 4 audit for the money cluster
- Reviewed [`pages/lesson4/lesson4-source-code.txt`](C:\Development\lebanese-arabic\SEO\pages\lesson4\lesson4-source-code.txt) together with the Ubersuggest position-tracking export.
- Confirmed the current tracked near-win is:
  - `money in lebanese`
  - position `5`
  - search volume `590`
  - URL [`/lesson4/`](https://lebanese-arabic.com/lesson4/)
- Confirmed [`/lesson4/`](https://lebanese-arabic.com/lesson4/) remains the correct target page.
- Current issue identified:
  - the lesson content does include strong money material
  - but the page is still packaged primarily as a generic numbers lesson in the metadata and top framing
- Practical decision:
  - keep the page as a combined numbers-and-money lesson
  - but preserve its numbers-first intent rather than fully repackaging it as a money-first page
  - if a future dedicated money article is created, it should be based on separate keyword research and clearly differentiated from `lesson4`
  - avoid introducing time-sensitive exchange-rate claims as evergreen copy unless those are explicitly dated or maintained
- Recommended conservative patch direction:
  - keep the current numbers-first lesson framing
  - strengthen metadata and a short answer block so the page still reads as relevant for `money in lebanese`
  - add a small FAQ around money / banknotes without turning the page into a pure money article
- Reviewed the updated WordPress-exported source after the `lesson4` patch was applied.
- Confirmed the page now uses stronger metadata and on-page framing:
  - title/H1: `Numbers in Lebanese Arabic: Counting Money and Banknotes | Lesson 4`
  - meta description now explicitly mentions Lebanese money, coins, banknotes, and Lebanese lira amounts
  - new FAQ block clarifies that the lesson remains numbers-first while still covering money vocabulary
- Remaining caveat:
  - the historical `30,000 liras per US dollar` statement still exists inside the transcript/video-derived body text
  - this is now partially mitigated by the new explanatory note and FAQ that frame the exchange-rate reference as historical only
  - future cleanup can remove or annotate the old transcript line if desired, but the page is acceptable to leave as-is for now
- Rechecked the current Ubersuggest position-tracking near-wins after the lesson-page pass.
- Confirmed that the remaining tracked page-1-near-win not yet optimized is:
  - [`/books/`](https://lebanese-arabic.com/books/) for `lebanese arabic books`
  - current tracked position: `6`
- Practical sequencing decision:
  - let the recently updated lesson pages settle
  - use the next page-optimization pass on the books page rather than continuing to rework pages already updated this cycle

### Books page live UX/SEO audit
- Visited the live [`/books/`](https://lebanese-arabic.com/books/) page with Puppeteer and compared it to the local source snapshot at [`pages/books/books-source-code.txt`](C:\Development\lebanese-arabic\SEO\pages\books\books-source-code.txt).
- Confirmed the page currently behaves more like a narrow blog article than a reusable commercial books landing page.
- Main issues identified:
  - the above-the-fold layout is visually sparse and weakly commercial
  - the primary CTA is a marketplace dropdown rather than a strong buying decision section
  - the page is very text-heavy and not structured like a scalable multi-book catalog
  - the mobile rendering is poor and overly compressed
  - metadata is outdated and too Amazon-specific for a future direct-sales path
- Strategic direction set:
  - redesign the page as a proper books landing page
  - support both current Amazon marketplace purchase flow and future on-site sales
  - align the page more directly with `lebanese arabic books` search intent and answer-engine retrieval
- Prepared a WordPress-ready redesign brief for the next implementation pass.
- Core structure to use:
  - full-width landing-page layout without the standard blog sidebar
  - direct books hero with dual product cards
  - comparison / choose-your-book section
  - scannable feature bullets instead of long article paragraphs
  - FAQ and future-ready buy section
- Metadata direction:
  - move away from Amazon-centric copy
  - target broader book/self-study intent while preserving current marketplace purchase flow
- Added a branding constraint for the books-page rewrite:
  - use `Lebanese Arabic with Hiba` consistently
  - do not use `Hiba Najem` in the page-level sales copy or metadata rewrite
- Replaced the old Gutenberg draft at [`pages/books/books-gutenberg.txt`](C:\Development\lebanese-arabic\SEO\pages\books\books-gutenberg.txt) with a new full landing-page version.
- The new Gutenberg draft:
  - keeps the existing book-cover assets, chapter/sample visuals, video, and marketplace selectors
  - restructures the page around hero, product cards, comparison, detailed book sections, FAQ, and lessons/videos support CTA
  - removes personal-name branding from the page copy and uses `Lebanese Arabic with Hiba` consistently

### Books page Gutenberg rewrite using official block docs
- Rechecked Gutenberg serialization guidance via Context7 against the official WordPress Gutenberg docs before rewriting the books-page block file again.
- Confirmed the correct storage model is standard comment-delimited block serialization, with simple saved HTML inside each block wrapper rather than an overbuilt mix of custom wrappers.
- Rewrote [`pages/books/books-gutenberg.txt`](C:\Development\lebanese-arabic\SEO\pages\books\books-gutenberg.txt) from scratch into a cleaner core-block structure using:
  - `core/group`
  - `core/heading`
  - `core/paragraph`
  - `core/list`
  - `core/buttons`
  - `core/button`
  - `core/columns`
  - `core/column`
  - `core/image`
  - `core/separator`
  - `core/embed`
  - `core/html` only where needed for the marketplace selectors
- Simplified the page architecture so it is easier to paste into the Gutenberg code editor and less likely to break block parsing:
  - hero
  - two-book catalog
  - buy sections
  - proof / teaching-method section
  - Volume 1 contents
  - FAQ
  - soft CTA to lessons and videos

### Books page implementation approach reset
- Reframed the `/books/` redesign approach around how Gutenberg should actually be used, based on the official WordPress Gutenberg docs.
- Decision:
  - stop treating the page as a long hand-authored saved-HTML artifact
  - build it as a small set of normal core blocks inside the editor
  - reserve `core/html` only for elements Gutenberg cannot express cleanly, such as the existing Amazon marketplace selectors
- Practical layout rule for the next implementation pass:
  - keep the page architecture simple and native to Astra/Gutenberg
  - let the theme handle most styling
  - avoid deeply nested custom wrappers and over-styled serialized markup

### Books page editor-first content pack
- Shifted the next implementation step from serialized Gutenberg code to an editor-first content pack.
- Purpose:
  - make the `/books/` redesign easier to build directly in the block editor
  - reduce risk of broken markup or awkward block parsing
  - keep the landing-page structure while letting Astra/Gutenberg handle presentation naturally
- Deliverable prepared:
  - section-by-section copy for hero, book cards, proof section, Volume 1 contents, FAQ, and final CTA
  - intended to be pasted into native core blocks rather than into one oversized raw-code file

## 2026-04-11
### Draft review: what language do Lebanese speak
- Reviewed unpublished preview source at [`blogposts/what-language-do-lebanese-speak-source-code.txt`](C:\Development\lebanese-arabic\SEO\blogposts\what-language-do-lebanese-speak-source-code.txt) and extracted main article region for cleaner analysis.
- Confirmed the draft is academically detailed and linguistically rigorous, but currently under-optimized for the primary search intent of `what language do lebanese speak`.
- Main intent gap identified:
  - the article opens with technical framing and sectioned dialectology
  - it does not deliver the practical answer fast enough for top-of-funnel users
- Publish-readiness issues identified:
  - no custom Yoast meta description is set in preview
  - no clear answer-first block near the top
  - section headings are expert-facing (`Section 1/2/3`) rather than direct user-question phrasing
  - visible encoding artifacts appear in transliteration/reference strings in the source snapshot
  - references list contains repeated duplicate entries and one in-text uncertainty note that should be removed before publish
- Recommended direction:
  - keep the linguistic depth, but move a practical one-paragraph answer to the top:
    - daily life: Lebanese Arabic
    - formal writing/news: Modern Standard Arabic
    - common bilingual reality: French and English (plus Armenian in Armenian communities)
  - then keep the deeper linguistic sections below as supporting detail.

### Retarget package for the technical Lebanese-language draft
- Chosen positioning for the current draft:
  - keep as a specialist linguistics explainer
  - do not use it as the primary page for `what language do lebanese speak`
- Recommended technical query cluster:
  - `lebanese arabic dialect features`
  - `lebanese arabic phonology`
  - `lebanese arabic grammar features`
  - `beirut arabic dialect features`
  - `diglossia in lebanon`
  - `lebanese arabic and modern standard arabic`
  - `code switching in lebanon arabic french english`
  - `is lebanese levantine arabic`
- Retarget metadata and structure package prepared:
  - technical title/slug/meta
  - query-aligned H2 map
  - FAQ set centered on dialect features, diglossia, and code-switching
  - cleanup note to remove duplicated references and in-text uncertainty notes before publish

### Implemented rewrite: technical linguistics markdown draft
- Rewrote [`blogposts/linguistic-features.txt`](C:\Development\lebanese-arabic\SEO\blogposts\linguistic-features.txt) end-to-end to match the technical focus.
- Changes made:
  - replaced practical-query framing with specialist linguistic framing
  - updated title to a technical intent target (`phonology, grammar, diglossia, code-switching`)
  - replaced generic `Section 1/2/3` headings with query-aligned technical headings
  - removed duplicated references and removed uncertainty-note language
- added a technical FAQ section to align with AI-answer retrieval patterns
- normalized file content to ASCII to avoid encoding artifacts on WordPress import

### Continuum nuance correction in technical draft
- Updated [`blogposts/linguistic-features.txt`](C:\Development\lebanese-arabic\SEO\blogposts\linguistic-features.txt) to remove over-generalized wording that implied all Lebanese speech is strictly urban Levantine.
- Added explicit distinction between:
  - Lebanese as a Levantine continuum (urban + rural)
  - urban leveled Lebanese koine as the dominant prestige/interop code in media and interregional communication
- Applied this correction in:
  - opening paragraph
  - section title and framing paragraph
  - first FAQ answer
  - final conclusion sentence

### Feature-list enrichment from source draft
- Updated the feature sections in [`blogposts/linguistic-features.txt`](C:\Development\lebanese-arabic\SEO\blogposts\linguistic-features.txt) using stronger explanatory detail from [`blogposts/what-language-do-lebanese-speak-source-code.txt`](C:\Development\lebanese-arabic\SEO\blogposts\what-language-do-lebanese-speak-source-code.txt).
- Added/clarified high-value linguistic signals for AI and search extraction:
  - qaf shift with urban/rural variation note
  - j-to-zh realization in urban Lebanese
  - interdental reduction outcomes
  - diphthong leveling
  - imperative vowel lengthening
  - b- imperfect marking with example
  - fi- capability construction with example
  - la- direct-object marking pattern with example
  - urban gender-neutral plural tendency
- Updated technical FAQ answers to reflect the richer feature set.
- Reason: improve technical precision and answer quality for SEO/GEO/AEO while keeping the page role distinct from practical intent posts.

### Scientific nuance pass for linguistic-features draft
- Refined [`blogposts/linguistic-features.txt`](C:\Development\lebanese-arabic\SEO\blogposts\linguistic-features.txt) to reduce over-simplification risk while keeping readability.
- Added a dedicated `Methodological Caveats and Scope` section covering:
  - urban-koine framing vs full rural/regional coverage
  - lexical-overlap percentage caveat (restricted basic-vocabulary lists vs total modern lexicon)
  - diglossia as functional continuum rather than strict binary
  - distinction between illustrative examples and directly sourced claims
- Updated diglossia and FAQ wording so the article explicitly states continuum behavior and avoids implying that one fixed model explains all Lebanese speech.
- Reason: align learner-facing copy with stricter sociolinguistic and dialectological accuracy without weakening accessibility.

### Preview-source validation: linguistic-features post
- Reviewed [`blogposts/linguistic-features-source-code.txt`](C:\Development\lebanese-arabic\SEO\blogposts\linguistic-features-source-code.txt) (WordPress preview export).
- Confirmed the latest content updates are present in preview:
  - `Methodological Caveats and Scope` section
  - expanded technical FAQ including:
    - `Does "urban Levantine Lebanese" describe all speech in Lebanon?`
    - `Are high Lebanese-MSA overlap percentages straightforward?`
  - updated conclusion wording (`dynamic diglossic interaction`)
  - clean, de-duplicated references list
- Confirmed current preview metadata is directionally correct for title and description.
- Noted expected preview-only artifacts (not publish blockers by themselves):
  - canonical URL and schema `mainEntityOfPage` still use preview URL format (`?p=5996`)
  - Yoast schema `datePublished` shows invalid draft sentinel value (`-0001-11-30...`)
  - admin/debug/preview noise (`Query Monitor`, admin bar, preview conditionals)
- Remaining manual publish checks:
  - set final slug before publish
  - assign a real category (currently `Uncategorized`)
  - confirm social image fields (no `og:image` / `twitter:image` found in this preview source snapshot)
  - optionally disable comments if not wanted for this post type

### Featured image asset created: linguistic-features post
- Created a new first-party featured/social image for the linguistic-features post:
  - [`blogposts/images/linguistic-features-featured.png`](C:\Development\lebanese-arabic\SEO\blogposts\images\linguistic-features-featured.png)
- Added a reproducible generator script:
  - [`blogposts/images/generate_linguistic_features_featured.py`](C:\Development\lebanese-arabic\SEO\blogposts\images\generate_linguistic_features_featured.py)
- Output specs:
  - `1200x630` PNG
  - style aligned with recent first-party featured-image direction
  - branding kept as `Lebanese Arabic with Hiba`
- Follow-up refinement applied:
  - reduced right-side pill and arc visual scale slightly
  - shifted the right-side graphic cluster slightly to the right for better balance

### Internal-link map drafted for linguistic-features post
- Reviewed current source snapshots for:
  - [`blogposts/linguistic-features-source-code.txt`](C:\Development\lebanese-arabic\SEO\blogposts\linguistic-features-source-code.txt)
  - [`blogposts/is-lebanese-a-language-or-dialect-source-code.txt`](C:\Development\lebanese-arabic\SEO\blogposts\is-lebanese-a-language-or-dialect-source-code.txt)
  - [`blogposts/closest-dialect-source-code.txt`](C:\Development\lebanese-arabic\SEO\blogposts\closest-dialect-source-code.txt)
- Found that the linguistic-features preview currently has no in-body editorial links.
- Proposed outbound links from linguistic-features (technical hub behavior):
  - to `/blog/is-lebanese-a-language-or-dialect/` from a Levantine-classification sentence
  - to `/closest-arabic-dialect-to-msa/` from MSA/diglossia discussion
  - optional to `/lebanese-lessons/` only as a single soft CTA in conclusion
- Proposed inbound links to linguistic-features from existing relevant posts using already-present phrases:
  - from language-vs-dialect post via `structural classification`, `vocabulary or grammar`, or `Levantine Arabic continuum`
  - from closest-to-MSA post via `linguistic morphology and syntax` or `shared vocabulary and lexical cognation`
- Purpose: strengthen topical cluster depth and reduce reliance on only related-post widgets for contextual internal linking.

### Ubersuggest AI-visibility export review (11-04-2026)
- Reviewed new exports in [`ubersuggest-ai-visibility/11-04-2026/`](C:\Development\lebanese-arabic\SEO\ubersuggest-ai-visibility\11-04-2026), including:
  - brand/prompt AI visibility CSVs
  - competitor/common keyword CSVs
  - keyword gap CSVs
  - backlinks opportunity CSVs
- Brand-level change vs 2026-03-19 snapshot:
  - `Lebanese Arabic with Hiba`: visibility `10 -> 25`
  - mentions `2 -> 5`
  - avg rank `4.0 -> 3.2`
- Prompt-level finding:
  - currently visible in 3 prompts (`beginners`, `group classes`, `immersive experiences`)
  - zero visibility in 7 prompts
- Highest-value zero-visibility prompts that match current service offer:
  - live tutoring with native speakers
  - private lessons tailored to adults
  - flexible scheduling for lessons
  - lessons with cultural context
- Non-fit prompt caution:
  - avoid overclaiming for `certified programs`, `apps`, or `subscription services` unless these offers are actually present.
- Next recommended action:
  - run a targeted content/FAQ prompt-match pass on [`/lebanese-lessons/`](https://lebanese-arabic.com/lebanese-lessons/) before starting broader new-page expansion.

## Open Next Steps
- Run AI-prompt-fit optimization on [`/lebanese-lessons/`](https://lebanese-arabic.com/lebanese-lessons/) for the 4 high-fit zero-visibility prompt themes
- Recheck AI visibility prompt export after recrawl/indexing to confirm whether zero-visibility prompts begin mentioning `Lebanese Arabic with Hiba`
- Continue `/books/` commercialization + intent alignment pass for `lebanese arabic books`
- Reassess priorities when Semrush and Ahrefs exports are added

## Logging Rule
Future SEO work should append short entries here covering:
- what was analyzed
- what changed
- why the change was made
- what page or report was affected
- what open follow-up remains
