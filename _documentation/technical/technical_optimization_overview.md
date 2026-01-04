# Technical Optimization Overview

This document outlines the specific and non-standard performance optimization strategy used for the lebanese-arabic.com website.

## 1. Primary Optimization Tool: NitroPack

The site uses **NitroPack** as its primary, site-wide performance optimization suite. It handles caching, image optimization, and asset minification/deferral for the majority of the site.

## 2. Critical Exception: High-Priority Pages

Several key pages, most notably the conversion-focused page `/lebanese-lessons/`, are **explicitly excluded** from all NitroPack optimizations.

- **Reason for Exclusion:** NitroPack's aggressive JavaScript optimization conflicts with and **breaks the functionality of the embedded JotForm forms**. As JotForm is the mission-critical tool for trial sign-ups, its successful operation takes precedence over automated optimization.

## 3. Manual Optimization Method for Excluded Pages

To apply performance improvements to the pages excluded from NitroPack, a custom PHP script is used.

- **File Location:** `landing pages/php snippet.php`
- **Mechanism:** This script uses WordPress action and filter hooks (`wp_head`, `wp_enqueue_scripts`, `script_loader_tag`, etc.) to manually inject optimizations into the `<head>` and modify how assets are loaded.

### Summary of Manual Optimizations via PHP Snippet:

The script performs the following actions on targeted pages (like `/lebanese-lessons/`):

1.  **Disables Competing Scripts:** Silences MailMunch to prevent script conflicts.
2.  **Removes jQuery Migrate:** Drops the unnecessary `jquery-migrate.js` script.
3.  **Manual Asset Cleanup:** Dequeues and deregisters a specific list of non-essential scripts and stylesheets (e.g., `wp-customer-reviews`, `social-pug`).
4.  **JavaScript Deferral:** Adds the `defer` attribute to a curated list of scripts (e.g., `astra-frontend`, `pys-public`) to prevent them from blocking the initial page render.
5.  **CSS Async Loading:** Asynchronously loads specific CSS files by changing their `rel` attribute to `preload` and using an `onload` handler.
6.  **Resource Hints:** Adds `preconnect` and `dns-prefetch` directives for critical third-party domains like JotForm, Stripe, and analytics providers to speed up the initial connection and DNS lookup.

## 4. Advanced TTI Optimization (Implemented Nov 19, 2025)

To combat a high Time to Interactive (TTI), a JavaScript "delay" strategy was implemented via the `php snippet.php` file.

- **Technique:** Instead of only `defer`, non-essential tracking scripts (e.g., PixelYourSite) have their `src` attribute changed to `data-src`.
- **Trigger:** A small footer script listens for the first user interaction (`scroll`, `mousemove`, `click`, etc.) and then loads these delayed scripts.
- **Result:** This change dramatically improved the TTI and overall mobile performance score to **98**, proving it to be a highly effective, surgical optimization.

## 5. Site-Wide Caching & Delivery Architecture (Effective Nov 21, 2025)

Following a deep analysis to resolve inconsistent LCP and high TTFB, a multi-layer caching and delivery architecture was implemented site-wide. This architecture creates a clear hierarchy of responsibility to ensure stability and performance.

### 1. Level 1: Server-Side (Origin)
- **Problem:** High database load and slow page generation on uncached visits (~2.6s).
- **Solution:** A persistent object cache was implemented using the server's available **APCu** PHP extension, connected to WordPress via the "APCu Manager" plugin.
- **Impact:** This drastically reduced the number of database queries (from 88 to 9 on the homepage) and cut the uncached page generation time by ~45%, providing a much faster base for all downstream optimizers.

### 2. Level 2: Primary Optimization (Nitropack)
- **Role:** Nitropack remains the **sole and primary front-end optimization engine**. It is responsible for all HTML, CSS, and JavaScript optimization, image optimization, and serving device-specific (desktop/mobile) cached pages.

### 3. Level 3: CDN & Delivery (Cloudflare)
- **Problem:** Direct conflicts between Cloudflare's own optimization features (APO, "Cache Everything" rules) and Nitropack's optimizations were causing severe LCP inconsistency.
- **Solution:** Cloudflare was reconfigured to act strictly as a CDN and security layer, handing off all performance-related tasks to Nitropack.
- **Configuration:**
    - **Automatic Platform Optimization (APO):** Turned **OFF**.
    - **Cache Rules:** The primary rule for HTML content (`WordPress: Cache Everything`) was modified to **"Bypass cache"**. This forces Cloudflare to always fetch the latest HTML from Nitropack.
    - **Performance Features:** "Rocket Loader" and "Auto Minify" were globally **DISABLED**.
- **Impact:** This configuration eliminates the conflict between the two services. Cloudflare now serves static assets (images, JS, CSS) from its cache as a CDN, but relies on Nitropack to provide the fully-optimized HTML document for every request, ensuring consistency. The result is a predictable cache status (`Cloudflare: DYNAMIC`, `Nitropack: HIT`) and a stable LCP.

### 4. Manual Overrides for LCP Stability
Even with the correct architecture, PageSpeed Insights tests revealed that automated optimizations were insufficient or failing for mobile LCP. The final stable state was achieved by implementing the following manual overrides:

- **Manual LCP Preloading:** Nitropack's "LCP Preload" feature failed to correctly identify or prioritize the homepage hero image. This was resolved by manually injecting a `<link rel="preload">` tag with `fetchpriority="high"` into the site's header for the homepage LCP image. This is managed in the `hero images snippet.php` file.

- **Careful Script Exclusion Management:** The `pixelyoursite` plugin scripts were found to be render-blocking for over 3.5 seconds on mobile tests because they were in Nitropack's exclusion list. Removing them from the exclusion list allowed Nitropack's "Delay JS" feature to work correctly, preventing them from blocking the main thread. This highlights the principle that exclusions should be used sparingly and only when a script is definitively broken by optimization.

- **Manual Asset Compression:** The LCP hero image, even after Nitropack's optimization, was too large (>230 KiB). The final fix required manually compressing the image to under 100 KiB and re-uploading it. This confirms that critical, high-impact assets may require manual optimization before being handled by automated systems.
