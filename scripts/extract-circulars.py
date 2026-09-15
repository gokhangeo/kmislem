from pathlib import Path
import json
import pdfplumber

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    Path(r"C:\Users\Administrator\Downloads\2025-4 Tescile  Konu  Harita  ve  Planlarin  Yapimi  ve  Kontrolu  Genelgesi.pdf"),
    Path(r"C:\Users\Administrator\Downloads\2023_5 Sayılı Talebe Bağlı İşlemlerin Yapımı ve Kontrolü Genelgesi.pdf"),
]

out = ROOT / "tmp" / "pdfs"
out.mkdir(parents=True, exist_ok=True)
manifest = []
for source in SOURCES:
    with pdfplumber.open(source) as pdf:
        pages = [page.extract_text(x_tolerance=2, y_tolerance=3) or "" for page in pdf.pages]
    target = out / f"{source.stem}.txt"
    target.write_text("\n\n".join(f"--- SAYFA {i + 1} ---\n{text}" for i, text in enumerate(pages)), encoding="utf-8")
    manifest.append({"file": str(source), "pages": len(pages), "text": str(target)})

print(json.dumps(manifest, ensure_ascii=False, indent=2))
