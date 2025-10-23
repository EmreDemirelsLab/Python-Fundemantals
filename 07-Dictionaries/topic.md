# Dictionary (Sözlük) - Python Fundamentals

## İçindekiler
1. [Dictionary Nedir?](#dictionary-nedir)
2. [Dictionary Oluşturma](#dictionary-oluşturma)
3. [Elemanlara Erişim](#elemanlara-erişim)
4. [Dictionary Metodları](#dictionary-metodları)
5. [Dictionary Comprehension](#dictionary-comprehension)
6. [İç İçe Dictionary'ler](#iç-içe-dictionaryler)
7. [İleri Seviye Kullanım](#ileri-seviye-kullanım)

---

## Dictionary Nedir?

**Dictionary (Sözlük)**, Python'da anahtar-değer (key-value) çiftleri şeklinde veri saklayan, değiştirilebilir (mutable) ve sırasız bir veri yapısıdır. Dictionary'ler süslü parantezler `{}` ile tanımlanır ve her eleman bir anahtar ve ona karşılık gelen bir değerden oluşur.

### Temel Özellikler:
- **Anahtar-Değer Çiftleri**: Her eleman bir key ve value içerir
- **Değiştirilebilir**: Elemanlar eklenebilir, silinebilir veya güncellenebilir
- **Anahtarlar Benzersizdir**: Her anahtar sadece bir kez kullanılabilir
- **Hızlı Erişim**: Anahtarlar üzerinden O(1) karmaşıklığında erişim
- **Python 3.7+**: Ekleme sırası korunur

---

## Dictionary Oluşturma

### Örnek 1: Temel Dictionary Oluşturma

```python
# Boş dictionary oluşturma
bos_sozluk = {}
bos_sozluk2 = dict()

# Anahtar-değer çiftleri ile dictionary oluşturma
ogrenci = {
    "ad": "Ahmet",
    "soyad": "Yılmaz",
    "yas": 20,
    "not_ortalamasi": 85.5
}

print(ogrenci)  # {'ad': 'Ahmet', 'soyad': 'Yılmaz', 'yas': 20, 'not_ortalamasi': 85.5}
print(type(ogrenci))  # <class 'dict'>
```

### Örnek 2: dict() Fonksiyonu ile Oluşturma

```python
# dict() constructor kullanarak
kisi = dict(ad="Ayşe", soyad="Demir", yas=25, sehir="İstanbul")
print(kisi)  # {'ad': 'Ayşe', 'soyad': 'Demir', 'yas': 25, 'sehir': 'İstanbul'}

# Tuple listesinden dictionary oluşturma
bilgiler = [("ad", "Mehmet"), ("yas", 30), ("meslek", "Mühendis")]
kisi2 = dict(bilgiler)
print(kisi2)  # {'ad': 'Mehmet', 'yas': 30, 'meslek': 'Mühendis'}

# İki listeden dictionary oluşturma (zip kullanarak)
anahtarlar = ["marka", "model", "yil"]
degerler = ["Toyota", "Corolla", 2023]
araba = dict(zip(anahtarlar, degerler))
print(araba)  # {'marka': 'Toyota', 'model': 'Corolla', 'yil': 2023}
```

### Örnek 3: Farklı Veri Tipleri ile Dictionary

```python
# Farklı tipte değerler içeren dictionary
karmasik_sozluk = {
    "string": "metin",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "dict": {"ic": "sozluk"},
    "none": None
}

print(karmasik_sozluk["list"])  # [1, 2, 3]
print(karmasik_sozluk["dict"])  # {'ic': 'sozluk'}
```

---

## Elemanlara Erişim

### Örnek 4: Köşeli Parantez ile Erişim

```python
ogrenci = {
    "ad": "Zeynep",
    "soyad": "Kaya",
    "yas": 22,
    "bolum": "Bilgisayar Mühendisliği"
}

# Anahtarla değere erişim
print(ogrenci["ad"])      # Zeynep
print(ogrenci["bolum"])   # Bilgisayar Mühendisliği

# Olmayan bir anahtara erişim - HATA!
try:
    print(ogrenci["telefon"])  # KeyError hatası verir
except KeyError as e:
    print(f"Hata: {e} anahtarı bulunamadı")
```

### Örnek 5: get() Metodu ile Güvenli Erişim

```python
ogrenci = {
    "ad": "Ali",
    "soyad": "Veli",
    "yas": 21
}

# get() metodu - olmayan anahtar için None döner
print(ogrenci.get("ad"))       # Ali
print(ogrenci.get("telefon"))  # None

# Varsayılan değer belirtme
print(ogrenci.get("telefon", "Telefon numarası yok"))  # Telefon numarası yok
print(ogrenci.get("email", "email@example.com"))       # email@example.com

# in operatörü ile anahtar kontrolü
if "yas" in ogrenci:
    print(f"Yaş: {ogrenci['yas']}")  # Yaş: 21

if "adres" not in ogrenci:
    print("Adres bilgisi mevcut değil")
```

### Örnek 6: Dictionary Elemanlarını Değiştirme ve Ekleme

```python
urun = {
    "isim": "Laptop",
    "fiyat": 15000,
    "stok": 50
}

# Mevcut değeri değiştirme
urun["fiyat"] = 14500
print(urun)  # {'isim': 'Laptop', 'fiyat': 14500, 'stok': 50}

# Yeni anahtar-değer çifti ekleme
urun["marka"] = "Dell"
urun["garanti"] = "2 yıl"
print(urun)  # {'isim': 'Laptop', 'fiyat': 14500, 'stok': 50, 'marka': 'Dell', 'garanti': '2 yıl'}

# Birden fazla güncelleme
urun["stok"] = 45
urun["indirim"] = True
print(urun)
```

---

## Dictionary Metodları

### Örnek 7: keys(), values() ve items() Metodları

```python
kitap = {
    "baslik": "Python Programlama",
    "yazar": "Guido van Rossum",
    "yil": 2023,
    "sayfa": 450
}

# keys() - Tüm anahtarları döner
anahtarlar = kitap.keys()
print(anahtarlar)       # dict_keys(['baslik', 'yazar', 'yil', 'sayfa'])
print(list(anahtarlar)) # ['baslik', 'yazar', 'yil', 'sayfa']

# values() - Tüm değerleri döner
degerler = kitap.values()
print(degerler)       # dict_values(['Python Programlama', 'Guido van Rossum', 2023, 450])
print(list(degerler)) # ['Python Programlama', 'Guido van Rossum', 2023, 450]

# items() - Tüm anahtar-değer çiftlerini tuple olarak döner
ciftler = kitap.items()
print(ciftler)       # dict_items([('baslik', 'Python Programlama'), ...])
print(list(ciftler)) # [('baslik', 'Python Programlama'), ('yazar', 'Guido van Rossum'), ...]

# Döngü ile kullanım
print("\n--- Kitap Bilgileri ---")
for anahtar, deger in kitap.items():
    print(f"{anahtar}: {deger}")
```

### Örnek 8: update() Metodu

```python
kullanici = {
    "username": "ahmet123",
    "email": "ahmet@example.com"
}

# Yeni bilgiler ekleme ve mevcut bilgileri güncelleme
kullanici.update({
    "email": "ahmet.yeni@example.com",  # Güncelleme
    "telefon": "555-1234",              # Yeni ekleme
    "adres": "İstanbul"                 # Yeni ekleme
})
print(kullanici)
# {'username': 'ahmet123', 'email': 'ahmet.yeni@example.com', 'telefon': '555-1234', 'adres': 'İstanbul'}

# İki dictionary'yi birleştirme
ek_bilgiler = {"yas": 28, "meslek": "Yazılımcı"}
kullanici.update(ek_bilgiler)
print(kullanici)

# Python 3.9+ için birleştirme operatörü
yeni_kullanici = kullanici | {"durum": "aktif", "seviye": "pro"}
print(yeni_kullanici)
```

### Örnek 9: pop() ve popitem() Metodları

```python
envanter = {
    "kalem": 100,
    "defter": 50,
    "silgi": 75,
    "cetvel": 30
}

# pop() - Belirtilen anahtarı siler ve değerini döner
kalem_sayisi = envanter.pop("kalem")
print(f"Silinen kalem sayısı: {kalem_sayisi}")  # 100
print(envanter)  # {'defter': 50, 'silgi': 75, 'cetvel': 30}

# Olmayan anahtar için varsayılan değer
boya = envanter.pop("boya", 0)
print(f"Boya sayısı: {boya}")  # 0

# popitem() - Son eklenen elemanı siler (Python 3.7+)
son_eleman = envanter.popitem()
print(f"Silinen eleman: {son_eleman}")  # ('cetvel', 30)
print(envanter)  # {'defter': 50, 'silgi': 75}

# clear() - Tüm elemanları siler
envanter.clear()
print(envanter)  # {}
```

### Örnek 10: setdefault() ve copy() Metodları

```python
sayac = {"a": 1, "b": 2}

# setdefault() - Anahtar varsa değerini döner, yoksa ekler
deger1 = sayac.setdefault("a", 0)  # "a" var, mevcut değeri döner
print(deger1)  # 1

deger2 = sayac.setdefault("c", 0)  # "c" yok, ekler ve varsayılan değeri döner
print(deger2)  # 0
print(sayac)   # {'a': 1, 'b': 2, 'c': 0}

# copy() - Dictionary'nin sığ kopyasını oluşturur
orijinal = {"x": 10, "y": 20}
kopya = orijinal.copy()

kopya["x"] = 100
print(orijinal)  # {'x': 10, 'y': 20}  - Değişmedi
print(kopya)     # {'x': 100, 'y': 20} - Değişti

# Referans ile kopyalama (DİKKAT!)
referans = orijinal
referans["x"] = 999
print(orijinal)  # {'x': 999, 'y': 20}  - Değişti!
```

### Örnek 11: fromkeys() Metodu

```python
# fromkeys() - Belirtilen anahtarlarla yeni dictionary oluşturur
anahtarlar = ["ad", "soyad", "yas", "email"]
bos_form = dict.fromkeys(anahtarlar)
print(bos_form)  # {'ad': None, 'soyad': None, 'yas': None, 'email': None}

# Varsayılan değer ile
varsayilan_form = dict.fromkeys(anahtarlar, "Bilinmiyor")
print(varsayilan_form)
# {'ad': 'Bilinmiyor', 'soyad': 'Bilinmiyor', 'yas': 'Bilinmiyor', 'email': 'Bilinmiyor'}

# Sayısal değerlerle
sifirla = dict.fromkeys(["a", "b", "c"], 0)
print(sifirla)  # {'a': 0, 'b': 0, 'c': 0}
```

---

## Dictionary Comprehension

### Örnek 12: Temel Dictionary Comprehension

```python
# Liste elemanlarının karelerini dictionary olarak oluşturma
sayilar = [1, 2, 3, 4, 5]
kareler = {sayi: sayi**2 for sayi in sayilar}
print(kareler)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# String'lerin uzunluklarını dictionary olarak
kelimeler = ["elma", "armut", "muz", "çilek"]
uzunluklar = {kelime: len(kelime) for kelime in kelimeler}
print(uzunluklar)  # {'elma': 4, 'armut': 5, 'muz': 3, 'çilek': 5}

# Tuple listesinden dictionary oluşturma
ogrenciler = [("Ahmet", 85), ("Ayşe", 92), ("Mehmet", 78)]
notlar = {isim: not_degeri for isim, not_degeri in ogrenciler}
print(notlar)  # {'Ahmet': 85, 'Ayşe': 92, 'Mehmet': 78}
```

### Örnek 13: Koşullu Dictionary Comprehension

```python
# Çift sayıların karelerini alma
sayilar = range(1, 11)
cift_kareler = {sayi: sayi**2 for sayi in sayilar if sayi % 2 == 0}
print(cift_kareler)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Geçen öğrencileri filtreleme
tum_notlar = {"Ali": 45, "Veli": 75, "Ayşe": 88, "Fatma": 52, "Mehmet": 90}
gecenler = {isim: not_degeri for isim, not_degeri in tum_notlar.items() if not_degeri >= 50}
print(gecenler)  # {'Veli': 75, 'Ayşe': 88, 'Fatma': 52, 'Mehmet': 90}

# Büyük harfle başlayanları seçme
kelimeler = {"elma": 5, "Armut": 8, "muz": 3, "Çilek": 10}
buyuk_harfli = {k: v for k, v in kelimeler.items() if k[0].isupper()}
print(buyuk_harfli)  # {'Armut': 8, 'Çilek': 10}
```

### Örnek 14: Dictionary'leri Dönüştürme ve Manipülasyon

```python
# Fiyatları TL'den USD'ye çevirme
urunler_tl = {"laptop": 30000, "telefon": 15000, "tablet": 8000}
kur = 30.5
urunler_usd = {urun: round(fiyat / kur, 2) for urun, fiyat in urunler_tl.items()}
print(urunler_usd)  # {'laptop': 983.61, 'telefon': 491.8, 'tablet': 262.3}

# Anahtar ve değerleri yer değiştirme
orijinal = {"tr": "Türkiye", "us": "Amerika", "uk": "İngiltere"}
ters_cevrilmis = {deger: anahtar for anahtar, deger in orijinal.items()}
print(ters_cevrilmis)  # {'Türkiye': 'tr', 'Amerika': 'us', 'İngiltere': 'uk'}

# Değerleri büyük harfe çevirme
sehirler = {"ankara": "turkey", "paris": "france", "london": "uk"}
buyuk_harf = {k: v.upper() for k, v in sehirler.items()}
print(buyuk_harf)  # {'ankara': 'TURKEY', 'paris': 'FRANCE', 'london': 'UK'}
```

---

## İç İçe Dictionary'ler

### Örnek 15: İç İçe Dictionary Oluşturma ve Erişim

```python
# Öğrenci veritabanı - iç içe dictionary
ogrenciler = {
    "001": {
        "ad": "Ahmet",
        "soyad": "Yılmaz",
        "yas": 20,
        "notlar": {
            "matematik": 85,
            "fizik": 78,
            "kimya": 92
        }
    },
    "002": {
        "ad": "Ayşe",
        "soyad": "Demir",
        "yas": 21,
        "notlar": {
            "matematik": 95,
            "fizik": 88,
            "kimya": 90
        }
    },
    "003": {
        "ad": "Mehmet",
        "soyad": "Kaya",
        "yas": 22,
        "notlar": {
            "matematik": 72,
            "fizik": 85,
            "kimya": 79
        }
    }
}

# İç içe elemanlara erişim
print(ogrenciler["001"]["ad"])  # Ahmet
print(ogrenciler["002"]["notlar"]["matematik"])  # 95

# Döngü ile tüm öğrencileri listeleme
for ogrenci_no, bilgiler in ogrenciler.items():
    print(f"\nÖğrenci No: {ogrenci_no}")
    print(f"Ad Soyad: {bilgiler['ad']} {bilgiler['soyad']}")
    print(f"Yaş: {bilgiler['yas']}")
    print("Notlar:")
    for ders, not_degeri in bilgiler['notlar'].items():
        print(f"  {ders}: {not_degeri}")

    # Ortalama hesaplama
    ortalama = sum(bilgiler['notlar'].values()) / len(bilgiler['notlar'])
    print(f"Ortalama: {ortalama:.2f}")
```

### Örnek 16: Şirket Organizasyon Yapısı

```python
sirket = {
    "genel_mudurluk": {
        "mudur": "Ali Veli",
        "calisanlar": ["Ayşe", "Fatma"],
        "departmanlar": {
            "yazilim": {
                "mudur": "Mehmet Yılmaz",
                "calisanlar": ["Ahmet", "Zeynep", "Can"],
                "teknolojiler": ["Python", "JavaScript", "Java"]
            },
            "muhasebe": {
                "mudur": "Elif Demir",
                "calisanlar": ["Hasan", "Selin"],
                "yazilimlar": ["SAP", "Excel"]
            },
            "pazarlama": {
                "mudur": "Kemal Öz",
                "calisanlar": ["Deniz", "Burak", "Özge"],
                "platformlar": ["Instagram", "LinkedIn", "Twitter"]
            }
        }
    }
}

# Yazılım departmanı bilgilerine erişim
yazilim_dept = sirket["genel_mudurluk"]["departmanlar"]["yazilim"]
print(f"Yazılım Müdürü: {yazilim_dept['mudur']}")
print(f"Çalışan Sayısı: {len(yazilim_dept['calisanlar'])}")
print(f"Kullanılan Teknolojiler: {', '.join(yazilim_dept['teknolojiler'])}")

# Tüm departmanları listeleme
print("\n--- Tüm Departmanlar ---")
for dept_ad, dept_bilgi in sirket["genel_mudurluk"]["departmanlar"].items():
    print(f"\n{dept_ad.upper()} Departmanı:")
    print(f"  Müdür: {dept_bilgi['mudur']}")
    print(f"  Çalışanlar: {', '.join(dept_bilgi['calisanlar'])}")
```

### Örnek 17: E-Ticaret Sepet Sistemi

```python
# Alışveriş sepeti - iç içe dictionary
sepet = {
    "musteri": {
        "ad": "Ahmet Yılmaz",
        "email": "ahmet@example.com",
        "adres": {
            "il": "İstanbul",
            "ilce": "Kadıköy",
            "posta_kodu": "34710"
        }
    },
    "urunler": {
        "001": {
            "isim": "Laptop",
            "fiyat": 15000,
            "adet": 1,
            "kategori": "Elektronik"
        },
        "002": {
            "isim": "Klavye",
            "fiyat": 500,
            "adet": 2,
            "kategori": "Aksesuar"
        },
        "003": {
            "isim": "Mouse",
            "fiyat": 300,
            "adet": 1,
            "kategori": "Aksesuar"
        }
    },
    "kargo": {
        "firma": "MNG Kargo",
        "ucret": 50,
        "tahmini_sure": "2-3 gün"
    }
}

# Sepet özeti
print("=" * 50)
print("ALIŞVERİŞ SEPETİ ÖZETİ")
print("=" * 50)
print(f"Müşteri: {sepet['musteri']['ad']}")
print(f"Email: {sepet['musteri']['email']}")
print(f"Adres: {sepet['musteri']['adres']['ilce']}/{sepet['musteri']['adres']['il']}")
print("\n--- ÜRÜNLER ---")

toplam_tutar = 0
for urun_id, urun_bilgi in sepet["urunler"].items():
    ara_toplam = urun_bilgi["fiyat"] * urun_bilgi["adet"]
    toplam_tutar += ara_toplam
    print(f"{urun_bilgi['isim']} - {urun_bilgi['adet']} adet x {urun_bilgi['fiyat']} TL = {ara_toplam} TL")

kargo_ucreti = sepet["kargo"]["ucret"]
genel_toplam = toplam_tutar + kargo_ucreti

print(f"\nAra Toplam: {toplam_tutar} TL")
print(f"Kargo ({sepet['kargo']['firma']}): {kargo_ucreti} TL")
print(f"GENEL TOPLAM: {genel_toplam} TL")
print(f"Tahmini Teslimat: {sepet['kargo']['tahmini_sure']}")
print("=" * 50)
```

---

## İleri Seviye Kullanım

### Örnek 18: Dictionary ile Veri Analizi

```python
# Satış verileri analizi
satis_verileri = {
    "2023-01": {"gelir": 50000, "gider": 30000, "musteri": 120},
    "2023-02": {"gelir": 55000, "gider": 32000, "musteri": 135},
    "2023-03": {"gelir": 62000, "gider": 35000, "musteri": 150},
    "2023-04": {"gelir": 58000, "gider": 33000, "musteri": 145},
    "2023-05": {"gelir": 70000, "gider": 38000, "musteri": 160}
}

# Toplam istatistikler
toplam_gelir = sum(ay["gelir"] for ay in satis_verileri.values())
toplam_gider = sum(ay["gider"] for ay in satis_verileri.values())
toplam_kar = toplam_gelir - toplam_gider
ortalama_musteri = sum(ay["musteri"] for ay in satis_verileri.values()) / len(satis_verileri)

print("SATIŞ VERİLERİ ANALİZİ")
print("=" * 50)
print(f"Toplam Gelir: {toplam_gelir:,} TL")
print(f"Toplam Gider: {toplam_gider:,} TL")
print(f"Net Kar: {toplam_kar:,} TL")
print(f"Ortalama Müşteri Sayısı: {ortalama_musteri:.1f}")

# En iyi performans gösteren ay
en_iyi_ay = max(satis_verileri.items(), key=lambda x: x[1]["gelir"] - x[1]["gider"])
print(f"\nEn Karlı Ay: {en_iyi_ay[0]} - Kar: {en_iyi_ay[1]['gelir'] - en_iyi_ay[1]['gider']:,} TL")

# Aylık detaylar
print("\n--- AYLIK DETAYLAR ---")
for ay, veriler in satis_verileri.items():
    kar = veriler["gelir"] - veriler["gider"]
    kar_marji = (kar / veriler["gelir"]) * 100
    print(f"{ay}: Gelir={veriler['gelir']:,} TL, Kar={kar:,} TL, Müşteri={veriler['musteri']}, Kar Marjı=%{kar_marji:.1f}")
```

### Örnek 19: Kelime Frekans Analizi

```python
# Metin içindeki kelimelerin frekansını bulma
metin = """
Python programlama dili modern yazılım geliştirme için en popüler dillerden biridir.
Python öğrenmek kolaydır ve Python ile web geliştirme veri analizi makine öğrenmesi
gibi birçok alanda çalışabilirsiniz. Python topluluğu çok büyük ve aktiftir.
"""

# Metni kelimelere ayırma ve küçük harfe çevirme
kelimeler = metin.lower().split()

# Kelime frekanslarını sayma
kelime_frekansi = {}
for kelime in kelimeler:
    # Noktalama işaretlerini temizleme
    temiz_kelime = kelime.strip(".,!?;:")
    if temiz_kelime:  # Boş string kontrolü
        kelime_frekansi[temiz_kelime] = kelime_frekansi.get(temiz_kelime, 0) + 1

# Dictionary comprehension ile de yapılabilir
# kelime_frekansi = {kelime: kelimeler.count(kelime) for kelime in set(kelimeler)}

# Frekansa göre sıralama
sirali_kelimeler = sorted(kelime_frekansi.items(), key=lambda x: x[1], reverse=True)

print("KELİME FREKANS ANALİZİ")
print("=" * 40)
print(f"Toplam Kelime: {len(kelimeler)}")
print(f"Benzersiz Kelime: {len(kelime_frekansi)}")
print("\nEn Çok Kullanılan 10 Kelime:")
for i, (kelime, frekans) in enumerate(sirali_kelimeler[:10], 1):
    print(f"{i}. {kelime}: {frekans} kez")
```

### Örnek 20: Gelişmiş Dictionary İşlemleri ve Pratik Uygulamalar

```python
from collections import defaultdict, Counter

# 1. defaultdict - Otomatik varsayılan değer ataması
ogrenci_notlari = defaultdict(list)
ogrenci_notlari["Ahmet"].append(85)
ogrenci_notlari["Ahmet"].append(92)
ogrenci_notlari["Ayşe"].append(78)
ogrenci_notlari["Ayşe"].append(88)
ogrenci_notlari["Ayşe"].append(95)

print("Öğrenci Notları (defaultdict):")
for ogrenci, notlar in ogrenci_notlari.items():
    ortalama = sum(notlar) / len(notlar)
    print(f"{ogrenci}: {notlar} - Ortalama: {ortalama:.2f}")

# 2. Counter - Eleman sayma
metin = "python programlama python django python flask"
kelimeler = metin.split()
kelime_sayaci = Counter(kelimeler)
print(f"\nEn çok geçen 2 kelime: {kelime_sayaci.most_common(2)}")

# 3. Dictionary birleştirme yöntemleri
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 20, "e": 5}

# Python 3.9+ ile | operatörü
birlesik = dict1 | dict2 | dict3
print(f"\nBirleştirilmiş dictionary: {birlesik}")

# 4. Dictionary filtreleme
urunler = {"elma": 5, "armut": 12, "muz": 3, "çilek": 8, "kiraz": 15}
pahali_urunler = {k: v for k, v in urunler.items() if v > 10}
print(f"\n10 TL'den pahalı ürünler: {pahali_urunler}")

# 5. İç içe dictionary güncelleme
from copy import deepcopy

orijinal = {
    "kullanici": {
        "ad": "Ahmet",
        "ayarlar": {"tema": "dark", "dil": "tr"}
    }
}

# Derin kopya (deep copy)
kopya = deepcopy(orijinal)
kopya["kullanici"]["ayarlar"]["tema"] = "light"

print(f"\nOrijinal tema: {orijinal['kullanici']['ayarlar']['tema']}")  # dark
print(f"Kopya tema: {kopya['kullanici']['ayarlar']['tema']}")  # light

# 6. Dictionary'den veri çıkarma ve dönüştürme
kullanicilar = [
    {"id": 1, "ad": "Ahmet", "sehir": "İstanbul"},
    {"id": 2, "ad": "Ayşe", "sehir": "Ankara"},
    {"id": 3, "ad": "Mehmet", "sehir": "İzmir"},
    {"id": 4, "ad": "Zeynep", "sehir": "İstanbul"}
]

# Şehirlere göre gruplama
sehir_gruplari = defaultdict(list)
for kullanici in kullanicilar:
    sehir_gruplari[kullanici["sehir"]].append(kullanici["ad"])

print("\nŞehirlere Göre Kullanıcılar:")
for sehir, isimler in sehir_gruplari.items():
    print(f"{sehir}: {', '.join(isimler)}")
```

---

## Özet

Dictionary'ler Python'da en güçlü ve esnek veri yapılarından biridir. Anahtar-değer çiftleri ile veri saklama, hızlı erişim ve zengin metod desteği sayesinde birçok programlama görevinde kullanılır.

### Temel Noktalar:
- **Oluşturma**: `{}` veya `dict()` ile
- **Erişim**: Köşeli parantez `[]` veya `get()` metodu
- **Değiştirme**: Anahtar ile doğrudan atama
- **Metodlar**: keys(), values(), items(), update(), pop(), clear() vb.
- **Comprehension**: Hızlı ve elegant dictionary oluşturma
- **İç İçe**: Karmaşık veri yapılarını temsil etme

Dictionary'leri etkili kullanmak, Python programlamada veri yönetimi ve manipülasyonu için kritik öneme sahiptir.
