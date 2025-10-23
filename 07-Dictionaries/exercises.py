"""
PYTHON DICTIONARIES - ALIŞTIRMALAR
===================================

Bu dosya, Python Dictionary (Sözlük) konusunu pekiştirmek için
hazırlanmış kapsamlı alıştırmaları içerir.

Zorluk Seviyeleri:
- Kolay (Easy): 1-5
- Orta (Medium): 6-10
- Zor (Challenge): 11-15

Her alıştırma şu yapıya sahiptir:
1. Soru açıklaması
2. TODO bölümü (buraya kod yazın)
3. Detaylı çözüm ve açıklama
"""

print("=" * 70)
print("PYTHON DICTIONARIES - ALIŞTIRMALAR".center(70))
print("=" * 70)

# =============================================================================
# KOLAY SEVİYE ALIŞTIRMALAR (1-5)
# =============================================================================

print("\n" + "=" * 70)
print("KOLAY SEVİYE ALIŞTIRMALAR".center(70))
print("=" * 70)

# -----------------------------------------------------------------------------
# Alıştırma 1: Temel Dictionary Oluşturma ve Erişim
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 1: Temel Dictionary Oluşturma ve Erişim ---")
print("""
Soru: Bir öğrenci bilgilerini içeren dictionary oluşturun ve şu bilgileri ekleyin:
- ad: "Ahmet"
- soyad: "Yılmaz"
- yas: 20
- bolum: "Bilgisayar Mühendisliği"

Ardından tüm bilgileri ekrana yazdırın ve öğrencinin yaşını 21'e güncelleyin.
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 1:")
print("-" * 70)

# Dictionary oluşturma
ogrenci = {
    "ad": "Ahmet",
    "soyad": "Yılmaz",
    "yas": 20,
    "bolum": "Bilgisayar Mühendisliği"
}

# Bilgileri yazdırma
print("Öğrenci Bilgileri:")
for anahtar, deger in ogrenci.items():
    print(f"  {anahtar}: {deger}")

# Yaşı güncelleme
ogrenci["yas"] = 21
print(f"\nGüncellenmiş yaş: {ogrenci['yas']}")

"""
Açıklama:
- Dictionary'ler süslü parantez {} içinde anahtar-değer çiftleri ile oluşturulur
- Her anahtar-değer çifti : ile ayrılır
- items() metodu tüm anahtar-değer çiftlerini tuple olarak döner
- Mevcut bir değeri güncellemek için anahtarı kullanarak doğrudan atama yapılır
"""

# -----------------------------------------------------------------------------
# Alıştırma 2: get() Metodu ve Güvenli Erişim
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 2: get() Metodu ve Güvenli Erişim ---")
print("""
Soru: Bir ürün dictionary'si oluşturun (isim, fiyat, stok bilgileri).
get() metodunu kullanarak hem var olan hem olmayan anahtarlara erişin.
Olmayan anahtarlar için uygun varsayılan değerler belirleyin.
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 2:")
print("-" * 70)

# Ürün dictionary'si
urun = {
    "isim": "Laptop",
    "fiyat": 15000,
    "stok": 50
}

# Var olan anahtara erişim
print(f"Ürün İsmi: {urun.get('isim')}")
print(f"Fiyat: {urun.get('fiyat')} TL")

# Olmayan anahtara erişim - varsayılan değer ile
print(f"Marka: {urun.get('marka', 'Belirtilmemiş')}")
print(f"Garanti: {urun.get('garanti', 'Yok')}")

# in operatörü ile kontrol
if "indirim" in urun:
    print(f"İndirim var: {urun['indirim']}")
else:
    print("İndirim bilgisi yok")

"""
Açıklama:
- get() metodu olmayan anahtarlar için KeyError hatası vermez, None döner
- İkinci parametre ile varsayılan değer belirtebiliriz
- 'in' operatörü ile anahtarın varlığını kontrol edebiliriz
- get() metodu köşeli parantez [] kullanımından daha güvenlidir
"""

# -----------------------------------------------------------------------------
# Alıştırma 3: Dictionary Metodları - keys(), values(), items()
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 3: Dictionary Metodları ---")
print("""
Soru: Bir kitap dictionary'si oluşturun (baslik, yazar, yil, sayfa).
keys(), values() ve items() metodlarını kullanarak:
1. Tüm anahtarları listeleyin
2. Tüm değerleri listeleyin
3. Tüm anahtar-değer çiftlerini döngü ile yazdırın
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 3:")
print("-" * 70)

kitap = {
    "baslik": "Python Programlama",
    "yazar": "Guido van Rossum",
    "yil": 2023,
    "sayfa": 450
}

# 1. Tüm anahtarlar
print("Anahtarlar:")
for anahtar in kitap.keys():
    print(f"  - {anahtar}")

# 2. Tüm değerler
print("\nDeğerler:")
for deger in kitap.values():
    print(f"  - {deger}")

# 3. Anahtar-değer çiftleri
print("\nKitap Bilgileri:")
for anahtar, deger in kitap.items():
    print(f"  {anahtar.capitalize()}: {deger}")

"""
Açıklama:
- keys() metodu sadece anahtarları döner (dict_keys nesnesi)
- values() metodu sadece değerleri döner (dict_values nesnesi)
- items() metodu anahtar-değer çiftlerini tuple olarak döner (dict_items nesnesi)
- Bu metodlar döngü ile kullanılabilir veya list() ile listeye çevrilebilir
- items() metodu for döngüsünde tuple unpacking ile kullanışlıdır
"""

# -----------------------------------------------------------------------------
# Alıştırma 4: Dictionary'ye Eleman Ekleme ve Güncelleme
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 4: Eleman Ekleme ve Güncelleme ---")
print("""
Soru: Boş bir envanter dictionary'si oluşturun. Aşağıdaki ürünleri ekleyin:
- kalem: 100 adet
- defter: 50 adet
- silgi: 75 adet

Sonra kalem sayısını 120'ye güncelleyin ve cetvel ekleyin (30 adet).
Tüm envanteri yazdırın.
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 4:")
print("-" * 70)

# Boş dictionary oluşturma
envanter = {}

# Ürün ekleme
envanter["kalem"] = 100
envanter["defter"] = 50
envanter["silgi"] = 75

print("İlk Envanter:")
for urun, adet in envanter.items():
    print(f"  {urun}: {adet} adet")

# Güncelleme ve yeni ekleme
envanter["kalem"] = 120  # Güncelleme
envanter["cetvel"] = 30  # Yeni ekleme

print("\nGüncellenmiş Envanter:")
for urun, adet in envanter.items():
    print(f"  {urun}: {adet} adet")

# Toplam stok
toplam = sum(envanter.values())
print(f"\nToplam Stok: {toplam} adet")

"""
Açıklama:
- Boş dictionary {} veya dict() ile oluşturulur
- Yeni anahtar-değer çifti eklemek için: sozluk[anahtar] = deger
- Mevcut değeri güncellemek için aynı sözdizimi kullanılır
- Anahtarın var olup olmadığı önemli değildir, yoksa ekler varsa günceller
- values() metodu ile tüm değerlere erişip sum() ile toplayabiliriz
"""

# -----------------------------------------------------------------------------
# Alıştırma 5: update() Metodu ile Birleştirme
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 5: update() Metodu ---")
print("""
Soru: İki ayrı dictionary oluşturun:
1. kullanici: username ve email içeren
2. profil: yas, sehir ve meslek içeren

update() metodunu kullanarak bu iki dictionary'yi birleştirin.
Sonra email'i güncelleyin ve yeni bir "telefon" alanı ekleyin.
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 5:")
print("-" * 70)

# İki ayrı dictionary
kullanici = {
    "username": "ahmet123",
    "email": "ahmet@example.com"
}

profil = {
    "yas": 25,
    "sehir": "İstanbul",
    "meslek": "Yazılımcı"
}

print("Kullanıcı (önce):")
print(kullanici)

print("\nProfil:")
print(profil)

# Dictionary'leri birleştirme
kullanici.update(profil)
print("\nBirleştirilmiş Kullanıcı:")
print(kullanici)

# Güncelleme ve yeni ekleme
kullanici.update({
    "email": "ahmet.yeni@example.com",
    "telefon": "555-1234"
})

print("\nSon Durum:")
for anahtar, deger in kullanici.items():
    print(f"  {anahtar}: {deger}")

"""
Açıklama:
- update() metodu bir dictionary'ye başka bir dictionary'yi ekler
- Aynı anahtarlar varsa değerler güncellenir
- Olmayan anahtarlar yeni olarak eklenir
- update() metodu birden fazla anahtar-değer çiftini tek seferde eklemek için idealdir
- Python 3.9+ için | operatörü ile de birleştirme yapılabilir: dict1 | dict2
"""

# =============================================================================
# ORTA SEVİYE ALIŞTIRMALAR (6-10)
# =============================================================================

print("\n" + "=" * 70)
print("ORTA SEVİYE ALIŞTIRMALAR".center(70))
print("=" * 70)

# -----------------------------------------------------------------------------
# Alıştırma 6: pop() ve popitem() Metodları
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 6: pop() ve popitem() Metodları ---")
print("""
Soru: Bir not defteri dictionary'si oluşturun (en az 5 giriş).
1. pop() ile belirli bir girişi silin ve değerini yazdırın
2. popitem() ile son girişi silin
3. Olmayan bir anahtarı pop() ile silmeye çalışın (varsayılan değer kullanın)
4. Kalan girişleri listeleyin
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 6:")
print("-" * 70)

notlar = {
    "gorev1": "Rapor hazırla",
    "gorev2": "Email gönder",
    "gorev3": "Toplantıya katıl",
    "gorev4": "Kod incele",
    "gorev5": "Dokümantasyon yaz"
}

print("Başlangıç Notları:")
print(notlar)

# pop() ile belirli bir girişi silme
silinen = notlar.pop("gorev2")
print(f"\nSilinen görev: {silinen}")

# popitem() ile son girişi silme
son_giris = notlar.popitem()
print(f"Son silinen görev: {son_giris}")

# Olmayan anahtar için pop() - varsayılan değer
yok = notlar.pop("gorev10", "Böyle bir görev yok")
print(f"Olmayan görev: {yok}")

# Kalan girişler
print("\nKalan Görevler:")
for anahtar, deger in notlar.items():
    print(f"  {anahtar}: {deger}")

"""
Açıklama:
- pop(anahtar) belirtilen anahtarı siler ve değerini döner
- pop(anahtar, varsayılan) anahtar yoksa KeyError vermez, varsayılan değeri döner
- popitem() son eklenen (Python 3.7+) elemanı siler ve (anahtar, değer) tuple'ı döner
- popitem() boş dictionary'de KeyError verir
- Her iki metod da dictionary'yi değiştirir (mutable)
"""

# -----------------------------------------------------------------------------
# Alıştırma 7: Dictionary Comprehension
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 7: Dictionary Comprehension ---")
print("""
Soru: Aşağıdaki görevleri dictionary comprehension kullanarak yapın:
1. 1'den 10'a kadar sayıların karelerini içeren dictionary
2. Bir kelime listesinden kelimelerin uzunluklarını içeren dictionary
3. Bir sayı listesinden sadece çift sayıların küplerini içeren dictionary
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 7:")
print("-" * 70)

# 1. Sayıların kareleri
kareler = {sayi: sayi**2 for sayi in range(1, 11)}
print("Kareler:")
print(kareler)

# 2. Kelimelerin uzunlukları
kelimeler = ["python", "javascript", "java", "c++", "ruby", "go"]
uzunluklar = {kelime: len(kelime) for kelime in kelimeler}
print("\nKelime Uzunlukları:")
print(uzunluklar)

# 3. Çift sayıların küpleri
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_kupler = {sayi: sayi**3 for sayi in sayilar if sayi % 2 == 0}
print("\nÇift Sayıların Küpleri:")
print(cift_kupler)

# Bonus: Sıcaklık dönüşümü (Celsius -> Fahrenheit)
celsius = [0, 10, 20, 30, 40]
fahrenheit = {c: (c * 9/5) + 32 for c in celsius}
print("\nCelsius -> Fahrenheit:")
for c, f in fahrenheit.items():
    print(f"  {c}°C = {f}°F")

"""
Açıklama:
- Dictionary comprehension: {anahtar: değer for item in iterable}
- Koşullu comprehension: {... for item in iterable if koşul}
- List comprehension'a benzer ama süslü parantez {} kullanır
- Kısa ve okunabilir kod yazmanın elegant bir yolu
- Her döngü iterasyonunda bir anahtar-değer çifti oluşturulur
"""

# -----------------------------------------------------------------------------
# Alıştırma 8: İç İçe Dictionary'ler
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 8: İç İçe Dictionary'ler ---")
print("""
Soru: Bir sınıftaki 3 öğrencinin bilgilerini içeren iç içe dictionary oluşturun.
Her öğrenci için: ad, soyad ve 3 ders notu
Tüm öğrencilerin:
1. Bilgilerini yazdırın
2. Not ortalamalarını hesaplayın
3. En yüksek ortalamaya sahip öğrenciyi bulun
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 8:")
print("-" * 70)

ogrenciler = {
    "001": {
        "ad": "Ahmet",
        "soyad": "Yılmaz",
        "notlar": [85, 78, 92]
    },
    "002": {
        "ad": "Ayşe",
        "soyad": "Demir",
        "notlar": [95, 88, 90]
    },
    "003": {
        "ad": "Mehmet",
        "soyad": "Kaya",
        "notlar": [72, 85, 79]
    }
}

# 1. Bilgileri yazdırma ve 2. Ortalama hesaplama
ortalamar = {}

print("ÖĞRENCİ BİLGİLERİ VE ORTALAMALAR:")
print("-" * 70)

for ogrenci_no, bilgiler in ogrenciler.items():
    ad_soyad = f"{bilgiler['ad']} {bilgiler['soyad']}"
    notlar = bilgiler['notlar']
    ortalama = sum(notlar) / len(notlar)
    ortalamar[ogrenci_no] = ortalama

    print(f"\nÖğrenci No: {ogrenci_no}")
    print(f"Ad Soyad: {ad_soyad}")
    print(f"Notlar: {notlar}")
    print(f"Ortalama: {ortalama:.2f}")

# 3. En yüksek ortalamaya sahip öğrenci
en_basarili_no = max(ortalamar, key=ortalamar.get)
en_basarili = ogrenciler[en_basarili_no]

print("\n" + "=" * 70)
print("EN BAŞARILI ÖĞRENCİ:")
print(f"{en_basarili['ad']} {en_basarili['soyad']} - Ortalama: {ortalamar[en_basarili_no]:.2f}")

"""
Açıklama:
- İç içe dictionary'lerde her değer başka bir dictionary olabilir
- Erişim: sozluk[anahtar1][anahtar2][anahtar3]...
- İç içe döngülerle tüm verilere erişilebilir
- max() fonksiyonu key parametresi ile dictionary'den maksimum değer bulur
- İç içe yapılar karmaşık veri modellerini temsil etmek için idealdir
"""

# -----------------------------------------------------------------------------
# Alıştırma 9: Frekans Sayma ve Analiz
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 9: Frekans Sayma ---")
print("""
Soru: Bir metin içindeki her karakterin kaç kez geçtiğini sayan bir program yazın.
- Boşlukları sayma
- Büyük/küçük harf duyarlı olmasın
- Sonuçları frekansa göre sıralayarak yazdırın
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 9:")
print("-" * 70)

metin = "Python programlama dili çok güçlü ve esnek bir dildir"

# Karakterleri sayma
karakter_frekansi = {}

for karakter in metin.lower():
    if karakter != ' ':  # Boşlukları sayma
        karakter_frekansi[karakter] = karakter_frekansi.get(karakter, 0) + 1

# Alternative: Dictionary comprehension ile
# from collections import Counter
# karakter_frekansi = Counter(metin.lower().replace(' ', ''))

# Frekansa göre sıralama (yüksekten düşüğe)
sirali = sorted(karakter_frekansi.items(), key=lambda x: x[1], reverse=True)

print(f"Metin: {metin}")
print(f"Toplam karakter (boşluksuz): {sum(karakter_frekansi.values())}")
print(f"Benzersiz karakter sayısı: {len(karakter_frekansi)}")

print("\nKARAKTER FREKANS ANALİZİ:")
print("-" * 40)
for karakter, frekans in sirali:
    bar = "█" * frekans
    print(f"'{karakter}': {frekans:2d} {bar}")

# En çok geçen 5 karakter
print("\nEn Çok Geçen 5 Karakter:")
for i, (karakter, frekans) in enumerate(sirali[:5], 1):
    print(f"{i}. '{karakter}': {frekans} kez")

"""
Açıklama:
- get(anahtar, 0) ile başlangıç değeri 0 olarak ayarlanır
- Her geçişte mevcut değer 1 artırılır
- sorted() ile sıralama yapılır, key=lambda x: x[1] değere göre sıralar
- reverse=True ile büyükten küçüğe sıralama
- Bu teknik kelime sayma, veri analizi gibi birçok alanda kullanılır
"""

# -----------------------------------------------------------------------------
# Alıştırma 10: Dictionary ile Veri Dönüşümü
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 10: Veri Dönüşümü ---")
print("""
Soru: Ürün fiyatlarını içeren bir dictionary'niz var (TL cinsinden).
1. %18 KDV ekleyerek yeni fiyatları hesaplayın
2. Fiyatları USD'ye çevirin (kur: 30.5)
3. 1000 TL üzeri ürünleri filtreleyin
4. Sonuçları formatlı olarak yazdırın
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 10:")
print("-" * 70)

urunler_tl = {
    "Laptop": 25000,
    "Telefon": 15000,
    "Tablet": 8000,
    "Kulaklık": 500,
    "Mouse": 300,
    "Klavye": 1200
}

KDV_ORANI = 0.18
USD_KUR = 30.5

# 1. KDV eklenmiş fiyatlar
kdv_ekli = {urun: fiyat * (1 + KDV_ORANI) for urun, fiyat in urunler_tl.items()}

# 2. USD'ye çevirme
urunler_usd = {urun: round(fiyat / USD_KUR, 2) for urun, fiyat in kdv_ekli.items()}

# 3. 1000 TL üzeri ürünler (KDV dahil)
pahali_urunler = {urun: fiyat for urun, fiyat in kdv_ekli.items() if fiyat > 1000}

# Sonuçları yazdırma
print("ÜRÜN FİYAT ANALİZİ")
print("=" * 70)
print(f"{'Ürün':<15} {'Fiyat (TL)':>12} {'KDV Dahil':>12} {'USD':>10}")
print("-" * 70)

for urun in urunler_tl:
    fiyat_tl = urunler_tl[urun]
    fiyat_kdv = kdv_ekli[urun]
    fiyat_usd = urunler_usd[urun]
    print(f"{urun:<15} {fiyat_tl:>12,.2f} {fiyat_kdv:>12,.2f} {fiyat_usd:>10.2f}")

print("\n1000 TL Üzeri Ürünler (KDV Dahil):")
for urun, fiyat in pahali_urunler.items():
    print(f"  {urun}: {fiyat:,.2f} TL")

print(f"\nToplam Ürün Değeri: {sum(kdv_ekli.values()):,.2f} TL")
print(f"Ortalama Fiyat: {sum(kdv_ekli.values())/len(kdv_ekli):,.2f} TL")

"""
Açıklama:
- Dictionary comprehension ile matematiksel işlemler yapılabilir
- round() ile ondalık basamak sayısı ayarlanır
- Koşullu comprehension ile filtreleme yapılır
- Format string (f-string) ile hizalama ve sayı formatlama: {deger:>12,.2f}
  - :>12 = sağa yasla, 12 karakter genişlik
  - , = binlik ayracı
  - .2f = 2 ondalık basamak
"""

# =============================================================================
# ZOR SEVİYE ALIŞTIRMALAR (11-15)
# =============================================================================

print("\n" + "=" * 70)
print("ZOR SEVİYE ALIŞTIRMALAR".center(70))
print("=" * 70)

# -----------------------------------------------------------------------------
# Alıştırma 11: Karmaşık İç İçe Yapı - Şirket Organizasyonu
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 11: Karmaşık İç İçe Yapı ---")
print("""
Soru: Bir şirketin departman yapısını modelleyin:
- 3 departman (Yazılım, Pazarlama, Muhasebe)
- Her departmanda: müdür, çalışanlar listesi, bütçe
- Yazılım departmanında ayrıca projeler listesi (proje adı ve durum)

Şunları yapın:
1. Tüm yapıyı oluşturun
2. Toplam çalışan sayısını bulun
3. Toplam bütçeyi hesaplayın
4. Yazılım departmanındaki aktif projeleri listeleyin
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 11:")
print("-" * 70)

sirket = {
    "departmanlar": {
        "yazilim": {
            "mudur": "Ahmet Yılmaz",
            "calisanlar": ["Mehmet", "Ayşe", "Zeynep", "Can", "Elif"],
            "butce": 500000,
            "projeler": {
                "proje1": {"ad": "E-Ticaret Sitesi", "durum": "aktif"},
                "proje2": {"ad": "Mobil Uygulama", "durum": "aktif"},
                "proje3": {"ad": "CRM Sistemi", "durum": "tamamlandi"}
            }
        },
        "pazarlama": {
            "mudur": "Fatma Demir",
            "calisanlar": ["Ali", "Deniz", "Burak"],
            "butce": 300000
        },
        "muhasebe": {
            "mudur": "Kemal Öz",
            "calisanlar": ["Selin", "Hasan"],
            "butce": 200000
        }
    }
}

# 1. Tüm yapıyı gösterme
print("ŞİRKET DEPARTMAN YAPISI")
print("=" * 70)

for dept_ad, dept_bilgi in sirket["departmanlar"].items():
    print(f"\n{dept_ad.upper()} Departmanı:")
    print(f"  Müdür: {dept_bilgi['mudur']}")
    print(f"  Çalışan Sayısı: {len(dept_bilgi['calisanlar'])}")
    print(f"  Bütçe: {dept_bilgi['butce']:,} TL")

    if "projeler" in dept_bilgi:
        print(f"  Proje Sayısı: {len(dept_bilgi['projeler'])}")

# 2. Toplam çalışan sayısı
toplam_calisan = sum(len(dept['calisanlar']) for dept in sirket["departmanlar"].values())
toplam_mudur = len(sirket["departmanlar"])

print("\n" + "=" * 70)
print("GENEL İSTATİSTİKLER")
print("-" * 70)
print(f"Toplam Departman: {toplam_mudur}")
print(f"Toplam Çalışan: {toplam_calisan}")
print(f"Toplam Personel (Müdür + Çalışan): {toplam_mudur + toplam_calisan}")

# 3. Toplam bütçe
toplam_butce = sum(dept['butce'] for dept in sirket["departmanlar"].values())
print(f"Toplam Bütçe: {toplam_butce:,} TL")

# 4. Yazılım departmanı aktif projeleri
print("\n" + "=" * 70)
print("YAZILIM DEPARTMANI AKTİF PROJELERİ")
print("-" * 70)

yazilim_projeleri = sirket["departmanlar"]["yazilim"]["projeler"]
aktif_projeler = {
    proje_id: proje_bilgi
    for proje_id, proje_bilgi in yazilim_projeleri.items()
    if proje_bilgi["durum"] == "aktif"
}

for proje_id, proje_bilgi in aktif_projeler.items():
    print(f"  - {proje_bilgi['ad']} ({proje_id})")

print(f"\nAktif Proje Sayısı: {len(aktif_projeler)}/{len(yazilim_projeleri)}")

"""
Açıklama:
- İç içe dictionary'ler gerçek dünya veri modellerini temsil eder
- Generator expression ile toplam hesaplama: sum(... for item in iterable)
- İç içe comprehension ile filtreleme yapılabilir
- "in" operatörü ile opsiyonel alanlar kontrol edilir
- Derin erişim: sozluk[anahtar1][anahtar2][anahtar3]...
- Bu yapı JSON verilere benzer ve API'larla çalışmaya hazırlar
"""

# -----------------------------------------------------------------------------
# Alıştırma 12: Gelişmiş Dictionary İşlemleri
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 12: Gelişmiş Dictionary İşlemleri ---")
print("""
Soru: İki ayrı dictionary'niz var:
- stok: ürün adı ve stok miktarı
- fiyat: ürün adı ve fiyat

Şunları yapın:
1. Her iki dictionary'de de olan ürünleri bulun (kesişim)
2. Her iki dictionary'yi birleştirerek yeni bir yapı oluşturun
3. Toplam envanter değerini hesaplayın (stok * fiyat)
4. Stokta olup fiyatı olmayan veya tam tersi ürünleri listeleyin
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 12:")
print("-" * 70)

stok = {
    "laptop": 15,
    "telefon": 30,
    "tablet": 20,
    "kulaklik": 50,
    "monitor": 10
}

fiyat = {
    "laptop": 25000,
    "telefon": 15000,
    "tablet": 8000,
    "mouse": 300,
    "klavye": 1200
}

# 1. Ortak ürünler (kesişim)
ortak_urunler = set(stok.keys()) & set(fiyat.keys())
print("Ortak Ürünler:")
print(f"  {ortak_urunler}")

# 2. Birleştirilmiş yapı
envanter = {}
tum_urunler = set(stok.keys()) | set(fiyat.keys())  # Birleşim

for urun in tum_urunler:
    envanter[urun] = {
        "stok": stok.get(urun, 0),
        "fiyat": fiyat.get(urun, 0),
        "deger": stok.get(urun, 0) * fiyat.get(urun, 0)
    }

print("\nBirleştirilmiş Envanter:")
print(f"{'Ürün':<12} {'Stok':>8} {'Fiyat':>12} {'Değer':>15}")
print("-" * 50)
for urun, bilgi in sorted(envanter.items()):
    print(f"{urun:<12} {bilgi['stok']:>8} {bilgi['fiyat']:>12,} {bilgi['deger']:>15,}")

# 3. Toplam envanter değeri
toplam_deger = sum(bilgi['deger'] for bilgi in envanter.values())
print(f"\nToplam Envanter Değeri: {toplam_deger:,} TL")

# 4. Eksik bilgiler
sadece_stokta = set(stok.keys()) - set(fiyat.keys())
sadece_fiyatta = set(fiyat.keys()) - set(stok.keys())

print("\nUYARILAR:")
if sadece_stokta:
    print(f"  Stokta var ama fiyatı yok: {sadece_stokta}")
if sadece_fiyatta:
    print(f"  Fiyatı var ama stokta yok: {sadece_fiyatta}")

# Detaylı analiz
print("\nDETAYLI ANALİZ:")
tam_urunler = [urun for urun in envanter if envanter[urun]['stok'] > 0 and envanter[urun]['fiyat'] > 0]
eksik_urunler = [urun for urun in envanter if envanter[urun]['stok'] == 0 or envanter[urun]['fiyat'] == 0]

print(f"  Tam bilgili ürün sayısı: {len(tam_urunler)}")
print(f"  Eksik bilgili ürün sayısı: {len(eksik_urunler)}")

"""
Açıklama:
- set() operasyonları ile kesişim (&), birleşim (|), fark (-) bulunur
- get(anahtar, varsayılan) ile eksik anahtarlar için varsayılan değer kullanılır
- İç içe dictionary ile karmaşık veri yapısı oluşturulur
- Generator expression ile verimli toplama yapılır
- List comprehension ile filtreleme yapılır
- sorted() ile dictionary alfabetik sıralanabilir
"""

# -----------------------------------------------------------------------------
# Alıştırma 13: Kelime Frekans Analizi ve İstatistik
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 13: Kelime Frekans Analizi ---")
print("""
Soru: Bir metin üzerinde gelişmiş kelime analizi yapın:
1. Her kelimenin geçme sıklığını bulun
2. En çok ve en az geçen kelimeleri bulun
3. Ortalama kelime uzunluğunu hesaplayın
4. Belirli uzunluktaki kelimeleri filtreleyin
5. Sonuçları görselleştirin (basit bar chart)
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 13:")
print("-" * 70)

metin = """
Python programlama dili modern yazılım geliştirme için en popüler dillerden biridir.
Python öğrenmek kolaydır ve Python ile web geliştirme veri analizi makine öğrenmesi
yapay zeka gibi birçok alanda çalışabilirsiniz. Python topluluğu çok büyüktür ve
Python dokümantasyonu oldukça kapsamlıdır. Python ile projeler geliştirmek eğlencelidir.
"""

# Metni temizleme ve kelimelere ayırma
import string

kelimeler = metin.lower().translate(str.maketrans('', '', string.punctuation)).split()

# 1. Kelime frekansları
kelime_frekansi = {}
for kelime in kelimeler:
    kelime_frekansi[kelime] = kelime_frekansi.get(kelime, 0) + 1

# 2. En çok ve en az geçen kelimeler
en_cok = max(kelime_frekansi.items(), key=lambda x: x[1])
en_az = min(kelime_frekansi.items(), key=lambda x: x[1])

print("KELİME FREKANS ANALİZİ")
print("=" * 70)
print(f"Toplam kelime: {len(kelimeler)}")
print(f"Benzersiz kelime: {len(kelime_frekansi)}")
print(f"En çok geçen: '{en_cok[0]}' ({en_cok[1]} kez)")
print(f"En az geçen: '{en_az[0]}' ({en_az[1]} kez)")

# 3. Ortalama kelime uzunluğu
toplam_uzunluk = sum(len(kelime) for kelime in kelimeler)
ortalama_uzunluk = toplam_uzunluk / len(kelimeler)
print(f"Ortalama kelime uzunluğu: {ortalama_uzunluk:.2f} karakter")

# 4. Uzunluğa göre filtreleme (5+ karakter)
uzun_kelimeler = {k: v for k, v in kelime_frekansi.items() if len(k) >= 5}
print(f"5+ karakter kelime sayısı: {len(uzun_kelimeler)}")

# 5. En çok geçen 10 kelime ve görselleştirme
print("\nEN ÇOK GEÇEN 10 KELİME:")
print("-" * 70)

sirali = sorted(kelime_frekansi.items(), key=lambda x: x[1], reverse=True)
max_frekans = sirali[0][1]

for i, (kelime, frekans) in enumerate(sirali[:10], 1):
    # Basit bar chart
    bar_uzunluk = int((frekans / max_frekans) * 40)
    bar = "█" * bar_uzunluk
    print(f"{i:2d}. {kelime:<15} {frekans:2d} {bar}")

# Uzunluk bazlı analiz
print("\nKELİME UZUNLUĞUNA GÖRE DAĞILIM:")
print("-" * 70)

uzunluk_dagilimi = {}
for kelime in kelime_frekansi.keys():
    uzunluk = len(kelime)
    uzunluk_dagilimi[uzunluk] = uzunluk_dagilimi.get(uzunluk, 0) + 1

for uzunluk in sorted(uzunluk_dagilimi.keys()):
    adet = uzunluk_dagilimi[uzunluk]
    bar = "▪" * adet
    print(f"{uzunluk:2d} karakter: {adet:2d} kelime {bar}")

"""
Açıklama:
- string.punctuation ile noktalama işaretleri temizlenir
- translate() ve str.maketrans() ile karakter dönüşümü yapılır
- max() ve min() fonksiyonları key parametresi ile dictionary'den değer bulur
- lambda fonksiyonları kısa, anonim fonksiyonlar oluşturur
- Veri görselleştirme için basit ASCII bar chart kullanılır
- Bu teknik metin madenciliği ve doğal dil işleme için temeldir
"""

# -----------------------------------------------------------------------------
# Alıştırma 14: E-Ticaret Sepet Sistemi
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 14: E-Ticaret Sepet Sistemi ---")
print("""
Soru: Kapsamlı bir alışveriş sepeti sistemi oluşturun:
1. Ürün kataloğu (id, isim, fiyat, kategori, stok)
2. Sepet işlemleri (ekleme, çıkarma, güncelleme)
3. İndirim kuponları (%10, %15, %20)
4. Kargo hesaplama (100 TL altı 30 TL, üstü ücretsiz)
5. Detaylı fatura çıktısı
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 14:")
print("-" * 70)

# Ürün kataloğu
katalog = {
    "101": {"isim": "Laptop", "fiyat": 25000, "kategori": "Elektronik", "stok": 15},
    "102": {"isim": "Telefon", "fiyat": 15000, "kategori": "Elektronik", "stok": 30},
    "103": {"isim": "Kulaklık", "fiyat": 500, "kategori": "Aksesuar", "stok": 50},
    "104": {"isim": "Klavye", "fiyat": 1200, "kategori": "Aksesuar", "stok": 25},
    "105": {"isim": "Mouse", "fiyat": 300, "kategori": "Aksesuar", "stok": 40}
}

# Alışveriş sepeti
sepet = {}

# İndirim kuponları
kuponlar = {
    "INDIRIM10": 0.10,
    "INDIRIM15": 0.15,
    "INDIRIM20": 0.20
}

# Sepete ürün ekleme fonksiyonu
def sepete_ekle(urun_id, adet=1):
    """Sepete ürün ekler"""
    if urun_id in katalog:
        if katalog[urun_id]["stok"] >= adet:
            if urun_id in sepet:
                sepet[urun_id]["adet"] += adet
            else:
                sepet[urun_id] = {
                    "isim": katalog[urun_id]["isim"],
                    "fiyat": katalog[urun_id]["fiyat"],
                    "adet": adet
                }
            return True
        else:
            print(f"  HATA: Yeterli stok yok! (Mevcut: {katalog[urun_id]['stok']})")
            return False
    else:
        print(f"  HATA: Ürün bulunamadı!")
        return False

# Sepetten ürün çıkarma
def sepetten_cikar(urun_id):
    """Sepetten ürün çıkarır"""
    if urun_id in sepet:
        del sepet[urun_id]
        return True
    return False

# Sepeti hesaplama
def sepet_hesapla(kupon_kodu=None):
    """Sepet toplamını hesaplar"""
    ara_toplam = sum(urun["fiyat"] * urun["adet"] for urun in sepet.values())

    # İndirim hesaplama
    indirim_miktari = 0
    if kupon_kodu and kupon_kodu in kuponlar:
        indirim_orani = kuponlar[kupon_kodu]
        indirim_miktari = ara_toplam * indirim_orani

    toplam = ara_toplam - indirim_miktari

    # Kargo hesaplama
    kargo = 0 if toplam >= 100 else 30

    return {
        "ara_toplam": ara_toplam,
        "indirim": indirim_miktari,
        "kargo": kargo,
        "genel_toplam": toplam + kargo
    }

# Fatura yazdırma
def fatura_yazdir(kupon_kodu=None):
    """Detaylı fatura çıktısı"""
    print("\n" + "=" * 70)
    print("ALIŞ VERİŞ FATURASI".center(70))
    print("=" * 70)

    if not sepet:
        print("Sepetiniz boş!")
        return

    print(f"{'Ürün':<20} {'Fiyat':>12} {'Adet':>8} {'Toplam':>15}")
    print("-" * 70)

    for urun_id, urun in sepet.items():
        tutar = urun["fiyat"] * urun["adet"]
        print(f"{urun['isim']:<20} {urun['fiyat']:>12,} TL {urun['adet']:>6} {tutar:>15,} TL")

    hesap = sepet_hesapla(kupon_kodu)

    print("-" * 70)
    print(f"{'Ara Toplam:':<48} {hesap['ara_toplam']:>18,} TL")

    if hesap['indirim'] > 0:
        print(f"{'İndirim (' + kupon_kodu + '):':<48} {-hesap['indirim']:>18,.2f} TL")

    print(f"{'Kargo:':<48} {hesap['kargo']:>18,} TL")

    if hesap['ara_toplam'] >= 100:
        print(f"{'(100 TL üzeri ücretsiz kargo!)':<48}")

    print("=" * 70)
    print(f"{'GENEL TOPLAM:':<48} {hesap['genel_toplam']:>18,.2f} TL")
    print("=" * 70)

# Simülasyon
print("E-TİCARET SEPET SİSTEMİ SİMÜLASYONU")
print("=" * 70)

print("\n1. Sepete ürün ekleme:")
sepete_ekle("101", 1)  # Laptop
print("  ✓ Laptop eklendi")
sepete_ekle("103", 2)  # Kulaklık
print("  ✓ 2 adet Kulaklık eklendi")
sepete_ekle("104", 1)  # Klavye
print("  ✓ Klavye eklendi")

print("\n2. Stok kontrolü:")
sepete_ekle("101", 20)  # Stok yetersiz

print("\n3. Fatura (kupon yok):")
fatura_yazdir()

print("\n4. İndirim kuponu ile fatura:")
fatura_yazdir("INDIRIM15")

print("\n5. Sepetten ürün çıkarma:")
sepetten_cikar("101")
print("  ✓ Laptop sepetten çıkarıldı")
fatura_yazdir("INDIRIM10")

"""
Açıklama:
- Fonksiyonlar ile kod modüler ve yeniden kullanılabilir hale gelir
- İç içe dictionary'ler karmaşık veri modellerini temsil eder
- Koşullu mantık (if-else) ile iş kuralları uygulanır
- Dictionary'ler parametre ve dönüş değeri olarak kullanılır
- Format string ile profesyonel çıktılar oluşturulur
- Bu yapı gerçek e-ticaret uygulamalarının temelini oluşturur
"""

# -----------------------------------------------------------------------------
# Alıştırma 15: Öğrenci Yönetim Sistemi (Final Challenge)
# -----------------------------------------------------------------------------
print("\n--- Alıştırma 15: Öğrenci Yönetim Sistemi ---")
print("""
Soru: Kapsamlı bir öğrenci yönetim sistemi oluşturun:
1. Öğrenci kayıt sistemi (ad, soyad, numara, bölüm)
2. Not girişi (3 vize, 1 final)
3. Ortalama hesaplama (Vize %30, Final %70)
4. Harf notu hesaplama (AA, BA, BB, CB, CC, DC, DD, FF)
5. Sınıf istatistikleri (ortalama, en yüksek/düşük, geçme oranı)
6. Öğrenci raporu oluşturma
""")

# TODO: Buraya kodunuzu yazın




# ÇÖZÜM:
print("Çözüm 15:")
print("-" * 70)

# Öğrenci veritabanı
ogrenciler = {}

# Harf notu skalası
def harf_notu_hesapla(ortalama):
    """Sayısal notu harf notuna çevirir"""
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 65:
        return "DC"
    elif ortalama >= 60:
        return "DD"
    else:
        return "FF"

# Öğrenci ekleme
def ogrenci_ekle(numara, ad, soyad, bolum):
    """Yeni öğrenci kaydı oluşturur"""
    ogrenciler[numara] = {
        "ad": ad,
        "soyad": soyad,
        "bolum": bolum,
        "notlar": {
            "vize1": None,
            "vize2": None,
            "vize3": None,
            "final": None
        }
    }

# Not girişi
def not_gir(numara, vize1=None, vize2=None, vize3=None, final=None):
    """Öğrenci notlarını girer"""
    if numara in ogrenciler:
        if vize1 is not None:
            ogrenciler[numara]["notlar"]["vize1"] = vize1
        if vize2 is not None:
            ogrenciler[numara]["notlar"]["vize2"] = vize2
        if vize3 is not None:
            ogrenciler[numara]["notlar"]["vize3"] = vize3
        if final is not None:
            ogrenciler[numara]["notlar"]["final"] = final

# Ortalama hesaplama
def ortalama_hesapla(numara):
    """Öğrenci ortalamasını hesaplar (Vize %30, Final %70)"""
    if numara in ogrenciler:
        notlar = ogrenciler[numara]["notlar"]

        # Tüm notlar girilmiş mi kontrol et
        if all(notlar.values()):
            vize_ort = (notlar["vize1"] + notlar["vize2"] + notlar["vize3"]) / 3
            ortalama = (vize_ort * 0.3) + (notlar["final"] * 0.7)
            return round(ortalama, 2)
    return None

# Öğrenci raporu
def ogrenci_raporu(numara):
    """Tek öğrenci için detaylı rapor"""
    if numara not in ogrenciler:
        print("Öğrenci bulunamadı!")
        return

    ogr = ogrenciler[numara]
    notlar = ogr["notlar"]
    ortalama = ortalama_hesapla(numara)

    print("\n" + "=" * 70)
    print("ÖĞRENCİ RAPORU".center(70))
    print("=" * 70)
    print(f"Öğrenci No: {numara}")
    print(f"Ad Soyad: {ogr['ad']} {ogr['soyad']}")
    print(f"Bölüm: {ogr['bolum']}")
    print("-" * 70)
    print("NOTLAR:")
    print(f"  Vize 1: {notlar['vize1']}")
    print(f"  Vize 2: {notlar['vize2']}")
    print(f"  Vize 3: {notlar['vize3']}")
    print(f"  Final:  {notlar['final']}")

    if ortalama:
        harf = harf_notu_hesapla(ortalama)
        durum = "GEÇTİ" if ortalama >= 60 else "KALDI"
        print("-" * 70)
        print(f"Ortalama: {ortalama}")
        print(f"Harf Notu: {harf}")
        print(f"Durum: {durum}")
    else:
        print("\n(Not girişi tamamlanmamış)")

    print("=" * 70)

# Sınıf istatistikleri
def sinif_istatistikleri():
    """Tüm sınıf için istatistikler"""
    print("\n" + "=" * 70)
    print("SINIF İSTATİSTİKLERİ".center(70))
    print("=" * 70)

    if not ogrenciler:
        print("Kayıtlı öğrenci yok!")
        return

    # Ortalama hesaplanan öğrenciler
    ortalamalar = {}
    for numara in ogrenciler:
        ort = ortalama_hesapla(numara)
        if ort:
            ortalamalar[numara] = ort

    if not ortalamalar:
        print("Henüz not girişi yapılmamış!")
        return

    # İstatistikler
    sinif_ortalamasi = sum(ortalamalar.values()) / len(ortalamalar)
    en_yuksek = max(ortalamalar.values())
    en_dusuk = min(ortalamalar.values())
    gecenler = sum(1 for ort in ortalamalar.values() if ort >= 60)
    gecme_orani = (gecenler / len(ortalamalar)) * 100

    print(f"Toplam Öğrenci: {len(ogrenciler)}")
    print(f"Not Girişi Tamamlanan: {len(ortalamalar)}")
    print(f"Sınıf Ortalaması: {sinif_ortalamasi:.2f}")
    print(f"En Yüksek Not: {en_yuksek:.2f}")
    print(f"En Düşük Not: {en_dusuk:.2f}")
    print(f"Geçen Öğrenci: {gecenler}/{len(ortalamalar)}")
    print(f"Geçme Oranı: %{gecme_orani:.1f}")

    # Harf notu dağılımı
    print("\nHARF NOTU DAĞILIMI:")
    harf_dagilimi = {}
    for ort in ortalamalar.values():
        harf = harf_notu_hesapla(ort)
        harf_dagilimi[harf] = harf_dagilimi.get(harf, 0) + 1

    for harf in ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF"]:
        adet = harf_dagilimi.get(harf, 0)
        if adet > 0:
            bar = "█" * adet
            print(f"  {harf}: {adet:2d} öğrenci {bar}")

    # En başarılı öğrenci
    en_basarili_no = max(ortalamalar, key=ortalamalar.get)
    en_basarili = ogrenciler[en_basarili_no]
    print(f"\nEn Başarılı Öğrenci:")
    print(f"  {en_basarili['ad']} {en_basarili['soyad']} ({en_basarili_no})")
    print(f"  Ortalama: {ortalamalar[en_basarili_no]:.2f}")
    print("=" * 70)

# Tüm öğrencileri listeleme
def ogrenci_listesi():
    """Tüm öğrencileri listeler"""
    print("\n" + "=" * 70)
    print("ÖĞRENCİ LİSTESİ".center(70))
    print("=" * 70)
    print(f"{'No':<10} {'Ad Soyad':<25} {'Bölüm':<20} {'Ortalama':>10}")
    print("-" * 70)

    for numara, ogr in sorted(ogrenciler.items()):
        ad_soyad = f"{ogr['ad']} {ogr['soyad']}"
        ortalama = ortalama_hesapla(numara)
        ort_str = f"{ortalama:.2f}" if ortalama else "---"
        print(f"{numara:<10} {ad_soyad:<25} {ogr['bolum']:<20} {ort_str:>10}")

    print("=" * 70)

# SİMÜLASYON
print("ÖĞRENCİ YÖNETİM SİSTEMİ SİMÜLASYONU")
print("=" * 70)

# Öğrenci kayıtları
print("\n1. Öğrenci kayıtları yapılıyor...")
ogrenci_ekle("2023001", "Ahmet", "Yılmaz", "Bilgisayar Mühendisliği")
ogrenci_ekle("2023002", "Ayşe", "Demir", "Bilgisayar Mühendisliği")
ogrenci_ekle("2023003", "Mehmet", "Kaya", "Bilgisayar Mühendisliği")
ogrenci_ekle("2023004", "Zeynep", "Öz", "Bilgisayar Mühendisliği")
ogrenci_ekle("2023005", "Can", "Şahin", "Bilgisayar Mühendisliği")
print("  ✓ 5 öğrenci kaydedildi")

# Not girişleri
print("\n2. Notlar giriliyor...")
not_gir("2023001", vize1=85, vize2=78, vize3=92, final=88)
not_gir("2023002", vize1=95, vize2=88, vize3=90, final=92)
not_gir("2023003", vize1=65, vize2=72, vize3=68, final=70)
not_gir("2023004", vize1=45, vize2=52, vize3=48, final=55)
not_gir("2023005", vize1=88, vize2=85, vize3=90, final=87)
print("  ✓ Notlar girildi")

# Öğrenci listesi
ogrenci_listesi()

# Bireysel rapor
print("\n3. Örnek öğrenci raporu:")
ogrenci_raporu("2023002")

# Sınıf istatistikleri
print("\n4. Sınıf istatistikleri:")
sinif_istatistikleri()

"""
Açıklama:
- Kapsamlı bir uygulama örneği
- Fonksiyonlar ile modüler kod yapısı
- İç içe dictionary'ler ile karmaşık veri modeli
- Matematiksel hesaplamalar ve iş mantığı
- Koşullu ifadeler ve veri validasyonu
- Veri analizi ve istatistik hesaplamaları
- Formatlı çıktılar ve raporlama
- Gerçek dünya uygulamalarına hazırlık

Bu alıştırma, dictionary'lerin tüm özelliklerini kullanarak
gerçekçi bir yönetim sistemi oluşturmayı gösterir. Bu tür
projeler, öğrendiklerinizi pratiğe dökmenin en iyi yoludur.
"""

# =============================================================================
# SONUÇ
# =============================================================================

print("\n" + "=" * 70)
print("ALIŞTIRMALAR TAMAMLANDI!".center(70))
print("=" * 70)
print("""
Bu alıştırmalarla Python Dictionary konusunda şunları öğrendiniz:

✓ Dictionary oluşturma ve temel işlemler
✓ Elemanlara erişim ve güvenli erişim metodları
✓ Dictionary metodları (keys, values, items, update, pop, vb.)
✓ Dictionary comprehension
✓ İç içe dictionary yapıları
✓ Gerçek dünya uygulamaları

Bir sonraki adım: Bu bilgileri kendi projelerinizde kullanmak!

Başarılar! 🚀
""")
