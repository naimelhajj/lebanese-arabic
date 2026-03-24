# PPC Campaign Analysis: "V2 Spearhead" (Jan 4 - Jan 12, 2026)

**Date Range:** January 4, 2026 - January 12, 2026
**Data Source:** Microsoft Clarity Session Recordings
**Filter:** URLs matching `ppc-` (capturing `ppc-trial-offer` variants)

---

## 1. Executive Summary

*   **Total Sessions Analyzed:** ~55 (Sample set from filtered recordings)
*   **Confirmed Conversions:** 1 (`Ad 2 - Social Proof - JD Video`)
*   **Dominant Traffic Source:** Facebook Mobile (`m.facebook.com`)
*   **Winning Creative:** **Ad 2 - Social Proof - JD Video** is the undisputed driver of engagement and the *only* source of conversion.
*   **Critical Issue:** **"Hook Failure" remains high.** A significant portion (~40%) of traffic bounces in under 5 seconds, indicating the landing page still struggles to capture "snap judgment" attention for many users.

---

## 2. Traffic & Creative Performance

### Ad Creative Breakdown (by UTM Content)
*   **Ad 2 - Social Proof - JD Video:** **Dominant.** Accounts for ~70% of identifiable ad traffic.
    *   *Result:* Generated the ONLY confirmed sale.
    *   *Behavior:* Users dwell longer (avg 30s - 1m) compared to other ads.
*   **Ad 1 - Founder - Group Photo:** **Weak.**
    *   *Result:* Zero conversions.
    *   *Behavior:* Mostly high-bounce traffic (3s, 4s, 52s).
*   **Ad 3 - Product Preview - Video:** **Negligible.**
    *   *Result:* Very few sessions recorded.
    *   *Behavior:* Quick abandonment (14s).
*   **Direct Action Video:** **Mixed.**
    *   *Result:* Some engagement (14m session - likely idle), but no conversions.

### Anomalies Detected
*   **Newsletter Traffic:** Several sessions (`utm_source=newsletter`) landed on this PPC page. This suggests a link in a recent email ("New Year gift") points here. These users generally bounced quickly (0-3s).
*   **Admin Traffic:** At least one session involved a user clicking "Edit Page" and referring from `wp-admin`. These are internal team views and have been excluded from performance metrics.

---

## 3. Behavioral Analysis

### The "Hook Failure" Metric
Defining "Hook Failure" as a session lasting **< 10 seconds** (user lands, scans, and immediately leaves/closes).

*   **Failure Rate:** ~45% of total sessions.
*   **Implication:** The Hero Section (Headline + Video/Image) is failing to convince nearly half of all visitors to scroll or engage. The "snap judgment" is "NO."

### The "Engaged" User Profile
When users *do* pass the 10-second mark, engagement improves significantly:
*   **Scroll & Read:** Users with 30s+ duration are reading testimonials.
*   **Click Maps:**
    *   "Real Results from Real Students" (Testimonial headers).
    *   "Book Your $15 Risk-Free Trial" (Primary CTA).
    *   FAQ Accordions (implied by duration).

---

## 4. Conversion Deep Dive: The Winning Session

**Session ID:** `w1qoot/w102mf`
**Date:** Jan 9, 06:07 AM
**Source:** Facebook Mobile (`m.facebook.com`)
**Ad:** `Ad 2 - Social Proof - JD Video`

**User Journey:**
1.  **Landing:** User arrives on `ppc-trial-offer`.
2.  **Engagement:** Spends **3 minutes 16 seconds** on the page. This is a *massive* dwell time, implying deep reading of copy and watching of testimonial videos.
3.  **Action:** Clicks "Book Your $15 Risk-Free Trial".
4.  **Conversion:** Successfully lands on `/trial-payment-confirmed/`.
5.  **Post-Conversion:** Returns to the offer page briefly (likely hitting "Back" or checking details).

**Takeaway:** The funnel *works* technically. The friction is removed. The challenge is purely **persuasion** (getting more users to stay past 10 seconds).

---

## 5. Strategic Recommendations

1.  **Kill "Ad 1" & "Ad 3":** Stop spending money on "Founder" and "Product Preview" angles. They are not generating engaged traffic. Consolidate budget into "Ad 2 - Social Proof".
2.  **Hero Section Iteration:** The high <10s bounce rate points to a weak Hero.
    *   *Test:* A/B test the **Headline** on the landing page.
    *   *Current:* (Likely transactional).
    *   *Test Variant:* Use a strong "Social Proof" headline matching the winning ad (e.g., *"Join the students speaking confident Lebanese after just 4 weeks"*).
3.  **Investigate Email Link:** Check the "New Year" newsletter. If it links to this PPC page, ensure the messaging matches. High bounce rates from email suggest a mismatch in expectation vs. reality.
