#!/usr/bin/env python3
"""
Extract verbatim rule/section text from codes.ohio.gov (Ohio Administrative Code
and Ohio Revised Code) and emit clean, hierarchy-preserving Markdown.

Accepts any mix of:
  * chapter URLs      https://codes.ohio.gov/ohio-administrative-code/chapter-5122-25
  * single rule URLs  https://codes.ohio.gov/ohio-administrative-code/rule-5122-25-01
  * ORC chapter URLs  https://codes.ohio.gov/ohio-revised-code/chapter-5119
  * ORC section URLs  https://codes.ohio.gov/ohio-revised-code/section-5119.36
  * bare identifiers  5122-25            (OAC chapter)
                      5122-25-01         (OAC rule)
                      5160-1-05.1        (OAC rule with decimal)
                      section-5119.36    (ORC section)

Usage:
  python ohio_laws_to_markdown.py <url-or-id> [<url-or-id> ...] \
      [-o OUTPUT.md] [--split OUTDIR] [--cache DIR] [--no-supplemental] [--delay SEC]

Examples:
  python ohio_laws_to_markdown.py chapter-5122-25 -o oac_5122-25.md
  python ohio_laws_to_markdown.py 5122-25-01 5122-25-02 -o two_rules.md
  python ohio_laws_to_markdown.py https://codes.ohio.gov/ohio-revised-code/chapter-5119 \
      --split ./orc_5119

Notes:
  * Text is reproduced verbatim; only HTML markup is removed. Hyperlink targets
    (cross-references to other rules/sections) are dropped, the visible text stays.
  * Paragraph depth comes from the site's own level-N classes when present (OAC).
    ORC pages carry no level classes, so depth is inferred from the (A)/(1)/(a)/(i)/(I)
    designator ladder. Inference is best-effort -- verify deep nesting against the
    authenticated PDF before relying on it for a compliance determination.
"""

import argparse
import html as htmllib
import os
import re
import sys
import time
import urllib.error
import urllib.request

BASE = "https://codes.ohio.gov"
UA = "Mozilla/5.0 (compatible; ohio-laws-to-markdown/1.1)"

ROMAN_LOWER = {
    "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x",
    "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx",
}
ROMAN_UPPER = {r.upper() for r in ROMAN_LOWER}


# ---------------------------------------------------------------- fetching ---
def fetch(url, cache_dir=None, delay=0.5, retries=3):
    """GET live HTML, optionally save it on disk, and retry on failure.

    Saved HTML is evidence/debugging output, never a substitute for a live
    retrieval. Reusing it would incorrectly stamp stale text as retrieved today.
    """
    key = None
    if cache_dir:
        os.makedirs(cache_dir, exist_ok=True)
        key = os.path.join(cache_dir, re.sub(r"[^A-Za-z0-9._-]", "_", url) + ".html")

    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as resp:
                text = resp.read().decode("utf-8", errors="replace")
            if key:
                with open(key, "w", encoding="utf-8") as fh:
                    fh.write(text)
            time.sleep(delay)
            return text
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError("failed to fetch %s: %s" % (url, last))


# ------------------------------------------------------------ url handling ---
def normalize(token):
    """Turn a URL or bare identifier into a canonical codes.ohio.gov URL."""
    token = token.strip().rstrip("/")
    if token.startswith("http"):
        return token
    token = token.lstrip("/")
    if token.startswith(("chapter-", "rule-", "section-", "ohio-")):
        if token.startswith("ohio-"):
            return "%s/%s" % (BASE, token)
        seg = "ohio-administrative-code"
        if token.startswith("section-"):
            seg = "ohio-revised-code"
        elif re.fullmatch(r"chapter-\d+(\.\d+)?", token):
            # ORC chapters have no hyphen in the number (5119); OAC chapters do (5122-25)
            seg = "ohio-revised-code"
        return "%s/%s/%s" % (BASE, seg, token)
    # bare numbers: 5122-25 -> OAC chapter; 5122-25-01 -> OAC rule; 5119.36 -> ORC section
    if re.fullmatch(r"\d+(\.\d+)+", token):
        return "%s/ohio-revised-code/section-%s" % (BASE, token)
    parts = token.split("-")
    if len(parts) >= 3:
        return "%s/ohio-administrative-code/rule-%s" % (BASE, token)
    return "%s/ohio-administrative-code/chapter-%s" % (BASE, token)


def page_kind(url):
    if "/rule-" in url:
        return "rule"
    if "/section-" in url:
        return "section"
    if "/chapter-" in url:
        return "chapter"
    return "container"


def child_links(html_text, url):
    """Rule/section links on a chapter (or other container) page, in page order."""
    if "/ohio-revised-code/" in url:
        seg, kind = "ohio-revised-code", "section"
    else:
        seg, kind = "ohio-administrative-code", "rule"
    # chapter pages use absolute hrefs on some templates and relative on others
    pat = r'href="(?:/%s/)?(%s-[0-9A-Za-z.\-]+)"' % (seg, kind)
    seen, out = set(), []
    for m in re.finditer(pat, html_text):
        full = "%s/%s/%s" % (BASE, seg, m.group(1))
        if full not in seen:
            seen.add(full)
            out.append(full)
    return out


# --------------------------------------------------------------- cleaning ----
def strip_tags(fragment):
    s = re.sub(r"(?is)<(script|style).*?</\1>", "", fragment)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = htmllib.unescape(s)
    s = s.replace("\u00a0", " ").replace("\u2011", "-")
    # source HTML hard-wraps mid-sentence; collapse all whitespace so a paragraph
    # renders as one Markdown list item instead of breaking the bullet
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def designator(text):
    """Return the leading (X) designator token, or None."""
    m = re.match(r"\(([A-Za-z0-9]{1,5})\)", text)
    return m.group(1) if m else None


class DepthInferrer:
    """Infer nesting depth from the (A)/(1)/(a)/(i)/(I) designator ladder."""

    def __init__(self):
        self.last_at = {}   # depth -> last designator token
        self.current = 0

    def depth_for(self, token):
        if token is None:
            return None
        if token.isdigit():
            cand = [1, 5]
        elif token.isupper():
            cand = [4] if (token in ROMAN_UPPER and len(token) > 1) else [0]
        else:  # lowercase
            if token in ROMAN_LOWER and len(token) > 1:
                cand = [3]
            elif token == "i":
                # ambiguous: letter (i) after (h), else first roman sub-item
                cand = [2] if self.last_at.get(2) == "h" else [3]
            else:
                cand = [2]
        # choose the candidate closest to the current position, preferring
        # a level already open or exactly one level deeper
        best = None
        for d in cand:
            if d <= self.current + 1:
                best = d if best is None else min(best, d)
        depth = cand[0] if best is None else best
        self.last_at[depth] = token
        for deeper in [k for k in self.last_at if k > depth]:
            del self.last_at[deeper]
        self.current = depth
        return depth


def table_to_markdown(table_html):
    rows = re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", table_html)
    md, widths = [], 0
    for row in rows:
        cells = [strip_tags(c).replace("\n", " ").replace("|", "\\|")
                 for c in re.findall(r"(?is)<t[hd][^>]*>(.*?)</t[hd]>", row)]
        if not cells:
            continue
        widths = max(widths, len(cells))
        md.append(cells)
    if not md:
        return []
    md = [r + [""] * (widths - len(r)) for r in md]
    out = ["| " + " | ".join(md[0]) + " |",
           "| " + " | ".join(["---"] * widths) + " |"]
    out += ["| " + " | ".join(r) + " |" for r in md[1:]]
    return out


# ----------------------------------------------------------------- parsing ---
def parse_document(html_text, url):
    """Return dict with title, meta, blocks, supplemental for one rule/section page."""
    h1 = re.search(r"(?is)<h1>(.*?)</h1>", html_text)
    title = strip_tags(h1.group(1)) if h1 else url.rsplit("/", 1)[-1]
    title = re.sub(r"\s*\|\s*", " | ", re.sub(r"\s+", " ", title)).strip()

    meta = {}
    for m in re.finditer(
        r'(?is)<div class="label">(.*?)</div>\s*<div class="value">(.*?)</div>', html_text
    ):
        k = strip_tags(m.group(1)).rstrip(":").strip()
        v = strip_tags(m.group(2)).strip()
        if k and v and k.lower() != "pdf":
            meta[k] = v

    body_m = re.search(r'(?is)<section class="laws-body">(.*?)</section>', html_text)
    blocks = []
    if body_m:
        body = body_m.group(1)
        inferrer = DepthInferrer()
        last_depth = 0
        # walk paragraphs and tables in document order
        for m in re.finditer(r"(?is)<p([^>]*)>(.*?)</p>|<table([^>]*)>(.*?)</table>", body):
            if m.group(4) is not None:
                rows = table_to_markdown(m.group(4))
                if rows:
                    blocks.append(("table", last_depth, rows))
                continue
            attrs, text = m.group(1) or "", strip_tags(m.group(2) or "")
            if not text:
                continue
            lvl = re.search(r"level-(\d+)", attrs)
            if lvl:
                depth = int(lvl.group(1)) - 1
                inferrer.current = depth
                tok = designator(text)
                if tok:
                    inferrer.last_at[depth] = tok
            else:
                tok = designator(text)
                depth = inferrer.depth_for(tok)
                if depth is None:
                    depth = last_depth  # unnumbered continuation paragraph
            last_depth = depth
            blocks.append(("p", depth, text))

    supplemental = {}
    sup = re.search(r'(?is)<div class="laws-additional-information">(.*?)</div>', html_text)
    if sup:
        chunk = re.sub(r"(?s)<!--.*?-->", "", sup.group(1))
        for m in re.finditer(r"(?is)<strong>(.*?)</strong>\s*<span>(.*?)</span>", chunk):
            k = strip_tags(m.group(1)).rstrip(":").strip()
            v = strip_tags(m.group(2)).strip()
            if k and v:
                supplemental[k] = v

    return {"url": url, "title": title, "meta": meta,
            "blocks": blocks, "supplemental": supplemental}


def render(doc, heading_level=2, include_supplemental=True):
    hl = "#" * heading_level
    out = ["%s %s" % (hl, doc["title"]), "", "URL: %s" % doc["url"], ""]
    for k, v in doc["meta"].items():
        out.append("**%s:** %s  " % (k, v))
    if doc["meta"]:
        out.append("")
    for kind, depth, payload in doc["blocks"]:
        indent = "    " * max(depth, 0)
        if kind == "p":
            out += ["%s- %s" % (indent, payload), ""]
        else:
            out += ["%s%s" % (indent, row) for row in payload]
            out.append("")
    if include_supplemental and doc["supplemental"]:
        out += ["%s Supplemental Information" % ("#" * (heading_level + 1)), ""]
        for k, v in doc["supplemental"].items():
            out.append("**%s:** %s  " % (k, v))
        out.append("")
    if not doc["blocks"]:
        out += ["> No rule text found on this page (it may be rescinded, "
                "reserved, or rendered differently).", ""]
    return out


def slug(doc):
    return re.sub(r"[^A-Za-z0-9.\-]+", "_", doc["url"].rsplit("/", 1)[-1])


# --------------------------------------------------------------------- main ---
def main():
    ap = argparse.ArgumentParser(description="codes.ohio.gov -> Markdown")
    ap.add_argument("targets", nargs="+", help="chapter/rule/section URLs or bare identifiers")
    ap.add_argument("-o", "--output", help="single combined .md output path")
    ap.add_argument("--split", help="directory: write one .md per rule/section")
    ap.add_argument("--cache", default=None, help="save live HTML here; never reuse cached responses")
    ap.add_argument("--delay", type=float, default=0.5, help="seconds between requests")
    ap.add_argument("--no-supplemental", action="store_true",
                    help="omit Authorized By / Prior Effective Dates blocks")
    args = ap.parse_args()

    if not args.output and not args.split:
        args.output = "ohio_laws_extract.md"

    pages, containers = [], []
    for token in args.targets:
        url = normalize(token)
        kind = page_kind(url)
        if kind in ("rule", "section"):
            pages.append(url)
        else:
            text = fetch(url, args.cache, args.delay)
            title = re.search(r"(?is)<h1>(.*?)</h1>", text)
            containers.append((url, strip_tags(title.group(1)) if title else url))
            kids = child_links(text, url)
            if not kids:
                print("warning: no child rules/sections found on %s" % url, file=sys.stderr)
            pages.extend(kids)

    seen, ordered = set(), []
    for u in pages:
        if u not in seen:
            seen.add(u)
            ordered.append(u)

    docs = []
    for i, u in enumerate(ordered, 1):
        print("[%d/%d] %s" % (i, len(ordered), u), file=sys.stderr)
        docs.append(parse_document(fetch(u, args.cache, args.delay), u))

    stamp = time.strftime("%B %d, %Y")
    if args.split:
        os.makedirs(args.split, exist_ok=True)
        for d in docs:
            body = ["# %s" % d["title"], "", "URL: %s" % d["url"], "",
                    "Retrieved: %s" % stamp, "", "---", ""]
            body += render(d, 2, not args.no_supplemental)[2:]
            path = os.path.join(args.split, slug(d) + ".md")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("\n".join(body).rstrip() + "\n")
        print("wrote %d files to %s" % (len(docs), args.split))

    if args.output:
        if containers:
            head = "# " + re.sub(r"\s*\|\s*", " | ", re.sub(r"\s+", " ", containers[0][1]))
        else:
            head = "# Ohio Laws Extract"
        lines = [head, ""]
        for u, t in containers:
            lines.append("Source: %s" % u)
        if not containers:
            lines.append("Source: codes.ohio.gov")
        lines += ["", "Retrieved: %s" % stamp, "",
                  "Documents: %d" % len(docs), "", "---", ""]
        for d in docs:
            lines += render(d, 2, not args.no_supplemental)
            lines += ["---", ""]
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines).rstrip() + "\n")
        print("wrote %s (%d documents)" % (args.output, len(docs)))


if __name__ == "__main__":
    main()

