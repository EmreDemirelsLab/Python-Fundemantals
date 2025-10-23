"""
KONTROL YAPILARI ALIŞTIRMALARI
===============================

Bu dosya, Python kontrol yapıları konusunda pratik yapmanız için
hazırlanmış alıştırmaları içerir.

Her alıştırma şu bölümlerden oluşur:
1. Soru açıklaması
2. TODO: Buraya kodunuzu yazın
3. Çözüm ve açıklama

Zorluk Seviyeleri:
- KOLAY: Temel kavramlar
- ORTA: Birden fazla konsept kombinasyonu
- ZOR: Karmaşık mantık ve optimizasyon
"""

print("=" * 70)
print("KONTROL YAPILARI ALIŞTIRMALARI")
print("=" * 70)

# =============================================================================
# ALIŞTIRMA 1: Sayı Kontrol (KOLAY)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 1: Sayı Kontrol (KOLAY)")
print("=" * 70)
print("""
Kullanıcıdan bir sayı alın ve aşağıdaki kontrolleri yapın:
- Sayı pozitif mi, negatif mi, yoksa sıfır mı?
- Sayı tek mi, çift mi?
- Sayı 10'dan büyük mü, küçük mü, eşit mi?
""")

# TODO: Çözümünüzü buraya yazın
# sayi = int(input("Bir sayı girin: "))


# ÇÖZÜM:
print("ÇÖZÜM 1:")
print("-" * 70)

# Demo için sabit değer kullanıyoruz
sayi = 15

# Pozitif/Negatif/Sıfır kontrolü
if sayi > 0:
    print(f"{sayi} pozitif bir sayıdır")
elif sayi < 0:
    print(f"{sayi} negatif bir sayıdır")
else:
    print(f"{sayi} sıfırdır")

# Tek/Çift kontrolü
if sayi % 2 == 0:
    print(f"{sayi} çift bir sayıdır")
else:
    print(f"{sayi} tek bir sayıdır")

# 10 ile karşılaştırma
if sayi > 10:
    print(f"{sayi}, 10'dan büyüktür")
elif sayi < 10:
    print(f"{sayi}, 10'dan küçüktür")
else:
    print(f"{sayi}, 10'a eşittir")

# AÇIKLAMA:
print("\nAçıklama:")
print("- if-elif-else yapısı ile çoklu koşul kontrolü yapıldı")
print("- % operatörü ile tek/çift kontrolü yapıldı")
print("- Karşılaştırma operatörleri (>, <, ==) kullanıldı")


# =============================================================================
# ALIŞTIRMA 2: Harf Notu Hesaplama (KOLAY)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 2: Harf Notu Hesaplama (KOLAY)")
print("=" * 70)
print("""
Öğrenci notuna göre harf notu veren bir program yazın:
90-100: AA
80-89:  BA
70-79:  BB
60-69:  CB
50-59:  CC
40-49:  DC
0-39:   FF
Ayrıca geçme/kalma durumunu belirtin (50 ve üzeri geçer)
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 2:")
print("-" * 70)

not_puani = 76

# Harf notu belirleme
if not_puani >= 90:
    harf = "AA"
elif not_puani >= 80:
    harf = "BA"
elif not_puani >= 70:
    harf = "BB"
elif not_puani >= 60:
    harf = "CB"
elif not_puani >= 50:
    harf = "CC"
elif not_puani >= 40:
    harf = "DC"
else:
    harf = "FF"

# Geçme/Kalma durumu
durum = "GEÇTİ" if not_puani >= 50 else "KALDI"

print(f"Not: {not_puani}")
print(f"Harf Notu: {harf}")
print(f"Durum: {durum}")

# AÇIKLAMA:
print("\nAçıklama:")
print("- elif yapısı ile not aralıkları kontrol edildi")
print("- Ternary operatör ile tek satırda geçme/kalma kontrolü yapıldı")
print("- Koşullar büyükten küçüğe sıralandı (90, 80, 70...)")


# =============================================================================
# ALIŞTIRMA 3: 1'den N'e Kadar Toplam (KOLAY)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 3: 1'den N'e Kadar Toplam (KOLAY)")
print("=" * 70)
print("""
1'den kullanıcının girdiği sayıya kadar olan tüm sayıların toplamını hesaplayın.
Örnek: N=5 için 1+2+3+4+5 = 15
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 3:")
print("-" * 70)

n = 10
toplam = 0

# Yöntem 1: for döngüsü ile
for i in range(1, n + 1):
    toplam += i

print(f"1'den {n}'e kadar toplam (for): {toplam}")

# Yöntem 2: while döngüsü ile
toplam_while = 0
sayac = 1

while sayac <= n:
    toplam_while += sayac
    sayac += 1

print(f"1'den {n}'e kadar toplam (while): {toplam_while}")

# Yöntem 3: sum() ve range() ile
toplam_sum = sum(range(1, n + 1))
print(f"1'den {n}'e kadar toplam (sum): {toplam_sum}")

# Bonus: Matematiksel formül
toplam_formul = n * (n + 1) // 2
print(f"1'den {n}'e kadar toplam (formül): {toplam_formul}")

# AÇIKLAMA:
print("\nAçıklama:")
print("- for döngüsü: range(1, n+1) ile 1'den n'e kadar sayıları dolaşır")
print("- while döngüsü: Sayaç mantığı ile çalışır")
print("- sum() fonksiyonu: En Pythonic yöntem")
print("- Matematiksel formül: n*(n+1)/2 - En hızlı yöntem")


# =============================================================================
# ALIŞTIRMA 4: Çarpım Tablosu (ORTA)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 4: Çarpım Tablosu (ORTA)")
print("=" * 70)
print("""
Kullanıcının girdiği sayının çarpım tablosunu (1'den 10'a kadar) yazdırın.
Ayrıca tüm çarpımların toplamını hesaplayın.
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 4:")
print("-" * 70)

sayi = 7
toplam = 0

print(f"{sayi} Çarpım Tablosu:")
print("-" * 30)

for i in range(1, 11):
    carpim = sayi * i
    toplam += carpim
    print(f"{sayi} x {i:2d} = {carpim:3d}")

print("-" * 30)
print(f"Toplam: {toplam}")

# AÇIKLAMA:
print("\nAçıklama:")
print("- for döngüsü ile 1'den 10'a kadar çarpma işlemi yapıldı")
print("- Formatlamalı string kullanıldı (f-string ve :2d, :3d)")
print("- Her çarpım sonucu toplama eklendi")


# =============================================================================
# ALIŞTIRMA 5: Asal Sayı Kontrolü (ORTA)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 5: Asal Sayı Kontrolü (ORTA)")
print("=" * 70)
print("""
Verilen bir sayının asal olup olmadığını kontrol edin.
Asal sayı: 1'den büyük ve sadece 1 ve kendisi ile bölünebilen sayılardır.
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 5:")
print("-" * 70)

sayi = 29

if sayi < 2:
    print(f"{sayi} asal sayı değildir")
else:
    asal = True
    # 2'den sayının kareköküne kadar kontrol etmek yeterli
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            print(f"{sayi}, {i} ile tam bölündüğü için asal değildir")
            asal = False
            break

    if asal:
        print(f"{sayi} bir asal sayıdır")

# Alternatif çözüm: Daha detaylı
def asal_mi(n):
    """Bir sayının asal olup olmadığını kontrol eder"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Tek sayılar için 3'ten başlayarak 2'şer atlayarak kontrol
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test
test_sayilari = [2, 3, 4, 17, 25, 29, 97, 100]
print("\nÇeşitli sayılar için test:")
for s in test_sayilari:
    sonuc = "asal" if asal_mi(s) else "asal değil"
    print(f"{s:3d}: {sonuc}")

# AÇIKLAMA:
print("\nAçıklama:")
print("- 2'den küçük sayılar asal değildir")
print("- Karekök optimizasyonu: sadece sqrt(n)'e kadar kontrol yeterli")
print("- break ile ilk böleni bulduğumuzda döngüden çıkıyoruz")
print("- Alternatif çözümde çift sayılar hemen eleniyor")


# =============================================================================
# ALIŞTIRMA 6: FizzBuzz Oyunu (ORTA)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 6: FizzBuzz Oyunu (ORTA)")
print("=" * 70)
print("""
1'den 30'a kadar sayıları yazdırın, ancak:
- 3'ün katları için "Fizz" yazdırın
- 5'in katları için "Buzz" yazdırın
- Hem 3 hem 5'in katları için "FizzBuzz" yazdırın
- Diğer sayılar için sayının kendisini yazdırın
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 6:")
print("-" * 70)

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i:2d}: FizzBuzz")
    elif i % 3 == 0:
        print(f"{i:2d}: Fizz")
    elif i % 5 == 0:
        print(f"{i:2d}: Buzz")
    else:
        print(f"{i:2d}: {i}")

# Alternatif çözüm: String birleştirme
print("\nAlternatif Çözüm:")
for i in range(1, 31):
    cikti = ""
    if i % 3 == 0:
        cikti += "Fizz"
    if i % 5 == 0:
        cikti += "Buzz"
    print(f"{i:2d}: {cikti if cikti else i}")

# AÇIKLAMA:
print("\nAçıklama:")
print("- Önce hem 3 hem 5'e bölünebilirlik kontrol edilmeli")
print("- elif kullanımı ile gereksiz kontroller önlenir")
print("- Alternatif çözüm daha genişletilebilir (örn: 7 için 'Bazz')")


# =============================================================================
# ALIŞTIRMA 7: Fibonacci Serisi (ORTA)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 7: Fibonacci Serisi (ORTA)")
print("=" * 70)
print("""
İlk N tane Fibonacci sayısını yazdırın.
Fibonacci: Her sayı kendinden önceki iki sayının toplamıdır
Örnek: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 7:")
print("-" * 70)

n = 10
a, b = 0, 1

print(f"İlk {n} Fibonacci sayısı:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Eşzamanlı atama

print("\n\nListe olarak:")
fib_listesi = [0, 1]
for i in range(2, n):
    fib_listesi.append(fib_listesi[i-1] + fib_listesi[i-2])

print(fib_listesi)

# Belirli bir sayıya kadar Fibonacci
print("\n100'den küçük Fibonacci sayıları:")
a, b = 0, 1
while a < 100:
    print(a, end=" ")
    a, b = b, a + b

# AÇIKLAMA:
print("\n\nAçıklama:")
print("- a, b = b, a+b: Python'un eşzamanlı atama özelliği")
print("- İlk iki sayı 0 ve 1'dir")
print("- Her yeni sayı önceki ikisinin toplamıdır")
print("- while döngüsü ile belirli bir limite kadar üretilebilir")


# =============================================================================
# ALIŞTIRMA 8: Yıldız Desenleri (ORTA)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 8: Yıldız Desenleri (ORTA)")
print("=" * 70)
print("""
İç içe döngüler kullanarak üçgen desenler oluşturun:
1. Artan üçgen
2. Azalan üçgen
3. Piramit
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 8:")
print("-" * 70)

satir = 5

# 1. Artan üçgen
print("1. Artan Üçgen:")
for i in range(1, satir + 1):
    print("*" * i)

# 2. Azalan üçgen
print("\n2. Azalan Üçgen:")
for i in range(satir, 0, -1):
    print("*" * i)

# 3. Piramit
print("\n3. Piramit:")
for i in range(1, satir + 1):
    bosluk = " " * (satir - i)
    yildiz = "*" * (2 * i - 1)
    print(bosluk + yildiz)

# 4. Ters piramit
print("\n4. Ters Piramit:")
for i in range(satir, 0, -1):
    bosluk = " " * (satir - i)
    yildiz = "*" * (2 * i - 1)
    print(bosluk + yildiz)

# 5. Elmas
print("\n5. Elmas:")
# Üst kısım
for i in range(1, satir + 1):
    print(" " * (satir - i) + "*" * (2 * i - 1))
# Alt kısım
for i in range(satir - 1, 0, -1):
    print(" " * (satir - i) + "*" * (2 * i - 1))

# AÇIKLAMA:
print("\nAçıklama:")
print("- Artan üçgen: Her satırda yıldız sayısı artıyor")
print("- Piramit: Boşluklar + yıldızlar kombinasyonu")
print("- 2*i-1 formülü: Merkezi hizalama için tek sayılar")
print("- İç içe döngü yerine string çarpma kullanıldı")


# =============================================================================
# ALIŞTIRMA 9: Liste Filtreleme (ORTA)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 9: Liste Filtreleme (ORTA)")
print("=" * 70)
print("""
Verilen sayı listesinden:
1. Çift sayıları filtreleyin
2. 50'den büyük sayıları filtreleyin
3. Hem çift hem de 50'den büyük sayıları filtreleyin
Hem klasik döngü hem de list comprehension kullanın.
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 9:")
print("-" * 70)

sayilar = [12, 45, 67, 23, 89, 34, 56, 90, 15, 78, 42, 101]

print(f"Orijinal liste: {sayilar}")

# 1. Çift sayılar - Klasik yöntem
cift_sayilar = []
for sayi in sayilar:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)

print(f"\n1. Çift sayılar (klasik): {cift_sayilar}")

# Çift sayılar - List comprehension
cift_sayilar_lc = [sayi for sayi in sayilar if sayi % 2 == 0]
print(f"1. Çift sayılar (list comp): {cift_sayilar_lc}")

# 2. 50'den büyük sayılar
buyuk_sayilar = [sayi for sayi in sayilar if sayi > 50]
print(f"\n2. 50'den büyük sayılar: {buyuk_sayilar}")

# 3. Hem çift hem 50'den büyük
cift_ve_buyuk = [sayi for sayi in sayilar if sayi % 2 == 0 and sayi > 50]
print(f"\n3. Çift ve 50'den büyük: {cift_ve_buyuk}")

# Bonus: Kategorilere ayırma
tek_sayilar = [sayi for sayi in sayilar if sayi % 2 != 0]
print(f"\nBonus - Tek sayılar: {tek_sayilar}")

# İstatistikler
print(f"\nİstatistikler:")
print(f"Toplam sayı adedi: {len(sayilar)}")
print(f"Çift sayı adedi: {len(cift_sayilar)}")
print(f"Tek sayı adedi: {len(tek_sayilar)}")
print(f"50'den büyük sayı adedi: {len(buyuk_sayilar)}")

# AÇIKLAMA:
print("\nAçıklama:")
print("- List comprehension daha kısa ve okunabilir")
print("- Birden fazla koşul 'and' ile birleştirilebilir")
print("- Performans: List comprehension genelde daha hızlı")


# =============================================================================
# ALIŞTIRMA 10: Sayı Tahmin Oyunu (ZOR)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 10: Sayı Tahmin Oyunu (ZOR)")
print("=" * 70)
print("""
1-100 arası rastgele sayı tahmin oyunu:
- Kullanıcı sayı tahmini yapacak
- "Daha büyük" veya "Daha küçük" ipucu verilecek
- Maksimum 7 tahmin hakkı olacak
- Kalan hak gösterilecek
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 10:")
print("-" * 70)

import random

# Rastgele sayı üret
gizli_sayi = random.randint(1, 100)
max_tahmin = 7
tahmin_sayisi = 0

print("1-100 arası bir sayı tuttum. Bulabilir misin?")
print(f"Toplam {max_tahmin} tahmin hakkınız var.")

# Demo için otomatik tahmin
demo_tahminler = [50, 75, 88, 95, 92, 90, 91]  # Örnek tahmin stratejisi

for tahmin in demo_tahminler:
    tahmin_sayisi += 1
    kalan_hak = max_tahmin - tahmin_sayisi

    print(f"\n{tahmin_sayisi}. Tahmin: {tahmin}")

    if tahmin == gizli_sayi:
        print(f"🎉 Tebrikler! {tahmin_sayisi} tahminde doğru sayıyı buldunuz!")
        print(f"Doğru sayı: {gizli_sayi}")
        break
    elif tahmin < gizli_sayi:
        print("⬆️  Daha büyük bir sayı söyleyin")
    else:
        print("⬇️  Daha küçük bir sayı söyleyin")

    if kalan_hak > 0:
        print(f"Kalan tahmin hakkı: {kalan_hak}")
    else:
        print(f"\n😞 Tahmin hakkınız bitti!")
        print(f"Doğru sayı: {gizli_sayi}")
        break

# Gerçek oyun için kod (yorumlu)
"""
# Gerçek kullanıcı girdisi ile oyun:
while tahmin_sayisi < max_tahmin:
    try:
        tahmin = int(input(f"\nTahmin {tahmin_sayisi + 1}: "))

        if tahmin < 1 or tahmin > 100:
            print("Lütfen 1-100 arası bir sayı girin!")
            continue

        tahmin_sayisi += 1

        if tahmin == gizli_sayi:
            print(f"Tebrikler! {tahmin_sayisi} tahminde buldunuz!")
            break
        elif tahmin < gizli_sayi:
            print("Daha büyük")
        else:
            print("Daha küçük")

        kalan = max_tahmin - tahmin_sayisi
        if kalan > 0:
            print(f"Kalan hak: {kalan}")

    except ValueError:
        print("Geçerli bir sayı girin!")
        continue

if tahmin_sayisi == max_tahmin and tahmin != gizli_sayi:
    print(f"Oyun bitti! Doğru sayı: {gizli_sayi}")
"""

# AÇIKLAMA:
print("\nAçıklama:")
print("- random.randint() ile rastgele sayı üretildi")
print("- while döngüsü ile sınırlı sayıda tahmin kontrolü")
print("- try-except ile geçersiz giriş kontrolü")
print("- break ile erken çıkış (doğru tahmin)")
print("- continue ile geçersiz girdileri atlama")


# =============================================================================
# ALIŞTIRMA 11: Liste İçinde Arama ve Değiştirme (ZOR)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 11: Liste İçinde Arama ve Değiştirme (ZOR)")
print("=" * 70)
print("""
Bir kelime listesinde:
1. Belirli bir harfle başlayan kelimeleri bulun
2. Belirli uzunluktaki kelimeleri filtreleyin
3. Kelimelerin ilk harfini büyük yapın
4. En uzun ve en kısa kelimeyi bulun
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 11:")
print("-" * 70)

kelimeler = ["python", "programlama", "algoritma", "veri", "yapıları",
             "fonksiyon", "döngü", "koşul", "liste", "sözlük", "demet"]

print(f"Kelime listesi: {kelimeler}")

# 1. 'p' ile başlayan kelimeler
p_ile_baslayanlar = [kelime for kelime in kelimeler if kelime.startswith('p')]
print(f"\n1. 'p' ile başlayan kelimeler: {p_ile_baslayanlar}")

# Alternatif: Klasik döngü
p_kelimeler_klasik = []
for kelime in kelimeler:
    if kelime[0] == 'p':
        p_kelimeler_klasik.append(kelime)

# 2. 7 karakterden uzun kelimeler
uzun_kelimeler = [kelime for kelime in kelimeler if len(kelime) > 7]
print(f"\n2. 7 harften uzun kelimeler: {uzun_kelimeler}")

# 3. İlk harfi büyük yap
buyuk_harfli = [kelime.capitalize() for kelime in kelimeler]
print(f"\n3. İlk harfi büyük: {buyuk_harfli}")

# 4. En uzun ve en kısa kelime
en_uzun = ""
en_kisa = kelimeler[0]

for kelime in kelimeler:
    if len(kelime) > len(en_uzun):
        en_uzun = kelime
    if len(kelime) < len(en_kisa):
        en_kisa = kelime

print(f"\n4. En uzun kelime: {en_uzun} ({len(en_uzun)} harf)")
print(f"   En kısa kelime: {en_kisa} ({len(en_kisa)} harf)")

# Alternatif: max ve min kullanımı
en_uzun_alt = max(kelimeler, key=len)
en_kisa_alt = min(kelimeler, key=len)
print(f"\n   (max/min) En uzun: {en_uzun_alt}, En kısa: {en_kisa_alt}")

# Bonus: Harf sayısına göre gruplama
print("\n5. Bonus - Harf sayısına göre gruplandırma:")
harf_gruplari = {}
for kelime in kelimeler:
    uzunluk = len(kelime)
    if uzunluk not in harf_gruplari:
        harf_gruplari[uzunluk] = []
    harf_gruplari[uzunluk].append(kelime)

for uzunluk in sorted(harf_gruplari.keys()):
    print(f"   {uzunluk} harf: {harf_gruplari[uzunluk]}")

# AÇIKLAMA:
print("\nAçıklama:")
print("- startswith(): String'in başlangıcını kontrol eder")
print("- capitalize(): İlk harfi büyük yapar")
print("- max/min with key: Özel karşılaştırma fonksiyonu")
print("- Dictionary ile gruplama yapıldı")


# =============================================================================
# ALIŞTIRMA 12: Matris İşlemleri (ZOR)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 12: Matris İşlemleri (ZOR)")
print("=" * 70)
print("""
İç içe listeler kullanarak 3x3 matris oluşturun ve:
1. Matrisin tüm elemanlarını yazdırın
2. Köşegen elemanlarını bulun
3. Satır ve sütun toplamlarını hesaplayın
4. Matrisin transpozunu alın
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 12:")
print("-" * 70)

# Matris oluşturma
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Matris yazdırma
print("1. Matris:")
for satir in matris:
    print("  ", satir)

# Daha güzel görünüm
print("\nFormatlanmış matris:")
for satir in matris:
    print("  ", end="")
    for eleman in satir:
        print(f"{eleman:3}", end=" ")
    print()

# 2. Köşegen elemanları
print("\n2. Köşegen elemanlar:")
kosegen = []
for i in range(len(matris)):
    kosegen.append(matris[i][i])
print(f"   Ana köşegen: {kosegen}")

# Ters köşegen
ters_kosegen = []
n = len(matris)
for i in range(n):
    ters_kosegen.append(matris[i][n-1-i])
print(f"   Ters köşegen: {ters_kosegen}")

# 3. Satır ve sütun toplamları
print("\n3. Toplamlar:")

# Satır toplamları
for i, satir in enumerate(matris):
    toplam = sum(satir)
    print(f"   Satır {i+1} toplamı: {toplam}")

# Sütun toplamları
print()
for j in range(len(matris[0])):
    toplam = sum(matris[i][j] for i in range(len(matris)))
    print(f"   Sütun {j+1} toplamı: {toplam}")

# 4. Transpoz (satırları sütun yapma)
print("\n4. Transpoz:")
transpoz = []
for j in range(len(matris[0])):
    yeni_satir = []
    for i in range(len(matris)):
        yeni_satir.append(matris[i][j])
    transpoz.append(yeni_satir)

for satir in transpoz:
    print("  ", end="")
    for eleman in satir:
        print(f"{eleman:3}", end=" ")
    print()

# List comprehension ile transpoz
transpoz_lc = [[matris[i][j] for i in range(len(matris))]
               for j in range(len(matris[0]))]

print("\nBonus - zip() ile transpoz:")
transpoz_zip = list(zip(*matris))
for satir in transpoz_zip:
    print("  ", list(satir))

# AÇIKLAMA:
print("\nAçıklama:")
print("- İç içe listeler matris temsil eder")
print("- matris[i][j]: i. satır, j. sütun")
print("- Ana köşegen: matris[i][i] elemanları")
print("- Ters köşegen: matris[i][n-1-i] elemanları")
print("- Transpoz: Satır ve sütunları yer değiştirme")
print("- zip(*matris): Pythonic transpoz yöntemi")


# =============================================================================
# ALIŞTIRMA 13: Kelime Sıklığı Analizi (ZOR)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 13: Kelime Sıklığı Analizi (ZOR)")
print("=" * 70)
print("""
Bir metindeki kelime sıklıklarını analiz edin:
1. Her kelimenin kaç kez geçtiğini bulun
2. En sık geçen 3 kelimeyi bulun
3. Belirli uzunluktaki kelimelerin sayısını hesaplayın
4. Sadece bir kez geçen kelimeleri listeleyin
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 13:")
print("-" * 70)

metin = """
Python programlama dili öğrenmek çok eğlenceli. Python ile
web geliştirme yapabilir, veri analizi yapabilir ve
yapay zeka projeleri geliştirebilirsiniz. Python öğrenmek
her geçen gün daha da popüler hale geliyor.
"""

# Metni küçük harfe çevir ve noktalama işaretlerini kaldır
metin = metin.lower()
for karakter in ".,!?;:":
    metin = metin.replace(karakter, "")

# Kelimelere ayır
kelimeler = metin.split()

print(f"Toplam kelime sayısı: {len(kelimeler)}")

# 1. Kelime sıklıkları
kelime_sayaci = {}
for kelime in kelimeler:
    if kelime in kelime_sayaci:
        kelime_sayaci[kelime] += 1
    else:
        kelime_sayaci[kelime] = 1

print("\n1. Kelime sıklıkları:")
for kelime, sayi in sorted(kelime_sayaci.items()):
    print(f"   {kelime}: {sayi}")

# 2. En sık geçen 3 kelime
print("\n2. En sık geçen 3 kelime:")
# Sıklığa göre sırala
sirali_kelimeler = sorted(kelime_sayaci.items(), key=lambda x: x[1], reverse=True)
for i in range(min(3, len(sirali_kelimeler))):
    kelime, sayi = sirali_kelimeler[i]
    print(f"   {i+1}. {kelime}: {sayi} kez")

# 3. Uzunluğa göre kelime sayısı
print("\n3. Uzunluğa göre kelime dağılımı:")
uzunluk_sayaci = {}
for kelime in kelimeler:
    uzunluk = len(kelime)
    uzunluk_sayaci[uzunluk] = uzunluk_sayaci.get(uzunluk, 0) + 1

for uzunluk in sorted(uzunluk_sayaci.keys()):
    print(f"   {uzunluk} harfli: {uzunluk_sayaci[uzunluk]} kelime")

# 4. Sadece bir kez geçen kelimeler
print("\n4. Sadece bir kez geçen kelimeler:")
tekil_kelimeler = [kelime for kelime, sayi in kelime_sayaci.items() if sayi == 1]
print(f"   {tekil_kelimeler}")
print(f"   Toplam: {len(tekil_kelimeler)} kelime")

# Bonus: İstatistikler
print("\n5. Bonus - Detaylı istatistikler:")
benzersiz_kelime = len(kelime_sayaci)
toplam_kelime = len(kelimeler)
print(f"   Benzersiz kelime sayısı: {benzersiz_kelime}")
print(f"   Toplam kelime sayısı: {toplam_kelime}")
print(f"   Ortalama kelime uzunluğu: {sum(len(k) for k in kelimeler) / toplam_kelime:.1f}")

# AÇIKLAMA:
print("\nAçıklama:")
print("- Dictionary ile kelime sayma (kelime: sıklık)")
print("- get() metodu: Varsayılan değer ile güvenli erişim")
print("- sorted() with key: Özel sıralama (lambda fonksiyonu)")
print("- List comprehension ile filtreleme")
print("- String metodları: lower(), replace(), split()")


# =============================================================================
# ALIŞTIRMA 14: Sayı Piramidi (ZOR)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 14: Sayı Piramidi (ZOR)")
print("=" * 70)
print("""
Sayılardan oluşan farklı piramit desenleri oluşturun:
1. Artan sayı piramidi
2. Tekrarlayan sayı piramidi
3. Floyd üçgeni
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 14:")
print("-" * 70)

n = 5

# 1. Artan sayı piramidi
print("1. Artan Sayı Piramidi:")
for i in range(1, n + 1):
    # Boşluklar
    print(" " * (n - i), end="")
    # Sayılar (artan)
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 2. Tekrarlayan sayı piramidi
print("\n2. Tekrarlayan Sayı Piramidi:")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(i, end=" ")
    print()

# 3. Floyd üçgeni (ardışık sayılar)
print("\n3. Floyd Üçgeni:")
sayi = 1
for i in range(1, n + 1):
    for j in range(i):
        print(f"{sayi:3}", end=" ")
        sayi += 1
    print()

# 4. Sayı elması
print("\n4. Sayı Elması:")
# Üst kısım
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

# Alt kısım
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

# 5. Pascal üçgeni
print("\n5. Pascal Üçgeni (İkili katsayılar):")
for i in range(n):
    # Boşluklar
    print(" " * (n - i), end="")

    # Pascal sayısı hesaplama
    sayi = 1
    for j in range(i + 1):
        print(f"{sayi:3}", end=" ")
        sayi = sayi * (i - j) // (j + 1)
    print()

# AÇIKLAMA:
print("\nAçıklama:")
print("- İç içe döngülerle desen oluşturma")
print("- Boşluk sayısı = n - i (merkezleme için)")
print("- Floyd üçgeni: Ardışık sayılarla doldurma")
print("- Pascal üçgeni: Her sayı üstündeki iki sayının toplamı")
print("- Elmas: Artan + azalan döngü kombinasyonu")


# =============================================================================
# ALIŞTIRMA 15: Liste Sıralama (Binary Search için) (ZOR)
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMA 15: Binary Search (İkili Arama) (ZOR)")
print("=" * 70)
print("""
Sıralı bir listede binary search (ikili arama) algoritması uygulayın.
Binary search, sıralı listede ortadan bölerek arama yapan hızlı bir algoritmadır.
Aranan sayıyı bulana kadar liste sürekli yarıya bölünür.
""")

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM:
print("ÇÖZÜM 15:")
print("-" * 70)

def binary_search(liste, aranan):
    """
    Binary search algoritması

    Args:
        liste: Sıralı sayı listesi
        aranan: Aranacak sayı

    Returns:
        Bulunan indeks veya -1 (bulunamadıysa)
    """
    sol = 0
    sag = len(liste) - 1
    adim = 0

    print(f"\nAranan: {aranan}")
    print(f"Liste: {liste}")
    print("-" * 50)

    while sol <= sag:
        adim += 1
        orta = (sol + sag) // 2
        orta_deger = liste[orta]

        print(f"Adım {adim}:")
        print(f"  Sol: {sol}, Sağ: {sag}, Orta: {orta}")
        print(f"  Orta değer: {orta_deger}")

        if orta_deger == aranan:
            print(f"  ✓ Bulundu! İndeks: {orta}")
            return orta
        elif orta_deger < aranan:
            print(f"  {orta_deger} < {aranan}, sağ yarıya geç")
            sol = orta + 1
        else:
            print(f"  {orta_deger} > {aranan}, sol yarıya geç")
            sag = orta - 1

    print(f"  ✗ Bulunamadı!")
    return -1

# Test
sirali_liste = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]

# Test 1: Var olan eleman
print("Test 1: Var olan eleman")
sonuc = binary_search(sirali_liste, 23)

# Test 2: Olmayan eleman
print("\n" + "=" * 50)
print("Test 2: Olmayan eleman")
sonuc = binary_search(sirali_liste, 30)

# Test 3: İlk eleman
print("\n" + "=" * 50)
print("Test 3: İlk eleman")
sonuc = binary_search(sirali_liste, 2)

# Test 4: Son eleman
print("\n" + "=" * 50)
print("Test 4: Son eleman")
sonuc = binary_search(sirali_liste, 78)

# Karşılaştırma: Linear search vs Binary search
print("\n" + "=" * 50)
print("Linear Search vs Binary Search Karşılaştırması:")
print("-" * 50)

# Büyük liste oluştur
buyuk_liste = list(range(0, 10000, 2))  # 0'dan 10000'e çift sayılar
aranan = 8888

# Linear search
print("Linear Search:")
linear_adim = 0
for i, sayi in enumerate(buyuk_liste):
    linear_adim += 1
    if sayi == aranan:
        print(f"  Bulundu! İndeks: {i}, Adım sayısı: {linear_adim}")
        break

# Binary search (adım sayısı için)
print("\nBinary Search:")
sol, sag = 0, len(buyuk_liste) - 1
binary_adim = 0

while sol <= sag:
    binary_adim += 1
    orta = (sol + sag) // 2
    if buyuk_liste[orta] == aranan:
        print(f"  Bulundu! İndeks: {orta}, Adım sayısı: {binary_adim}")
        break
    elif buyuk_liste[orta] < aranan:
        sol = orta + 1
    else:
        sag = orta - 1

print(f"\nPerformans Farkı:")
print(f"  Liste boyutu: {len(buyuk_liste)}")
print(f"  Linear search adım: {linear_adim}")
print(f"  Binary search adım: {binary_adim}")
print(f"  Verimlilik artışı: {linear_adim / binary_adim:.1f}x daha hızlı")

# AÇIKLAMA:
print("\n" + "=" * 50)
print("Açıklama:")
print("- Binary search sadece SIRALI listelerde çalışır")
print("- Her adımda liste yarıya indirilir (log n karmaşıklık)")
print("- Linear search: O(n), Binary search: O(log n)")
print("- Büyük listelerde binary search çok daha hızlıdır")
print("- orta = (sol + sag) // 2: Ortayı bulma formülü")


# =============================================================================
# SONUÇ VE ÖNERİLER
# =============================================================================
print("\n" + "=" * 70)
print("ALIŞTIRMALAR TAMAMLANDI!")
print("=" * 70)
print("""
Tebrikler! Kontrol yapıları alıştırmalarını tamamladınız.

Öğrendikleriniz:
✓ Koşullu ifadeler (if-elif-else)
✓ for ve while döngüleri
✓ break, continue, pass kullanımı
✓ İç içe döngüler
✓ List comprehensions
✓ Algoritmik düşünme

Sonraki Adımlar:
1. Bu alıştırmaları farklı değerlerle tekrar çalıştırın
2. Kendi sorularınızı oluşturun ve çözün
3. Gerçek dünya problemlerini çözmeye çalışın
4. Code challenges sitelerinde pratik yapın (HackerRank, LeetCode)

İpuçları:
- Kod yazmadan önce algoritmanızı kağıda çizin
- Karmaşık problemleri küçük parçalara bölün
- Kodunuzu test edin ve farklı senaryolar deneyin
- Hata mesajlarını okuyun ve anlayın
- Stack Overflow ve Python dokümantasyonunu kullanın

Başarılar! 🚀
""")
