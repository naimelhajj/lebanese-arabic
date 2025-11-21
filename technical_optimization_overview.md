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
