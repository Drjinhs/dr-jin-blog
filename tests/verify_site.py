import html.parser
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = "http://127.0.0.1:4173/"

class AuditParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.h1 = 0
        self.refs = []
        self.images = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        self.tags.append(tag)
        if data.get("id"):
            self.ids.add(data["id"])
        if tag == "h1":
            self.h1 += 1
        if tag in {"img", "script", "link"}:
            ref = data.get("src") or data.get("href")
            if ref and ref.startswith("./"):
                self.refs.append(ref[2:])
        if tag == "img":
            self.images.append(data)

def get(path=""):
    with urllib.request.urlopen(BASE + path, timeout=5) as response:
        assert response.status == 200, (path, response.status)
        return response.read()

document = get().decode("utf-8")
parser = AuditParser()
parser.feed(document)
assert parser.h1 == 1
assert {"header", "main", "section", "footer"}.issubset(parser.tags)
assert {"top", "about", "expertise", "activities", "programs", "insights", "career", "contact"}.issubset(parser.ids)
assert all(image.get("alt") for image in parser.images)
for ref in parser.refs:
    get(ref)
for required in ["404.html", "robots.txt", "sitemap.xml", "site.webmanifest", "favicon.ico"]:
    get(required)
print(f"PASS: semantic HTML, {len(parser.refs)} local assets, metadata endpoints, and image alternatives verified")
