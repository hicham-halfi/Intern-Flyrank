# ML Research Scout

An autonomous, bounded research-note workflow for Hicham Halfi. It reads an ML
document, asks a model to classify it and select source evidence, optionally
looks up unfamiliar algorithm names on arXiv, validates quotations, and writes a
new Markdown note. It never exposes a shell or arbitrary write tool to the model.

## Setup

1. Install Python 3.12 and [Ollama](https://ollama.com) using their official sources.
2. Install `pypdf`: `python -m pip install pypdf`.
3. Ensure the locally installed model is available: `ollama list`.
   This build was developed with `qwen2.5-coder:latest` (local model ID
   `dae161e27b0e`, approximately 4.7GB). If absent, install that model from Ollama's
   official library. Model requirements depend on your hardware.
4. Run Ollama's server using the normal installed app or `ollama serve`. It must
   listen on the default local address `127.0.0.1:11434`. Do not expose it publicly.
5. Create a workspace with a `papers/` folder; put the input PDF, Markdown or text
   file there. The program creates `notes/` and `runs/` inside that workspace.

## Usage

```sh
python scout.py tutorial.pdf --workspace ./demo
python scout.py paper.pdf --workspace ./demo --lookup "Proximal Policy Optimization"
python scout.py tutorial.pdf --workspace ./demo --backend codex --allow-cloud
```

The last command uses an installed, signed-in Codex CLI instead of Ollama. Install
Codex from its official source and sign in before using it. It uses the account's
configured default model in read-only, ephemeral mode; no model-generated shell
commands are needed. **It sends selected source excerpts to OpenAI/Codex.** Use
`--allow-cloud` only after approving that transmission for the document being
processed. Without that flag, cloud inference is blocked. Local Ollama is the
default; no cloud transmission occurs on that path.

The input is a filename relative to `papers/`, not an arbitrary absolute path.
The chosen workspace is the only location this program reads and writes.
The Ollama connection is fixed to localhost. An optional external research request
sends only an algorithm lookup term to arXiv, never the PDF or full source text.
Candidate papers are labeled as candidates, not verified definitions.

On the author's Windows installation, the bundled Python executable can be used:
`C:/Users/hp/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`.
This is an environment convenience, not a portable installation requirement.

## Architecture

```text
Request → list documents → PDF/text extraction → local-model classification/evidence
                                             → conditional arXiv lookup
       → exact-quote/page validation → exclusive-create Markdown note → JSON trace
```

The host selects short excerpts to bound runtime. The model determines document
type, relevant passages, and lookup terms within those excerpts. This is not an
exhaustive full-paper reading. Host code
enforces input containment, a 15MB/40-page/60,000-character input limit, bounded
generation, exact source evidence and collision-safe writes. A failed run records
its failure; it does not write a success note. No delete/overwrite operation exists.

## Changes from FL-06

- **Platform:** the submitted plan named Claude Desktop + MCP. The user later
  confirmed that environment was unavailable. The working path uses an already
  installed Ollama/Codex runtimes and narrow Python file/arXiv tools. The first
  local-model run took 549.5 seconds and incorrectly refused the PPO tutorial;
  that is a failed evaluation, not a successful demonstration. A Codex backend
  was added and tested only after the user explicitly approved sending the
  selected PDF to OpenAI/Codex. This is a documented platform deviation, not a claim that Claude/MCP
  was configured.
- **PDFs:** binary PDFs require PDF extraction, not a plain text filesystem read.
- **Output:** an extractive, source-grounded evidence note replaces a free-form
  technical interpretation. This reduces fabricated metrics and keeps the MVP
  narrow. It does not reproduce experiments or establish the paper's correctness.
- **Source sample:** `papers.pdf` is a PPO tutorial with corrupted numeric text
  extraction. The unrelated `marl_vrp.md` fixture is labeled separately; its 14.2%
  claim must never be attributed to the PDF.
- **External context:** arXiv lookup returns candidates and availability status;
  it does not promise a verified mathematical definition.

## Limits and guardrails

- Classification may be wrong; an unrelated document can be misclassified.
- A verbatim quote can still be selected out of context. Inspect the source.
- No OCR, image understanding, full corpus monitoring, or background scheduling.
- Damaged extraction causes all numerical metrics to be excluded.
- Tutorial examples are not accepted as experimental result metrics.
- arXiv lookup may fail or return irrelevant candidates; status is recorded.
- The model's free-form limitation suggestions are not published as source facts.
- Network/model timeout, invalid JSON, or absence of grounded evidence fails closed.
- Notes are created with exclusive file creation and a UTC timestamp. Source files
  and old notes are never modified by this program.

## Evaluation and recording

See `eval_results.json` and `BUILD_LOG.md` for actual results; do not infer a pass
from the existence of a test. A raw terminal/JSON trace is not a screen-capture
video. The internship's FL-07 raw video and FL-09 narrated video still require an
actual screen recording of the working system, with no invented narration or
substitute slides.

Suggested demo: start recording the real terminal, run the first command, wait for
the full loop, open the newly saved note and trace, and point out the damaged-PDF
guardrail. For a narrated demo explain the local-model platform choice and one
limitation. Do not describe a failed run as successful.

API references: [Ollama chat](https://docs.ollama.com/api/chat) and
[arXiv API manual](https://info.arxiv.org/help/api/user-manual.html).
