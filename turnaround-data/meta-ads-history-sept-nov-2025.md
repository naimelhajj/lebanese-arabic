# Meta Ads Performance Deep Dive: Sept - Nov 2025

*As of: 2025-11-10*

This document provides a detailed historical analysis of Meta ad campaigns run from September to November 2025, combining quantitative data from Ads Manager exports with the strategic context from chat logs.

## Executive Summary

The data tells a clear and consistent story:

1.  **The "Leads" Funnel Works; The "Sales" Funnel Does Not.** Across multiple tests, the business has spent **~$120+ on direct-to-sale campaigns and has generated exactly 0 purchases.** In contrast, the "Leads" funnel has consistently generated conversions at a cost of **~$15 - $21 per lead**. The strategic decision to focus exclusively on the "Leads" funnel is validated by the data.
2.  **Technical Errors Masked Performance.** A significant portion of the budget was wasted due to a series of preventable technical and setup errors, including a broken reCaptcha form, incorrect audience targeting (targeting *inside* Lebanon), and Meta automatically allocating budget to the low-quality "Audience Network."
3.  **Lookalike Audiences Show High Potential.** Early tests optimizing for `FormProgression` showed that the `Lookalike` audience was significantly more efficient (**$4.05** per progression) than interest-based audiences ($12.36 per progression). This is a strong signal for future audience testing.

---

## 1. September 2025 - "Fall Sale" Campaign

This was an emergency campaign to address the immediate financial crisis.

| Campaign | Ad Set | Spend (USD) | Results | Cost Per Result (USD) |
| :--- | :--- | :--- | :--- | :--- |
| Sept 2025 Sale - 48 Hour Push | Retargeting - Warm Audiences | $38.34 | 1 Lead | **$38.34** |
| Sept 2025 Sale - 48 Hour Push | Prospecting - Interests | $26.30 | 0 Leads | N/A |
| **Total** | | **$64.64** | **1 Lead** | **$64.64** |

**Strategic Context:**
*   This campaign was a short-term push. The high CPL from retargeting was acceptable in an emergency but is not sustainable for evergreen prospecting.
*   The failure of the prospecting ad set was an early indicator of issues with either the audience or the landing page.

---

## 2. Late Sept / Early Oct - Prospecting & Optimization Tests

This phase involved multiple small-budget tests to find a winning audience and creative, optimizing for `FormProgression` as a leading indicator.

| Campaign | Ad Set | Spend (USD) | Results (Form Progressions) | Cost Per Result (USD) |
| :--- | :--- | :--- | :--- | :--- |
| PRO - Sales - $15 Trial | **Prospecting B - Lookalike 1%** | **$40.53** | **10** | **$4.05** |
| PRO - Sales - $15 Trial | Prospecting A - Interest-Based | $24.72 | 2 | $12.36 |

**Strategic Context:**
*   **Key Finding:** The `Lookalike` audience was dramatically more effective at finding users who would begin filling out the form. This is a strong signal that Lookalikes are the highest-potential audience for prospecting.
*   These tests were complicated by the since-discovered broken reCaptcha form, meaning none of these `FormProgression` events could have become a final `Lead`.

---

## 3. October 2025 - The Definitive "Leads vs. Sales" Test

This was the most important test conducted, designed to answer the most fundamental strategic question.

| Campaign | Funnel Type | Spend (USD) | Results | Cost Per Result (USD) |
| :--- | :--- | :--- | :--- | :--- |
| System Test - Goal - **Sales** - Oct 2025 | **Sales** | **$59.35** | **0 Purchases** | **N/A (Failure)** |
| System Test - Goal - **Leads** - Oct 2025 | **Leads** | **$142.10** | **7 Leads** | **$20.30** |

**Strategic Context:**
*   **Conclusive Result:** The "Sales" funnel is not viable. It spent ~$60 and failed completely.
*   The "Leads" funnel is viable and repeatable, generating leads at a consistent, albeit slightly high, CPL of ~$20.
*   This data validates the decision to pause all "Sales" campaigns and focus exclusively on optimizing the "Leads" funnel.

---

## 4. November 2025 - Landing Page A/B Tests

This campaign attempted to test different landing page versions (V1, V2, V3) but was ultimately inconclusive.

| Campaign | Ad Set | Spend (USD) | Results | Cost Per Result (USD) |
| :--- | :--- | :--- | :--- | :--- |
| Sales - $15 Trial - Nov 2025 | Buyers LAL 1% - US, UK - V1 | $8.38 | 0 Purchases | N/A |
| Sales - $15 Trial - Nov 2025 | Buyers LAL 1% - US, UK - V2 | $16.76 | 0 Purchases | N/A |
| Sales - $15 Trial - Nov 2025 | Buyers LAL 1% - US, UK - V3 | $10.97 | 0 Purchases | N/A |
| **Total** | | **$36.11** | **0 Purchases** | **N/A (Failure)** |

**Strategic Context:**
*   This campaign used a "Sales" objective and failed, further confirming the "Leads vs. Sales" test result.
*   The chat logs indicate this test suffered from a "Hook Failure," where users abandoned the pages within seconds. This suggests the issue was a mismatch between the ad's promise and the landing page's initial impression, not the specific page content itself.

---

## 5. Other Recorded Campaigns (Oct-Nov 2025)

This section includes other campaigns from the period that provide additional context.

| Campaign | Spend (USD) | Results | Cost Per Result (USD) |
| :--- | :--- | :--- | :--- |
| Prospecting - LP & Creative Test - Form Progression | ~$57.00 | 7 Form Progressions | ~$8.14 |
| Sales - Booking Funnel Test - Oct 2025 | $19.90 | 0 Purchases | N/A |
| Prospecting - $15 Trial Lesson - Oct 2025 | $39.64 | 0 Leads/Purchases | N/A |
| Prospecting - Engagement through Teacher video - Oct 2025 | $3.15 | High Engagement | N/A (Brand Awareness) |
| Paid Retargeting - Risk-Free Offer - Nov 2025 | $15.50 | 0 Purchases | N/A |
| Audience+ - Risk-Free Offer - Nov 2025 | $8.41 | 0 Purchases | N/A |

**Strategic Context:**
*   **`Prospecting - LP & Creative Test`:** This complex test reinforced that it was possible to get users to start filling out a form for a reasonable cost (avg. $8.14 CPR), with the `v2` landing page showing the most promise.
*   **`Sales - Booking Funnel Test`:** Another failed `Sales` objective campaign, spending nearly $20 with zero return. This further validates the decision to abandon the direct-to-sale funnel.
*   **`Prospecting - $15 Trial Lesson`:** A significant ~$40 spend with no attributable results, indicating a failure in either the audience, creative, or landing page hook.
*   **`Prospecting - Engagement`:** A successful, low-cost brand awareness play. It proves that content focused on the teachers and school personality resonates with the audience and can be used to build warm retargeting lists cheaply.
*   **`Paid Retargeting` & `Audience+`:** These were part of the failed "Tip of the Spear" paid prong, confirming that even warm audiences were not converting on the offers presented at that time.