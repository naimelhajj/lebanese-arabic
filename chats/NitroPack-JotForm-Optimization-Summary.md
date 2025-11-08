Over this exchange we identified that aggressive optimization (lazy-loading, unused-CSS removal, JS delay) inside \*\*NitroPack\*\* and WordPress’ own default iframe-lazy-loading were hiding your embedded JotForm, preventing Google’s mobile crawler from seeing key pages, and sometimes blocking NitroPack from even generating a “mobile” variant.  Together we built an exclusion list, tuned NitroPack’s \*Strong\* preset, and hard-fixed the reservation page by forcing the iframe to load eagerly and disabling any extra lazy-load layer.  The steps below consolidate all findings and fixes so you can reproduce (or roll back) every change.



\## 1️⃣ Starting point



\* You shared PageSpeed reports showing JotForm scripts adding 300-340 ms blocking time and causing CLS.

\* NitroPack was on \*\*Strong\*\* or \*\*Ludicrous\*\* with Render-blocking removal, Remove-unused-CSS and Lazy-load iFrames turned on.

\* Goal: keep \*\*every JotForm embed 100 % visible\*\* while squeezing as much performance as possible from NitroPack.



\## 2️⃣ Key configuration decisions



| Area               | Final setting                                                                                                       | Reason                                                                                        |

| ------------------ | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |

| \*\*JS\*\*             | Delay non-critical scripts; exclude every `\*.jotform\*` URL.                                                         | Avoids hiding the form while still deferring analytics. (\[support.nitropack.io]\[1])           |

| \*\*CSS\*\*            | Remove unused CSS \*\*ON\*\* but with the long JotForm selector exclusion list you created.                             | Prevents broken styling. (\[freshysites.com]\[2])                                               |

| \*\*iFrames\*\*        | NitroPack “Lazy-load iFrames” \*\*OFF\*\* for pages with forms \*\*OR\*\* add `loading="eager"` on the `<iframe>` itself.   | Double lazy-loading plus `display:none` stopped the JotForm load. (\[support.nitropack.io]\[3]) |

| \*\*WordPress core\*\* | Disabled auto-lazy for iframes on the reservation page via a small filter.                                          | WordPress 5.7+ adds `loading="lazy"` by default. (\[Make WordPress]\[4])                        |

| \*\*Cache rules\*\*    | Page `/reserve-lebanese-trial/` excluded from optimisation and cache; all others warmed for desktop \*\*and\*\* mobile. | Ensures no conflicting markup rewrites on critical revenue page.                              |



\## 3️⃣ Troubleshooting milestones



1\. \*\*Mobile PSI blank screen\*\* traced to mobile Googlebot being blocked or critical CSS removed → disabling Remove-unused-CSS per-URL fixed it. (\[fr.docs.wp-rocket.me]\[5])

2\. \*\*NitroPack showed only a desktop variant\*\* because the first mobile warm-up failed; re-queueing after the fix generated the mobile copy. (\[support.nitropack.io]\[6])

3\. \*\*Reservation form spinner never disappeared\*\*: iframe had `display:none`, plus two lazy-load layers. Switching to `opacity:0` + eager load resolved the “iframe is not visible” console error. (\[jotform.com]\[7])



\## 4️⃣ Permanent hardening



\* WordPress filter to raise the lazy-loading threshold only on that page. (\[WordPress.org Français]\[8])

\* NitroPack “Optimize-only URLs” list now covers all pages except the reservation form, preventing future accidental rewrites. (\[support.nitropack.io]\[6])

\* Embed code simplified to pure `<iframe>` (no extra JotForm JS) for maximum compatibility. (\[jotform.com]\[7])



\## 5️⃣ Next steps



1\. Keep watching Core Web Vitals in Search Console; pay special attention to INP after enabling JS delay.

2\. If you attempt \*\*Ludicrous\*\* again, do it on a staging copy and re-check each form.

3\. Maintain the exclusion list; add any new third-party widgets (chat, video, etc.) before turning on Delay JS.



---



\[1]: https://support.nitropack.io/en/articles/8613977-using-nitropack-with-contact-form-plugins-ensuring-seamless-performance-with-dynamic-content?utm\_source=chatgpt.com "Using NitroPack with Contact Form Plugins: Ensuring ..."

\[2]: https://freshysites.com/resources/nitropack-hubspot-divi-css-exclusions/?utm\_source=chatgpt.com "Fixing NitroPack CSS exclusions to prevent HubSpot form ..."

\[3]: https://support.nitropack.io/en/articles/8390308-how-to-check-if-nitropack-is-lazy-loading-your-iframes-videos-properly?utm\_source=chatgpt.com "How to check if NitroPack is lazy loading your iFrames ..."

\[4]: https://make.wordpress.org/core/2021/02/19/lazy-loading-iframes-in-5-7/?utm\_source=chatgpt.com "Lazy-loading iframes in 5.7 – Make WordPress Core"

\[5]: https://fr.docs.wp-rocket.me/article/1769-lazyload-pour-les-iframes-et-les-videos?utm\_source=chatgpt.com "LazyLoad pour les iframes et les vidéos"

\[6]: https://support.nitropack.io/en/articles/8390310-nitropack-lazy-loading-feature-for-images?utm\_source=chatgpt.com "NitroPack Lazy Loading Feature for Images"

\[7]: https://www.jotform.com/answers/2356066-iframe-code-without-javascript?utm\_source=chatgpt.com "iFrame Code Without Javascript"

\[8]: https://fr.wordpress.org/plugins/disable-lazy-loading-for-iframes/?utm\_source=chatgpt.com "Disable Lazy Loading for IFRAMES"



