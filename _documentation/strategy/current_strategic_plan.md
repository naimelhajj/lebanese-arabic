# Current Strategic Directive: The "Tip of the Spear" Offensive

**Date:** November 4, 2025

**Objective:** Generate immediate, net-positive cash flow within 7-10 days by funneling all high-intent traffic to a single, optimized conversion path.

---

## Phase 1: Forge the Spearhead (Timeline: Next 24 Hours - *Currently on hold*)

**Objective:** Create a single, optimized conversion page (`lebanese-lessons-risk-free.html`) that combines the proven content of `lebanese-lessons-v2/` with a direct payment mechanism and the "Risk-Free" offer.

**Status:** **ON HOLD.** Awaiting the complete HTML content of the `lebanese-lessons-v2/` page from the user.

**Action Required from User:** Provide the full HTML content of the `lebanese-lessons-v2/` page.

**Once HTML is provided, I will:**
1.  Take the provided HTML content of `lebanese-lessons-v2/`.
2.  Remove any existing lead generation forms.
3.  Insert the direct payment booking form block (from `reserve-lebanese-trial-v2.html`).
4.  Inject the "Risk-Free Offer" block at the top of the page.
5.  Save this final, correct asset as `C:\development\lebanese-arabic\lebanese-lessons-risk-free.html`.

---

## Phase 2: The Two-Pronged Assault (Commencing after Spearhead is forged)

**Objective:** Funnel all high-intent traffic, from both paid and organic channels, to the single `lebanese-lessons-risk-free.html` landing page.

### Prong 1: The Paid Surgical Strike

*   **Action:** Rebuild the Paid Campaign.
    1.  **PAUSE ALL EXISTING CAMPAIGNS.**
    2.  **CREATE A NEW CAMPAIGN:**
        *   **Campaign Objective:** `Sales`.
        *   **Name:** `Paid Retargeting - Risk-Free Offer - Nov 2025`.
    3.  **CREATE A NEW AD SET:**
        *   **Name:** `High-Intent Retargeting (30d)`.
        *   **Audience:** Custom Audience combining users who have triggered any of the following events in the last 30 days: `HighEngagement`, `VideoPlay`, `FormProgression`. Exclude all users who have already triggered the `Purchase` pixel.
        *   **Budget:** Consolidate entire ad budget here (minimum $20/day).
    4.  **CREATE A NEW AD:**
        *   **Creative:** Use the "Direct Action Video."
        *   **Primary Text:**
            > You were close to starting. Your first step is now risk-free.
            >
            > Book your $15 trial lesson today. If you continue with a full package, the trial is on us.
            >
            > Click "Book Now" to secure your spot.
        *   **Destination URL:** The new `lebanese-lessons-risk-free.html` page.
    *   **KPI:** Cost Per Purchase (CPP) < $40.

### Prong 2: The Organic Ambush

*   **Action:** Modify Your Top 3 Organic Pages.
    1.  Identify your Top 3 highest-traffic organic pages (including `/lesson15/`).
    2.  On these 3 pages, implement a high-visibility block below the main content, featuring the exact same "Risk-Free" offer and a button linking directly to the `lebanese-lessons-risk-free.html` page.

    **HTML for Organic Pages:**
    ```html
    <!-- RISK-FREE OFFER BLOCK - ORGANIC -->
    <div style="background-color: #fef2f2; border: 2px solid #dc2626; border-radius: 8px; padding: 24px; margin: 32px 0; text-align: center;">
        <h2 style="font-size: 28px; font-weight: bold; color: #b91c1c; margin-top: 0; margin-bottom: 16px;">Your First Step is Risk-Free.</h2>
        <p style="font-size: 18px; color: #374151; margin: 0 0 24px;">Book your $15 trial lesson today. If you decide to continue with a full lesson package, the cost of your trial will be credited towards your purchase.</p>
        <a href="https://lebanese-arabic.com/lebanese-lessons-risk-free/" style="display: inline-block; background-color: #dc2626; color: #ffffff; font-size: 20px; font-weight: bold; padding: 16px 32px; border-radius: 6px; text-decoration: none;">Book Your Risk-Free Trial</a>
    </div>
    <!-- RISK-FREE OFFER BLOCK - END -->
    ```

---

## Phase 3: Resource Allocation & The Organic Question

*   **The 90/10 Rule:**
    *   **90% of working hours:** Dedicated to Phase 2: The Two-Pronged Assault (monitoring CPP, analyzing landing page behavior, managing cash flow).
    *   **10% of working hours:** Secondary, maintenance task for the "Organic Optimization Sprint" (transcribing one video at a time).

---

**Reporting Cadence:**
*   Report back in 24 hours confirming the "Spearhead" landing page is live (once HTML is provided).
*   Report back in 48 hours confirming the full assault is deployed.
*   Thereafter, provide a daily report containing two metrics: **Daily Cash Collected** and **Paid Campaign CPP**.
