# Kontrol Yapıları (Control Structures)

## İçindekiler
1. [Giriş](#giriş)
2. [Koşullu İfadeler](#koşullu-ifadeler)
3. [Döngüler](#döngüler)
4. [Döngü Kontrol İfadeleri](#döngü-kontrol-i̇fadeleri)
5. [İç İçe Döngüler](#iç-iç-döngüler)
6. [List Comprehensions](#list-comprehensions)
7. [En İyi Pratikler](#en-i̇yi-pratikler)

---

## Giriş

Kontrol yapıları, programın akışını kontrol etmemizi sağlayan temel programlama yapılarıdır. Python'da kontrol yapıları, koşullara göre farklı kod bloklarını çalıştırmamıza veya belirli işlemleri tekrar etmemize olanak tanır.

Python'daki ana kontrol yapıları:
- **Koşullu İfadeler**: if, elif, else
- **Döngüler**: for, while
- **Döngü Kontrolleri**: break, continue, pass
- **List Comprehensions**: Özet liste oluşturma yapıları

---

## Koşullu İfadeler

Koşullu ifadeler, belirli koşullara göre farklı kod bloklarının çalıştırılmasını sağlar.

### if İfadesi

`if` ifadesi, bir koşul doğru olduğunda belirli bir kod bloğunu çalıştırır.

```python
# Örnek 1: Basit if kullanımı
yas = 18

if yas >= 18:
    print("Reşitsiniz")
    print("Ehliyet alabilirsiniz")
```

**Çıktı:**
```
Reşitsiniz
Ehliyet alabilirsiniz
```

**Not:** Python'da kod blokları girinti (indentation) ile belirlenir. Genellikle 4 boşluk kullanılır.

### if-else İfadesi

`else` ifadesi, `if` koşulu yanlış olduğunda çalışacak alternatif bir kod bloğu sağlar.

```python
# Örnek 2: if-else kullanımı
sayi = -5

if sayi >= 0:
    print("Sayı pozitif veya sıfır")
else:
    print("Sayı negatif")
```

**Çıktı:**
```
Sayı negatif
```

### if-elif-else İfadesi

`elif` (else if), birden fazla koşulu test etmemizi sağlar.

```python
# Örnek 3: if-elif-else kullanımı
not_ortalamasi = 85

if not_ortalamasi >= 90:
    harf_notu = "A"
elif not_ortalamasi >= 80:
    harf_notu = "B"
elif not_ortalamasi >= 70:
    harf_notu = "C"
elif not_ortalamasi >= 60:
    harf_notu = "D"
else:
    harf_notu = "F"

print(f"Harf notunuz: {harf_notu}")
```

**Çıktı:**
```
Harf notunuz: B
```

### İç İçe Koşullar

Koşul ifadeleri içinde başka koşul ifadeleri kullanabiliriz.

```python
# Örnek 4: İç içe if kullanımı
yas = 25
ehliyet_var = True

if yas >= 18:
    if ehliyet_var:
        print("Araç kiralayabilirsiniz")
    else:
        print("Önce ehliyet almanız gerekiyor")
else:
    print("18 yaşından küçükler araç kiralayamaz")
```

**Çıktı:**
```
Araç kiralayabilirsiniz
```

### Mantıksal Operatörlerle Koşullar

`and`, `or`, `not` operatörleri ile karmaşık koşullar oluşturabiliriz.

```python
# Örnek 5: Mantıksal operatörler
kullanici_adi = "admin"
sifre = "12345"

if kullanici_adi == "admin" and sifre == "12345":
    print("Giriş başarılı")
else:
    print("Kullanıcı adı veya şifre hatalı")
```

**Çıktı:**
```
Giriş başarılı
```

### Ternary (Üçlü) Koşul Operatörü

Tek satırda basit koşullu atamalar yapabiliriz.

```python
# Örnek 6: Ternary operatör
yas = 20
durum = "Reşit" if yas >= 18 else "Reşit değil"
print(durum)

# Klasik if-else ile karşılaştırma:
# if yas >= 18:
#     durum = "Reşit"
# else:
#     durum = "Reşit değil"
```

**Çıktı:**
```
Reşit
```

---

## Döngüler

Döngüler, belirli kod bloklarını tekrar tekrar çalıştırmamızı sağlar.

### for Döngüsü

`for` döngüsü, bir dizi üzerinde iterasyon yapmak için kullanılır.

#### Liste ile for Döngüsü

```python
# Örnek 7: Liste üzerinde döngü
meyveler = ["elma", "armut", "muz", "kiraz"]

for meyve in meyveler:
    print(f"Meyve: {meyve}")
```

**Çıktı:**
```
Meyve: elma
Meyve: armut
Meyve: muz
Meyve: kiraz
```

#### range() ile for Döngüsü

`range()` fonksiyonu sayı dizileri oluşturur.

```python
# Örnek 8: range() kullanımı
# range(5) -> 0, 1, 2, 3, 4 sayılarını üretir

for i in range(5):
    print(f"Sayı: {i}")

print("\n--- Başlangıç ve bitiş belirtme ---")
# range(2, 6) -> 2, 3, 4, 5
for i in range(2, 6):
    print(f"Sayı: {i}")

print("\n--- Adım değeri belirtme ---")
# range(0, 10, 2) -> 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(f"Çift sayı: {i}")
```

**Çıktı:**
```
Sayı: 0
Sayı: 1
Sayı: 2
Sayı: 3
Sayı: 4

--- Başlangıç ve bitiş belirtme ---
Sayı: 2
Sayı: 3
Sayı: 4
Sayı: 5

--- Adım değeri belirtme ---
Çift sayı: 0
Çift sayı: 2
Çift sayı: 4
Çift sayı: 6
Çift sayı: 8
```

#### enumerate() ile for Döngüsü

`enumerate()` hem indeks hem de değeri döndürür.

```python
# Örnek 9: enumerate() kullanımı
renkler = ["kırmızı", "yeşil", "mavi"]

for indeks, renk in enumerate(renkler):
    print(f"İndeks {indeks}: {renk}")

print("\n--- Başlangıç indeksi belirtme ---")
for indeks, renk in enumerate(renkler, start=1):
    print(f"{indeks}. renk: {renk}")
```

**Çıktı:**
```
İndeks 0: kırmızı
İndeks 1: yeşil
İndeks 2: mavi

--- Başlangıç indeksi belirtme ---
1. renk: kırmızı
2. renk: yeşil
3. renk: mavi
```

### while Döngüsü

`while` döngüsü, bir koşul doğru olduğu sürece çalışmaya devam eder.

```python
# Örnek 10: Basit while döngüsü
sayac = 0

while sayac < 5:
    print(f"Sayaç: {sayac}")
    sayac += 1

print("Döngü bitti")
```

**Çıktı:**
```
Sayaç: 0
Sayaç: 1
Sayaç: 2
Sayaç: 3
Sayaç: 4
Döngü bitti
```

#### Kullanıcı Girişi ile while Döngüsü

```python
# Örnek 11: Kullanıcı girişi kontrolü
# Not: Bu örnek interaktif çalıştırıldığında işe yarar
# Otomatik gösterim için sabit değer kullanıyoruz

toplam = 0
sayac = 0

while sayac < 3:
    # Gerçek uygulamada: sayi = int(input("Bir sayı girin: "))
    sayi = sayac * 10  # Demo için sabit değer
    toplam += sayi
    sayac += 1

print(f"Toplam: {toplam}")
```

**Çıktı:**
```
Toplam: 30
```

---

## Döngü Kontrol İfadeleri

Döngü kontrol ifadeleri, döngülerin akışını değiştirmemize olanak tanır.

### break İfadesi

`break` ifadesi döngüyü tamamen sonlandırır.

```python
# Örnek 12: break kullanımı
for i in range(10):
    if i == 5:
        print("5'e ulaşıldı, döngü durduruluyor")
        break
    print(f"Sayı: {i}")

print("\n--- Arama örneği ---")
# Listede değer arama
sayilar = [3, 7, 12, 18, 21, 25]
aranan = 18

for sayi in sayilar:
    if sayi == aranan:
        print(f"{aranan} bulundu!")
        break
else:
    # Döngü break ile sonlanmadıysa else bloğu çalışır
    print(f"{aranan} bulunamadı!")
```

**Çıktı:**
```
Sayı: 0
Sayı: 1
Sayı: 2
Sayı: 3
Sayı: 4
5'e ulaşıldı, döngü durduruluyor

--- Arama örneği ---
18 bulundu!
```

### continue İfadesi

`continue` ifadesi döngünün mevcut iterasyonunu atlar ve bir sonraki iterasyona geçer.

```python
# Örnek 13: continue kullanımı
print("Tek sayıları atlama:")
for i in range(10):
    if i % 2 != 0:  # Tek sayı ise
        continue
    print(f"Çift sayı: {i}")

print("\n--- Negatif sayıları atlama ---")
sayilar = [5, -3, 8, -1, 12, -7, 15]
pozitif_toplam = 0

for sayi in sayilar:
    if sayi < 0:
        continue
    pozitif_toplam += sayi

print(f"Pozitif sayıların toplamı: {pozitif_toplam}")
```

**Çıktı:**
```
Tek sayıları atlama:
Çift sayı: 0
Çift sayı: 2
Çift sayı: 4
Çift sayı: 6
Çift sayı: 8

--- Negatif sayıları atlama ---
Pozitif sayıların toplamı: 40
```

### pass İfadesi

`pass` ifadesi hiçbir şey yapmaz. Genellikle yer tutucu olarak kullanılır.

```python
# Örnek 14: pass kullanımı
for i in range(5):
    if i == 2:
        pass  # Daha sonra kod eklenecek
    else:
        print(f"Sayı: {i}")

# Fonksiyon yer tutucusu olarak
def henuz_tamamlanmadi():
    pass  # TODO: Bu fonksiyonu tamamla

# Sınıf yer tutucusu olarak
class BosClass:
    pass  # Boş sınıf tanımı
```

**Çıktı:**
```
Sayı: 0
Sayı: 1
Sayı: 3
Sayı: 4
```

---

## İç İçe Döngüler

Bir döngü içinde başka bir döngü kullanabiliriz.

```python
# Örnek 15: İç içe for döngüleri - Çarpım tablosu
print("Çarpım Tablosu (5x5):")
print("-" * 40)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end=" ")
    print()  # Satır sonu

print("\n--- Matris oluşturma ---")
satir = 3
sutun = 4

for i in range(satir):
    for j in range(sutun):
        print(f"[{i},{j}]", end=" ")
    print()
```

**Çıktı:**
```
Çarpım Tablosu (5x5):
----------------------------------------
  1   2   3   4   5
  2   4   6   8  10
  3   6   9  12  15
  4   8  12  16  20
  5  10  15  20  25

--- Matris oluşturma ---
[0,0] [0,1] [0,2] [0,3]
[1,0] [1,1] [1,2] [1,3]
[2,0] [2,1] [2,2] [2,3]
```

### İç İçe Döngülerde break ve continue

```python
# Örnek 16: İç içe döngülerde kontrol ifadeleri
print("İç içe döngülerde break:")
for i in range(3):
    print(f"Dış döngü: {i}")
    for j in range(3):
        if j == 2:
            break  # Sadece iç döngüyü sonlandırır
        print(f"  İç döngü: {j}")

print("\n--- continue kullanımı ---")
for i in range(3):
    for j in range(5):
        if j % 2 == 0:
            continue
        print(f"[{i},{j}]", end=" ")
    print()
```

**Çıktı:**
```
İç içe döngülerde break:
Dış döngü: 0
  İç döngü: 0
  İç döngü: 1
Dış döngü: 1
  İç döngü: 0
  İç döngü: 1
Dış döngü: 2
  İç döngü: 0
  İç döngü: 1

--- continue kullanımı ---
[0,1] [0,3]
[1,1] [1,3]
[2,1] [2,3]
```

---

## List Comprehensions

List comprehensions, listeler oluşturmanın kısa ve okunabilir bir yoludur.

### Basit List Comprehension

```python
# Örnek 17: List comprehension temelleri
# Klasik yöntem
kareler_klasik = []
for i in range(10):
    kareler_klasik.append(i ** 2)

# List comprehension ile
kareler = [i ** 2 for i in range(10)]
print("Kareler:", kareler)

# String işlemleri
isimler = ["ahmet", "mehmet", "ayşe", "fatma"]
buyuk_harfli = [isim.upper() for isim in isimler]
print("Büyük harfli:", buyuk_harfli)
```

**Çıktı:**
```
Kareler: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Büyük harfli: ['AHMET', 'MEHMET', 'AYŞE', 'FATMA']
```

### Koşullu List Comprehension

```python
# Örnek 18: Koşul içeren list comprehension
# Çift sayıları filtreleme
sayilar = range(20)
cift_sayilar = [x for x in sayilar if x % 2 == 0]
print("Çift sayılar:", cift_sayilar)

# Tek sayıların kareleri
tek_kareler = [x ** 2 for x in range(10) if x % 2 != 0]
print("Tek sayıların kareleri:", tek_kareler)

# String filtreleme
kelimeler = ["python", "java", "c++", "javascript", "ruby"]
uzun_kelimeler = [kelime for kelime in kelimeler if len(kelime) > 4]
print("Uzun kelimeler:", uzun_kelimeler)
```

**Çıktı:**
```
Çift sayılar: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
Tek sayıların kareleri: [1, 9, 25, 49, 81]
Uzun kelimeler: ['python', 'javascript']
```

### if-else ile List Comprehension

```python
# Örnek 19: if-else içeren list comprehension
# Çift sayılar için "çift", tek sayılar için "tek"
sayilar = range(10)
etiketler = ["çift" if x % 2 == 0 else "tek" for x in sayilar]
print("Etiketler:", etiketler)

# Pozitif sayıları koruma, negatif sayıları sıfırlama
sayilar = [5, -3, 8, -1, 12, -7, 15]
pozitif_veya_sifir = [x if x > 0 else 0 for x in sayilar]
print("Pozitif veya sıfır:", pozitif_veya_sifir)
```

**Çıktı:**
```
Etiketler: ['çift', 'tek', 'çift', 'tek', 'çift', 'tek', 'çift', 'tek', 'çift', 'tek']
Pozitif veya sıfır: [5, 0, 8, 0, 12, 0, 15]
```

### İç İçe List Comprehension

```python
# Örnek 20: İç içe list comprehension
# 3x3 matris oluşturma
matris = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Matris:")
for satir in matris:
    print(satir)

# Düz liste haline getirme (flattening)
liste_listesi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
duz_liste = [eleman for alt_liste in liste_listesi for eleman in alt_liste]
print("\nDüzleştirilmiş liste:", duz_liste)

# Kombinasyonlar
harfler = ['A', 'B', 'C']
sayilar = [1, 2, 3]
kombinasyonlar = [harf + str(sayi) for harf in harfler for sayi in sayilar]
print("Kombinasyonlar:", kombinasyonlar)
```

**Çıktı:**
```
Matris:
[1, 2, 3]
[2, 4, 6]
[3, 6, 9]

Düzleştirilmiş liste: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Kombinasyonlar: ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
```

---

## En İyi Pratikler

### 1. Okunabilirlik Önceliklidir

```python
# Kötü: Karmaşık tek satır
sonuc = [x**2 for x in range(100) if x % 2 == 0 if x % 3 == 0 if x > 10]

# İyi: Okunabilir kod
sonuc = []
for x in range(100):
    if x > 10 and x % 2 == 0 and x % 3 == 0:
        sonuc.append(x ** 2)
```

### 2. Uygun Döngü Türünü Seçin

```python
# Liste üzerinde iterasyon için for kullanın
meyveler = ["elma", "armut", "muz"]
for meyve in meyveler:
    print(meyve)

# Koşul tabanlı tekrar için while kullanın
devam = True
while devam:
    # İşlemler...
    devam = False  # Koşul değiştiğinde döngü biter
```

### 3. Sonsuz Döngülerden Kaçının

```python
# Dikkat: Sonsuz döngü riski
# while True:
#     print("Sonsuz döngü")  # Hiç bitmez!

# İyi: Çıkış koşulu olan döngü
sayac = 0
while True:
    if sayac >= 5:
        break
    print(f"İterasyon: {sayac}")
    sayac += 1
```

### 4. enumerate() ve zip() Kullanın

```python
# Kötü: Manuel indeks yönetimi
isimler = ["Ali", "Veli", "Ayşe"]
for i in range(len(isimler)):
    print(f"{i}: {isimler[i]}")

# İyi: enumerate() kullanımı
for i, isim in enumerate(isimler):
    print(f"{i}: {isim}")

# zip() ile paralel iterasyon
isimler = ["Ali", "Veli", "Ayşe"]
yaslar = [25, 30, 28]
for isim, yas in zip(isimler, yaslar):
    print(f"{isim}: {yas} yaşında")
```

### 5. else Bloğunu Akıllıca Kullanın

```python
# for-else ve while-else
# else bloğu, döngü normal şekilde biterse (break olmadan) çalışır

sayilar = [2, 4, 6, 8, 10]
aranan = 5

for sayi in sayilar:
    if sayi == aranan:
        print(f"{aranan} bulundu!")
        break
else:
    print(f"{aranan} listede yok")
```

---

## Özet

Bu bölümde Python'daki kontrol yapılarını detaylı olarak inceledik:

- **if/elif/else**: Koşullu kod yürütme
- **for döngüsü**: Diziler üzerinde iterasyon
- **while döngüsü**: Koşul tabanlı tekrar
- **break**: Döngüyü sonlandırma
- **continue**: İterasyonu atlama
- **pass**: Yer tutucu ifade
- **İç içe döngüler**: Çok boyutlu işlemler
- **List comprehensions**: Özet liste oluşturma

Kontrol yapıları, programlama mantığının temelidir ve hemen hemen her programda kullanılır. Bu yapıları iyi anlamak, daha karmaşık programlar yazabilmeniz için kritik öneme sahiptir.

---

## Alıştırma Önerileri

1. Farklı koşul kombinasyonları deneyin
2. İç içe döngülerle desenler oluşturun
3. List comprehension'ları klasik döngülerle karşılaştırın
4. break ve continue'nun farklarını pratik edin
5. Gerçek dünya problemlerini kontrol yapılarıyla çözün

**Sonraki Adım:** `exercises.py` dosyasındaki alıştırmaları çözerek öğrendiklerinizi pekiştirin!
