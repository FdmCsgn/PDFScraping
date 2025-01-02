# 📄 PDF'den JSON'a Dönüştürme Aracı

Bu araç, PDF dosyalarından metin içeriğini çıkarıp yapılandırılmış JSON formatına dönüştüren bir Python uygulamasıdır.

## 🎯 Amaç

- PDF dosyalarından metin çıkarma
- Sayfa bazlı yapılandırılmış veri oluşturma
- JSON formatında kolay işlenebilir veri saklama

## 🛠️ Kullanılan Teknolojiler

- **pdfminer.six**: PDF metin çıkarma işlemleri
- **json**: Veri serileştirme ve dosya işlemleri
- **Python**: Temel programlama dili

## 📚 Kod Açıklaması

### 1. Gerekli İmportlar
```python
from pdfminer.high_level import extract_text
import json
```

### 2. Dosya Yolları Tanımlama
```python
pdf_path = "kuş_hastalıkları.pdf"
json_path = "output.json"
```

### 3. PDF'den Metin Çıkarma
```python
pages_text = extract_text(pdf_path).split("\x0c")
```
- `extract_text()`: PDF'den ham metni çıkarır
- `\x0c`: Sayfa sonu karakteri
- `split()`: Metni sayfalara böler

### 4. JSON Veri Yapısı Oluşturma
```python
data = [
    {
        "Text": page_text.strip(),
        "label": page_num
    } 
    for page_num, page_text in enumerate(pages_text, start=1)
]
```
- Her sayfa için bir sözlük oluşturulur
- `Text`: Sayfanın metin içeriği
- `label`: Sayfa numarası
- `strip()`: Gereksiz boşlukları temizler
- `enumerate()`: Sayfa numaralandırma

### 5. JSON Dosyasına Kaydetme
```python
with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
```
- `encoding='utf-8'`: Türkçe karakter desteği
- `ensure_ascii=False`: Unicode karakterleri koruma
- `indent=4`: Okunaklı JSON formatı

## 📂 Çıktı Format Örneği

```json
[
    {
        "Text": "Birinci sayfanın içeriği...",
        "label": 1
    },
    {
        "Text": "İkinci sayfanın içeriği...",
        "label": 2
    }
]
```

## 🔧 Özellikler

1. **Unicode Desteği**
   - Türkçe karakterler korunur
   - UTF-8 encoding kullanılır

2. **Sayfa Yapısı**
   - Her sayfa ayrı bir JSON nesnesi
   - Sayfa numaraları otomatik atanır

3. **Metin Temizleme**
   - Gereksiz boşluklar temizlenir
   - Sayfa sonu karakterleri kaldırılır

## ⚙️ Kullanım

1. Gerekli kütüphaneleri yükleme:
```bash
pip install pdfminer.six
```

2. Script'i çalıştırma:
```bash
python pdf_to_json.py
```

## 🔍 Çıktı Kontrolü

- JSON dosyası okunabilir formatda
- Her sayfa ayrı bir nesne olarak saklanır
- Metin içeriği ve sayfa numarası eşleştirilir

## 🛡️ Hata Yönetimi Önerileri

```python
try:
    pages_text = extract_text(pdf_path).split("\x0c")
except Exception as e:
    print(f"PDF okuma hatası: {e}")
    exit(1)

try:
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"JSON yazma hatası: {e}")
    exit(1)
```

## 🚀 Geliştirme Önerileri

1. **Metadata Ekleme**
   - PDF başlığı
   - Oluşturma tarihi
   - Dosya boyutu

2. **İçerik Zenginleştirme**
   - Başlık çıkarma
   - Resim konumları
   - Formatlamayı koruma

3. **Performans İyileştirmeleri**
   - Büyük dosyalar için chunk işleme
   - Paralel işleme desteği
   - Bellek optimizasyonu

## 📝 Notlar

1. PDF dosyası erişilebilir olmalıdır
2. Yeterli disk alanı gereklidir
3. Unicode karakter desteği önemlidir
4. Büyük dosyalarda bellek kullanımına dikkat edilmelidir
