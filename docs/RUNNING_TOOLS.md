# Reading and running tools

**Desktop/mobile browser → GitHub website:** read Markdown without installing anything.
For interactive HTML comparisons, download/extract the repository and open the HTML report
in a desktop browser. GitHub's HTML file view does not run the report. A ZIP does not auto-update.

## Windows

**Device:** Windows desktop. **Application:** Windows Terminal → PowerShell.
**Working folder:** repository root. **Prerequisite:** Python 3 installed and available via `py`.

```powershell
py -3 --version
py -3 .\skills\ohio-laws-to-markdown\scripts\ohio_laws_to_markdown.py 5122-29 -o .\example-5122-29.md
```

**Output:** local `example-5122-29.md`; requires HTTPS access to codes.ohio.gov. The script fetches
live pages; `--cache` saves this run's HTML but does not reuse older responses. Verify output
against the official document. No GitHub publication occurs.

## macOS/Linux

**Device:** macOS/Linux desktop. **Application:** Terminal → zsh/bash.
**Working folder:** repository root. **Prerequisite:** Python 3 available as `python3`.

```bash
python3 skills/ohio-laws-to-markdown/scripts/ohio_laws_to_markdown.py 5122-29 -o example-5122-29.md
```

**Output:** local `example-5122-29.md`. Both included skill scripts use the Python standard library.
The optional [curation builder](CURATION.md) also requires PyMuPDF and Python 3.10+.

PowerShell is the shell that launches Python. `py -3`/`python3` starts Python; Python does not
implicitly start PowerShell. The GitHub mobile app is not itself a Python runtime. Use a
separately configured runtime for mobile execution; that setup is not included here.

The report generator needs a reviewed JSON specification and local source files. It formats
provided evidence/analysis; it does not independently determine policy impacts. Agent skill
installation varies by application; downloading files alone does not activate a skill.
