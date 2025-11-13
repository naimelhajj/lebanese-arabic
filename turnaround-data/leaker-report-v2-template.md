# Leaker Report v2: Frictionless Funnel Analysis Template

*As of: YYYY-MM-DD*

## 1. Objective

This report is designed to identify and quantify the drop-off points in our current, frictionless conversion funnel. Unlike the previous leaker report which analyzed a broken manual process, this template uses quantitative data from our analytics platform (e.g., Google Analytics 4) to pinpoint where we are losing potential customers and cash.

---

## 2. Funnel Definition

This report analyzes the "Hook -> Hub -> Checkout" user journey, which our latest learnings suggest is the optimal path for converting organic traffic.

*   **Stage 1: The Hook (Organic Entry)**
    *   **Description:** A user lands on a high-traffic content page (e.g., `/lesson15/`, `/lebanese-love-phrases/`) from an organic search.
    *   **User Action:** Clicks the "Risk-Free Trial" banner/module.

*   **Stage 2: The Hub (Homepage `home-v2`)**
    *   **Description:** The user is sent to our high-trust homepage to see social proof, learn about the teachers, and build confidence.
    *   **User Action:** Clicks the primary "Book Your Trial" CTA.

*   **Stage 3: The Checkout (`/lebanese-lessons/`)**
    *   **Description:** The user lands on the final conversion page with the integrated Jotform for booking and payment.
    *   **User Action:** Successfully completes the payment form.

*   **Stage 4: The Conversion (Purchase Confirmed)**
    *   **Description:** The user lands on the `trial-payment-confirmed` page.
    *   **Result:** A `$15` trial is purchased.

---

## 3. Funnel Performance Data

**(Instructions: Create a Funnel Exploration report in GA4 with the stages defined above. Use the data to fill in this table for a specific date range.)**

| Funnel Stage | Users at Stage | Conversion to Next Stage | Drop-off Rate | Lost Revenue Opportunity* |
| :--- | :--- | :--- | :--- | :--- |
| **1. Clicked Banner (Hook)** | `[e.g., 100]` | `[e.g., 40%]` | `[e.g., 60%]` | `[e.g., $900]` |
| **2. Viewed Hub Page** | `[e.g., 40]` | `[e.g., 50%]` | `[e.g., 50%]` | `[e.g., $300]` |
| **3. Viewed Checkout Page** | `[e.g., 20]` | `[e.g., 25%]` | `[e.g., 75%]` | `[e.g., $225]` |
| **4. Purchase Confirmed** | `[e.g., 5]` | - | - | - |
| **Total** | | **`[e.g., 5%]` Overall CVR** | | **`[e.g., $1,425]` Total Loss** |

*\*Lost Revenue Opportunity is calculated based on the number of users who dropped off at that stage, multiplied by the final conversion rate of the remaining funnel, multiplied by the trial value ($15). This shows how much money is being left on the table at each step.*

---

## 4. Analysis & Action Plan

### Key Drop-off Points:
*   **(To be filled in) Identify the stage with the highest Drop-off Rate or Lost Revenue Opportunity.**
    *   *Example: The largest leak (60% of users) occurs between the "Hook" and the "Hub". This means most people who click the banner on the blog post do not arrive at the homepage.*

### Hypotheses for Leaks:
*   **(To be filled in) Based on the data, why do you think users are dropping off at that stage?**
    *   *Example: The banner click might be accidental, or the page transition is too slow, causing users to abandon before the Hub page loads.*

### Actionable Recommendations:
*   **(To be filled in) Propose a specific, measurable action to fix the biggest leak.**
    *   *Example: We will run an A/B test. Control: Banner links to `home-v2`. Challenger: Banner links directly to `/lebanese-lessons/`. We will measure which path has a higher conversion rate to the "Viewed Checkout Page" step.*
