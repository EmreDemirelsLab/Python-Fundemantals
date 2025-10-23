"""
PYTHON LISTELERI - ALISTIRMALAR
================================
Bu dosya Python listeler konusunda temel seviyeden ileri seviyeye kadar
alistirmalari icerir. Her soru icin once TODO bolumu, sonra cozum bulunur.
"""

# =============================================================================
# ALISTIRMA 1: Temel Liste Olusturma (KOLAY)
# =============================================================================
"""
Soru 1:
5 tane en sevdiginiz meyvenin ismini iceren bir liste olusturun.
Listenin uzunlugunu ve ilk ile son elemani ekrana yazdirin.
"""

# TODO: Buraya kodunuzu yazin


# COZUM 1:
print("=" * 50)
print("ALISTIRMA 1: Temel Liste Olusturma")
print("=" * 50)

# Meyve listesi olusturma
meyveler = ["elma", "armut", "muz", "cilek", "portakal"]

# Liste uzunlugu
print(f"Liste uzunlugu: {len(meyveler)}")

# Ilk ve son eleman
print(f"Ilk eleman: {meyveler[0]}")
print(f"Son eleman: {meyveler[-1]}")

# Aciklama:
# - len() fonksiyonu ile listenin eleman sayisini bulabiliriz
# - Indeks 0 ile ilk elemana erisiyoruz
# - Indeks -1 ile son elemana erisiyoruz (negatif indeksleme)
print()


# =============================================================================
# ALISTIRMA 2: Liste Indeksleme ve Slicing (KOLAY)
# =============================================================================
"""
Soru 2:
1'den 10'a kadar sayilari iceren bir liste olusturun.
- Ilk 3 elemani yazdirin
- Son 3 elemani yazdirin
- 3. indeksten 7. indekse kadar olan elemanlari yazdirin
- Listeyi ters cevirip yazdirin
"""

# TODO: Buraya kodunuzu yazin


# COZUM 2:
print("=" * 50)
print("ALISTIRMA 2: Liste Indeksleme ve Slicing")
print("=" * 50)

# 1'den 10'a kadar sayilari iceren liste
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Orijinal liste: {sayilar}")

# Ilk 3 eleman
print(f"Ilk 3 eleman: {sayilar[:3]}")

# Son 3 eleman
print(f"Son 3 eleman: {sayilar[-3:]}")

# 3. indeksten 7. indekse kadar (7 dahil degil)
print(f"3. indeksten 7. indekse kadar: {sayilar[3:7]}")

# Listeyi ters cevirme
print(f"Ters cevrilmis liste: {sayilar[::-1]}")

# Aciklama:
# - [:3] -> Bastan 3. indekse kadar (0, 1, 2)
# - [-3:] -> Sondan 3 eleman
# - [3:7] -> 3. indeksten 7. indekse kadar (3, 4, 5, 6)
# - [::-1] -> -1 adim ile ters cevirme
print()


# =============================================================================
# ALISTIRMA 3: Liste Metodlari - Ekleme (KOLAY)
# =============================================================================
"""
Soru 3:
Bos bir liste olusturun. Asagidaki islemleri yaparak listeyi doldurun:
- append() ile "python" ekleyin
- append() ile "java" ekleyin
- insert() ile basina "c++" ekleyin
- extend() ile ["javascript", "ruby"] listesini ekleyin
Her adimda listeyi yazdirin.
"""

# TODO: Buraya kodunuzu yazin


# COZUM 3:
print("=" * 50)
print("ALISTIRMA 3: Liste Metodlari - Ekleme")
print("=" * 50)

# Bos liste olusturma
diller = []
print(f"Baslangic: {diller}")

# append ile ekleme
diller.append("python")
print(f"'python' eklendi: {diller}")

diller.append("java")
print(f"'java' eklendi: {diller}")

# insert ile basina ekleme
diller.insert(0, "c++")
print(f"Basina 'c++' eklendi: {diller}")

# extend ile birden fazla eleman ekleme
diller.extend(["javascript", "ruby"])
print(f"['javascript', 'ruby'] eklendi: {diller}")

# Aciklama:
# - append(): Tek bir eleman ekler, sona ekler
# - insert(indeks, eleman): Belirtilen indekse ekler
# - extend(): Baska bir listeyi veya iterable'i ekler
print()


# =============================================================================
# ALISTIRMA 4: Liste Metodlari - Silme (KOLAY-ORTA)
# =============================================================================
"""
Soru 4:
[1, 2, 3, 4, 5, 4, 6, 7, 4, 8] listesi verilmistir.
- Ilk 4'u silin (remove)
- Son elemani silin ve ekrana yazdirin (pop)
- 2. indeksteki elemani silin (pop veya del)
- Liste uzunlugunu yazdirin
"""

# TODO: Buraya kodunuzu yazin


# COZUM 4:
print("=" * 50)
print("ALISTIRMA 4: Liste Metodlari - Silme")
print("=" * 50)

# Liste olusturma
sayilar = [1, 2, 3, 4, 5, 4, 6, 7, 4, 8]
print(f"Baslangic listesi: {sayilar}")

# Ilk 4'u silme
sayilar.remove(4)
print(f"Ilk 4 silindi: {sayilar}")

# Son elemani silme ve yazdirma
son_eleman = sayilar.pop()
print(f"Son eleman ({son_eleman}) silindi: {sayilar}")

# 2. indeksteki elemani silme
silinen = sayilar.pop(2)
print(f"2. indeksteki eleman ({silinen}) silindi: {sayilar}")

# Liste uzunlugu
print(f"Son liste uzunlugu: {len(sayilar)}")

# Aciklama:
# - remove(deger): Ilk bulduğu degeri siler
# - pop(): Son elemani siler ve dondurur
# - pop(indeks): Belirtilen indeksteki elemani siler ve dondurur
# - del liste[indeks]: Elemani siler ama dondermez
print()


# =============================================================================
# ALISTIRMA 5: Liste Metodlari - Siralama (ORTA)
# =============================================================================
"""
Soru 5:
[45, 12, 78, 23, 56, 34, 89, 10] listesi verilmistir.
- Listeyi kucukten buyuge siralayip yazdirin
- Listeyi buyukten kucuge siralayip yazdirin
- Orijinal listeyi degistirmeden sorted() ile siralanmis yeni liste olusturun
- Iki listenin de id'sini karsilastirin (farklı objeler mi?)
"""

# TODO: Buraya kodunuzu yazin


# COZUM 5:
print("=" * 50)
print("ALISTIRMA 5: Liste Metodlari - Siralama")
print("=" * 50)

# Liste olusturma
sayilar = [45, 12, 78, 23, 56, 34, 89, 10]
print(f"Orijinal liste: {sayilar}")
print(f"Orijinal liste ID: {id(sayilar)}")

# Kucukten buyuge siralama (in-place)
sayilar.sort()
print(f"Kucukten buyuge: {sayilar}")

# Buyukten kucuge siralama (in-place)
sayilar.sort(reverse=True)
print(f"Buyukten kucuge: {sayilar}")

# Yeni liste olusturma
yeni_sayilar = [45, 12, 78, 23, 56, 34, 89, 10]
siralanmis = sorted(yeni_sayilar)
print(f"\nOrijinal (degismedi): {yeni_sayilar}")
print(f"Yeni siralanmis liste: {siralanmis}")
print(f"Orijinal liste ID: {id(yeni_sayilar)}")
print(f"Siralanmis liste ID: {id(siralanmis)}")
print(f"Ayni obje mi? {id(yeni_sayilar) == id(siralanmis)}")

# Aciklama:
# - sort(): Listeyi yerinde (in-place) siralar, None dondurur
# - sorted(): Yeni siralanmis liste olusturur, orijinali degistirmez
# - reverse=True: Azalan sira icin kullanilir
# - id(): Objenin hafizadaki adresini verir
print()


# =============================================================================
# ALISTIRMA 6: Liste Comprehension - Temel (ORTA)
# =============================================================================
"""
Soru 6:
- 1'den 20'ye kadar olan sayilarin karelerini iceren liste olusturun
- 1'den 50'ye kadar olan cift sayilari iceren liste olusturun
- 1'den 100'e kadar olan 3'e bolunebilen sayilari iceren liste olusturun
Her birini liste comprehension ile yapin.
"""

# TODO: Buraya kodunuzu yazin


# COZUM 6:
print("=" * 50)
print("ALISTIRMA 6: Liste Comprehension - Temel")
print("=" * 50)

# 1'den 20'ye kadar sayilarin kareleri
kareler = [x**2 for x in range(1, 21)]
print(f"1-20 arasi sayilarin kareleri:\n{kareler}")

# 1'den 50'ye kadar cift sayilar
cift_sayilar = [x for x in range(1, 51) if x % 2 == 0]
print(f"\n1-50 arasi cift sayilar:\n{cift_sayilar}")

# 1'den 100'e kadar 3'e bolunebilen sayilar
uc_kati = [x for x in range(1, 101) if x % 3 == 0]
print(f"\n1-100 arasi 3'e bolunebilen sayilar:\n{uc_kati}")

# Aciklama:
# Liste comprehension syntax: [ifade for eleman in iterable if kosul]
# - ifade: Her eleman icin uygulanacak islem
# - for: Dongu
# - if: Filtreleme kosulu (opsiyonel)
print()


# =============================================================================
# ALISTIRMA 7: Liste Comprehension - If-Else (ORTA)
# =============================================================================
"""
Soru 7:
1'den 30'a kadar olan sayilar icin:
- Sayi cift ise sayinin karesi
- Sayi tek ise sayinin kupu
seklinde bir liste olusturun.
"""

# TODO: Buraya kodunuzu yazin


# COZUM 7:
print("=" * 50)
print("ALISTIRMA 7: Liste Comprehension - If-Else")
print("=" * 50)

# Cift ise kare, tek ise kup
sonuc = [x**2 if x % 2 == 0 else x**3 for x in range(1, 31)]
print("1-30 arasi sayilar (cift->kare, tek->kup):")
print(sonuc)

# Daha okunabilir gosterim
print("\nDetayli gosterim:")
for i in range(1, 31):
    if i % 2 == 0:
        print(f"{i} cift -> {i}^2 = {i**2}")
    else:
        print(f"{i} tek -> {i}^3 = {i**3}")

# Aciklama:
# If-else ile liste comprehension syntax:
# [true_ifadesi if kosul else false_ifadesi for eleman in iterable]
# - Kosul True ise true_ifadesi
# - Kosul False ise false_ifadesi uygulanir
print()


# =============================================================================
# ALISTIRMA 8: Ic Ice Listeler (ORTA)
# =============================================================================
"""
Soru 8:
3x3 boyutunda bir carpim tablosu matrisi olusturun.
Matrisin her elemanina erisip yazdirin.
"""

# TODO: Buraya kodunuzu yazin


# COZUM 8:
print("=" * 50)
print("ALISTIRMA 8: Ic Ice Listeler")
print("=" * 50)

# 3x3 carpim tablosu olusturma
carpim_tablosu = [[i * j for j in range(1, 4)] for i in range(1, 4)]

print("3x3 Carpim Tablosu Matrisi:")
for satir in carpim_tablosu:
    print(satir)

# Matris elemanlarini tek tek yazdirma
print("\nDetayli gosterim:")
for i, satir in enumerate(carpim_tablosu):
    for j, eleman in enumerate(satir):
        print(f"matris[{i}][{j}] = {eleman}")

# Alternatif yontem: Daha buyuk carpim tablosu
print("\n5x5 Carpim Tablosu:")
carpim_5x5 = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for satir in carpim_5x5:
    print(" ".join(f"{x:3}" for x in satir))

# Aciklama:
# Ic ice liste comprehension: [[ic_dongu] for dis_dongu]
# - Dis dongu satirlari olusturur
# - Ic dongu her satirdaki elemanlari olusturur
print()


# =============================================================================
# ALISTIRMA 9: Liste Kopyalama (ORTA-ZOR)
# =============================================================================
"""
Soru 9:
[1, [2, 3], 4] gibi ic ice liste olusturun.
- Siradan atama ile (=) kopyalayin ve degisiklik yapin
- copy() metodu ile kopyalayin ve ic listeyi degistirin
- deepcopy ile kopyalayin ve ic listeyi degistirin
Farklarini gozlemleyin.
"""

# TODO: Buraya kodunuzu yazin


# COZUM 9:
print("=" * 50)
print("ALISTIRMA 9: Liste Kopyalama")
print("=" * 50)

import copy

# Orijinal ic ice liste
orijinal = [1, [2, 3], 4]
print(f"Orijinal liste: {orijinal}")

# 1. Siradan atama (referans kopyalama)
print("\n1. SIRADAN ATAMA (=):")
referans = orijinal
referans[0] = 999
print(f"Referans degistirildi: {referans}")
print(f"Orijinal de degisti: {orijinal}")

# Orijinali sifirlama
orijinal = [1, [2, 3], 4]

# 2. Yuzeysel kopya (shallow copy)
print("\n2. SHALLOW COPY (copy):")
yuzeysel = orijinal.copy()
yuzeysel[0] = 111  # Dis seviye degisiklik
yuzeysel[1][0] = 222  # Ic liste degisiklik
print(f"Yuzeysel kopya: {yuzeysel}")
print(f"Orijinal: {orijinal}")
print("Not: Dis seviye degismedi ama ic liste degisti!")

# Orijinali tekrar sifirlama
orijinal = [1, [2, 3], 4]

# 3. Derin kopya (deep copy)
print("\n3. DEEP COPY (deepcopy):")
derin = copy.deepcopy(orijinal)
derin[0] = 111
derin[1][0] = 222
print(f"Derin kopya: {derin}")
print(f"Orijinal: {orijinal}")
print("Not: Hem dis hem ic seviye bagimsiz!")

# Aciklama:
# - Siradan atama (=): Ayni objeye referans, kopya degil
# - Shallow copy: Dis seviye kopyalar, ic objeler referans
# - Deep copy: Tum seviyeleri bagimsiz kopyalar
print()


# =============================================================================
# ALISTIRMA 10: Liste Manipulasyonu (ORTA-ZOR)
# =============================================================================
"""
Soru 10:
Bir liste verilmistir: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Asagidaki islemleri liste comprehension kullanarak tek satirda yapin:
- Cift indeksteki elemanlarin toplamini bulun
- Tek indeksteki elemanlarin carpimini bulun
"""

# TODO: Buraya kodunuzu yazin


# COZUM 10:
print("=" * 50)
print("ALISTIRMA 10: Liste Manipulasyonu")
print("=" * 50)

# Liste olusturma
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Orijinal liste: {sayilar}")

# Cift indeksteki elemanlar (0, 2, 4, 6, 8)
cift_indeks = [sayilar[i] for i in range(len(sayilar)) if i % 2 == 0]
print(f"\nCift indeksteki elemanlar: {cift_indeks}")
print(f"Toplamı: {sum(cift_indeks)}")

# Tek indeksteki elemanlar (1, 3, 5, 7, 9)
tek_indeks = [sayilar[i] for i in range(len(sayilar)) if i % 2 != 0]
print(f"\nTek indeksteki elemanlar: {tek_indeks}")

# Carpim hesaplama
carpim = 1
for sayi in tek_indeks:
    carpim *= sayi
print(f"Carpimi: {carpim}")

# Alternatif: reduce ile carpim
from functools import reduce
carpim_reduce = reduce(lambda x, y: x * y, tek_indeks)
print(f"Carpim (reduce ile): {carpim_reduce}")

# Aciklama:
# - range(len(liste)) ile indekslere erisiyoruz
# - sum() ile toplama islemi
# - Carpim icin manuel dongu veya reduce kullanilabilir
print()


# =============================================================================
# ALISTIRMA 11: Palindrom Liste (ORTA-ZOR)
# =============================================================================
"""
Soru 11:
Bir fonksiyon yazin: Bir listenin palindrom olup olmadigini kontrol etsin.
Palindrom: Liste tersten de ayni (orn: [1, 2, 3, 2, 1])
Farkli listelerle test edin.
"""

# TODO: Buraya kodunuzu yazin


# COZUM 11:
print("=" * 50)
print("ALISTIRMA 11: Palindrom Liste")
print("=" * 50)

def palindrom_mu(liste):
    """
    Bir listenin palindrom olup olmadigini kontrol eder.

    Args:
        liste: Kontrol edilecek liste

    Returns:
        bool: Palindrom ise True, degilse False
    """
    return liste == liste[::-1]

# Test listeler
test_listeleri = [
    [1, 2, 3, 2, 1],
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c', 'b', 'a'],
    ['elma', 'armut', 'elma'],
    [1],
    [],
    [1, 2, 2, 1],
]

for liste in test_listeleri:
    sonuc = palindrom_mu(liste)
    print(f"{liste} -> {'Palindrom' if sonuc else 'Palindrom degil'}")

# Alternatif yontem: Manuel kontrol
def palindrom_mu_manuel(liste):
    """Palindrom kontrolu manuel olarak yapar."""
    n = len(liste)
    for i in range(n // 2):
        if liste[i] != liste[n - 1 - i]:
            return False
    return True

print("\nManuel kontrol yontemi ile:")
for liste in test_listeleri:
    sonuc = palindrom_mu_manuel(liste)
    print(f"{liste} -> {'Palindrom' if sonuc else 'Palindrom degil'}")

# Aciklama:
# - liste[::-1] ile listeyi tersine ceviriyoruz
# - Orijinal ile ters halini karsilastiriyoruz
# - Manuel yontemde ilk ve son elemanlari karsilastiriyoruz
print()


# =============================================================================
# ALISTIRMA 12: Liste Birlestirme ve Gruplama (ZOR)
# =============================================================================
"""
Soru 12:
Iki liste verilmistir:
isimler = ["Ali", "Ayse", "Mehmet", "Zeynep"]
notlar = [85, 92, 78, 95]

Bu iki listeyi birlestirerek asagidaki formatta yazdirin:
Ali: 85
Ayse: 92
...

Sonra notlara gore siralayin ve en yuksek notu alan 3 kisiyi yazdirin.
"""

# TODO: Buraya kodunuzu yazin


# COZUM 12:
print("=" * 50)
print("ALISTIRMA 12: Liste Birlestirme ve Gruplama")
print("=" * 50)

# Listeler
isimler = ["Ali", "Ayse", "Mehmet", "Zeynep", "Fatma", "Ahmet"]
notlar = [85, 92, 78, 95, 88, 90]

print("Ogrenci Notlari:")
print("-" * 30)

# zip() ile birlestirme
for isim, not_ in zip(isimler, notlar):
    print(f"{isim}: {not_}")

# Notlara gore siralama
print("\nNota Gore Siralanmis (Buyukten Kucuge):")
print("-" * 30)

# Liste olusturma: [(isim, not), ...]
ogrenci_notlari = list(zip(isimler, notlar))

# Nota gore siralama (nota gore = ikinci elemana gore)
siralanmis = sorted(ogrenci_notlari, key=lambda x: x[1], reverse=True)

for isim, not_ in siralanmis:
    print(f"{isim}: {not_}")

# En yuksek 3 kisi
print("\nEn Yuksek Notlu 3 Ogrenci:")
print("-" * 30)
for i, (isim, not_) in enumerate(siralanmis[:3], 1):
    print(f"{i}. {isim}: {not_}")

# Alternatif: Dictionary comprehension ile
ogrenci_sozlugu = {isim: not_ for isim, not_ in zip(isimler, notlar)}
print("\nSozluk formatinda:")
print(ogrenci_sozlugu)

# Aciklama:
# - zip(): Iki veya daha fazla listeyi eslestirir
# - sorted(key=lambda): Belirli bir ozellege gore siralar
# - lambda x: x[1]: Tuple'in ikinci elemanina gore sirala
# - [:3]: Ilk 3 elemani al
print()


# =============================================================================
# ALISTIRMA 13: Liste ile Matrix Islemleri (ZOR)
# =============================================================================
"""
Soru 13:
3x3 boyutunda iki matris olusturun ve asagidaki islemleri yapin:
- Matrisleri toplayin (eleman eleman toplama)
- Matrisleri carpin (eleman eleman carpma)
- Birinci matrisin transpozunu alin
"""

# TODO: Buraya kodunuzu yazin


# COZUM 13:
print("=" * 50)
print("ALISTIRMA 13: Liste ile Matrix Islemleri")
print("=" * 50)

# Matris olusturma
matris_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matris_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def matris_yazdir(matris, baslik=""):
    """Matrisi duzenli sekilde yazdirir."""
    if baslik:
        print(f"\n{baslik}:")
    for satir in matris:
        print(" ".join(f"{x:3}" for x in satir))

matris_yazdir(matris_a, "Matris A")
matris_yazdir(matris_b, "Matris B")

# Matris toplama
def matris_topla(a, b):
    """Iki matrisi toplar."""
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]

toplam = matris_topla(matris_a, matris_b)
matris_yazdir(toplam, "Matris A + B")

# Matris carpma (eleman eleman)
def matris_carp_eleman(a, b):
    """Iki matrisi eleman eleman carpar."""
    return [[a[i][j] * b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]

carpim = matris_carp_eleman(matris_a, matris_b)
matris_yazdir(carpim, "Matris A * B (eleman eleman)")

# Matris transpoz
def matris_transpoz(matris):
    """Matrisin transpozunu alir."""
    return [[matris[j][i] for j in range(len(matris))]
            for i in range(len(matris[0]))]

transpoz_a = matris_transpoz(matris_a)
matris_yazdir(transpoz_a, "Matris A'nin Transpozu")

# Aciklama:
# - Matris toplama: Her karsilik gelen elemani topla
# - Eleman eleman carpma: Her karsilik gelen elemani carp
# - Transpoz: Satirlar sutun, sutunlar satir olur
# - Ic ice liste comprehension kullanarak yapiyoruz
print()


# =============================================================================
# ALISTIRMA 14: Liste ile Veri Filtreleme (ZOR)
# =============================================================================
"""
Soru 14:
Ogrenci bilgilerini iceren liste verilmistir:
Her ogrenci: [isim, yas, not]

Asagidaki filtreleri uygulayip yazdirin:
- 20 yasindan buyuk ogrenciler
- Notu 80'den yuksek ogrenciler
- Hem 20 yasindan buyuk hem de notu 80'den yuksek ogrenciler
- Isimleri 'A' ile baslayan ogrenciler
"""

# TODO: Buraya kodunuzu yazin


# COZUM 14:
print("=" * 50)
print("ALISTIRMA 14: Liste ile Veri Filtreleme")
print("=" * 50)

# Ogrenci bilgileri
ogrenciler = [
    ["Ali", 22, 85],
    ["Ayse", 19, 92],
    ["Mehmet", 21, 78],
    ["Zeynep", 23, 95],
    ["Ahmet", 20, 88],
    ["Fatma", 18, 75],
    ["Can", 24, 90],
]

print("Tum Ogrenciler:")
print("-" * 50)
for isim, yas, not_ in ogrenciler:
    print(f"{isim:10} - Yas: {yas}, Not: {not_}")

# 1. 20 yasindan buyuk ogrenciler
print("\n20 Yasindan Buyuk Ogrenciler:")
print("-" * 50)
buyuk_20 = [ogr for ogr in ogrenciler if ogr[1] > 20]
for isim, yas, not_ in buyuk_20:
    print(f"{isim:10} - Yas: {yas}, Not: {not_}")

# 2. Notu 80'den yuksek ogrenciler
print("\nNotu 80'den Yuksek Ogrenciler:")
print("-" * 50)
yuksek_not = [ogr for ogr in ogrenciler if ogr[2] > 80]
for isim, yas, not_ in yuksek_not:
    print(f"{isim:10} - Yas: {yas}, Not: {not_}")

# 3. Hem 20 yasindan buyuk hem de notu 80'den yuksek
print("\n20 Yasindan Buyuk VE Notu 80'den Yuksek:")
print("-" * 50)
her_ikisi = [ogr for ogr in ogrenciler if ogr[1] > 20 and ogr[2] > 80]
for isim, yas, not_ in her_ikisi:
    print(f"{isim:10} - Yas: {yas}, Not: {not_}")

# 4. Isimleri 'A' ile baslayan
print("\nIsmi 'A' ile Baslayan Ogrenciler:")
print("-" * 50)
a_ile_baslayanlar = [ogr for ogr in ogrenciler if ogr[0].startswith('A')]
for isim, yas, not_ in a_ile_baslayanlar:
    print(f"{isim:10} - Yas: {yas}, Not: {not_}")

# Istatistikler
print("\nIstatistikler:")
print("-" * 50)
ortalama_yas = sum(ogr[1] for ogr in ogrenciler) / len(ogrenciler)
ortalama_not = sum(ogr[2] for ogr in ogrenciler) / len(ogrenciler)
print(f"Ortalama Yas: {ortalama_yas:.1f}")
print(f"Ortalama Not: {ortalama_not:.1f}")

# Aciklama:
# - Liste comprehension ile filtreleme yapiyoruz
# - Kosullar: if, and, or kullanilabilir
# - String metodlari: startswith(), endswith() vs.
# - sum() ve len() ile istatistik hesaplama
print()


# =============================================================================
# ALISTIRMA 15: Liste ile Gelismis Problem Cozme (COK ZOR)
# =============================================================================
"""
Soru 15: Sliding Window (Kayar Pencere) Teknigi
Bir liste verilmistir: [2, 5, 3, 8, 1, 7, 9, 6, 4]
Boyutu 3 olan kayar pencere ile listeyi tarayarak:
- Her pencerenin toplamini hesaplayin
- En buyuk toplama sahip pencereyi bulun
- O pencerenin indeksini ve elemanlarini yazdirin

Ornek: [2, 5, 3] -> toplam 10, [5, 3, 8] -> toplam 16, ...
"""

# TODO: Buraya kodunuzu yazin


# COZUM 15:
print("=" * 50)
print("ALISTIRMA 15: Sliding Window Teknigi")
print("=" * 50)

# Liste olusturma
sayilar = [2, 5, 3, 8, 1, 7, 9, 6, 4]
pencere_boyutu = 3

print(f"Orijinal Liste: {sayilar}")
print(f"Pencere Boyutu: {pencere_boyutu}")
print("\nTum Pencereler:")
print("-" * 50)

# Tum pencereleri ve toplamlarini hesaplama
pencere_toplamlari = []

for i in range(len(sayilar) - pencere_boyutu + 1):
    pencere = sayilar[i:i + pencere_boyutu]
    toplam = sum(pencere)
    pencere_toplamlari.append((i, pencere, toplam))
    print(f"Indeks {i}: {pencere} -> Toplam: {toplam}")

# En buyuk toplami bulma
max_indeks, max_pencere, max_toplam = max(pencere_toplamlari, key=lambda x: x[2])

print("\nSonuc:")
print("-" * 50)
print(f"En buyuk toplam: {max_toplam}")
print(f"Pencere: {max_pencere}")
print(f"Baslangic indeksi: {max_indeks}")
print(f"Bitis indeksi: {max_indeks + pencere_boyutu - 1}")

# Liste comprehension ile daha kompakt cozum
print("\nAlternatif Cozum (Liste Comprehension):")
print("-" * 50)

# Tum pencere toplamlarini hesaplama
toplamlar = [sum(sayilar[i:i+pencere_boyutu])
             for i in range(len(sayilar) - pencere_boyutu + 1)]

print(f"Tum pencere toplamlari: {toplamlar}")
print(f"En buyuk toplam: {max(toplamlar)}")
print(f"En buyuk toplamin indeksi: {toplamlar.index(max(toplamlar))}")

# Optimize edilmis cozum: Kayar toplam
print("\nOptimize Edilmis Cozum (Kayar Toplam):")
print("-" * 50)

# Ilk pencerenin toplami
pencere_toplam = sum(sayilar[:pencere_boyutu])
max_toplam_opt = pencere_toplam
max_indeks_opt = 0

print(f"Baslangic penceresi toplami: {pencere_toplam}")

# Kayarak toplam hesaplama
for i in range(1, len(sayilar) - pencere_boyutu + 1):
    # Eski ilk elemani cikar, yeni son elemani ekle
    pencere_toplam = pencere_toplam - sayilar[i-1] + sayilar[i+pencere_boyutu-1]
    print(f"Pencere {i} toplami: {pencere_toplam}")

    if pencere_toplam > max_toplam_opt:
        max_toplam_opt = pencere_toplam
        max_indeks_opt = i

print(f"\nEn buyuk toplam: {max_toplam_opt}")
print(f"Indeks: {max_indeks_opt}")
print(f"Pencere: {sayilar[max_indeks_opt:max_indeks_opt+pencere_boyutu]}")

# Aciklama:
# - Sliding Window: Veri analizi ve algoritmalarda sikca kullanilir
# - Naive cozum: Her pencereyi tek tek toplama (O(n*k))
# - Optimize cozum: Kayar toplam kullanarak (O(n))
# - max() fonksiyonu key parametresi ile tuple'dan eleman secebilir
print()


print("\n" + "=" * 50)
print("TUM ALISTIRMALAR TAMAMLANDI!")
print("=" * 50)
