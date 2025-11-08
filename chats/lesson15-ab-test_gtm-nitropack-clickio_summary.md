\# Summary — AB test + GTM + NitroPack + Clickio (lesson15)



\## Goals



\* \*\*Macro ➔\*\* Increase % of visitors (entering via `/lesson15/`) who eventually reach \*\*`/lebanese-lessons/`\*\*—even after visiting other pages first.

\* \*\*Engagement ➔\*\* Lift meaningful on-site engagement (your GTM \*\*HighEngagement\*\*: ≥60s session time + ≥2 clicks), even if they don’t reach `/lebanese-lessons/`.



\## Measurement model (final)



\* \*\*Primary conversion ➔\*\* AB Split Test (ABST) \*\*URL/Page Visit\*\* goal for \*\*`/lebanese-lessons/`\*\*.

\* \*\*Secondary conversion ➔\*\* ABST \*\*JavaScript Subgoal\*\* fired from GTM when your \*\*HighEngagement\*\* event occurs.



&nbsp; \* Use ABST’s provided snippet:

&nbsp;   `(window.abGoal = window.abGoal || \[]).push(\[5564,3]); processAbstGoal?.();`

&nbsp; \* Keep HighEngagement \*\*site-wide\*\*, but \*\*credit the ABST subgoal only if the visitor saw the test\*\* (cookie guard below).

\* \*(Optional diagnostics)\* ➔ ABST \*\*Link Click\*\* subgoal for any `a\[href\*="/lebanese-lessons/"]` on lesson15 to measure direct CTA influence; ABST \*\*Time Active\*\* can be used on page (start at 30s if you want a softer threshold).



\## GTM wiring



\* \*\*Cookie guard ➔\*\* Create 1P cookie variable \*\*`btab\_5564`\*\*.

\* \*\*Duplicate\*\* your two HighEngagement triggers and add condition \*\*`{{btab\_5564}} matches RegEx .+`\*\*.

\* \*\*ABST Subgoal tag ➔\*\* Custom HTML with the snippet above; trigger on the \*\*cookie-guarded\*\* HighEngagement triggers.



&nbsp; \* This keeps HighEngagement firing everywhere, but \*\*only\*\* credits the AB test for users actually bucketed into \*\*Test 5564\*\*.



\## Cookie mismatch you saw (5459 vs 5564)



\* `btab\_5459` was from an older test. The correct cookie for the current test is \*\*`btab\_5564`\*\*.

\* Forced-variation URLs (`?abtid=5564\&abtv=…`) are for \*\*QA/preview\*\*; don’t use them for real data. For normal sessions, confirm only one test is active on `/lesson15/`.



\## NitroPack setup (so the test actually runs)



\* \*\*Never delay/combine/minify\*\* ABST scripts. Add \*\*Excluded Resources\*\* (use the exact paths you see in Network):



&nbsp; \* `\*/wp-content/plugins/\*bt\_experiments\*`

&nbsp; \* `\*/wp-content/plugins/\*bt-bb-ab\*`

&nbsp; \* `\*/wp-content/plugins/\*bt\_conversion\*`

\* Choose one caching strategy:



&nbsp; \* \*\*Option A (safest) ➔\*\* Exclude \*\*`/lesson15/`\*\* from optimization/caching.

&nbsp; \* \*\*Option B (faster) ➔\*\* “Exclude from optimization by cookie” for \*\*`btab\_5564`\*\* (use the \*\*exact\*\* name). First view still needs ABST JS to run; that’s why the resource excludes above matter.

\* Make sure NitroPack doesn’t ignore `abtid`/`abtv` query params (so previews behave).



\## Cloudflare notes



\* Disable \*\*Rocket Loader\*\* and aggressive HTML edge caching on `/lesson15/` during the test.

\* Add a cache rule to \*\*Bypass\*\* for preview URLs containing `?abtid=`.



\## Clickio CMP integration



Two viable policies—pick one:



\* \*\*A) Bucket before consent (recommended for reliability) ➔\*\* Allowlist ABST as \*\*Essential/Functional\*\* so the test buckets on first paint:



&nbsp; \* Don’t block first-party cookies named `btab\_\*`.

&nbsp; \* Don’t block ABST plugin scripts (same paths as NitroPack excludes).

\* \*\*B) Bucket after consent (stricter) ➔\*\* Keep ABST blocked until consent, then fire.



&nbsp; \* Expect lower test coverage (non-consent users won’t be bucketed).

&nbsp; \* If you gate the ABST subgoal too, check TCF Purpose 1 in your tag before calling the snippet.



\## WP snippet hardening



\* You already removed the line that deferred \*\*`bt-conversion`\*\*—good. On lesson posts, \*\*never\*\* defer ABST assets.



\## Debug/QA checklist



\* \*\*Cookie check ➔\*\* In console: `abstGetCookie \&\& abstGetCookie('btab\_5564')` (returns JSON string).

\* \*\*Readiness ➔\*\* Listen to `ab-test-setup-complete` to confirm the variation is shown.

\* \*\*GTM Preview ➔\*\* Verify your site-wide HighEngagement still fires, and the \*\*ABST subgoal\*\* fires \*\*only\*\* when `btab\_5564` exists.

\* \*\*ABST Results ➔\*\* Use the subgoal dropdown to confirm increments.

\* If NitroPack is ON and the test “disappears,” recheck: script excludes, cookie-based bypass (or page exclusion), and that Delay JS isn’t touching ABST or GTM.





