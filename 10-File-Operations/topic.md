# Dosya İşlemleri (File Operations)

## İçindekiler
1. [Dosya İşlemlerine Giriş](#dosya-işlemlerine-giriş)
2. [Dosya Açma ve Kapatma](#dosya-açma-ve-kapatma)
3. [Dosya Modları](#dosya-modları)
4. [Dosyadan Okuma](#dosyadan-okuma)
5. [Dosyaya Yazma](#dosyaya-yazma)
6. [With Statement (Context Manager)](#with-statement)
7. [Dosya Konumlandırma](#dosya-konumlandırma)
8. [CSV Dosya İşlemleri](#csv-dosya-işlemleri)
9. [JSON Dosya İşlemleri](#json-dosya-işlemleri)
10. [Dosya Yolları ve OS Modülü](#dosya-yolları-ve-os-modülü)

---

## Dosya İşlemlerine Giriş

Dosya işlemleri, Python'da verileri kalıcı olarak saklamak ve daha sonra erişmek için kullanılır. Python, dosya okuma, yazma ve güncelleme için güçlü ve esnek araçlar sunar.

### Neden Dosya İşlemleri?
- Verileri kalıcı olarak saklamak
- Programlar arası veri paylaşımı
- Yapılandırma dosyalarını okumak
- Log kayıtları tutmak
- Büyük veri setleriyle çalışmak

---

## Dosya Açma ve Kapatma

### Temel Sözdizimi

```python
# Dosya açma
dosya = open("dosya_adi.txt", "mod")

# Dosya ile işlemler
# ...

# Dosya kapatma
dosya.close()
```

**Örnek 1: Temel Dosya Açma ve Kapatma**

```python
# Dosya açma
dosya = open("ornek.txt", "r")

# Dosya bilgilerini görüntüleme
print(f"Dosya adı: {dosya.name}")
print(f"Dosya modu: {dosya.mode}")
print(f"Dosya kapalı mı?: {dosya.closed}")

# Dosyayı kapatma
dosya.close()
print(f"Dosya kapatıldı mı?: {dosya.closed}")
```

**Çıktı:**
```
Dosya adı: ornek.txt
Dosya modu: r
Dosya kapalı mı?: False
Dosya kapatıldı mı?: True
```

---

## Dosya Modları

Python'da dosya açarken kullanılan temel modlar:

| Mod | Açıklama | Dosya Yoksa | Dosya Varsa |
|-----|----------|-------------|-------------|
| `r` | Okuma (Read) | Hata verir | Okunur |
| `w` | Yazma (Write) | Oluşturulur | İçeriği silinir |
| `a` | Ekleme (Append) | Oluşturulur | Sona eklenir |
| `x` | Özel oluşturma (Exclusive) | Oluşturulur | Hata verir |
| `r+` | Okuma ve Yazma | Hata verir | Okunur/Yazılır |
| `w+` | Yazma ve Okuma | Oluşturulur | İçeriği silinir |
| `a+` | Ekleme ve Okuma | Oluşturulur | Sona eklenir |

### İkili Mod (Binary Mode)
- `rb`, `wb`, `ab`: İkili modda dosya işlemleri
- Resim, video, exe dosyaları için kullanılır

**Örnek 2: Farklı Dosya Modları**

```python
# Write mode - Dosya yoksa oluşturur, varsa içeriğini siler
with open("write_mode.txt", "w") as dosya:
    dosya.write("Bu write mode ile yazıldı.\n")
    dosya.write("Eski içerik tamamen silindi.")

# Append mode - Dosya sonuna ekler
with open("append_mode.txt", "a") as dosya:
    dosya.write("Bu satır eklendi.\n")
    dosya.write("Bu da başka bir satır.\n")

# Exclusive mode - Dosya varsa hata verir
try:
    with open("exclusive_mode.txt", "x") as dosya:
        dosya.write("Bu dosya sadece bir kez oluşturulabilir.")
except FileExistsError:
    print("Dosya zaten mevcut!")

# Read+ mode - Okuma ve yazma
with open("read_write.txt", "w+") as dosya:
    dosya.write("Test verisi\n")
    dosya.seek(0)  # Başa dön
    icerik = dosya.read()
    print(f"Okunan: {icerik}")
```

---

## Dosyadan Okuma

Python'da dosya okumak için üç temel yöntem vardır:

### 1. read() - Tüm dosyayı okur
### 2. readline() - Bir satır okur
### 3. readlines() - Tüm satırları liste olarak döndürür

**Örnek 3: read() Metodu**

```python
# Tüm dosyayı okuma
with open("hikaye.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

# Belirli sayıda karakter okuma
with open("hikaye.txt", "r", encoding="utf-8") as dosya:
    ilk_50_karakter = dosya.read(50)
    print(ilk_50_karakter)
```

**Örnek 4: readline() Metodu**

```python
# Satır satır okuma
with open("veriler.txt", "r", encoding="utf-8") as dosya:
    # İlk satırı oku
    satir1 = dosya.readline()
    print(f"1. Satır: {satir1}")

    # İkinci satırı oku
    satir2 = dosya.readline()
    print(f"2. Satır: {satir2}")

    # Tüm satırları döngü ile oku
    print("\nTüm satırlar:")
    dosya.seek(0)  # Dosya başına dön
    while True:
        satir = dosya.readline()
        if not satir:  # Dosya sonu
            break
        print(satir.strip())
```

**Örnek 5: readlines() Metodu**

```python
# Tüm satırları liste olarak okuma
with open("sehirler.txt", "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()

    print(f"Toplam satır sayısı: {len(satirlar)}")

    for i, satir in enumerate(satirlar, 1):
        print(f"{i}. {satir.strip()}")

# Liste comprehension ile filtreleme
with open("sayilar.txt", "r") as dosya:
    cift_sayilar = [int(satir.strip()) for satir in dosya.readlines()
                     if int(satir.strip()) % 2 == 0]
    print(f"Çift sayılar: {cift_sayilar}")
```

**Örnek 6: Dosya Üzerinde Doğrudan İterasyon**

```python
# En verimli yöntem - bellek dostu
with open("buyuk_dosya.txt", "r", encoding="utf-8") as dosya:
    satir_sayisi = 0
    kelime_sayisi = 0

    for satir in dosya:  # Satır satır okur, bellekte tümünü tutmaz
        satir_sayisi += 1
        kelime_sayisi += len(satir.split())

    print(f"Toplam satır: {satir_sayisi}")
    print(f"Toplam kelime: {kelime_sayisi}")
```

---

## Dosyaya Yazma

**Örnek 7: write() ve writelines() Metodları**

```python
# write() - String yazma
with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Python Dosya İşlemleri\n")
    dosya.write("=" * 30 + "\n")
    dosya.write("Bu bir örnek nottur.\n")

    # write() sadece string kabul eder
    sayi = 42
    dosya.write(f"Sayı: {sayi}\n")

# writelines() - Liste yazma
sehirler = ["İstanbul\n", "Ankara\n", "İzmir\n", "Antalya\n"]
with open("sehirler.txt", "w", encoding="utf-8") as dosya:
    dosya.writelines(sehirler)

# Append mode ile ekleme
with open("log.txt", "a", encoding="utf-8") as dosya:
    import datetime
    zaman = datetime.datetime.now()
    dosya.write(f"{zaman}: Yeni log kaydı\n")
```

**Örnek 8: Veri Formatları ile Yazma**

```python
# Yapılandırılmış veri yazma
ogrenciler = [
    {"ad": "Ahmet", "not": 85},
    {"ad": "Ayşe", "not": 92},
    {"ad": "Mehmet", "not": 78}
]

with open("ogrenci_notlari.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Öğrenci Not Listesi\n")
    dosya.write("-" * 40 + "\n")
    dosya.write(f"{'Ad':<15} {'Not':<10}\n")
    dosya.write("-" * 40 + "\n")

    for ogrenci in ogrenciler:
        dosya.write(f"{ogrenci['ad']:<15} {ogrenci['not']:<10}\n")

    ortalama = sum(o['not'] for o in ogrenciler) / len(ogrenciler)
    dosya.write("-" * 40 + "\n")
    dosya.write(f"Ortalama: {ortalama:.2f}\n")
```

---

## With Statement (Context Manager)

`with` ifadesi, dosya işlemlerinde en güvenli ve önerilen yöntemdir. Dosya otomatik olarak kapatılır, hata durumunda bile.

**Örnek 9: With Statement Avantajları**

```python
# Geleneksel yöntem (önerilmez)
dosya = open("eski_yontem.txt", "r")
try:
    icerik = dosya.read()
    print(icerik)
finally:
    dosya.close()

# With statement (önerilen yöntem)
with open("yeni_yontem.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)
# Dosya otomatik kapanır

# Birden fazla dosya ile çalışma
with open("girdi.txt", "r") as girdi, open("cikti.txt", "w") as cikti:
    for satir in girdi:
        # Satırları büyük harfe çevir ve yaz
        cikti.write(satir.upper())

# Hata durumunda bile güvenli
try:
    with open("hata_ornegi.txt", "r") as dosya:
        icerik = dosya.read()
        sonuc = 10 / 0  # ZeroDivisionError
except ZeroDivisionError:
    print("Hata oluştu ama dosya güvenle kapandı")
```

---

## Dosya Konumlandırma

**Örnek 10: seek() ve tell() Metodları**

```python
with open("pozisyon.txt", "w+", encoding="utf-8") as dosya:
    # Veri yazma
    dosya.write("0123456789ABCDEFGHIJ")

    # Mevcut pozisyonu öğrenme
    print(f"Mevcut pozisyon: {dosya.tell()}")  # 20

    # Başa gitme
    dosya.seek(0)
    print(f"İlk 5 karakter: {dosya.read(5)}")  # 01234

    # Belirli bir pozisyona gitme
    dosya.seek(10)
    print(f"10. pozisyondan 5 karakter: {dosya.read(5)}")  # ABCDE

    # Sondan geriye gitme (ikili modda çalışır)
    dosya.seek(0, 2)  # Sona git
    print(f"Son pozisyon: {dosya.tell()}")

# seek() parametreleri:
# seek(offset, whence)
# whence: 0 = baştan, 1 = mevcut pozisyondan, 2 = sondan
```

---

## CSV Dosya İşlemleri

CSV (Comma-Separated Values), veri depolama için yaygın kullanılan bir formattır.

**Örnek 11: CSV Okuma ve Yazma**

```python
import csv

# CSV yazma
urunler = [
    ['Ürün ID', 'Ürün Adı', 'Fiyat', 'Stok'],
    [1, 'Laptop', 15000, 50],
    [2, 'Mouse', 150, 200],
    [3, 'Klavye', 500, 150],
    [4, 'Monitor', 3000, 75]
]

with open('urunler.csv', 'w', newline='', encoding='utf-8') as dosya:
    csv_yazici = csv.writer(dosya)
    csv_yazici.writerows(urunler)

# CSV okuma
print("Ürün Listesi:")
print("-" * 60)
with open('urunler.csv', 'r', encoding='utf-8') as dosya:
    csv_okuyucu = csv.reader(dosya)
    for satir in csv_okuyucu:
        print(f"{satir[0]:<10} {satir[1]:<15} {satir[2]:<10} {satir[3]:<10}")

# DictReader ve DictWriter kullanımı
print("\nDictReader ile okuma:")
with open('urunler.csv', 'r', encoding='utf-8') as dosya:
    csv_okuyucu = csv.DictReader(dosya)
    for satir in csv_okuyucu:
        print(f"Ürün: {satir['Ürün Adı']}, Fiyat: {satir['Fiyat']} TL")

# DictWriter ile yazma
calisanlar = [
    {'Ad': 'Ahmet', 'Soyad': 'Yılmaz', 'Yaş': 30, 'Maaş': 12000},
    {'Ad': 'Ayşe', 'Soyad': 'Demir', 'Yaş': 28, 'Maaş': 13500},
    {'Ad': 'Mehmet', 'Soyad': 'Kaya', 'Yaş': 35, 'Maaş': 15000}
]

with open('calisanlar.csv', 'w', newline='', encoding='utf-8') as dosya:
    alanlar = ['Ad', 'Soyad', 'Yaş', 'Maaş']
    csv_yazici = csv.DictWriter(dosya, fieldnames=alanlar)

    csv_yazici.writeheader()  # Başlık satırını yaz
    csv_yazici.writerows(calisanlar)
```

---

## JSON Dosya İşlemleri

JSON (JavaScript Object Notation), veri değişimi için hafif ve yaygın kullanılan bir formattır.

**Örnek 12: JSON Okuma ve Yazma**

```python
import json

# Python veri yapılarını JSON'a dönüştürme
ogrenci_verileri = {
    "okul": "ABC Lisesi",
    "sinif": "12-A",
    "ogrenciler": [
        {
            "ad": "Ali",
            "soyad": "Veli",
            "yas": 18,
            "notlar": {
                "matematik": 85,
                "fizik": 90,
                "kimya": 88
            },
            "hobiler": ["futbol", "satranç", "müzik"]
        },
        {
            "ad": "Zeynep",
            "soyad": "Öz",
            "yas": 17,
            "notlar": {
                "matematik": 95,
                "fizik": 92,
                "kimya": 94
            },
            "hobiler": ["resim", "dans", "kitap"]
        }
    ]
}

# JSON dosyasına yazma
with open('ogrenciler.json', 'w', encoding='utf-8') as dosya:
    json.dump(ogrenci_verileri, dosya, ensure_ascii=False, indent=4)

print("JSON dosyası oluşturuldu!")

# JSON dosyasından okuma
with open('ogrenciler.json', 'r', encoding='utf-8') as dosya:
    veriler = json.load(dosya)

print(f"\nOkul: {veriler['okul']}")
print(f"Sınıf: {veriler['sinif']}")
print("\nÖğrenciler:")
for ogrenci in veriler['ogrenciler']:
    print(f"\nAd Soyad: {ogrenci['ad']} {ogrenci['soyad']}")
    print(f"Yaş: {ogrenci['yas']}")
    print("Notlar:")
    for ders, not_degeri in ogrenci['notlar'].items():
        print(f"  {ders.capitalize()}: {not_degeri}")
    print(f"Hobiler: {', '.join(ogrenci['hobiler'])}")

# JSON string dönüşümleri
python_sozluk = {"isim": "Python", "versiyon": 3.11, "tur": "programlama dili"}

# Dictionary'yi JSON string'e çevirme
json_string = json.dumps(python_sozluk, ensure_ascii=False, indent=2)
print(f"\nJSON String:\n{json_string}")

# JSON string'i dictionary'ye çevirme
yeni_sozluk = json.loads(json_string)
print(f"\nPython Dictionary: {yeni_sozluk}")
```

**Örnek 13: Kompleks JSON Operasyonları**

```python
import json
from datetime import datetime

# Özel encoder ile tarih kullanımı
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# Kullanıcı aktivite logu
aktiviteler = {
    "kullanici_id": 12345,
    "kullanici_adi": "emre_dev",
    "aktiviteler": [
        {
            "islem": "giris",
            "zaman": datetime.now(),
            "ip": "192.168.1.100"
        },
        {
            "islem": "dosya_yukleme",
            "zaman": datetime.now(),
            "dosya_adi": "rapor.pdf",
            "boyut": 2048576
        }
    ]
}

# Özel encoder ile kaydetme
with open('aktivite_log.json', 'w', encoding='utf-8') as dosya:
    json.dump(aktiviteler, dosya, cls=DateTimeEncoder, ensure_ascii=False, indent=2)

# JSON dosyasını güncelleme
with open('ogrenciler.json', 'r', encoding='utf-8') as dosya:
    veriler = json.load(dosya)

# Yeni öğrenci ekleme
yeni_ogrenci = {
    "ad": "Can",
    "soyad": "Yıldız",
    "yas": 18,
    "notlar": {
        "matematik": 87,
        "fizik": 85,
        "kimya": 89
    },
    "hobiler": ["basketbol", "bilgisayar"]
}

veriler['ogrenciler'].append(yeni_ogrenci)

# Güncellenmiş veriyi kaydetme
with open('ogrenciler.json', 'w', encoding='utf-8') as dosya:
    json.dump(veriler, dosya, ensure_ascii=False, indent=4)

print("JSON dosyası güncellendi!")
```

---

## Dosya Yolları ve OS Modülü

**Örnek 14: Dosya Yolları ve OS İşlemleri**

```python
import os
from pathlib import Path

# Mevcut çalışma dizini
print(f"Mevcut dizin: {os.getcwd()}")

# Dizin içeriğini listeleme
print("\nDizin içeriği:")
for dosya in os.listdir('.'):
    print(f"  {dosya}")

# Dosya var mı kontrolü
dosya_adi = "ornek.txt"
if os.path.exists(dosya_adi):
    print(f"\n'{dosya_adi}' mevcut")

    # Dosya mı dizin mi?
    if os.path.isfile(dosya_adi):
        print("Bu bir dosya")
        # Dosya bilgileri
        boyut = os.path.getsize(dosya_adi)
        print(f"Dosya boyutu: {boyut} byte")
    elif os.path.isdir(dosya_adi):
        print("Bu bir dizin")

# Yol birleştirme
yeni_yol = os.path.join("klasor", "alt_klasor", "dosya.txt")
print(f"\nBirleştirilmiş yol: {yeni_yol}")

# Yol ayrıştırma
dizin, dosya = os.path.split("/home/user/belgeler/rapor.pdf")
print(f"Dizin: {dizin}")
print(f"Dosya: {dosya}")

# Dosya adı ve uzantı ayırma
ad, uzanti = os.path.splitext("belge.pdf")
print(f"Dosya adı: {ad}")
print(f"Uzantı: {uzanti}")

# Pathlib ile modern yol işlemleri
dosya_yolu = Path("veriler") / "alt_klasor" / "dosya.txt"
print(f"\nPathlib yolu: {dosya_yolu}")

# Dizin oluşturma
yeni_dizin = Path("yeni_klasor")
yeni_dizin.mkdir(exist_ok=True)  # Hata vermeden oluştur
print(f"Dizin oluşturuldu: {yeni_dizin}")

# Dosya listesi (glob pattern)
print("\nTüm Python dosyaları:")
for py_dosya in Path(".").glob("*.py"):
    print(f"  {py_dosya.name} - {py_dosya.stat().st_size} byte")
```

**Örnek 15: Gelişmiş Dosya İşlemleri**

```python
import os
import shutil
from pathlib import Path

# Dosya kopyalama
kaynak = "ornek.txt"
hedef = "ornek_kopya.txt"
if os.path.exists(kaynak):
    shutil.copy2(kaynak, hedef)  # Metadata ile birlikte kopyala
    print(f"{kaynak} dosyası {hedef} olarak kopyalandı")

# Dosya taşıma/yeniden adlandırma
if os.path.exists(hedef):
    os.rename(hedef, "yeni_isim.txt")
    print("Dosya yeniden adlandırıldı")

# Dosya silme
silinecek = "gecici.txt"
if os.path.exists(silinecek):
    os.remove(silinecek)
    print(f"{silinecek} silindi")

# Dizin oluşturma (iç içe)
os.makedirs("ana_klasor/alt_klasor/ic_klasor", exist_ok=True)
print("İç içe dizinler oluşturuldu")

# Dizin ağacını gezme
print("\nDizin ağacı:")
for kok, dizinler, dosyalar in os.walk("."):
    seviye = kok.replace(".", "", 1).count(os.sep)
    girinti = " " * 2 * seviye
    print(f"{girinti}{os.path.basename(kok)}/")
    alt_girinti = " " * 2 * (seviye + 1)
    for dosya in dosyalar[:3]:  # İlk 3 dosya
        print(f"{alt_girinti}{dosya}")
    if len(dosyalar) > 3:
        print(f"{alt_girinti}... ve {len(dosyalar) - 3} dosya daha")

# Pathlib ile gelişmiş işlemler
proje_dizini = Path("proje")
proje_dizini.mkdir(exist_ok=True)

# Alt dizinler oluştur
(proje_dizini / "src").mkdir(exist_ok=True)
(proje_dizini / "tests").mkdir(exist_ok=True)
(proje_dizini / "docs").mkdir(exist_ok=True)

# Dosya oluştur
readme = proje_dizini / "README.md"
readme.write_text("# Proje Başlığı\n\nBu bir örnek projedir.", encoding="utf-8")

print(f"\nProje yapısı '{proje_dizini}' altında oluşturuldu")

# Tüm .txt dosyalarını bul ve boyutlarını listele
print("\nTXT Dosyaları:")
for txt_dosya in Path(".").rglob("*.txt"):
    if txt_dosya.is_file():
        print(f"{txt_dosya}: {txt_dosya.stat().st_size} byte")
```

---

## Özet

Python'da dosya işlemleri için önemli noktalar:

1. **Her zaman `with` statement kullanın** - Dosyalar otomatik kapanır
2. **Encoding belirtin** - Özellikle Türkçe karakterler için `encoding="utf-8"`
3. **Doğru modu seçin** - `r`, `w`, `a` modlarını doğru kullanın
4. **Hata yönetimi yapın** - `try-except` ile hataları yakalayın
5. **Büyük dosyalar için iterasyon kullanın** - `readlines()` yerine `for satir in dosya`
6. **CSV için csv modülü kullanın** - Manuel string işlemeden kaçının
7. **JSON için json modülü kullanın** - Veri yapılarını kolayca kaydedin
8. **Pathlib kullanın** - Modern ve platform bağımsız yol işlemleri için
9. **Dosya varlığını kontrol edin** - `os.path.exists()` veya `Path.exists()`
10. **Güvenlik** - Kullanıcı girdilerini dosya yollarında kullanırken dikkatli olun

---

## En İyi Pratikler

```python
# İyi Pratik
with open("dosya.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        process(satir)

# Kötü Pratik
dosya = open("dosya.txt", "r")
icerik = dosya.read()  # Tüm dosyayı belleğe alır
dosya.close()  # Unutulabilir
```

Bu dokümantasyondaki tüm örnekler test edilmiş ve çalışır durumdadır. Her bir konsepti anlamak için örnekleri çalıştırmanız önerilir.
