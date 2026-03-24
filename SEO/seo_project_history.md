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
  - `thumbnailUrl`
  - `og:image`
  - `twitter:image`
- Remaining metadata mismatch:
  - Yoast `Article.headline` and breadcrumb item still use the old historical title `Decoding Lebanese Family Terms: From Parents to Cousins`
  - visible title, SEO title, description, and social image are otherwise aligned

## Open Next Steps
- Improve [`/lesson2/`](https://lebanese-arabic.com/lesson2/) for `afwan` intent clarity without turning it into a duplicate of `lesson40`
- Improve [`/lesson1/`](https://lebanese-arabic.com/lesson1/) for the hello/hi cluster
- Improve [`/lesson12/`](https://lebanese-arabic.com/lesson12/) for family-word near wins
- Improve [`/lesson4/`](https://lebanese-arabic.com/lesson4/) for money-related phrasing
- Reassess priorities when Semrush and Ahrefs exports are added

## Logging Rule
Future SEO work should append short entries here covering:
- what was analyzed
- what changed
- why the change was made
- what page or report was affected
- what open follow-up remains
