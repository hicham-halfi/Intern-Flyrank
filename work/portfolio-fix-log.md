# Portfolio fix log — 20 October 2026

Live URL: https://hicham-halfi.github.io/Intern-Flyrank/portfolio/

- Before: a one-item result said “1 complete reviews”. After: singular/plural follows the count.
- Before: very long calculator output had no explicit emergency wrapping. After: output wraps within its container; grid children can shrink.
- Before: smooth scrolling ignored reduced-motion preference. After: reduced-motion users get immediate scrolling.
- Existing responsive layout stacks forms, projects and experience at 700px; figures scale with their containers. Body text uses 17px and 1.7 line height.
- User reports opening the real live site on a phone, trying the links/calculator, and confirms everything is clear. No device model or phone screenshot was provided. The attempted browser viewport override was inconclusive.
- Verified calculator examples: 300/30/1 gives 10; 100/30/2 gives 1; zero budget gives zero; zero rate is rejected. Values stay in the browser.

Independent peer design/hardening review, analytics, badge verification and recorded demos remain separate pending evidence.

Static checks: all relative portfolio file targets resolve; two research PNGs are 46,352 and 40,822 bytes. Measured normal-text palette contrasts range from 4.55:1 to 13.34:1 for the checked foreground/background pairs, above 4.5:1. This is a color calculation, not a full accessibility certification.
