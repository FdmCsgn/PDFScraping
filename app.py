from pdfminer.high_level import extract_text
import json

# PDF dosyasının yolu
pdf_path = "kuş_hastalıkları.pdf"
# Çıktı olarak oluşturulacak JSON dosyasının yolu
json_path = "output.json"

# Sayfa sayfa metni çıkarma ve JSON formatına kaydetme
pages_text = extract_text(pdf_path).split("\x0c")  # Sayfa sonu karakterine göre böl

# JSON verisini oluştur
data = [{"Text": page_text.strip(),"label": page_num} for page_num, page_text in enumerate(pages_text, start=1)]

# JSON dosyasına yazma
with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"PDF içeriği {json_path} dosyasına başarıyla kaydedildi.")
