# Python Sets (Kümeler)

## İçindekiler
1. [Set Nedir?](#set-nedir)
2. [Set Oluşturma](#set-oluşturma)
3. [Set Operasyonları](#set-operasyonları)
4. [Set Metodları](#set-metodları)
5. [Frozen Sets](#frozen-sets)
6. [Set Comprehensions](#set-comprehensions)
7. [Set Kullanım Senaryoları](#set-kullanım-senaryoları)

---

## Set Nedir?

**Set (Küme)**, Python'da sırasız, değiştirilebilir ve tekrarsız (unique) elemanlar içeren bir veri yapısıdır. Setler, matematiksel küme teorisine dayalı işlemler yapmak için idealdir.

### Set Özellikleri:
- **Sırasız (Unordered)**: Elemanların belirli bir sırası yoktur
- **Benzersiz Elemanlar (Unique)**: Aynı değer iki kez bulunamaz
- **Değiştirilebilir (Mutable)**: Eleman eklenip çıkarılabilir
- **Hashable Elemanlar**: Sadece hashable (değişmez) tipler içerebilir
- **Hızlı Üyelik Kontrolü**: O(1) zaman karmaşıklığı

---

## Set Oluşturma

### Örnek 1: Temel Set Oluşturma

```python
# Küme parantezleri {} ile set oluşturma
meyveler = {'elma', 'armut', 'muz', 'kiraz'}
print(f"Meyveler: {meyveler}")
print(f"Tip: {type(meyveler)}")

# set() fonksiyonu ile oluşturma
sayilar = set([1, 2, 3, 4, 5])
print(f"\nSayılar: {sayilar}")

# String'den set oluşturma (her karakter bir eleman)
harfler = set('python')
print(f"Harfler: {harfler}")

# Boş set oluşturma (DİKKAT: {} değil, set() kullanılmalı)
bos_set = set()  # Doğru
bos_dict = {}    # Bu bir dictionary'dir!
print(f"\nBoş set: {bos_set}, Tip: {type(bos_set)}")
print(f"Boş dict: {bos_dict}, Tip: {type(bos_dict)}")
```

**Çıktı:**
```
Meyveler: {'kiraz', 'muz', 'elma', 'armut'}
Tip: <class 'set'>

Sayılar: {1, 2, 3, 4, 5}
Harfler: {'h', 'o', 'n', 'p', 't', 'y'}

Boş set: set(), Tip: <class 'set'>
Boş dict: {}, Tip: <class 'dict'>
```

---

### Örnek 2: Tekrarlanan Elemanlar Otomatik Kaldırılır

```python
# Tekrarlı elemanlar otomatik olarak kaldırılır
sayilar = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"Set: {sayilar}")  # {1, 2, 3, 4}

# Liste içindeki tekrarları kaldırma
liste = [1, 2, 2, 3, 3, 3, 4, 4, 5]
benzersiz = list(set(liste))
print(f"Orijinal liste: {liste}")
print(f"Benzersiz elemanlar: {benzersiz}")

# String içindeki tekrarlı karakterleri kaldırma
kelime = "merhaba dünya"
benzersiz_karakterler = set(kelime)
print(f"\nKelime: '{kelime}'")
print(f"Benzersiz karakterler: {benzersiz_karakterler}")
print(f"Benzersiz karakter sayısı: {len(benzersiz_karakterler)}")
```

**Çıktı:**
```
Set: {1, 2, 3, 4}
Orijinal liste: [1, 2, 2, 3, 3, 3, 4, 4, 5]
Benzersiz elemanlar: [1, 2, 3, 4, 5]

Kelime: 'merhaba dünya'
Benzersiz karakterler: {' ', 'a', 'b', 'd', 'e', 'h', 'm', 'n', 'r', 'y', 'ü'}
Benzersiz karakter sayısı: 11
```

---

## Set Operasyonları

### Örnek 3: Union (Birleşim) - Tüm Elemanlar

```python
# Union: İki veya daha fazla setin birleşimi
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {5, 6, 7, 8}

# | operatörü ile birleşim
birlesim1 = set_a | set_b
print(f"A | B = {birlesim1}")

# union() metodu ile birleşim
birlesim2 = set_a.union(set_b)
print(f"A.union(B) = {birlesim2}")

# Çoklu set birleşimi
birlesim3 = set_a | set_b | set_c
print(f"A | B | C = {birlesim3}")

# Matematiksel gösterim
print(f"\nA = {set_a}")
print(f"B = {set_b}")
print(f"C = {set_c}")
print(f"A ∪ B ∪ C = {birlesim3}")
```

**Çıktı:**
```
A | B = {1, 2, 3, 4, 5, 6}
A.union(B) = {1, 2, 3, 4, 5, 6}
A | B | C = {1, 2, 3, 4, 5, 6, 7, 8}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {5, 6, 7, 8}
A ∪ B ∪ C = {1, 2, 3, 4, 5, 6, 7, 8}
```

---

### Örnek 4: Intersection (Kesişim) - Ortak Elemanlar

```python
# Intersection: İki setin ortak elemanları
frontend = {'JavaScript', 'HTML', 'CSS', 'TypeScript'}
backend = {'Python', 'JavaScript', 'Java', 'Go'}
mobile = {'Java', 'Swift', 'Kotlin', 'JavaScript'}

# & operatörü ile kesişim
ortak1 = frontend & backend
print(f"Frontend & Backend = {ortak1}")

# intersection() metodu ile kesişim
ortak2 = frontend.intersection(backend)
print(f"Frontend.intersection(Backend) = {ortak2}")

# Üç setin ortak elemanları
ortak3 = frontend & backend & mobile
print(f"Üç platformda da kullanılan: {ortak3}")

# İki setin kesişimi (farklı kombinasyonlar)
print(f"\nFrontend & Mobile = {frontend & mobile}")
print(f"Backend & Mobile = {backend & mobile}")
```

**Çıktı:**
```
Frontend & Backend = {'JavaScript'}
Frontend.intersection(Backend) = {'JavaScript'}
Üç platformda da kullanılan: {'JavaScript'}

Frontend & Mobile = {'JavaScript'}
Backend & Mobile = {'Java', 'JavaScript'}
```

---

### Örnek 5: Difference (Fark) - Farklı Elemanlar

```python
# Difference: Bir sette olup diğerinde olmayan elemanlar
python_bilenlere = {'Ali', 'Ayşe', 'Mehmet', 'Fatma', 'Can'}
java_bilenler = {'Ayşe', 'Mehmet', 'Zeynep', 'Ahmet'}

# - operatörü ile fark
sadece_python = python_bilenlere - java_bilenler
print(f"Sadece Python bilenler: {sadece_python}")

# difference() metodu ile fark
sadece_java = java_bilenler.difference(python_bilenlere)
print(f"Sadece Java bilenler: {sadece_java}")

# Her iki dilde uzman olanlar (kesişim)
her_ikisi = python_bilenlere & java_bilenler
print(f"Her iki dili de bilenler: {her_ikisi}")

# Toplam programcı sayısı (birleşim)
toplam = python_bilenlere | java_bilenler
print(f"Toplam programcı sayısı: {len(toplam)}")
print(f"Tüm programcılar: {toplam}")
```

**Çıktı:**
```
Sadece Python bilenler: {'Can', 'Ali', 'Fatma'}
Sadece Java bilenler: {'Zeynep', 'Ahmet'}
Her iki dili de bilenler: {'Mehmet', 'Ayşe'}
Toplam programcı sayısı: 7
Tüm programcılar: {'Ali', 'Ayşe', 'Mehmet', 'Fatma', 'Can', 'Zeynep', 'Ahmet'}
```

---

### Örnek 6: Symmetric Difference (Simetrik Fark)

```python
# Symmetric Difference: Her iki sette de olup ortak olmayan elemanlar
# (Birleşim - Kesişim)

online_kurs = {'Python', 'JavaScript', 'SQL', 'Git'}
okul_dersi = {'Java', 'C++', 'SQL', 'Veri Yapıları'}

# ^ operatörü ile simetrik fark
fark1 = online_kurs ^ okul_dersi
print(f"Simetrik fark (^): {fark1}")

# symmetric_difference() metodu ile
fark2 = online_kurs.symmetric_difference(okul_dersi)
print(f"Simetrik fark (metod): {fark2}")

# Manuel hesaplama (birleşim - kesişim)
birlesim = online_kurs | okul_dersi
kesisim = online_kurs & okul_dersi
manuel_fark = birlesim - kesisim
print(f"\nManuel hesaplama:")
print(f"Birleşim: {birlesim}")
print(f"Kesişim: {kesisim}")
print(f"Birleşim - Kesişim: {manuel_fark}")

# Alternatif: (A - B) | (B - A)
alternatif_fark = (online_kurs - okul_dersi) | (okul_dersi - online_kurs)
print(f"Alternatif hesaplama: {alternatif_fark}")
```

**Çıktı:**
```
Simetrik fark (^): {'Git', 'JavaScript', 'Python', 'C++', 'Veri Yapıları', 'Java'}
Simetrik fark (metod): {'Git', 'JavaScript', 'Python', 'C++', 'Veri Yapıları', 'Java'}

Manuel hesaplama:
Birleşim: {'Git', 'JavaScript', 'Python', 'SQL', 'C++', 'Veri Yapıları', 'Java'}
Kesişim: {'SQL'}
Birleşim - Kesişim: {'Git', 'JavaScript', 'Python', 'C++', 'Veri Yapıları', 'Java'}
Alternatif hesaplama: {'Git', 'JavaScript', 'Python', 'C++', 'Veri Yapıları', 'Java'}
```

---

## Set Metodları

### Örnek 7: Eleman Ekleme ve Çıkarma

```python
# add(): Tek eleman ekleme
meyveler = {'elma', 'armut'}
print(f"Başlangıç: {meyveler}")

meyveler.add('muz')
print(f"Muz eklendi: {meyveler}")

# Aynı elemanı tekrar eklemeye çalışma
meyveler.add('elma')  # Hiçbir değişiklik olmaz
print(f"Elma tekrar eklendi: {meyveler}")

# update(): Çoklu eleman ekleme (iterable gerekir)
meyveler.update(['kiraz', 'üzüm', 'portakal'])
print(f"Çoklu ekleme: {meyveler}")

# update() ile set birleştirme
diger_meyveler = {'kavun', 'karpuz'}
meyveler.update(diger_meyveler)
print(f"Set birleştirme: {meyveler}")

# remove(): Eleman çıkarma (yoksa hata verir)
meyveler.remove('muz')
print(f"\nMuz çıkarıldı: {meyveler}")

try:
    meyveler.remove('ananas')  # Hata verecek
except KeyError as e:
    print(f"Hata: {e} sette bulunamadı")

# discard(): Eleman çıkarma (yoksa hata vermez)
meyveler.discard('kiraz')
print(f"Kiraz çıkarıldı: {meyveler}")

meyveler.discard('ananas')  # Hata vermez
print(f"Olmayan eleman discard edildi: {meyveler}")

# pop(): Rastgele eleman çıkarma
cikarilan = meyveler.pop()
print(f"\nPop ile çıkarılan: {cikarilan}")
print(f"Kalan elemanlar: {meyveler}")

# clear(): Tüm elemanları temizleme
meyveler.clear()
print(f"Temizlendi: {meyveler}")
```

---

### Örnek 8: Set İlişki Kontrolleri

```python
# Alt küme ve üst küme kontrolleri

tum_sayilar = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
cift_sayilar = {2, 4, 6, 8, 10}
tek_sayilar = {1, 3, 5, 7, 9}
kucuk_sayilar = {1, 2, 3}

# issubset(): Alt küme kontrolü
print(f"Çift sayılar, tüm sayıların alt kümesi mi? {cift_sayilar.issubset(tum_sayilar)}")
print(f"Küçük sayılar <= Tüm sayılar? {kucuk_sayilar <= tum_sayilar}")

# issuperset(): Üst küme kontrolü
print(f"\nTüm sayılar, çift sayıların üst kümesi mi? {tum_sayilar.issuperset(cift_sayilar)}")
print(f"Tüm sayılar >= Tek sayılar? {tum_sayilar >= tek_sayilar}")

# isdisjoint(): Kesişimsiz mi? (hiç ortak eleman yok mu?)
print(f"\nÇift ve tek sayılar kesişimsiz mi? {cift_sayilar.isdisjoint(tek_sayilar)}")
print(f"Çift ve tüm sayılar kesişimsiz mi? {cift_sayilar.isdisjoint(tum_sayilar)}")

# Özel durumlar
print(f"\nBoş küme her kümenin alt kümesi: {set().issubset(tum_sayilar)}")
print(f"Her küme kendinin alt kümesi: {tum_sayilar.issubset(tum_sayilar)}")

# < ve > operatörleri (gerçek alt/üst küme - eşit olamaz)
print(f"\nÇift sayılar < Tüm sayılar (gerçek alt küme)? {cift_sayilar < tum_sayilar}")
print(f"Tüm sayılar < Tüm sayılar? {tum_sayilar < tum_sayilar}")  # False (eşitler)
```

**Çıktı:**
```
Çift sayılar, tüm sayıların alt kümesi mi? True
Küçük sayılar <= Tüm sayılar? True

Tüm sayılar, çift sayıların üst kümesi mi? True
Tüm sayılar >= Tek sayılar? True

Çift ve tek sayılar kesişimsiz mi? True
Çift ve tüm sayılar kesişimsiz mi? False

Boş küme her kümenin alt kümesi: True
Her küme kendinin alt kümesi: True

Çift sayılar < Tüm sayılar (gerçek alt küme)? True
Tüm sayılar < Tüm sayılar? False
```

---

### Örnek 9: In-place Set Operasyonları

```python
# In-place operasyonlar: Orijinal seti değiştirir

# update() veya |=: Birleşim (in-place)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"A: {set_a}, B: {set_b}")

set_a |= set_b  # set_a = set_a | set_b
print(f"A |= B sonrası A: {set_a}")

# intersection_update() veya &=: Kesişim (in-place)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"\nA: {set_a}, B: {set_b}")

set_a &= set_b  # set_a = set_a & set_b
print(f"A &= B sonrası A: {set_a}")

# difference_update() veya -=: Fark (in-place)
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5}
print(f"\nA: {set_a}, B: {set_b}")

set_a -= set_b  # set_a = set_a - set_b
print(f"A -= B sonrası A: {set_a}")

# symmetric_difference_update() veya ^=: Simetrik fark (in-place)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"\nA: {set_a}, B: {set_b}")

set_a ^= set_b  # set_a = set_a ^ set_b
print(f"A ^= B sonrası A: {set_a}")

# Karşılaştırma: Normal vs In-place
set_x = {1, 2, 3}
set_y = {3, 4, 5}

set_z = set_x | set_y  # Yeni set oluşturur
print(f"\nNormal: X | Y = {set_z}, X değişmedi: {set_x}")

set_x |= set_y  # Orijinal set_x'i değiştirir
print(f"In-place: X |= Y sonrası X: {set_x}")
```

---

## Frozen Sets

### Örnek 10: Frozenset - Değişmez Kümeler

```python
# frozenset: Değiştirilemez (immutable) set
# Hashable olduğu için set elemanı veya dictionary key'i olabilir

# Frozenset oluşturma
normal_set = {1, 2, 3, 4, 5}
frozen = frozenset([1, 2, 3, 4, 5])

print(f"Normal set: {normal_set}, Tip: {type(normal_set)}")
print(f"Frozenset: {frozen}, Tip: {type(frozen)}")

# Frozenset değiştirilemez
try:
    frozen.add(6)  # Hata verecek
except AttributeError as e:
    print(f"\nHata: Frozenset değiştirilemez - {e}")

# Frozenset'i set elemanı olarak kullanma
set_koleksiyonu = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6]),
    frozenset([7, 8, 9])
}
print(f"\nSet içinde frozenset'ler: {set_koleksiyonu}")

# Normal set'i set elemanı yapamazsınız
try:
    yanlis_kullanim = {{1, 2}, {3, 4}}  # Hata verecek
except TypeError as e:
    print(f"Hata: Normal set hashable değil - {e}")

# Frozenset'i dictionary key olarak kullanma
koordinatlar = {
    frozenset(['x', 'y']): (10, 20),
    frozenset(['lat', 'long']): (41.0082, 28.9784)
}
print(f"\nFrozenset key'li dictionary: {koordinatlar}")

# Frozenset operasyonları (yeni frozenset döner)
frozen_a = frozenset([1, 2, 3, 4])
frozen_b = frozenset([3, 4, 5, 6])

print(f"\nFrozen A: {frozen_a}")
print(f"Frozen B: {frozen_b}")
print(f"Birleşim: {frozen_a | frozen_b}")
print(f"Kesişim: {frozen_a & frozen_b}")
print(f"Fark: {frozen_a - frozen_b}")
```

---

## Set Comprehensions

### Örnek 11: Set Comprehension - Gelişmiş Set Oluşturma

```python
# Set comprehension: List comprehension'a benzer syntax

# Basit set comprehension
kareler = {x**2 for x in range(10)}
print(f"Kareler: {kareler}")

# Koşullu set comprehension
cift_kareler = {x**2 for x in range(10) if x % 2 == 0}
print(f"Çift sayıların kareleri: {cift_kareler}")

# String işlemleri ile set comprehension
kelimeler = ['Python', 'Java', 'JavaScript', 'C++', 'Go']
ilk_harfler = {kelime[0].upper() for kelime in kelimeler}
print(f"\nİlk harfler: {ilk_harfler}")

# Kelime uzunlukları
uzunluklar = {len(kelime) for kelime in kelimeler}
print(f"Kelime uzunlukları: {uzunluklar}")

# İç içe döngüler ile set comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tum_elemanlar = {eleman for satir in matrix for eleman in satir}
print(f"\nMatrix elemanları: {tum_elemanlar}")

# Karmaşık koşullar
sayilar = range(1, 51)
# 3'e veya 5'e bölünen sayılar
bolunebilen = {x for x in sayilar if x % 3 == 0 or x % 5 == 0}
print(f"\n3'e veya 5'e bölünen sayılar (1-50): {bolunebilen}")

# String manipulation
cumle = "Python ile veri yapıları öğreniyorum"
benzersiz_harfler = {harf.lower() for harf in cumle if harf.isalpha()}
print(f"\nCümledeki benzersiz harfler: {sorted(benzersiz_harfler)}")

# If-else ile set comprehension
sayilar = range(-5, 6)
mutlak_degerler = {abs(x) for x in sayilar}
print(f"\nMutlak değerler: {mutlak_degerler}")

# Çoklu koşullar
# 1-100 arası asal sayılar (basit kontrol)
asallar = {x for x in range(2, 100) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))}
print(f"\n1-100 arası asal sayılar: {asallar}")
print(f"Toplam asal sayı: {len(asallar)}")
```

---

### Örnek 12: Gerçek Dünya Uygulamaları

```python
# Set'lerin pratik kullanım örnekleri

# 1. Tekrarlı verileri temizleme
kullanici_girisler = [
    'user1@email.com', 'user2@email.com', 'user1@email.com',
    'user3@email.com', 'user2@email.com', 'user4@email.com'
]
benzersiz_kullanicilar = set(kullanici_girisler)
print(f"Toplam giriş: {len(kullanici_girisler)}")
print(f"Benzersiz kullanıcı: {len(benzersiz_kullanicilar)}")
print(f"Benzersiz kullanıcılar: {benzersiz_kullanicilar}")

# 2. Hızlı üyelik kontrolü
yasakli_kelimeler = {
    'spam', 'reklam', 'sahte', 'dolandırıcılık',
    'illegal', 'yasadışı', 'hack'
}

def mesaj_kontrol(mesaj):
    kelimeler = mesaj.lower().split()
    return any(kelime in yasakli_kelimeler for kelime in kelimeler)

mesaj1 = "Merhaba, nasılsın?"
mesaj2 = "Bu bir spam mesajıdır"
print(f"\nMesaj 1 yasak kelime içeriyor mu? {mesaj_kontrol(mesaj1)}")
print(f"Mesaj 2 yasak kelime içeriyor mu? {mesaj_kontrol(mesaj2)}")

# 3. İki liste arasındaki farklılıkları bulma
eski_urunler = ['laptop', 'mouse', 'keyboard', 'monitor', 'webcam']
yeni_urunler = ['laptop', 'mouse', 'keyboard', 'headset', 'microphone']

eklenen = set(yeni_urunler) - set(eski_urunler)
cikarilan = set(eski_urunler) - set(yeni_urunler)
degismeyen = set(eski_urunler) & set(yeni_urunler)

print(f"\nEklenen ürünler: {eklenen}")
print(f"Çıkarılan ürünler: {cikarilan}")
print(f"Değişmeyen ürünler: {degismeyen}")

# 4. Anagram kontrolü
def anagram_mi(kelime1, kelime2):
    return set(kelime1.lower()) == set(kelime2.lower()) and \
           sorted(kelime1.lower()) == sorted(kelime2.lower())

print(f"\n'listen' ve 'silent' anagram mı? {anagram_mi('listen', 'silent')}")
print(f"'python' ve 'java' anagram mı? {anagram_mi('python', 'java')}")

# 5. Ortak ilgi alanları bulma
kullanici_1_ilgiler = {'programlama', 'müzik', 'spor', 'seyahat', 'okuma'}
kullanici_2_ilgiler = {'müzik', 'sinema', 'spor', 'yemek', 'fotograf'}
kullanici_3_ilgiler = {'programlama', 'oyun', 'spor', 'müzik', 'teknoloji'}

# İki kullanıcının ortak ilgileri
ortak_12 = kullanici_1_ilgiler & kullanici_2_ilgiler
print(f"\nKullanıcı 1 ve 2'nin ortak ilgileri: {ortak_12}")

# Üç kullanıcının ortak ilgileri
ortak_hepsi = kullanici_1_ilgiler & kullanici_2_ilgiler & kullanici_3_ilgiler
print(f"Üç kullanıcının ortak ilgileri: {ortak_hepsi}")

# En az iki kullanıcıda olan ilgiler
en_az_iki = (kullanici_1_ilgiler & kullanici_2_ilgiler) | \
            (kullanici_1_ilgiler & kullanici_3_ilgiler) | \
            (kullanici_2_ilgiler & kullanici_3_ilgiler)
print(f"En az iki kullanıcıda olan ilgiler: {en_az_iki}")
```

---

### Örnek 13: Performans Karşılaştırması

```python
import time

# Set vs List performans karşılaştırması

# Büyük veri setleri oluşturma
liste_buyuk = list(range(100000))
set_buyuk = set(range(100000))

# Üyelik kontrolü performansı
aranan = 99999

# Liste ile arama (O(n))
start = time.time()
sonuc = aranan in liste_buyuk
liste_sure = time.time() - start

# Set ile arama (O(1))
start = time.time()
sonuc = aranan in set_buyuk
set_sure = time.time() - start

print(f"Liste arama süresi: {liste_sure:.6f} saniye")
print(f"Set arama süresi: {set_sure:.6f} saniye")
print(f"Set, listeden {liste_sure/set_sure:.2f} kat daha hızlı")

# Tekrar eden elemanları kaldırma
tekrarli_liste = [i % 1000 for i in range(10000)]

# Liste yöntemi
start = time.time()
benzersiz_liste = []
for item in tekrarli_liste:
    if item not in benzersiz_liste:
        benzersiz_liste.append(item)
liste_temizleme_sure = time.time() - start

# Set yöntemi
start = time.time()
benzersiz_set = list(set(tekrarli_liste))
set_temizleme_sure = time.time() - start

print(f"\nListe ile tekrar temizleme: {liste_temizleme_sure:.6f} saniye")
print(f"Set ile tekrar temizleme: {set_temizleme_sure:.6f} saniye")
print(f"Set yöntemi {liste_temizleme_sure/set_temizleme_sure:.2f} kat daha hızlı")

# Bellek kullanımı
import sys
liste_sample = list(range(10000))
set_sample = set(range(10000))

print(f"\nListe bellek kullanımı: {sys.getsizeof(liste_sample)} byte")
print(f"Set bellek kullanımı: {sys.getsizeof(set_sample)} byte")
```

---

### Örnek 14: Gelişmiş Set Kullanımları

```python
# Gelişmiş set teknikleri ve püf noktaları

# 1. Çoklu set operasyonları
sets = [
    {1, 2, 3, 4},
    {3, 4, 5, 6},
    {5, 6, 7, 8},
    {7, 8, 9, 10}
]

# Tüm setlerin birleşimi
tum_birlesim = set.union(*sets)
print(f"Tüm setlerin birleşimi: {tum_birlesim}")

# Tüm setlerin kesişimi
tum_kesisim = set.intersection(*sets)
print(f"Tüm setlerin kesişimi: {tum_kesisim}")

# 2. Set ile veri filtreleme
sayilar = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
filtrelenen = {x for x in sayilar if x > 5}
print(f"\n5'ten büyük sayılar: {filtrelenen}")

# 3. Set ile veri dönüşümü
kelimeler = {'python', 'java', 'javascript', 'go'}
buyuk_harfler = {kelime.upper() for kelime in kelimeler}
print(f"Büyük harfler: {buyuk_harfler}")

# 4. İç içe set operasyonları
kategoriler = {
    'backend': {'Python', 'Java', 'Go', 'Node.js'},
    'frontend': {'JavaScript', 'TypeScript', 'React', 'Vue'},
    'mobile': {'Java', 'Kotlin', 'Swift', 'React Native'},
    'data_science': {'Python', 'R', 'SQL', 'Julia'}
}

# Her yerde kullanılan teknolojiler
tum_teknolojiler = set.union(*kategoriler.values())
print(f"\nTüm teknolojiler: {tum_teknolojiler}")

# Python kullanan alanlar
python_alanlari = {alan for alan, tekno in kategoriler.items() if 'Python' in tekno}
print(f"Python kullanan alanlar: {python_alanlari}")

# Birden fazla alanda kullanılan teknolojiler
tekno_sayac = {}
for teknolojiler in kategoriler.values():
    for tekno in teknolojiler:
        tekno_sayac[tekno] = tekno_sayac.get(tekno, 0) + 1

cok_kullanilanlar = {tekno for tekno, sayi in tekno_sayac.items() if sayi > 1}
print(f"Birden fazla alanda kullanılan: {cok_kullanilanlar}")

# 5. Set ile graph algoritmaları (basit örnek)
# Komşuluk listesi ile graf
graf = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def komsular_bul(dugum):
    return graf.get(dugum, set())

def ikinci_derece_komsular(dugum):
    """Bir düğümün komşularının komşularını bulur"""
    birinci_derece = komsular_bul(dugum)
    ikinci_derece = set()
    for komsu in birinci_derece:
        ikinci_derece.update(komsular_bul(komsu))
    # Kendisini ve direkt komşuları çıkar
    ikinci_derece -= {dugum}
    ikinci_derece -= birinci_derece
    return ikinci_derece

print(f"\nA'nın komşuları: {komsular_bul('A')}")
print(f"A'nın ikinci derece komşuları: {ikinci_derece_komsular('A')}")
```

---

### Örnek 15: Set ile Veri Analizi

```python
# Gerçek veri analizi senaryoları

# Veri seti: E-ticaret müşteri analizi
ocak_musteriler = {'M001', 'M002', 'M003', 'M004', 'M005', 'M006'}
subat_musteriler = {'M003', 'M004', 'M007', 'M008', 'M009'}
mart_musteriler = {'M001', 'M004', 'M005', 'M010', 'M011', 'M012'}

# 1. Sadık müşteriler (her ay alışveriş yapan)
sadik_musteriler = ocak_musteriler & subat_musteriler & mart_musteriler
print(f"Sadık müşteriler (3 ayda da alışveriş): {sadik_musteriler}")

# 2. Churn analizi (kayıp müşteriler)
ocak_subat_aktif = ocak_musteriler & subat_musteriler
subat_churn = ocak_subat_aktif - mart_musteriler
print(f"Şubat'ta kayıp müşteriler: {subat_churn}")

# 3. Yeni müşteri kazanımı
yeni_subat = subat_musteriler - ocak_musteriler
yeni_mart = mart_musteriler - (ocak_musteriler | subat_musteriler)
print(f"Şubat'ta yeni müşteriler: {yeni_subat}")
print(f"Mart'ta yeni müşteriler: {yeni_mart}")

# 4. Toplam benzersiz müşteri sayısı
toplam_benzersiz = ocak_musteriler | subat_musteriler | mart_musteriler
print(f"\nÇeyrek toplam müşteri: {len(toplam_benzersiz)}")

# 5. Müşteri segmentasyonu
tek_ay = (ocak_musteriler | subat_musteriler | mart_musteriler) - \
         (ocak_musteriler & subat_musteriler) - \
         (subat_musteriler & mart_musteriler) - \
         (ocak_musteriler & mart_musteriler)
iki_ay = (ocak_musteriler & subat_musteriler) | \
         (subat_musteriler & mart_musteriler) | \
         (ocak_musteriler & mart_musteriler) - sadik_musteriler
uc_ay = sadik_musteriler

print(f"\nMüşteri Segmentasyonu:")
print(f"Tek ay alışveriş yapan: {len(tek_ay)} müşteri")
print(f"İki ay alışveriş yapan: {len(iki_ay)} müşteri")
print(f"Üç ay alışveriş yapan: {len(uc_ay)} müşteri")

# 6. Retention rate (elde tutma oranı)
ocak_subat_retention = len(ocak_musteriler & subat_musteriler) / len(ocak_musteriler) * 100
subat_mart_retention = len(subat_musteriler & mart_musteriler) / len(subat_musteriler) * 100

print(f"\nOcak-Şubat retention: {ocak_subat_retention:.1f}%")
print(f"Şubat-Mart retention: {subat_mart_retention:.1f}%")

# 7. Ürün kategorisi analizi
kategori_elektronik = {'M001', 'M003', 'M007', 'M010'}
kategori_giyim = {'M002', 'M004', 'M008', 'M011'}
kategori_ev = {'M005', 'M006', 'M009', 'M012'}

# Sadık müşterilerin ilgi alanları
sadik_elektronik = sadik_musteriler & kategori_elektronik
sadik_giyim = sadik_musteriler & kategori_giyim
sadik_ev = sadik_musteriler & kategori_ev

print(f"\nSadık müşterilerin ilgi alanları:")
print(f"Elektronik: {len(sadik_elektronik)} müşteri")
print(f"Giyim: {len(sadik_giyim)} müşteri")
print(f"Ev: {len(sadik_ev)} müşteri")

# 8. Cross-selling fırsatları
# Hem elektronik hem giyim alan müşteriler
cross_sell_target = kategori_elektronik & kategori_giyim
print(f"\nCross-sell hedef müşteriler (elektronik + giyim): {cross_sell_target}")
```

---

## Özet

### Set Özellikleri
- ✓ Sırasız, benzersiz elemanlar
- ✓ O(1) üyelik kontrolü
- ✓ Matematiksel küme operasyonları
- ✓ Hashable tipler içerebilir
- ✗ İndeksleme yapılamaz
- ✗ Değiştirilebilir (mutable)

### Kullanım Alanları
- Tekrarlı verileri temizleme
- Hızlı üyelik kontrolü
- Küme teorisi operasyonları
- Veri analizi ve karşılaştırma
- Performans kritik uygulamalar

### Set vs List vs Tuple
| Özellik | Set | List | Tuple |
|---------|-----|------|-------|
| Sıralı | ✗ | ✓ | ✓ |
| Değiştirilebilir | ✓ | ✓ | ✗ |
| Tekrarlı eleman | ✗ | ✓ | ✓ |
| İndeksleme | ✗ | ✓ | ✓ |
| Üyelik kontrolü | O(1) | O(n) | O(n) |
| Kullanım | Benzersiz veri | Genel liste | Sabit veri |

---

## Kaynaklar ve İleri Okuma
- [Python Resmi Dokümantasyon - Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python Set Methods](https://docs.python.org/3/library/stdtypes.html#set)
- [frozenset Documentation](https://docs.python.org/3/library/stdtypes.html#frozenset)
- [Time Complexity](https://wiki.python.org/moin/TimeComplexity)
