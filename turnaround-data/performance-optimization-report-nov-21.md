# Performance Optimization Report: LCP & TTFB

- **Date:** November 21, 2025
- **Objective:** Diagnose and resolve high variability in homepage Largest Contentful Paint (LCP) and reduce Time to First Byte (TTFB).

---

## 1. Initial Problem

The homepage exhibited extreme LCP inconsistency in lab tests, with scores fluctuating from an excellent 1.7s to a poor 9s+. Real-user data (CrUX) showed a borderline LCP of 2.35s and a very high TTFB of 1.83s, indicating a severe server-side bottleneck on uncached requests.

### Initial State Metrics (from Query Monitor):
-   **Page Generation Time:** `2.5833s`
-   **Database Queries:** 88
-   **Total Database Time:** `0.9589s`

---

## 2. Diagnosis & Action Plan

The investigation proceeded in two phases, first addressing the server backend, then the caching layer conflicts.

### Phase 1: Backend Optimization

-   **Diagnosis:** Analysis of Query Monitor data revealed two primary issues:
    1.  A single slow database query originating from the "Latest Posts" block was taking over **0.6 seconds**.
    2.  The WordPress installation was not using a persistent object cache, leading to an excessive number of database queries (88 total).

-   **Action Taken:**
    1.  The "Latest Posts" block was removed from the homepage.
    2.  The "APCu Manager" plugin was installed to enable the server's existing APCu extension as a persistent object cache for WordPress.

### Phase 2: Caching Layer Configuration

-   **Diagnosis:** Despite a much faster backend, LCP remained inconsistent. Further testing revealed a direct conflict between Cloudflare's and Nitropack's optimization services. Cloudflare APO was serving its own cached HTML, which was not the version Nitropack had optimized for different devices, causing a cache `MISS` at the Nitropack level.

-   **Action Taken:**
    1.  **Cloudflare APO was disabled.**
    2.  A Cloudflare **Cache Rule** was modified to **"Bypass Cache"** for all HTML pages, giving Nitropack full control over page caching.
    3.  Cloudflare's performance features (**Auto Minify, Rocket Loader**) were disabled to prevent conflicts.

---

## 3. Architectural Outcome & Metrics

The implemented changes successfully resolved the backend bottleneck and the caching layer conflict.

### Final Architectural State Metrics (from Query Monitor):
-   **Page Generation Time:** `1.4072s` (**-45% reduction**)
-   **Database Queries:** 9 (**-89% reduction**)
-   **Total Database Time:** `0.0062s` (**-99.3% reduction**)

While the server performance and caching hierarchy were now correct, the primary business goal was not met, as real-world testing still produced unacceptable mobile LCP scores.

---
## 4. Final Breakthrough: Asset & Content-Level Optimization

- **Problem:** Despite a fast backend and correct caching architecture, PageSpeed Insights continued to report a 7s+ LCP on mobile.
- **Final Diagnosis:** A deep analysis of the PSI report revealed the root cause was not the architecture, but the content being served by Nitropack. Three specific issues were identified:
    1.  **Render-Blocking JavaScript:** The `pixelyoursite` plugin was in Nitropack's exclusion list and was blocking the main thread for over 3.5 seconds.
    2.  **Oversized LCP Image:** The hero image file was over 230 KiB, too large for a throttled mobile network.
    3.  **Missing LCP Priority:** Nitropack's automatic LCP detection was failing, so the browser was not prioritizing the image download.

- **Final Action Plan:**
    1.  **Enabled Script Delaying:** `pixelyoursite` was removed from Nitropack's exclusion list, allowing Nitropack to correctly delay its execution until user interaction.
    2.  **Forced LCP Preloading:** A manual `<link rel="preload">` tag for the hero image was injected into the site's header via a custom PHP snippet to override Nitropack's failed detection.
    3.  **Compressed LCP Asset:** The hero image was manually compressed to under 100 KiB and re-uploaded.

### Conclusion

The severe mobile LCP issue was a multi-layered problem requiring a holistic, three-phase solution. Success was achieved only after addressing all three layers:
1.  **Backend Optimization:** Fixing the database load and enabling an object cache.
2.  **Caching Architecture:** Resolving conflicts between Cloudflare and Nitropack.
3.  **Asset & Script Optimization:** Directly fixing the render-blocking scripts and oversized/un-prioritized LCP image identified in the PSI report.

With these combined fixes, the mobile LCP finally achieved a fast and stable "Good" score.