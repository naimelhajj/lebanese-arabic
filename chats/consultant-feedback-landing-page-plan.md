# Consultant Feedback — Trial Booking Landing Page Plan

## Objective
- Reduce leaks and increase session → paid trial conversions by answering decision‑critical questions on the page, before the booking form, without sending users elsewhere.

## Decisive Recommendation
- Ship a single conversion‑focused page now. Structure content into six blocks (below), keep details in accordions/modals, repeat CTAs after each block, and avoid outbound links until after purchase.

## What To Include (high‑impact)
- How It Works (3 steps)
  - 1) Pick a time  2) Pay $15 securely  3) Meet your teacher and get a plan.
  - Removes uncertainty; shortens time to action.
- Trial Value Proposition (what’s included)
  - 55‑minute live lesson with a native teacher, level check, personalized plan, $15 credit valid 10 days.
- Choose Your Path (Prepared vs Conversational)
  - Prepared: step‑by‑step grammar & vocabulary to build foundations.
  - Conversational: real‑life topics to speak confidently with family/friends.
- High‑Trust Cues (above the fold)
  - “10 yrs online teaching”, 2–4 short testimonials, “Secure checkout by Stripe”, time‑zone clarity.
- Focused FAQ (accordion)
  - Scheduling/weekly slots, working hours (Beirut time), teacher choice, method/materials, Zoom requirements, level placement, trial credit.
- Minimal Pricing Snapshot (compact)
  - Singles + bundles for Prepared/Conversational; group pricing via modal. Default collapsed.

## Page Order (no‑leak funnel)
1) Hero: headline + subtext + trust pills (Stripe, time‑zone, years) + primary CTA to form.
2) How It Works (3 steps) → CTA repeat.
3) Trial Value Proposition → CTA repeat.
4) Choose Your Path (Prepared vs Conversational) → CTA repeat.
5) Pricing Snapshot (collapsed) + inline Policies microcopy (no outbound links).
6) Meet Our Teachers (2–3 cards, real photos/bios) → CTA repeat.
7) FAQ (accordion, 6–8 items) → final CTA.
8) Booking section: existing lazy‑loaded JotForm embed with sticky mobile CTA.

## Copy / Source Map (repo references)
- Steps + FAQ seeds: `v1.txt` (multiple sections referenced in internal notes).
- Path one‑liners + trial explainer: `v2.txt`, `v3.txt`.
- Pricing structure + modal pattern: `v3.txt`.
- Existing booking block to embed/anchor: `new booking html block.html`.
- Planning rationale: `landing_page_improvement_plan.md`, `new-booking-block-additions.md`.

## UX / Content Details
- Zero‑leak design: use accordions/modals for details; omit header/footer nav in this funnel.
- Sticky mobile CTA “Book $15 Trial” (anchors to booking form). Repeat CTA after each major block.
- Policies inline (microcopy near CTAs): “Free reschedule ≤24h. No‑show forfeits. Secure checkout by Stripe. $15 credit valid 10 days.”
- Time‑zone clarity near any scheduling mention: “All times shown in Beirut time (auto‑converted).”
- Performance: keep the current lazy‑loaded JotForm; inline scoped CSS; compress teacher images; defer anything non‑critical.

## Measurement & Guardrails
- Events (via GTM data attributes): `cta_click`, `faq_open`, `scroll_75`, `slot_select`, `begin_checkout`, `purchase_trial`, `nav_link_click`.
- Simple A/B: `?v=A|B` toggles FAQ depth/pricing default; pass `variant` into a hidden JotForm field for attribution.
- Success target: +15–25% uplift in session → paid trial within 2 weeks at steady traffic.
- Guardrails: zero console errors; mobile CLS < 0.1; maintain page speed.

## Risks & Mitigations
- Pricing snapshot causes analysis paralysis → default collapsed; show “from $X”; reveal full price list in modal.
- Generic trust cues feel stock → use real teacher photos/names or keep text‑only; avoid obvious stock imagery.
- Time‑zone confusion → state Beirut time consistently; echo auto‑conversion near the form.
- Content sprawl → keep all detail on‑page; no external links pre‑purchase.

## Assumptions & Unknowns
- Baselines: current visit→form‑start and form‑start→submit rates, by device/source (needed to size the lift).
- Form integration: confirm live JotForm ID/URL and whether embed vs deep‑link is required.
- Assets: approved teacher photos/bios and any testimonials allowed for use.
- Publishing: confirm target (WordPress/Gutenberg vs static file for test traffic).

## Implementation Notes
- Reuse the existing lightweight embed (`new booking html block.html`) for the booking section; do not modify vendor JS (`lead generation/.../js/vendor/`).
- Place details in accordions/modals; repeat CTAs after each section; keep hero trust pills concise.
- Source copy from `v1.txt`, `v2.txt`, `v3.txt` per the mapping above; refine for brevity and match ad promises.

## Next Steps
1) Assemble `reserve-lebanese-trial.html` with the sections/order above and wire to the JotForm.
2) Add hidden `variant` field; propagate URL params into the form.
3) Tag events via data attributes; verify in GTM preview.
4) Validate locally (desktop/mobile), ensure zero console errors, and run an HTML validator.
5) Route a controlled traffic slice; monitor submit rate, bounce, and guardrails; iterate.

