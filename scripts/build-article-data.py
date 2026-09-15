from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PDF_TEXT = ROOT / "tmp" / "pdfs"
FILES = {
    "2025/4": next(PDF_TEXT.glob("2025*.txt")),
    "2023/5": next(PDF_TEXT.glob("2023*.txt")),
}

noise = re.compile(
    r"^(--- SAYFA \d+ ---|T\.C\.|ÇEVRE, ŞEHİRCİLİK VE İKLİM DEĞİŞİKLİĞİ BAKANLIĞI|"
    r"Tapu ve Kadastro Genel Müdürlüğü|Kadastro Dairesi Başkanlığı|Bu belge, güvenli elektronik imza ile imzalanmıştır\.|"
    r"Doğrulama Kodu:.*|Doğrulama Adresi:.*|Dikmen Cad\..*|Tel:.*|www\.tkgm\.gov\.tr.*|"
    r"Teknik İnceleme Birimi|KEP Adresi.*|\d+ / \d+)$",
    re.IGNORECASE,
)

result = {}
for circular, path in FILES.items():
    raw = path.read_text(encoding="utf-8")
    cleaned = "\n".join(line.strip() for line in raw.splitlines() if line.strip() and not noise.match(line.strip()))
    matches = list(re.finditer(r"(?m)^MADDE\s+(\d+)\s*-?", cleaned))
    articles = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(cleaned)
        text = cleaned[match.start():end].strip()
        text = re.sub(r"\n{3,}", "\n\n", text)
        articles[match.group(1)] = text
    result[circular] = articles

(ROOT / "app" / "circular-articles.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
)
print({key: len(value) for key, value in result.items()})
