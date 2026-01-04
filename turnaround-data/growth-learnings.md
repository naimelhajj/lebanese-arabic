# Growth Learnings Log

This document is the single source of truth for everything we learn about the business, its customers, and what makes them convert. We will update this after every experiment.

---

## Guiding Principles

*   **Speed & Data > "Big Bang" Perfection:** Small, rapid, measurable tests are proving more effective than large, slow projects.
*   **Friction is the Enemy:** The single biggest lever we've found is reducing steps in the conversion process (e.g., moving from manual lead follow-up to a direct booking form).
*   **Log Every Learning:** Every experiment, pass or fail, teaches us something. We will record it here.

---

## Audience Insights

*   **The "Organic Explorer" Persona (CONFIRMED Nov 11, 2025):** Analysis of two separate converting users (including User `9bt7rl`) confirms that when faced with friction or uncertainty, users will often navigate back to the homepage to re-orient and build trust before completing a purchase. They do not follow a perfectly linear path.

---

## Offer & Pricing Insights

*   **Two-Price Strategy is Viable (Learned Nov 11, 2025):** We can successfully offer different prices to different segments.
    *   **$10 Trial:** Converts warm, recent leads via email (Wave 1 Win-Back).
    *   **$15 Trial:** Converts anonymous, organic traffic.
*   **"Risk-Free" Angle is Strong (Learned Nov 11, 2025):** The concept of crediting the trial fee towards a full package is a powerful risk-reversal. The offer is compelling enough to make a user attempt to purchase four separate times, overcoming technical friction and a 9-minute "cart abandonment" period (User `9bt7rl`).
*   **Competitor Pricing is a Major Objection (Learned Nov 11, 2025 - Deng's Case):** Even with personalized follow-up, leads will churn if they perceive competitor rates as more "affordable." This highlights a need to either justify our pricing, offer more competitive entry points, or better articulate value.

---

## Channel & Funnel Insights

*   **Direct Booking Form is Validated (Learned Nov 7-11, 2025):** The frictionless Jotform that allows direct payment is a proven conversion mechanism, responsible for both our recent email sale and organic sale. The old manual follow-up process is obsolete.
*   **Homepage is the "Safety Net" (Learned Nov 11, 2025):** When users encounter friction or are uncertain, they retreat to the homepage to re-orient. This makes the homepage the most critical asset for rebuilding and redirecting user intent.
*   **Conversion Funnel Abandonment is Happening (Learned Nov 11, 2025 - User `9bt7rl`):** A converting user showed strong intent by visiting the `/lebanese-lessons/` conversion page multiple times over a ~10 minute period before finally completing the purchase. This behavior, analogous to cart abandonment, shows that even highly motivated users can get distracted or delayed. This indicates an opportunity for future recovery tactics.
*   **Win-Back Email Campaigns Work (Learned Nov 11, 2025):** Wave 1, targeting recent (post-August) unconverted leads with a low-friction $10 offer, generated a sale within 24 hours. This is a valid, zero-cost revenue channel.
*   **Long-Dormant Leads Can Be Reactivated with a Strong Offer (Learned Nov 11, 2025 - Dina Dada's Case):** Dina Dada, a lead from 2020, converted to a $15 trial after receiving a targeted email campaign and confirming the availability of a trial lesson. This demonstrates the power of a compelling offer and re-engagement.
*   **Cold Reactivation Email Campaigns Do NOT Work (Learned Nov 11, 2025):** Wave 3, targeting old (pre-August) cold leads, resulted in zero clicks and zero sales from over 100 sends. This channel is not worth further investment at this time.
*   **The "Hook -> Hub -> Checkout" Model (Learned Nov 11, 2025):** Based on the "Organic Explorer" insight, the optimal path for converting organic traffic is not a direct link from a content page ("Hook") to the checkout. The best path sends them to a high-context page with social proof first (the "Hub," i.e., `home-v2`), which then links to the final checkout page. This is the strategy we will test after the current A/B test concludes.

---

## Technical & Tracking Insights

---

## Chronological Log

*   **Nov 11, 2025 - User `9bt7rl` (Successful Conversion):**
    *   **Summary:** User entered on the homepage and quickly navigated to the `/lebanese-lessons/` conversion page. They showed strong but delayed intent, clicking the "Book Your Risk-Free Trial" button multiple times over a ~10 minute period before finally converting. During this time, they retreated to the homepage to re-orient before successfully navigating back to complete the purchase.
    *   **Learning:** This is the second recorded instance of the "Organic Explorer" persona, strongly validating the "Hook -> Hub -> Checkout" model. It also confirms that conversion funnel abandonment is occurring and that the "Risk-Free Trial" offer is strong enough to overcome significant friction.
*   **Nov 11, 2025 - Dina Dada's Case (Successful Conversion):**
    *   **Summary:** Long-dormant lead (initial inquiry 2020) re-engaged via application form Oct 2025, then converted to a $15 trial via the "New Leads" email campaign. Explicitly asked about the "$15 class" (trial lesson).
    *   **Learning:** The $15 trial offer is a powerful re-engagement tool. The "trial lesson" concept is highly appealing and can reactivate even very old leads. The previous "no trial lessons" policy was a significant barrier.
*   **Nov 11, 2025 - Deng's Case (Lost Lead - Price Objection):**
    *   **Summary:** Lead inquired about availability, received personalized options, but ultimately churned due to finding "affordable rates somewhere else."
    *   **Learning:** Competitor pricing is a significant objection. Even with personalized service, a perceived price disadvantage can lead to lost sales. This highlights a need to either justify our pricing, offer more competitive entry points, or better articulate value against competitors.
*   **Dec 15, 2025 - Meta Platform Divergence & Mobile UX (Analysis of Dec 3-15 Data):**
    *   **Summary:** A detailed audit of the "V2 Spearhead" campaign revealed a stark contrast. Instagram traffic had a near-instant bounce rate (1-4s), while Facebook traffic showed deep engagement (20s-6m). This led to the strategic decision to kill IG ads and consolidate budget on FB.
    *   **Learning 1 (Platform Split):** Instagram users in this niche/creative mix are "Accidental Clickers." Facebook users are "Readers." Optimizing for the latter is the path to profitability.
    *   **Learning 2 (Mobile Friction):** Clarity logs showed frequent "Resized page" events on Facebook mobile sessions, indicating a "Pinch-to-Zoom" necessity. We must use larger base fonts (18px+) for mobile readability.
    *   **Learning 3 (Dead Clicks):** Users attempted to click on non-interactive "Trust Metrics" (e.g., "400+ Learners"). We must make these elements clickable links that scroll to the social proof section to satisfy this skepticism.

---

## Technical & Tracking Insights

*   **Preloading is Critical (Learned Dec 15, 2025):** Despite optimizations, some users still experience 7s+ load times. Preloading the LCP image/video is a non-negotiable requirement for paid traffic pages.

## Creative Insights

*   **Static Image > Video (Learned Dec 15, 2025):** The "Ad 1 - Founder - Group Photo" creative (static image) outperformed all video variations on Facebook, generating the only attributable purchase. This suggests that for a high-trust service like tutoring, a "real" photo of the teacher builds trust faster than a polished video ad.
