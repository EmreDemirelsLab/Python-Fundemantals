# Python Listeleri (Lists)

## Giris

Liste, Python'da en cok kullanilan veri yapilarindan biridir. Listeler, birden fazla ogeden olusan, siralı ve degistirilebilir (mutable) veri yapilaridir. Listeler koseli parantezler `[]` ile tanimlanir ve her turlu veri tipini icinde barindirabilir.

## Liste Olusturma

### 1. Bos Liste Olusturma

```python
# Bos liste olusturmanin iki yolu
bos_liste = []
bos_liste2 = list()

print(bos_liste)      # []
print(type(bos_liste)) # <class 'list'>
```

### 2. Elemanli Liste Olusturma

```python
# Farkli veri tipleriyle liste olusturma
sayilar = [1, 2, 3, 4, 5]
isimler = ["Ali", "Ayse", "Mehmet", "Zeynep"]
karisik = [1, "iki", 3.0, True, None]

print(sayilar)    # [1, 2, 3, 4, 5]
print(isimler)    # ['Ali', 'Ayse', 'Mehmet', 'Zeynep']
print(karisik)    # [1, 'iki', 3.0, True, None]
```

### 3. Range ile Liste Olusturma

```python
# range() fonksiyonu ile liste olusturma
rakamlar = list(range(10))
print(rakamlar)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cift_sayilar = list(range(0, 20, 2))
print(cift_sayilar)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## Liste Indeksleme (Indexing)

Listelerdeki elemanlara erisimde indeks kullanilir. Python'da indeksler 0'dan baslar.

```python
meyveler = ["elma", "armut", "muz", "cilek", "kiraz"]

# Pozitif indeksleme (bastan baslar)
print(meyveler[0])   # elma
print(meyveler[2])   # muz
print(meyveler[4])   # kiraz

# Negatif indeksleme (sondan baslar)
print(meyveler[-1])  # kiraz (son eleman)
print(meyveler[-2])  # cilek (sondan ikinci)
print(meyveler[-5])  # elma (bastan birinci)
```

## Liste Dilimleme (Slicing)

Slice islemleri ile listenin bir bolumuunu alabiliriz.

### Temel Slicing

```python
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Syntax: liste[baslangic:bitis:adim]
print(sayilar[2:7])      # [2, 3, 4, 5, 6]
print(sayilar[:5])       # [0, 1, 2, 3, 4] (bastan 5'e kadar)
print(sayilar[5:])       # [5, 6, 7, 8, 9] (5'ten sona kadar)
print(sayilar[::2])      # [0, 2, 4, 6, 8] (2'ser atlayarak)
print(sayilar[1::2])     # [1, 3, 5, 7, 9] (tek sayilar)
print(sayilar[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (ters cevirme)
```

### Ileri Seviye Slicing

```python
harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Negatif indeks ile slicing
print(harfler[-5:-2])    # ['d', 'e', 'f']
print(harfler[-3:])      # ['f', 'g', 'h']
print(harfler[:-3])      # ['a', 'b', 'c', 'd', 'e']

# Ters siralamayla belirli bolum alma
print(harfler[6:2:-1])   # ['g', 'f', 'e', 'd']
```

## Liste Metodlari

### 1. append() - Liste Sonuna Eleman Ekleme

```python
sehirler = ["Istanbul", "Ankara", "Izmir"]
sehirler.append("Bursa")
print(sehirler)  # ['Istanbul', 'Ankara', 'Izmir', 'Bursa']

# Farkli tip ekleme
sayilar = [1, 2, 3]
sayilar.append([4, 5])
print(sayilar)  # [1, 2, 3, [4, 5]] (liste icinde liste)
```

### 2. extend() - Liste Sonuna Baska Liste Ekleme

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste1.extend(liste2)
print(liste1)  # [1, 2, 3, 4, 5, 6]

# String ile extend
harfler = ['a', 'b']
harfler.extend('cd')
print(harfler)  # ['a', 'b', 'c', 'd']
```

### 3. insert() - Belirli Konuma Eleman Ekleme

```python
meyveler = ["elma", "armut", "muz"]
meyveler.insert(1, "cilek")  # 1. indekse ekle
print(meyveler)  # ['elma', 'cilek', 'armut', 'muz']

# Basina ekleme
meyveler.insert(0, "kavun")
print(meyveler)  # ['kavun', 'elma', 'cilek', 'armut', 'muz']
```

### 4. remove() - Belirli Elemani Silme

```python
renkler = ["kirmizi", "mavi", "yesil", "sari", "mavi"]
renkler.remove("mavi")  # Ilk bulduğu "mavi"yi siler
print(renkler)  # ['kirmizi', 'yesil', 'sari', 'mavi']

# Olmayan eleman silinmeye calisilirsa hata verir
try:
    renkler.remove("mor")
except ValueError as e:
    print(f"Hata: {e}")  # Hata: list.remove(x): x not in list
```

### 5. pop() - Indekse Gore Eleman Silme ve Dondurme

```python
sayilar = [10, 20, 30, 40, 50]

# Son elemani sil ve dondur
son_eleman = sayilar.pop()
print(son_eleman)  # 50
print(sayilar)     # [10, 20, 30, 40]

# Belirli indeksteki elemani sil ve dondur
ikinci_eleman = sayilar.pop(1)
print(ikinci_eleman)  # 20
print(sayilar)        # [10, 30, 40]
```

### 6. clear() - Tum Elemanlari Silme

```python
liste = [1, 2, 3, 4, 5]
liste.clear()
print(liste)  # []
```

### 7. index() - Elemanin Indeksini Bulma

```python
meyveler = ["elma", "armut", "muz", "cilek", "muz"]

# Elemanin ilk gorundugu indeks
print(meyveler.index("muz"))  # 2

# Belirli aralikta arama
print(meyveler.index("muz", 3))  # 4 (3. indeksten sonra ara)

# Olmayan eleman aranirsa hata verir
try:
    print(meyveler.index("kavun"))
except ValueError as e:
    print(f"Hata: {e}")  # Hata: 'kavun' is not in list
```

### 8. count() - Eleman Sayisini Bulma

```python
sayilar = [1, 2, 3, 2, 4, 2, 5, 2]
print(sayilar.count(2))  # 4
print(sayilar.count(7))  # 0 (listede yok)

# String listesinde sayma
harfler = ['a', 'b', 'a', 'c', 'a', 'b']
print(harfler.count('a'))  # 3
```

### 9. sort() - Listeyi Siralama

```python
# Artan siralamayla siralama
sayilar = [5, 2, 8, 1, 9, 3]
sayilar.sort()
print(sayilar)  # [1, 2, 3, 5, 8, 9]

# Azalan siralamayla siralama
sayilar.sort(reverse=True)
print(sayilar)  # [9, 8, 5, 3, 2, 1]

# String siralama
isimler = ["Zeynep", "Ali", "Mehmet", "Ayse"]
isimler.sort()
print(isimler)  # ['Ali', 'Ayse', 'Mehmet', 'Zeynep']

# Buyuk-kucuk harf duyarli olmadan siralama
kelimeler = ["elma", "Armut", "muz", "Cilek"]
kelimeler.sort(key=str.lower)
print(kelimeler)  # ['Armut', 'Cilek', 'elma', 'muz']
```

### 10. reverse() - Listeyi Ters Cevirme

```python
sayilar = [1, 2, 3, 4, 5]
sayilar.reverse()
print(sayilar)  # [5, 4, 3, 2, 1]

# Not: sorted() ve reversed() fonksiyonları da kullanilabilir
```

### 11. copy() - Liste Kopyalama

```python
orijinal = [1, 2, 3, 4, 5]
kopya = orijinal.copy()

kopya.append(6)
print(orijinal)  # [1, 2, 3, 4, 5] (degismedi)
print(kopya)     # [1, 2, 3, 4, 5, 6]
```

## Liste Kopyalama Yontemleri

```python
orijinal = [1, 2, 3, 4, 5]

# 1. copy() metodu
kopya1 = orijinal.copy()

# 2. list() fonksiyonu
kopya2 = list(orijinal)

# 3. Slicing ile
kopya3 = orijinal[:]

# 4. copy modulu ile (deep copy icin)
import copy
ic_liste = [[1, 2], [3, 4]]
derin_kopya = copy.deepcopy(ic_liste)

# Referans atama (DIKKAT: Kopya degil!)
referans = orijinal  # Ayni listeyi gosterir
referans.append(6)
print(orijinal)  # [1, 2, 3, 4, 5, 6] (degisti!)
```

## Liste Comprehensions

Liste comprehension, listeler olusturmak icin kompakt ve okunabilir bir yoldur.

### Temel Liste Comprehension

```python
# Geleneksel yontem
kareler = []
for x in range(10):
    kareler.append(x ** 2)
print(kareler)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Liste comprehension ile
kareler = [x ** 2 for x in range(10)]
print(kareler)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Kosullu Liste Comprehension

```python
# Cift sayilari alma
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = [x for x in sayilar if x % 2 == 0]
print(cift_sayilar)  # [2, 4, 6, 8, 10]

# If-else ile
etiketler = ["cift" if x % 2 == 0 else "tek" for x in range(1, 6)]
print(etiketler)  # ['tek', 'cift', 'tek', 'cift', 'tek']
```

### Ic Ice Liste Comprehension

```python
# 2D matris olusturma
matris = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matris)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Ic ice listeden tek bir liste olusturma
ic_liste = [[1, 2], [3, 4], [5, 6]]
duz_liste = [eleman for alt_liste in ic_liste for eleman in alt_liste]
print(duz_liste)  # [1, 2, 3, 4, 5, 6]
```

## Ic Ice Listeler (Nested Lists)

```python
# 2D liste (matris) olusturma
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Elemanlara erisim
print(matris[0])       # [1, 2, 3] (birinci satir)
print(matris[1][2])    # 6 (ikinci satir, ucuncu sutun)
print(matris[-1][-1])  # 9 (son satir, son sutun)

# Ic ice dongu ile gezinme
for satir in matris:
    for eleman in satir:
        print(eleman, end=" ")
    print()  # Yeni satir
```

## Liste Operatorleri

### Birlestirme (+)

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
birlesik = liste1 + liste2
print(birlesik)  # [1, 2, 3, 4, 5, 6]
```

### Coklu Kopyalama (*)

```python
tekrar = [0] * 5
print(tekrar)  # [0, 0, 0, 0, 0]

sifir_matris = [[0] * 3 for _ in range(3)]
print(sifir_matris)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### Uyelik Kontrolu (in, not in)

```python
meyveler = ["elma", "armut", "muz", "cilek"]

print("elma" in meyveler)      # True
print("kavun" in meyveler)     # False
print("kavun" not in meyveler) # True
```

## Yaygın Liste Islemleri

### Liste Uzunlugu

```python
liste = [1, 2, 3, 4, 5]
print(len(liste))  # 5
```

### Min, Max ve Sum

```python
sayilar = [5, 2, 8, 1, 9, 3]

print(min(sayilar))  # 1
print(max(sayilar))  # 9
print(sum(sayilar))  # 28
```

### Liste Iterasyonu

```python
meyveler = ["elma", "armut", "muz"]

# Dongu ile
for meyve in meyveler:
    print(meyve)

# Indeks ile dongu
for i in range(len(meyveler)):
    print(f"{i}: {meyveler[i]}")

# enumerate() ile
for indeks, meyve in enumerate(meyveler):
    print(f"{indeks}: {meyve}")

# enumerate() baslangic indeksi ile
for indeks, meyve in enumerate(meyveler, start=1):
    print(f"{indeks}. {meyve}")
```

### Listeden Diger Veri Tiplerine Donusum

```python
# Liste -> Tuple
liste = [1, 2, 3]
demet = tuple(liste)
print(demet)  # (1, 2, 3)

# Liste -> Set
liste = [1, 2, 2, 3, 3, 4]
kume = set(liste)
print(kume)  # {1, 2, 3, 4} (tekrarlar kaldirildi)

# Liste -> String
harfler = ['P', 'y', 't', 'h', 'o', 'n']
kelime = ''.join(harfler)
print(kelime)  # Python
```

## Onemli Notlar ve Ipuclari

1. **Liseler Degistirilebilir (Mutable)**: Listeler olusturulduktan sonra degistirilebilir.
2. **Indeksleme 0'dan Baslar**: Python'da ilk eleman indeks 0'dadir.
3. **Negatif Indeksler**: Sondan geriye dogru sayim icin kullanilir.
4. **Slice Islemleri**: Yeni liste olusturur, orijinali degistirmez.
5. **Liste Metodlari**: Cogu metod listeyi yerinde (in-place) degistirir ve None dondurur.
6. **Liste Comprehension**: Kod okunabilirligini artirir ve genellikle daha hizlidir.
7. **Kopya vs Referans**: Atama operatoru (=) referans olusturur, kopya degil.
8. **Performans**: Buyuk listelerde append() ve extend() kullanmak, + operatorunden daha hizlidir.

## Ozet

Python listeleri, guclu ve esnek veri yapilaridir. Sirali, degistirilebilir ve farkli veri tiplerini barindirabilir ozelliklere sahiptir. Liste metodlari, comprehension ve slicing gibi ozelliklerle verimli veri manipulasyonu yapilabilir. Liste kavrami Python programlamanin temelidir ve diger veri yapilarina geciste onemli bir rol oynar.
