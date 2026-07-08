"""
Site content audit — fact-collection only, no recommendations.
"""
import re
import subprocess
import json
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(r"C:\Users\teruh\sacred-japan")


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
        self.imgs = []
        self.jsonld_raw = []
        self._in_jsonld = False
        self._jsonld_buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript"):
            self.skip += 1
            if tag == "script" and a.get("type") == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_buf = []
        if tag == "img":
            src = a.get("src", "")
            self.imgs.append(src)

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.skip = max(0, self.skip - 1)
            if tag == "script" and self._in_jsonld:
                self.jsonld_raw.append("".join(self._jsonld_buf))
                self._in_jsonld = False

    def handle_data(self, data):
        if self._in_jsonld:
            self._jsonld_buf.append(data)
        if self.skip == 0:
            self.parts.append(data)

    def text(self):
        return " ".join(self.parts)


def word_count(text):
    # Simple whitespace-token count (English approx.)
    tokens = re.findall(r"\b[\w'-]+\b", text)
    return len(tokens)


def jsonld_types(raw_list):
    types = []
    for raw in raw_list:
        try:
            obj = json.loads(raw.strip())
            if isinstance(obj, list):
                for o in obj:
                    t = o.get("@type")
                    if t:
                        types.append(t)
            else:
                t = obj.get("@type")
                if t:
                    types.append(t)
        except Exception:
            types.append("PARSE_ERR")
    return types


def git_last_date(path: Path):
    rel = path.relative_to(ROOT).as_posix()
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "log", "-1", "--format=%ad", "--date=short", "--", rel],
            capture_output=True, text=True, check=True
        )
        return out.stdout.strip() or "(none)"
    except subprocess.CalledProcessError:
        return "(err)"


def audit_page(p: Path):
    html = p.read_text(encoding="utf-8", errors="ignore")
    parser = TextExtractor()
    parser.feed(html)
    wc = word_count(parser.text())
    types = jsonld_types(parser.jsonld_raw)
    return {
        "path": p.relative_to(ROOT).as_posix(),
        "url": "/" + p.relative_to(ROOT).as_posix().replace("index.html", "").rstrip("/"),
        "words": wc,
        "img_count": len(parser.imgs),
        "imgs": parser.imgs,
        "jsonld_count": len(parser.jsonld_raw),
        "jsonld_types": types,
        "git_date": git_last_date(p),
    }


def main():
    html_files = sorted([p for p in ROOT.rglob("*.html")
                         if "scripts" not in p.parts and "node_modules" not in p.parts])
    results = [audit_page(p) for p in html_files]

    print("=" * 110)
    print("PER-PAGE AUDIT")
    print("=" * 110)
    print(f"{'PATH':<46} {'WORDS':>6} {'IMG':>4} {'JSON-LD':>8}  {'LAST COMMIT':<12}")
    print("-" * 110)
    for r in results:
        types_str = ",".join(r["jsonld_types"])[:24] or "-"
        print(f"{r['path']:<46} {r['words']:>6} {r['img_count']:>4} {types_str:>8}  {r['git_date']:<12}")

    print()
    print("=" * 110)
    print("IMAGE FILENAMES BY PAGE")
    print("=" * 110)
    for r in results:
        print(f"\n[{r['path']}]  ({r['img_count']} imgs)")
        for src in r["imgs"]:
            print(f"  - {src}")

    print()
    print("=" * 110)
    print("SITE TOTALS")
    print("=" * 110)
    total_pages = len(results)
    total_words = sum(r["words"] for r in results)
    total_imgs = sum(r["img_count"] for r in results)
    print(f"Total HTML pages   : {total_pages}")
    print(f"Total body words   : {total_words}")
    print(f"Total <img> tags   : {total_imgs}")

    # Section breakdown
    print()
    print("--- Guides ---")
    guides = [r for r in results if r["path"].startswith("guides/")]
    print(f"Guides count       : {len(guides)}")
    for r in guides:
        print(f"  {r['url']:<52} {r['words']:>6} words")

    print()
    print("--- Subpages ---")
    subpage_paths = ["castles/index.html", "crafts/index.html", "anime/index.html",
                     "regional-food/index.html", "about/index.html"]
    flat_pages = ["contact.html", "privacy-policy.html", "terms.html", "index.html"]
    for r in results:
        if r["path"] in subpage_paths or r["path"] in flat_pages:
            print(f"  {r['path']:<46} {r['words']:>6} words")

    # Images folder
    print()
    print("=" * 110)
    print("images/ FOLDER")
    print("=" * 110)
    img_dir = ROOT / "images"
    files = sorted([f.name for f in img_dir.iterdir() if f.is_file()])
    print(f"Total files: {len(files)}")
    for f in files:
        print(f"  {f}")

    # Thin pages
    print()
    print("=" * 110)
    print("THIN PAGES (< 500 body words), sorted ascending")
    print("=" * 110)
    thin = sorted([r for r in results if r["words"] < 500], key=lambda x: x["words"])
    print(f"Count: {len(thin)}")
    for r in thin:
        print(f"  {r['words']:>5} words   {r['path']}")


if __name__ == "__main__":
    main()
