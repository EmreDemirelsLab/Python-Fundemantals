# Tuples (Demetler)

## İçindekiler
1. [Tuple Nedir?](#tuple-nedir)
2. [Tuple Oluşturma](#tuple-oluşturma)
3. [Tuple İmmutability (Değişmezlik)](#tuple-immutability-değişmezlik)
4. [Tuple İndexleme ve Slicing](#tuple-i̇ndexleme-ve-slicing)
5. [Tuple Metodları](#tuple-metodları)
6. [Tuple Unpacking](#tuple-unpacking)
7. [Tuple İşlemleri](#tuple-i̇şlemleri)
8. [Named Tuples](#named-tuples)
9. [Tuple vs List](#tuple-vs-list)
10. [Tuple ile İlgili İpuçları](#tuple-ile-i̇lgili-i̇puçları)

---

## Tuple Nedir?

Tuple, Python'da birden fazla değeri tek bir değişkende saklamanıza olanak tanıyan, sıralı ve değiştirilemez (immutable) bir veri yapısıdır. Tuple'lar parantez `()` ile tanımlanır ve listelerden farklı olarak oluşturulduktan sonra değiştirilemezler.

### Örnek 1: Basit Tuple Tanımlama

```python
# Tuple tanımlama
fruits = ("elma", "armut", "muz")
print(fruits)  # ('elma', 'armut', 'muz')
print(type(fruits))  # <class 'tuple'>

# Boş tuple
empty_tuple = ()
print(empty_tuple)  # ()
print(len(empty_tuple))  # 0

# Tek elemanlı tuple (virgül zorunlu!)
single_item = ("elma",)  # Virgül olmazsa string olur
print(type(single_item))  # <class 'tuple'>

single_without_comma = ("elma")  # Bu bir string!
print(type(single_without_comma))  # <class 'str'>
```

### Örnek 2: Farklı Veri Tiplerinde Tuple

```python
# Farklı veri tipleri içeren tuple
mixed_tuple = (1, "Python", 3.14, True, None)
print(mixed_tuple)
print(f"Uzunluk: {len(mixed_tuple)}")  # 5

# İç içe tuple (nested tuple)
nested = ((1, 2), (3, 4), (5, 6))
print(nested)  # ((1, 2), (3, 4), (5, 6))
print(nested[0])  # (1, 2)
print(nested[0][1])  # 2

# Liste içeren tuple
tuple_with_list = (1, 2, [3, 4, 5])
print(tuple_with_list)
print(tuple_with_list[2])  # [3, 4, 5]
```

---

## Tuple Oluşturma

Tuple oluşturmanın farklı yolları vardır.

### Örnek 3: Tuple Oluşturma Yöntemleri

```python
# Method 1: Parantez ile
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# Method 2: Parantez olmadan (tuple packing)
tuple2 = 1, 2, 3, 4, 5
print(tuple2)  # (1, 2, 3, 4, 5)
print(type(tuple2))  # <class 'tuple'>

# Method 3: tuple() constructor ile
tuple3 = tuple([1, 2, 3, 4, 5])  # Listeden tuple
print(tuple3)

tuple4 = tuple("Python")  # String'den tuple
print(tuple4)  # ('P', 'y', 't', 'h', 'o', 'n')

tuple5 = tuple(range(5))  # Range'den tuple
print(tuple5)  # (0, 1, 2, 3, 4)

# Method 4: Generator expression ile
tuple6 = tuple(x**2 for x in range(5))
print(tuple6)  # (0, 1, 4, 9, 16)
```

### Örnek 4: Tuple ile Çoklu Atama

```python
# Koordinat sistemi
point = (3, 5)
x, y = point
print(f"x: {x}, y: {y}")  # x: 3, y: 5

# Renk değerleri (RGB)
color = (255, 128, 0)
red, green, blue = color
print(f"R:{red}, G:{green}, B:{blue}")

# Fonksiyon birden fazla değer döndürebilir (tuple olarak)
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([1, 5, 3, 9, 2])
print(result)  # (1, 9)
print(type(result))  # <class 'tuple'>

min_val, max_val = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {min_val}, Max: {max_val}")
```

---

## Tuple İmmutability (Değişmezlik)

Tuple'ların en önemli özelliği değiştirilemez (immutable) olmalarıdır.

### Örnek 5: Tuple Değiştirilemez

```python
# Tuple oluşturma
numbers = (1, 2, 3, 4, 5)
print(numbers)

# Tuple elemanlarını değiştiremezsiniz
try:
    numbers[0] = 10  # Hata verir!
except TypeError as e:
    print(f"Hata: {e}")  # 'tuple' object does not support item assignment

# Tuple'a eleman ekleyemezsiniz
try:
    numbers.append(6)  # Hata verir!
except AttributeError as e:
    print(f"Hata: {e}")  # 'tuple' object has no attribute 'append'

# Tuple'dan eleman silemezsiniz
try:
    del numbers[0]  # Hata verir!
except TypeError as e:
    print(f"Hata: {e}")
```

### Örnek 6: Mutable Objeler İçeren Tuple

```python
# Tuple içindeki mutable objeler değiştirilebilir
tuple_with_list = (1, 2, [3, 4, 5])
print(f"Başlangıç: {tuple_with_list}")

# Tuple'ın kendisi değişmez ama içindeki liste değişebilir
tuple_with_list[2].append(6)
print(f"Liste değişti: {tuple_with_list}")  # (1, 2, [3, 4, 5, 6])

tuple_with_list[2][0] = 100
print(f"Liste elemanı değişti: {tuple_with_list}")  # (1, 2, [100, 4, 5, 6])

# Ancak tuple elemanını değiştiremezsiniz
try:
    tuple_with_list[0] = 10  # Hata!
except TypeError as e:
    print(f"Hata: {e}")

# Yeni bir tuple oluşturabilirsiniz
new_tuple = tuple_with_list + (7, 8)
print(f"Yeni tuple: {new_tuple}")
```

---

## Tuple İndexleme ve Slicing

Tuple'lar sıralı veri yapıları olduğu için indexleme ve slicing işlemleri listeler gibidir.

### Örnek 7: Tuple İndexleme

```python
# Tuple oluşturma
fruits = ("elma", "armut", "muz", "çilek", "kiraz")

# Pozitif indexleme
print(fruits[0])   # elma (ilk eleman)
print(fruits[2])   # muz
print(fruits[4])   # kiraz (son eleman)

# Negatif indexleme
print(fruits[-1])  # kiraz (son eleman)
print(fruits[-2])  # çilek (sondan ikinci)
print(fruits[-5])  # elma (baştan ilk)

# İç içe tuple indexleme
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested[0])      # (1, 2, 3)
print(nested[1][2])   # 6
print(nested[-1][-1]) # 9
```

### Örnek 8: Tuple Slicing

```python
# Tuple oluşturma
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Temel slicing
print(numbers[2:5])    # (2, 3, 4)
print(numbers[:4])     # (0, 1, 2, 3) - baştan 4 eleman
print(numbers[6:])     # (6, 7, 8, 9) - 6. indexten sona
print(numbers[:])      # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) - tüm tuple

# Negatif index ile slicing
print(numbers[-5:-2])  # (5, 6, 7)
print(numbers[:-3])    # (0, 1, 2, 3, 4, 5, 6) - son 3 hariç
print(numbers[-7:])    # (3, 4, 5, 6, 7, 8, 9) - son 7 eleman

# Step ile slicing
print(numbers[::2])    # (0, 2, 4, 6, 8) - ikişer ikişer
print(numbers[1::2])   # (1, 3, 5, 7, 9) - tekler
print(numbers[::3])    # (0, 3, 6, 9) - üçer üçer
print(numbers[::-1])   # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0) - ters çevir

# Karmaşık slicing
print(numbers[2:8:2])  # (2, 4, 6) - 2'den 8'e kadar ikişer
print(numbers[7:2:-1]) # (7, 6, 5, 4, 3) - 7'den 2'ye kadar geriye
```

---

## Tuple Metodları

Tuple'lar immutable olduğu için çok az metoda sahiptir.

### Örnek 9: count() Metodu

```python
# count(): Bir elemanın tuple içinde kaç kez geçtiğini sayar
numbers = (1, 2, 3, 2, 4, 2, 5, 2, 6)

print(numbers.count(2))  # 4 (2 sayısı 4 kez geçiyor)
print(numbers.count(5))  # 1
print(numbers.count(10)) # 0 (10 yok)

# String tuple'da count
letters = ('a', 'b', 'c', 'a', 'b', 'a')
print(letters.count('a'))  # 3
print(letters.count('d'))  # 0

# Karmaşık örnekler
mixed = (1, 2, 3, [1, 2], 'test', [1, 2], 3)
print(mixed.count(3))      # 2
print(mixed.count([1, 2])) # 2 (liste de sayılabilir)
```

### Örnek 10: index() Metodu

```python
# index(): Bir elemanın ilk geçtiği indexi döndürür
fruits = ("elma", "armut", "muz", "armut", "çilek")

print(fruits.index("muz"))    # 2
print(fruits.index("armut"))  # 1 (ilk geçen)

# Eleman yoksa hata verir
try:
    print(fruits.index("kiraz"))
except ValueError as e:
    print(f"Hata: {e}")  # 'kiraz' is not in tuple

# Arama aralığı belirtme: index(value, start, end)
numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.index(2))      # 1 (ilk 2)
print(numbers.index(2, 2))   # 3 (2. indexten sonra ilk 2)
print(numbers.index(2, 4))   # 5 (4. indexten sonra ilk 2)

# Güvenli kullanım
item = "kiraz"
if item in fruits:
    print(f"{item} indexi: {fruits.index(item)}")
else:
    print(f"{item} bulunamadı")
```

---

## Tuple Unpacking

Tuple unpacking, tuple elemanlarını ayrı değişkenlere atama işlemidir.

### Örnek 11: Basit Unpacking

```python
# Temel unpacking
point = (3, 5)
x, y = point
print(f"x={x}, y={y}")  # x=3, y=5

# Birden fazla değişken
person = ("Ali", 25, "İstanbul")
name, age, city = person
print(f"{name}, {age} yaşında, {city}'da yaşıyor")

# Değişken değerlerini swap etme
a = 10
b = 20
print(f"Öncesi: a={a}, b={b}")
a, b = b, a  # Tuple unpacking ile swap
print(f"Sonrası: a={a}, b={b}")

# Fonksiyonlardan dönen değerler
def divide(a, b):
    return a // b, a % b  # Bölüm ve kalan

quotient, remainder = divide(17, 5)
print(f"17 / 5 = {quotient} (kalan: {remainder})")
```

### Örnek 12: Extended Unpacking (*)

```python
# * operatörü ile geri kalan elemanları alma
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# İlk ve son, geri kalanlar
first, *middle, last = numbers
print(f"İlk: {first}")      # 1
print(f"Orta: {middle}")    # [2, 3, 4, 5, 6, 7, 8]
print(f"Son: {last}")       # 9
print(f"Orta tipi: {type(middle)}")  # <class 'list'>

# İlk iki, geri kalanlar
a, b, *rest = numbers
print(f"a={a}, b={b}, rest={rest}")

# İlk, geri kalanlar, son iki
first, *middle, second_last, last = numbers
print(f"İlk: {first}, Orta: {middle}, Sondan 2.: {second_last}, Son: {last}")

# Sadece bazı değerleri alma
first, *_, last = numbers  # Ortaları görmezden gel
print(f"İlk: {first}, Son: {last}")

# İç içe unpacking
nested = ((1, 2), (3, 4), (5, 6))
(a, b), (c, d), (e, f) = nested
print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")
```

### Örnek 13: Unpacking ile Fonksiyon Argümanları

```python
# Tuple'ı fonksiyon argümanlarına unpacking
def greet(name, age, city):
    return f"Merhaba {name}! {age} yaşındasın ve {city}'da yaşıyorsun."

person_info = ("Ayşe", 30, "Ankara")
message = greet(*person_info)  # * ile unpacking
print(message)

# Koordinat hesaplaması
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

point1 = (0, 0)
point2 = (3, 4)
dist = distance(*point1, *point2)
print(f"Mesafe: {dist}")  # 5.0

# Dictionary unpacking
def create_profile(name, age, city):
    return {"name": name, "age": age, "city": city}

data = ("Mehmet", 28, "İzmir")
profile = create_profile(*data)
print(profile)
```

---

## Tuple İşlemleri

Tuple'lar üzerinde çeşitli işlemler yapılabilir.

### Örnek 14: Tuple Birleştirme ve Tekrarlama

```python
# + operatörü ile birleştirme
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5, 6)

# Birden fazla tuple birleştirme
fruits = ("elma", "armut")
vegetables = ("havuç", "brokoli")
berries = ("çilek", "böğürtlen")
all_items = fruits + vegetables + berries
print(all_items)

# * operatörü ile tekrarlama
pattern = (1, 2)
repeated = pattern * 4
print(repeated)  # (1, 2, 1, 2, 1, 2, 1, 2)

stars = ("*",) * 10
print(stars)  # ('*', '*', '*', '*', '*', '*', '*', '*', '*', '*')

# Tekrar ve birleştirme kombinasyonu
header = ("=",) * 20
content = ("Python", "Tuples")
footer = ("=",) * 20
full_display = header + content + footer
print(full_display)
```

### Örnek 15: Tuple Karşılaştırma

```python
# Tuple'lar lexicographic (sözlük sırası) olarak karşılaştırılır
print((1, 2, 3) == (1, 2, 3))  # True
print((1, 2, 3) == (1, 2, 4))  # False

print((1, 2, 3) < (1, 2, 4))   # True (son eleman küçük)
print((1, 2, 3) < (1, 3, 0))   # True (ikinci eleman küçük)
print((2, 0, 0) > (1, 9, 9))   # True (ilk eleman büyük)

# String tuple karşılaştırma
print(("a", "b") < ("a", "c"))  # True
print(("apple",) < ("banana",)) # True

# Farklı uzunlukta tuple'lar
print((1, 2) < (1, 2, 3))      # True (kısa olanlar küçük)
print((1, 2, 3) > (1, 2))      # True

# Sıralama
numbers = [(3, 1), (1, 2), (2, 3), (1, 1)]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [(1, 1), (1, 2), (2, 3), (3, 1)]

# Özel karşılaştırma ile sıralama (ikinci elemana göre)
students = [("Ali", 85), ("Ayşe", 92), ("Mehmet", 78)]
by_grade = sorted(students, key=lambda x: x[1])
print(by_grade)  # [('Mehmet', 78), ('Ali', 85), ('Ayşe', 92)]
```

---

## Named Tuples

Named tuple'lar, tuple elemanlarına isimle erişim sağlar.

### Örnek 16: Named Tuple Kullanımı

```python
from collections import namedtuple

# Named tuple tanımlama
Point = namedtuple('Point', ['x', 'y'])

# Named tuple oluşturma
p1 = Point(3, 5)
print(p1)  # Point(x=3, y=5)

# Erişim yöntemleri
print(p1.x)      # 3 - isimle erişim
print(p1.y)      # 5 - isimle erişim
print(p1[0])     # 3 - index ile erişim
print(p1[1])     # 5 - index ile erişim

# Unpacking
x, y = p1
print(f"x={x}, y={y}")

# Named tuple immutable'dır
try:
    p1.x = 10
except AttributeError as e:
    print(f"Hata: {e}")
```

### Örnek 17: Named Tuple İleri Düzey

```python
from collections import namedtuple

# Öğrenci bilgisi
Student = namedtuple('Student', ['name', 'age', 'grade', 'city'])

student1 = Student('Ali', 20, 85, 'İstanbul')
student2 = Student('Ayşe', 22, 92, 'Ankara')
student3 = Student('Mehmet', 21, 78, 'İzmir')

print(f"{student1.name}, {student1.age} yaşında, notu: {student1.grade}")

# Named tuple listesi
students = [student1, student2, student3]

# En yüksek notu bulma
best_student = max(students, key=lambda s: s.grade)
print(f"En başarılı: {best_student.name} ({best_student.grade})")

# Şehre göre filtreleme
istanbul_students = [s for s in students if s.city == 'İstanbul']
print(f"İstanbul'daki öğrenciler: {[s.name for s in istanbul_students]}")

# _replace() metodu ile yeni tuple oluşturma
student1_updated = student1._replace(grade=90)
print(f"Güncellenmiş: {student1_updated}")
print(f"Orijinal: {student1}")  # Değişmedi!

# _asdict() ile dictionary'ye çevirme
student_dict = student1._asdict()
print(student_dict)  # {'name': 'Ali', 'age': 20, 'grade': 85, 'city': 'İstanbul'}

# _fields ile alan isimlerini görme
print(Student._fields)  # ('name', 'age', 'grade', 'city')
```

---

## Tuple vs List

Tuple ve list arasındaki farkları anlamak önemlidir.

### Örnek 18: Tuple ve List Karşılaştırması

```python
# List (mutable - değiştirilebilir)
my_list = [1, 2, 3, 4, 5]
my_list[0] = 10  # Değiştirilebilir
my_list.append(6)  # Eleman eklenebilir
print(f"List: {my_list}")

# Tuple (immutable - değiştirilemez)
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10  # Hata! Değiştirilemez
# my_tuple.append(6)  # Hata! Eleman eklenemez
print(f"Tuple: {my_tuple}")

# Performans: Tuple'lar daha hızlı
import sys
import timeit

list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

# Bellek kullanımı
print(f"List boyutu: {sys.getsizeof(list_data)} bytes")
print(f"Tuple boyutu: {sys.getsizeof(tuple_data)} bytes")

# Oluşturma hızı
list_time = timeit.timeit('x = [1, 2, 3, 4, 5]', number=1000000)
tuple_time = timeit.timeit('x = (1, 2, 3, 4, 5)', number=1000000)
print(f"List oluşturma: {list_time:.4f}s")
print(f"Tuple oluşturma: {tuple_time:.4f}s")
```

### Örnek 19: Ne Zaman Tuple, Ne Zaman List?

```python
# TUPLE kullanılmalı:
# 1. Sabit veri (koordinat, RGB renk değeri, vb.)
coordinates = (41.0082, 28.9784)  # İstanbul koordinatları
rgb_color = (255, 128, 0)  # Turuncu renk
dimensions = (1920, 1080)  # Ekran çözünürlüğü

# 2. Fonksiyon birden fazla değer döndürürken
def get_statistics(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

stats = get_statistics([1, 2, 3, 4, 5])
print(f"Min: {stats[0]}, Max: {stats[1]}, Avg: {stats[2]:.2f}")

# 3. Dictionary key olarak (tuple hashable, list değil)
locations = {}
locations[(41.0082, 28.9784)] = "İstanbul"
locations[(39.9334, 32.8597)] = "Ankara"
print(locations[(41.0082, 28.9784)])

# locations[[41.0082, 28.9784]] = "Test"  # Hata! List unhashable

# LIST kullanılmalı:
# 1. Değişecek veri
shopping_list = ["ekmek", "süt", "yumurta"]
shopping_list.append("peynir")
shopping_list.remove("ekmek")

# 2. Sıralama gerekirse
scores = [85, 92, 78, 95, 88]
scores.sort()
print(f"Sıralı notlar: {scores}")

# 3. Dinamik veri toplama
user_inputs = []
for i in range(3):
    user_inputs.append(f"input_{i}")
print(user_inputs)
```

---

## Tuple ile İlgili İpuçları

### Örnek 20: Pratik Tuple Kullanımları

```python
# 1. Çoklu değer atama
min_val, max_val = 0, 100
print(f"Aralık: {min_val}-{max_val}")

# 2. Değişken değerlerini değiştirme (swap)
a, b = 5, 10
a, b = b, a
print(f"a={a}, b={b}")

# 3. Tuple'ı dict'e çevirme
pairs = [("a", 1), ("b", 2), ("c", 3)]
dictionary = dict(pairs)
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}

# 4. Tuple ile enumerate
fruits = ("elma", "armut", "muz")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 5. Tuple ile zip
names = ("Ali", "Ayşe", "Mehmet")
ages = (25, 30, 28)
cities = ("İstanbul", "Ankara", "İzmir")

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age} yaşında, {city}'da yaşıyor")

# 6. Tuple unpacking ile fonksiyon parametreleri
def calculate_area(width, height):
    return width * height

dimensions = (10, 5)
area = calculate_area(*dimensions)
print(f"Alan: {area}")

# 7. Tuple ile max/min (key parametresi ile)
students = [
    ("Ali", 85),
    ("Ayşe", 92),
    ("Mehmet", 78),
    ("Zeynep", 95)
]

best = max(students, key=lambda x: x[1])
worst = min(students, key=lambda x: x[1])
print(f"En başarılı: {best[0]} ({best[1]})")
print(f"En düşük not: {worst[0]} ({worst[1]})")

# 8. Tuple ile any() ve all()
scores = (85, 90, 78, 92, 88)
print(f"Hepsi 70'den yüksek mü? {all(score > 70 for score in scores)}")
print(f"Herhangi biri 90'dan yüksek mü? {any(score > 90 for score in scores)}")

# 9. Tuple comprehension yok, generator expression var
gen = (x**2 for x in range(5))  # Bu generator
print(type(gen))  # <class 'generator'>
squares_tuple = tuple(gen)  # Tuple'a çevir
print(squares_tuple)  # (0, 1, 4, 9, 16)

# 10. Tuple ile hash kontrolü
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(f"t1 hash: {hash(t1)}")
print(f"t2 hash: {hash(t2)}")
print(f"Aynı hash? {hash(t1) == hash(t2)}")  # True

# Dictionary ve set'lerde kullanılabilir
my_set = {(1, 2), (3, 4), (5, 6)}
print(my_set)

my_dict = {(1, 2): "a", (3, 4): "b"}
print(my_dict[(1, 2)])
```

---

## Önemli Notlar

1. **İmmutability**: Tuple'lar değiştirilemez, bu onları güvenli ve hızlı yapar
2. **Tek Elemanlı Tuple**: Virgül koymayı unutmayın: `(5,)` tuple, `(5)` sadece integer
3. **Performans**: Tuple'lar listelerden daha hızlı ve daha az bellek kullanır
4. **Dictionary Key**: Tuple'lar hashable olduğu için dict key olarak kullanılabilir
5. **Unpacking**: Tuple unpacking kodu daha okunabilir yapar
6. **Named Tuple**: Daha açıklayıcı kod için named tuple kullanın
7. **Fonksiyon Dönüş**: Birden fazla değer döndürmek için tuple ideal
8. **Sabit Veri**: Değişmemesi gereken veriler için tuple tercih edin

---

## Özet

Bu bölümde öğrendikleriniz:
- Tuple tanımlama ve oluşturma
- Tuple'ların immutability özelliği
- İndexleme ve slicing işlemleri
- Tuple metodları (count, index)
- Tuple unpacking ve extended unpacking
- Tuple işlemleri (birleştirme, tekrarlama, karşılaştırma)
- Named tuple kullanımı
- Tuple vs List farkları ve kullanım senaryoları
- Pratik tuple kullanım örnekleri

Şimdi `exercises.py` dosyasındaki alıştırmaları yaparak öğrendiklerinizi pekiştirebilirsiniz!
