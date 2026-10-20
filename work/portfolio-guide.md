# Portfolio files and data flow

Public path: `docs/portfolio/` (served by GitHub Pages from `main` → `/docs`).

- `index.html`: semantic content, project case studies, navigation, form fields,
  page title and share metadata. Background is based on the CV supplied by Hicham.
- `cv.html`: a professional web CV linking back to the portfolio, with print CSS.
  It is a new web edition, not a modified copy of the original supplied PDF.
- `style.css`: colors, readable spacing, focus indicators, two-column desktop
  sections, and a single-column layout below 700px.
- `planner.js`: one working feature: a review-budget calculator. It validates
  inputs and computes whole reviews, time, total assumed cost and remaining budget.
  It uses no network requests, cookies, analytics, or persistent storage.

## What a backend is, and this feature's flow

A backend is server-side code that receives requests, applies rules, and can
store or retrieve data. This calculator does not need one: its arithmetic runs
inside the visitor's browser. GitHub Pages serves the static files over HTTPS.
The visitor enters a budget, an hourly rate and time per review, then submits the
form. JavaScript checks validity, calculates capacity, and updates an accessible
output on the same page. Nothing is transmitted to an inbox or stored remotely.
This is a functioning browser demo, not a contact-form backend.

## Add the next case study

Add a new `article` in `index.html` under `#work`, preserving the three parts:
the problem; what I did; what came of it. Include a real artifact link and a
limitation. Prefer changing the source string in `work/scripts/build_portfolio.py`
and rerunning it, so future regeneration preserves the edit. Check the links,
phone layout, keyboard navigation and image size, commit, then push. GitHub Pages
rebuilds automatically from `/docs`.

The next proposed case is the ML Research Scout: processing an ML PDF into a
source-grounded Markdown note. Add it only after a genuine working run, evaluated
guardrails and recorded demo exist. No reminder or successful agent run is claimed
by this note.

## Pending evidence, not inferred completion

The internship also requests a real-phone check, independent design feedback,
hardening review, profile/CV linking, booking link and later an approved badge.
Browser viewport checks alone cannot establish the phone check, and AI review is
not a substitute for a real peer review. Those pieces should be completed and
recorded before the corresponding assignment is described as finished.

## Verification record — 2026-10-20

- Public HTTPS portfolio and CV pages loaded in the browser; research link and local file references were checked.
- Live calculator: $300 / ($30 × 1 hour) = 10 reviews, $300 cost, $0 remaining.
- Live calculator: $100 / ($30 × 2 hours) = 1 review, $60 cost, $40 remaining.
- Hourly rate 0 was rejected by browser validation. Budget 0 returned 0 reviews and $0 cost.
- Both research figures loaded. The notebook and article metrics trace to executed receipts.
- Browser viewport override was attempted at 390px, but the reported viewport remained 1280px. It was reset. No mobile-browser or real-phone pass is claimed.
- LinkedIn target was extracted from the supplied CV; no LinkedIn account changes or booking setup were performed.

## Next-case reminder — created 2026-10-20

A one-time Codex reminder is active for Tuesday, 27 October 2026, to add the ML Research Scout case study. Automation ID: `add-the-research-scout-case-study`. The native automation tool confirmed creation, and its active configuration was read back. The prompt calls for real source/evaluation/demo evidence and forbids automatic external edits or messaging others.

The build context is preserved in this repository's scripts, requirements, notebooks, documentation and agent README instead of a Claude Project, which was not available in the user's environment. The reminder does not assert that an agent demo or video already exists.

The portfolio URL has now been saved in LinkedIn's contact information as a Professional Portfolio and verified by reopening the contact dialog. This supersedes the earlier verification entry saying no LinkedIn changes had been performed.
