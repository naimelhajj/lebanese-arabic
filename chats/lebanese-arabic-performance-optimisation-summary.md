\### Executive summary 📝



| Phase                                  | What we tackled                                                                                                                                                                          | Outcome                                                                           |

| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |

| \*\*Landing page (reservation form)\*\*    | • Re-wrote the heavy Tailwind/JotForm embed into a lightweight HTML block.<br>• Added lazy iframe loading, query-param propagation, CLS-safe styling.                                    | Reservation page now scores > 90 on Lighthouse (mobile + desktop).                |

| \*\*Initial mu-plugin (v 2 → 4)\*\*        | • Split logic: \*\*Profile A\*\* – kill unused plugins on `/reserve-lebanese-trial/`; \*\*Profile B\*\* – defer/async on lesson posts.<br>• Dropped `jquery-migrate`, trimmed block-library CSS. | Console errors fixed; large speed gain but gallery \& button layouts broke.        |

| \*\*Layout regressions \& fixes (v 5.x)\*\* | • Restored core block CSS for lesson posts.<br>• Switched from dequeue to \*\*preload → onload\*\* so styles don’t block rendering.<br>• Injected < 400 B critical flex rules as fallback.   | Sponsored-items grid now stays 4-in-a-row; CTA buttons no longer wrap.            |

| \*\*A/B-test compatibility\*\*             | • Detect `\[bt\_bb\_ab]` shortcode / Beaver Builder AB meta.<br>• Keep `bt-conversion.js` sync only when a test is active.                                                                  | Variant chosen before first paint → no flicker; no extra JS cost on normal posts. |

| \*\*Remaining optimisation\*\*             | • MailMunch removed on landing page; deferred on posts.<br>• Added resource hints, removed emoji script, preconnected JotForm/YouTube.                                                   | Mobile Lighthouse mid-70 – 80 on lesson posts with Nitro disabled.                |



\#### Final deliverables



\* \*\*Custom HTML block:\*\* `Reservation-iframe-block` (v 3.2) — lean, lazy-loaded JotForm embed.

\* \*\*mu-plugin:\*\* `smart-optimiser.php` (v 5.2) — self-contained, safe to disable:



&nbsp; \* Reservation page: kills MailMunch, reviews, social share, CV grids, etc.

&nbsp; \* Lesson posts: defers heavy JS, async-loads Astra \& plugin CSS, \*\*leaves\*\* core block CSS synchronous.

&nbsp; \* A/B pages: keeps `bt-conversion.js` in head; otherwise deferred.

&nbsp; \* Removes `jquery-migrate` everywhere.

&nbsp; \* Adds resource hints (JotForm / YouTube).

\* \*\*Rollback behaviour:\*\* Deleting or disabling the mu-plugin fully restores WordPress’s default asset stack; no styles/scripts remain dequeued.



---



\*\*Next steps\*\*



1\. Keep v 5.2 active and purge all caches.

2\. Re-test with `?nonitro=1` to confirm mobile score rebounds (~75-80).

3\. For further gains: optimise oversized images, raise cache TTLs, consider self-hosting Clarity.



