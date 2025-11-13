# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Lebanese Arabic Language Learning Business** - Online language lessons with a trial-to-package conversion model.

- **Business Model**: $15 trial lessons → 50% convert to full packages (avg $89) → LTV: $104
- **Current Focus**: Optimizing organic traffic conversion through systematic A/B testing
- **Strategic Approach**: Data-driven, iterative experimentation with detailed documentation

## Architecture

### Static HTML-First Design

- **No build system** - All pages are standalone HTML files with inline CSS/JS
- **No backend** - JotForm handles all form processing and payment integration
- **Deployment**: Static files served directly (WordPress-hosted)

### Directory Structure

```
C:\development\lebanese-arabic/
├── landing pages/
│   ├── frictionless versions/          # Trial booking page variants
│   │   ├── reserve-lebanese-trial.html
│   │   ├── reserve-lebanese-trial-v2.html  (current active)
│   │   └── v3-final-implementation.html    (social proof variant)
│   └── organic lebanese-lessons variants/
│       └── lebanese-lessons-v2.html        (WordPress/Yoast SEO optimized)
├── lead generation/
│   └── [JotForm exports and lead data]
├── Home-V2/                               # Homepage optimization project
│   └── home-v2_cro_seo_report.md         # Intent router strategy
├── surgical_strike_module*.html           # CTA module A/B test variants (v1-v9)
├── lebanese-lessons-risk-free.html        # Main "spear" conversion page (1,471 lines)
├── current_strategic_plan.md              # Current strategic directive
└── Project History.md                     # Complete historical record of all pivots
```

### Key Pages

- **Main conversion page**: `lebanese-lessons-risk-free.html` (The "Spearhead")
- **Active trial booking**: `landing pages/frictionless versions/reserve-lebanese-trial-v2.html` (392 lines)
- **Organic SEO variant**: `landing pages/organic lebanese-lessons variants/lebanese-lessons-v2.html`

## Core Technical Patterns

### File Naming Conventions

- **Landing pages**: `[purpose]-[variant]-[version].html`
  - Example: `reserve-lebanese-trial-v2.html`
- **A/B test variants**: `surgical_strike_module_v[1-9].html`
- **Organic pages**: Include WordPress/Yoast SEO metadata

### JotForm Integration

All lead capture and payment processing uses JotForm iframe embeds:

```html
<!-- Standard pattern -->
<iframe
  id="jf_iframe"
  data-src="https://form.jotform.com/252822451108047"
  loading="lazy"
  allow="geolocation; microphone; camera; payment"
  style="min-width:100%;max-width:100%;border:none;">
</iframe>
```

**Form ID**: `252822451108047`

**UTM Parameter Passthrough**: All forms capture campaign parameters via JavaScript:

```javascript
function buildSrc(){
  const base = new URL(iframe.dataset.src);
  const params = new URLSearchParams(window.location.search);
  params.forEach((v,k) => base.searchParams.set(k,v));
  return base.toString();
}
```

**Lazy-load pattern**: Forms load on scroll using Intersection Observer for performance.

### Analytics & Tracking

**Custom data attributes** for conversion tracking:

```html
<button data-analytics="cta_surgical_strike">Book Your Trial</button>
<a data-analytics="cta_hero" href="#contact-form">Start Learning</a>
```

**Integrated services**:
- JotForm for forms/payments
- PixelYourSite for pixel tracking
- WordPress/Yoast SEO on organic pages
- Microsoft Clarity for session recordings (mentioned in strategic docs)

### CSS Design System

```css
:root {
  --primary-color: #1c5c4e;      /* Lebanese green/teal */
  --secondary-color: #f4e7d0;    /* Warm cream */
  --accent-color: #dc2626;       /* Risk-free red */
  --text-dark: #111827;
  --text-light: #4b5563;
}
```

**Layout patterns**:
- Mobile-first responsive design
- `clamp()` for fluid typography
- Inline styles (no external CSS)
- `prefers-reduced-motion` support

### "Risk-Free" Offer Block Pattern

This block appears consistently across pages:

```html
<div style="background:rgba(235, 255, 240, 0.95);border:2px solid #dc2626;...">
  <h2>Your $15 Trial Is Now Risk-Free</h2>
  <p>Love your trial lesson and decide to purchase a package?
     We'll credit the full $15 towards your purchase.</p>
  <a href="/lebanese-lessons/">Book Your Risk-Free Trial</a>
</div>
```

## Strategic Documentation System

This project is **heavily documentation-driven**. All major decisions are recorded in markdown files.

### Key Strategic Documents

1. **`current_strategic_plan.md`** - Active strategy and next steps
   - Contains phases, timelines, and specific tactical directives
   - Currently on hold awaiting user input

2. **`Project History.md`** - Complete historical record
   - 15+ documented phases with dates
   - Records all pivots, A/B tests, and their outcomes
   - Tracks key metrics (LTV, CPP thresholds, conversion rates)

3. **`Home-V2/home-v2_cro_seo_report.md`** - Homepage optimization strategy
   - "Intent router" design with 3-card pathway system
   - SEO alignment to top queries (e.g., "learn lebanese arabic")
   - 8-section homepage structure

4. **Agency Reports** (in `agency-reports/`)
   - Stakeholder performance dashboards
   - Campaign analysis and recommendations

### Strategic Patterns

**RED/YELLOW/GREEN LIGHT Framework** (from Phase 7):
- **GREEN**: Cost Per Purchase (CPP) < $40 = Success
- **YELLOW**: CPP $40-80 = Monitor closely
- **RED**: CPP > $80 = Failure (LTV is $104)

**Current Active Test** (from Phase 16, Nov 8, 2025):
- **Test**: "Surgical Strike" A/B test on `/lesson15/`
- **Variants**: Original page (A) vs. new "Surgical Strike" module (B)
- **Objective**: Find optimal CTA to drive conversions on high-traffic organic page
- **Duration**: 14-day sprint (Nov 8-22)
- **Success metric**: Total revenue generated per variant (minimum 2 conversions required)

## Working in This Codebase

### Making Changes to Landing Pages

1. **Always read the full file first** - Pages contain critical inline CSS and JS
2. **Check `current_strategic_plan.md`** - Understand active strategy before modifying
3. **Review `Project History.md`** - Avoid repeating past failures
4. **Test JotForm integration** - Verify iframe loading and parameter passing
5. **Maintain "Risk-Free" messaging** - This is a core conversion element

### Creating New Variants

When creating A/B test variants:

1. **Use version suffixes**: `surgical_strike_module_v10.html` (next available number)
2. **Add tracking attributes**: `data-analytics="[descriptive_name]"`
3. **Preserve JotForm integration**: Copy entire iframe + lazy-load JS block
4. **Document in strategic plan**: Update `current_strategic_plan.md` with test details
5. **Log the hypothesis**: Record what you're testing and why

### A/B Testing Workflow

The project uses **file-based A/B testing** (not code splits):

```
1. Create variant file (e.g., surgical_strike_module_v10.html)
2. Deploy both files to server
3. Use server-side redirect (50/50 split) or manual URL distribution
4. Track conversions via JotForm submissions + analytics attributes
5. Document results in Project History.md
6. Roll out winner to 100% traffic
```

### SEO Optimization

For organic pages (served through WordPress):

- **Include Yoast SEO metadata**:
  ```html
  <!-- Yoast SEO Premium plugin -->
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://lebanese-arabic.com/page-name/" />
  ```
- **Add JSON-LD structured data**:
  ```json
  {
    "@type": ["SoftwareApplication", "LearningResource"],
    "name": "Page Title",
    "applicationCategory": "EducationalApplication",
    "inLanguage": ["ar-LB", "en"]
  }
  ```
- **Align to top queries**: "learn lebanese arabic" (pos 1.9, 230 clicks), "lebanese arabic lessons" (pos 1.2, 72 clicks)

### Git Workflow

Recent commits show this pattern:

```bash
# Strategic documentation updates
git commit -m "docs(strategy): Update plan with homepage diagnostic"

# Feature launches
git commit -m "feat(marketing): Finalize 'Surgical Strike' module and optimize lesson page"

# Historical corrections
git commit -m "docs: Restore full project history to master strategic plan"
```

**Branching**: Currently on `main` branch with no configured remote main branch.

## Performance Optimization

### Critical Patterns

1. **DNS prefetch for JotForm**:
   ```html
   <link rel="dns-prefetch" href="//form.jotform.com">
   <link rel="preconnect" href="https://form.jotform.com" crossorigin>
   ```

2. **Intersection Observer for lazy iframe loading**:
   ```javascript
   new IntersectionObserver((entries) => {
     entries.forEach(entry => {
       if (entry.isIntersecting) {
         iframe.src = buildSrc();
         observer.disconnect();
       }
     });
   }).observe(jf_iframe);
   ```

3. **Minimal external dependencies** - All CSS/JS inline to reduce requests

## Multi-AI Development Setup

This project is configured for **multiple AI coding assistants**:

- **Cline**: `.clinerules/cline_rules.md`
- **Cursor**: `.cursor/mcp.json`
- **Windsurf**: `.windsurf/mcp.json`
- **Roo**: `.roo/mcp.json`
- **Gemini**: `GEMINI.md` (identical to Task Master AI integration)

### Task Master AI Integration

If Task Master AI is configured (see `AGENTS.md` and `GEMINI.md`):

```bash
# View tasks
task-master list

# Get next task
task-master next

# Mark task complete
task-master set-status --id=<id> --status=done
```

**Note**: Task Master setup files exist in documentation, but no `.taskmaster/` directory is currently present in the working directory.

## Important Context for Claude Code

### Business Constraints

- **Cash-constrained operation** - Every decision focuses on ROI and cash flow
- **Failed paid campaigns** - Organic traffic is the primary reliable channel
- **50% trial-to-package conversion** - This is the key metric driving strategy

### What NOT to Do

- ❌ **Don't create new "theoretical" variants** - Only create pages when explicitly requested
- ❌ **Don't modify strategic documents** without understanding full context
- ❌ **Don't break JotForm integration** - This is the only payment mechanism
- ❌ **Don't remove "Risk-Free" messaging** - It's a proven conversion element
- ❌ **Don't suggest paid campaigns** - Recent paid tests failed (see Phase 15)

### What TO Do

- ✅ **Read strategic docs first** - Understand the business context
- ✅ **Preserve working patterns** - JotForm integration, lazy-load, tracking
- ✅ **Document all changes** - Update strategic plan when making significant changes
- ✅ **Focus on organic optimization** - Homepage and high-traffic pages like `/lesson15/`
- ✅ **Test incrementally** - Small, measurable changes with clear hypotheses

## Quick Reference

### File Paths You'll Use Often

- Main conversion page: `C:\development\lebanese-arabic\lebanese-lessons-risk-free.html`
- Strategic plan: `C:\development\lebanese-arabic\current_strategic_plan.md`
- Project history: `C:\development\lebanese-arabic\Project History.md`
- Homepage strategy: `C:\development\lebanese-arabic\Home-V2\home-v2_cro_seo_report.md`

### Key Metrics to Know

- **LTV**: $104 per customer ($15 trial + $89 avg package)
- **Trial-to-Package Conversion**: 50%
- **CPP Threshold (RED LIGHT)**: $80
- **Top Organic Page**: `/lesson15/` (high traffic, currently being A/B tested)

### CTA Standardization

Per `home-v2_cro_seo_report.md`:

- **Primary CTA**: "Book Your $15 Trial" → `/lebanese-lessons/`
- **Secondary CTA**: "Explore Free Lessons" → `/#popular-lessons`
- **Inline micro-link**: "Try a $15 risk-free trial" → `/lebanese-lessons/`

Avoid mixing labels like "Lessons / Online Classes / Online Lessons" - use the standardized CTAs above.

---

**Last Updated**: 2025-11-09
**Current Phase**: Phase 16 - "Surgical Strike" A/B Test (LIVE, Nov 8-22)
**Status**: Awaiting daily reporting of variant performance
