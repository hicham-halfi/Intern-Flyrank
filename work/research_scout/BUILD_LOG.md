# Build log — real observations

## 2026-10-20

1. Inspected the submitted FL-06 plan and local files. Claude Desktop + MCP was
   planned, but the user confirmed they did not have that environment available.
2. Found an existing Ollama installation and `qwen2.5-coder:latest`. The initial
   sandbox-local connection was blocked; authorized local network access was
   needed. A second server start found the port already occupied. The existing
   local server then answered `ollama list` and a real readiness prompt.
3. Implemented bounded PDF/text ingestion, local structured model inference,
   conditional arXiv lookup, quote/page validation and exclusive-create notes.
4. The input tutorial contains damaged numeric extraction, so host code excludes
   all result metrics for that input. Tutorial type also excludes illustrative
   numbers from the experimental-results section.
5. Started an actual end-to-end run against the seven-page user-provided tutorial.
   Final status, durations and outcomes are captured in run JSON traces and eval
   receipts. This log does not claim those checks passed before they finish.

No elapsed build-hour claim or successful screen video is fabricated. Further
entries are added as tests actually run.

6. The first local PDF run completed in 549.5 seconds but classified the tutorial
   as unrelated and refused it. This is a relevance failure. No note was written.
7. Reduced model context to selected source excerpts, while checking every quote
   against the full extracted pages. This improves boundedness at the cost of
   exhaustive coverage; notes disclose that tradeoff.
8. Tested the installed Codex CLI with a readiness prompt. Added an optional Codex
   structured-inference backend with no model tools requested, read-only sandbox,
   ephemeral sessions, and host-side evidence/write enforcement.
9. Automatic approval review initially rejected the PDF transmission because
   specific document/destination approval was missing. The user then explicitly
   approved sending `C:\ML_Projects\papers.pdf` to OpenAI/Codex. Only then was the
   same-file PDF test retried. Future CLI cloud runs require `--allow-cloud`.

10. Approved user-PDF Codex run saved a grounded tutorial note in 38.3 inference seconds. It accepted two architecture quotes and one data quote, and excluded experimental metrics.
11. Live synthetic checks retained one failed predicate for fictional metrics, plus successful missing-baseline, unrelated-refusal, repeat-filename and previous-note checks. Unknown-algorithm lookup executed but arXiv returned HTTPError; retrieval success remains unproven.
12. Five deterministic path/query/write guardrails passed.
13. Public full-PDF integration used Attention Is All You Need (arxiv:1706.03762), 15 extracted pages. Codex inference took 49.03 seconds and saved a note with one architecture quote, one data quote and two metrics, all checked against source pages. No source PDF is committed.
