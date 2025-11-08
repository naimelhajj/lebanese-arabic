Here is a summary of our conversation:



\* You first came to me with a custom HTML block from your WordPress site that was causing a JavaScript error: `Uncaught SyntaxError: Unexpected token '-'`.

\* We diagnosed the problem: the error was caused by using hyphens (`-`) in JavaScript function names (like `openLightboxblock-1759737087598()`), which JavaScript interprets as a subtraction sign.

\* I provided a fix for your first "Greetings" infographic by replacing the hyphens in the function names and `onclick` calls with underscores (`\_`). I also added improvements like a better copy-to-clipboard function and a "click-outside-to-close" feature for the embed popup.

\* We applied the exact same fix to your second "Coffee" infographic block, which had the same issue.

\* Finally, we fixed the root cause of the problem: the `infographic-generator.html` file itself. We modified its code to generate new `uniqueId`s using underscores (e.g., `block\_12345`) instead of hyphens, ensuring any new blocks you create will be free of this error.





