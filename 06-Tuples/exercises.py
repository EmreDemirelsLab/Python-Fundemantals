"""
TUPLES - ALIŞTIRMALAR
=====================

Her soruyu çözmeye çalışın. Takılırsanız, her sorunun altındaki
ÇÖZÜM bölümünü inceleyebilirsiniz.

Zorluk Seviyeleri:
[Kolay] - Temel kavramları test eder
[Orta] - Birden fazla kavramı birleştirir
[Zor] - Daha karmaşık problemler
[Challenge] - Dünya standartlarında zorlayıcı sorular
"""

# =============================================================================
# SORU 1: [Kolay] Tuple Oluşturma ve Temel İşlemler
# =============================================================================
# Aşağıdaki tuple'ları oluşturun:
# 1. İlk 5 pozitif tam sayıyı içeren bir tuple
# 2. Farklı veri tiplerini içeren bir tuple (int, str, float, bool)
# 3. İç içe tuple (nested tuple)
# Her tuple'ın uzunluğunu ve tipini yazdırın

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Tuple parantez () ile oluşturulur
- len() fonksiyonu tuple uzunluğunu verir
- type() fonksiyonu veri tipini gösterir
- İç içe tuple ile kompleks veri yapıları oluşturulabilir
"""

# 1. Sayı tuple'ı
numbers = (1, 2, 3, 4, 5)
print(f"Sayılar: {numbers}")
print(f"Uzunluk: {len(numbers)}, Tip: {type(numbers)}")

# 2. Karışık tuple
mixed = (42, "Python", 3.14, True)
print(f"\nKarışık: {mixed}")
print(f"Uzunluk: {len(mixed)}, Tip: {type(mixed)}")

# 3. İç içe tuple
nested = ((1, 2), (3, 4), (5, 6))
print(f"\nİç içe: {nested}")
print(f"Uzunluk: {len(nested)}, Tip: {type(nested)}")
print(f"İlk eleman: {nested[0]}, İlk elemanın ikinci değeri: {nested[0][1]}")

# Tek elemanlı tuple (virgül önemli!)
single = (5,)
print(f"\nTek elemanlı tuple: {single}, Tip: {type(single)}")

not_tuple = (5)  # Bu bir integer!
print(f"Parantez içinde tek değer: {not_tuple}, Tip: {type(not_tuple)}")


# =============================================================================
# SORU 2: [Kolay] Tuple İndexleme ve Slicing
# =============================================================================
# Aşağıdaki tuple ile çalışın:
# fruits = ("elma", "armut", "muz", "çilek", "kiraz", "üzüm", "portakal")
#
# 1. İlk ve son elemanı yazdırın
# 2. İlk 3 elemanı alın (slicing)
# 3. Son 3 elemanı alın
# 4. 2. indexten 5. indexe kadar olan elemanları alın
# 5. Tuple'ı tersten yazdırın

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Pozitif index: 0'dan başlar
- Negatif index: -1 son elemandır
- Slicing: [start:end:step] formatında
- [::-1] ile ters çevirme
"""

fruits = ("elma", "armut", "muz", "çilek", "kiraz", "üzüm", "portakal")

print("\n--- Tuple İndexleme ve Slicing ---")

# 1. İlk ve son
print(f"İlk eleman: {fruits[0]}")
print(f"Son eleman: {fruits[-1]}")

# 2. İlk 3 eleman
print(f"İlk 3: {fruits[:3]}")

# 3. Son 3 eleman
print(f"Son 3: {fruits[-3:]}")

# 4. 2. indexten 5. indexe
print(f"2-5 arası: {fruits[2:5]}")

# 5. Ters çevirme
print(f"Ters: {fruits[::-1]}")

# Bonus: Çift indexlerdeki elemanlar
print(f"Çift indexler: {fruits[::2]}")

# Bonus: 1. indexten sonra ikişer ikişer
print(f"Tekli indexler: {fruits[1::2]}")


# =============================================================================
# SORU 3: [Kolay] Tuple Metodları (count ve index)
# =============================================================================
# numbers = (1, 2, 3, 2, 4, 2, 5, 6, 2, 7)
#
# 1. 2 sayısı kaç kez geçiyor?
# 2. 5 sayısı kaç kez geçiyor?
# 3. 3 sayısının indexi nedir?
# 4. 2 sayısının ilk geçtiği indexi bulun
# 5. 2 sayısının 5. indexten sonra ilk geçtiği yeri bulun

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- count(): Elemanın kaç kez geçtiğini sayar
- index(): Elemanın ilk geçtiği indexi döndürür
- index(value, start): Belirtilen indexten sonra ara
"""

numbers = (1, 2, 3, 2, 4, 2, 5, 6, 2, 7)

print("\n--- Tuple Metodları ---")

# 1. 2 sayısının tekrarı
count_2 = numbers.count(2)
print(f"2 sayısı {count_2} kez geçiyor")

# 2. 5 sayısının tekrarı
count_5 = numbers.count(5)
print(f"5 sayısı {count_5} kez geçiyor")

# 3. 3 sayısının indexi
index_3 = numbers.index(3)
print(f"3 sayısının indexi: {index_3}")

# 4. 2 sayısının ilk indexi
first_2 = numbers.index(2)
print(f"2 sayısının ilk indexi: {first_2}")

# 5. 2 sayısının 5. indexten sonra
second_2 = numbers.index(2, 5)
print(f"5. indexten sonra ilk 2: {second_2}")

# Güvenli kullanım (eleman yoksa hata vermez)
target = 10
if target in numbers:
    print(f"{target} bulundu, index: {numbers.index(target)}")
else:
    print(f"{target} tuple içinde bulunamadı")


# =============================================================================
# SORU 4: [Kolay] Tuple Unpacking
# =============================================================================
# 1. (3, 5) tuple'ını x ve y değişkenlerine atayın
# 2. ("Ali", 25, "İstanbul") tuple'ını name, age, city değişkenlerine atayın
# 3. İki değişkenin değerini tuple unpacking ile swap edin
# 4. (1, 2, 3, 4, 5, 6) tuple'ında ilk, son ve ortadaki elemanları alın

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Tuple unpacking ile elemanlar değişkenlere atanır
- Değişken sayısı tuple eleman sayısına eşit olmalı
- * operatörü ile geri kalan elemanlar alınabilir
"""

print("\n--- Tuple Unpacking ---")

# 1. Koordinat unpacking
point = (3, 5)
x, y = point
print(f"x={x}, y={y}")

# 2. Kişi bilgisi unpacking
person = ("Ali", 25, "İstanbul")
name, age, city = person
print(f"{name}, {age} yaşında, {city}'da yaşıyor")

# 3. Swap işlemi
a = 10
b = 20
print(f"Öncesi: a={a}, b={b}")
a, b = b, a
print(f"Sonrası: a={a}, b={b}")

# 4. Extended unpacking (*)
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print(f"İlk: {first}, Orta: {middle}, Son: {last}")

# Bonus: Sadece bazı değerleri alma
first, *_, last = numbers  # Ortaları görmezden gel
print(f"İlk: {first}, Son: {last}")

# İlk iki ve geri kalanlar
a, b, *rest = numbers
print(f"a={a}, b={b}, geri kalan={rest}")


# =============================================================================
# SORU 5: [Orta] Tuple İmmutability (Değiştirilemezlik)
# =============================================================================
# 1. Bir tuple oluşturun ve elemanını değiştirmeyi deneyin
# 2. Liste içeren bir tuple oluşturun ve liste elemanını değiştirin
# 3. İki tuple'ı birleştirerek yeni bir tuple oluşturun
# 4. Tuple'ı 3 kez tekrarlayan yeni tuple oluşturun

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Tuple immutable'dır, elemanları değiştirilemez
- Ancak tuple içindeki mutable objeler (liste) değiştirilebilir
- + operatörü yeni tuple oluşturur
- * operatörü tuple'ı tekrarlar
"""

print("\n--- Tuple Immutability ---")

# 1. Tuple elemanı değiştirme denemesi
original = (1, 2, 3, 4, 5)
print(f"Orijinal: {original}")

try:
    original[0] = 10
except TypeError as e:
    print(f"Hata: Tuple elemanı değiştirilemez - {e}")

# 2. Liste içeren tuple
tuple_with_list = (1, 2, [3, 4, 5])
print(f"\nListeli tuple: {tuple_with_list}")

# Tuple değiştirilemez ama içindeki liste değiştirilebilir!
tuple_with_list[2].append(6)
print(f"Liste değişti: {tuple_with_list}")

tuple_with_list[2][0] = 100
print(f"Liste elemanı değişti: {tuple_with_list}")

# 3. Tuple birleştirme
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"\nBirleştirilmiş: {combined}")
print(f"Orijinal tuple1: {tuple1}")  # Değişmedi

# 4. Tuple tekrarlama
pattern = ("*", "-")
repeated = pattern * 3
print(f"Tekrarlanan: {repeated}")

# Bonus: Yeni tuple oluşturma
old_tuple = (1, 2, 3)
new_tuple = old_tuple + (4, 5)  # Yeni tuple oluştur
print(f"Eski: {old_tuple}, Yeni: {new_tuple}")


# =============================================================================
# SORU 6: [Orta] Tuple ile Çoklu Değer Döndürme
# =============================================================================
# Bir fonksiyon yazın:
# - calculate_statistics(numbers) adında
# - Bir sayı listesi alsın
# - Minimum, maksimum, ortalama ve toplam değerleri tuple olarak döndürsün
# Test: [10, 20, 30, 40, 50]

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Fonksiyonlar birden fazla değeri tuple olarak döndürebilir
- return değer1, değer2, değer3 şeklinde yazılır (parantez opsiyonel)
- Dönen değerler unpacking ile alınabilir
"""

def calculate_statistics(numbers):
    """Sayı listesinin istatistiklerini hesaplar"""
    if not numbers:
        return None, None, None, None

    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return minimum, maximum, average, total


print("\n--- Çoklu Değer Döndürme ---")

# Test verisi
test_numbers = [10, 20, 30, 40, 50]
print(f"Sayılar: {test_numbers}")

# Method 1: Tuple olarak alma
result = calculate_statistics(test_numbers)
print(f"Sonuç tuple'ı: {result}")
print(f"Tip: {type(result)}")

# Method 2: Unpacking ile alma
min_val, max_val, avg_val, sum_val = calculate_statistics(test_numbers)
print(f"\nMinimum: {min_val}")
print(f"Maksimum: {max_val}")
print(f"Ortalama: {avg_val}")
print(f"Toplam: {sum_val}")

# Farklı veri seti
grades = [85, 92, 78, 95, 88, 91, 87]
min_grade, max_grade, avg_grade, total_grade = calculate_statistics(grades)
print(f"\nNotlar analizi:")
print(f"En düşük: {min_grade}, En yüksek: {max_grade}, Ortalama: {avg_grade:.2f}")


# =============================================================================
# SORU 7: [Orta] Tuple ile Sıralama
# =============================================================================
# Öğrenci bilgilerini içeren tuple listesi:
# students = [("Ali", 85), ("Ayşe", 92), ("Mehmet", 78), ("Zeynep", 95)]
#
# 1. İsme göre alfabetik sıralayın
# 2. Nota göre artan sıralayın
# 3. Nota göre azalan sıralayın
# 4. En yüksek notu alan öğrenciyi bulun
# 5. Ortalamanın üzerinde not alan öğrencileri bulun

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- sorted() fonksiyonu yeni sıralı liste döndürür
- key parametresi ile sıralama kriterini belirtebiliriz
- lambda fonksiyonu ile tuple elemanlarına erişiriz
- reverse=True ile azalan sıralama
"""

students = [("Ali", 85), ("Ayşe", 92), ("Mehmet", 78), ("Zeynep", 95)]

print("\n--- Tuple Sıralama ---")
print(f"Orijinal: {students}")

# 1. İsme göre sıralama (alfabetik)
by_name = sorted(students, key=lambda x: x[0])
print(f"\nİsme göre: {by_name}")

# 2. Nota göre artan sıralama
by_grade_asc = sorted(students, key=lambda x: x[1])
print(f"Nota göre (artan): {by_grade_asc}")

# 3. Nota göre azalan sıralama
by_grade_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Nota göre (azalan): {by_grade_desc}")

# 4. En yüksek notu alan
best_student = max(students, key=lambda x: x[1])
print(f"\nEn başarılı: {best_student[0]} ({best_student[1]} puan)")

# 5. Ortalamanın üzerinde olanlar
average = sum(grade for _, grade in students) / len(students)
print(f"Ortalama: {average:.2f}")

above_average = [student for student in students if student[1] > average]
print(f"Ortalamanın üzerinde: {above_average}")

# Bonus: En düşük not
worst_student = min(students, key=lambda x: x[1])
print(f"En düşük not: {worst_student[0]} ({worst_student[1]} puan)")


# =============================================================================
# SORU 8: [Orta] Named Tuple Kullanımı
# =============================================================================
# collections.namedtuple kullanarak:
# 1. Point adında x, y koordinatlarını tutan bir named tuple oluşturun
# 2. İki nokta oluşturun: p1(3, 4) ve p2(6, 8)
# 3. İki nokta arasındaki Öklid mesafesini hesaplayın
# 4. Noktaları hem isimle hem index ile erişim gösterin

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- namedtuple ile tuple elemanlarına isimle erişebiliriz
- Hem x.name hem x[0] şeklinde erişim mümkün
- Öklid mesafesi: sqrt((x2-x1)^2 + (y2-y1)^2)
- _replace() ile yeni tuple oluşturabiliriz
"""

from collections import namedtuple
import math

print("\n--- Named Tuple ---")

# Named tuple tanımlama
Point = namedtuple('Point', ['x', 'y'])

# Noktalar oluşturma
p1 = Point(3, 4)
p2 = Point(6, 8)

print(f"Nokta 1: {p1}")
print(f"Nokta 2: {p2}")

# İsimle erişim
print(f"\np1.x = {p1.x}, p1.y = {p1.y}")

# Index ile erişim
print(f"p1[0] = {p1[0]}, p1[1] = {p1[1]}")

# Öklid mesafesi hesaplama
def distance(point1, point2):
    """İki nokta arasındaki Öklid mesafesini hesaplar"""
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    return math.sqrt(dx**2 + dy**2)

dist = distance(p1, p2)
print(f"\nİki nokta arası mesafe: {dist:.2f}")

# _replace() ile yeni tuple
p3 = p1._replace(x=10)
print(f"p1: {p1}")
print(f"p3 (x değişti): {p3}")

# _asdict() ile dictionary'ye çevirme
p1_dict = p1._asdict()
print(f"Dictionary: {p1_dict}")

# Bonus: Daha kompleks named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person1 = Person('Ali', 25, 'İstanbul')
print(f"\n{person1.name}, {person1.age} yaşında, {person1.city}'da yaşıyor")


# =============================================================================
# SORU 9: [Zor] Tuple ile Veri Analizi
# =============================================================================
# Satış verileri (ürün, adet, fiyat):
# sales = [
#     ("Laptop", 5, 15000),
#     ("Mouse", 20, 150),
#     ("Keyboard", 12, 500),
#     ("Monitor", 8, 3000),
#     ("Headphone", 15, 800)
# ]
#
# 1. Toplam geliri hesaplayın
# 2. En çok satan ürünü bulun (adete göre)
# 3. En yüksek gelir getiren ürünü bulun
# 4. Ortalama ürün fiyatını hesaplayın
# 5. 1000 TL'den pahalı ürünleri listeleyin
# 6. Her ürün için toplam gelirini gösterin

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Tuple unpacking ile verilere erişim
- max/min fonksiyonları key parametresi ile
- List comprehension ile filtreleme
- Toplam gelir = adet * fiyat
"""

sales = [
    ("Laptop", 5, 15000),
    ("Mouse", 20, 150),
    ("Keyboard", 12, 500),
    ("Monitor", 8, 3000),
    ("Headphone", 15, 800)
]

print("\n--- Satış Veri Analizi ---")

# 1. Toplam gelir
total_revenue = sum(quantity * price for _, quantity, price in sales)
print(f"Toplam Gelir: {total_revenue:,} TL")

# 2. En çok satan ürün (adete göre)
best_seller = max(sales, key=lambda x: x[1])
print(f"\nEn çok satan: {best_seller[0]} ({best_seller[1]} adet)")

# 3. En yüksek gelir getiren
highest_revenue = max(sales, key=lambda x: x[1] * x[2])
revenue = highest_revenue[1] * highest_revenue[2]
print(f"En yüksek gelir: {highest_revenue[0]} ({revenue:,} TL)")

# 4. Ortalama ürün fiyatı
average_price = sum(price for _, _, price in sales) / len(sales)
print(f"\nOrtalama fiyat: {average_price:,.2f} TL")

# 5. 1000 TL'den pahalı ürünler
expensive = [product for product, _, price in sales if price > 1000]
print(f"Pahalı ürünler: {expensive}")

# 6. Her ürün için toplam gelir
print("\n--- Ürün Bazında Gelir ---")
print(f"{'Ürün':<15} {'Adet':<8} {'Fiyat':<12} {'Toplam Gelir':<15}")
print("-" * 50)

for product, quantity, price in sales:
    product_revenue = quantity * price
    print(f"{product:<15} {quantity:<8} {price:<12,} {product_revenue:<15,}")

# Bonus: En düşük gelir getiren
lowest_revenue = min(sales, key=lambda x: x[1] * x[2])
low_revenue = lowest_revenue[1] * lowest_revenue[2]
print(f"\nEn düşük gelir: {lowest_revenue[0]} ({low_revenue:,} TL)")

# Bonus: Ortalama üstü gelir getirenler
avg_revenue = total_revenue / len(sales)
above_avg = [s for s in sales if s[1] * s[2] > avg_revenue]
print(f"Ortalama üstü gelir: {[s[0] for s in above_avg]}")


# =============================================================================
# SORU 10: [Zor] Tuple ile Koordinat Sistemi
# =============================================================================
# Bir koordinat sistemi simüle edin:
# - Noktalar tuple olarak (x, y) şeklinde
# - calculate_distance(p1, p2): İki nokta arası mesafe
# - midpoint(p1, p2): Orta nokta bulma
# - is_collinear(p1, p2, p3): Üç nokta aynı doğru üzerinde mi?
#
# Test noktaları: (0, 0), (3, 4), (6, 8), (1, 1)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Mesafe: sqrt((x2-x1)^2 + (y2-y1)^2)
- Orta nokta: ((x1+x2)/2, (y1+y2)/2)
- Collinear kontrol: Üç noktanın oluşturduğu üçgenin alanı 0 ise collinear
  Alan = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
"""

import math

def calculate_distance(p1, p2):
    """İki nokta arasındaki Öklid mesafesini hesaplar"""
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def midpoint(p1, p2):
    """İki noktanın orta noktasını bulur"""
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def is_collinear(p1, p2, p3):
    """Üç noktanın aynı doğru üzerinde olup olmadığını kontrol eder"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Üçgenin alanını hesapla (0 ise collinear)
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area < 1e-10  # Float hassasiyeti için küçük threshold


print("\n--- Koordinat Sistemi ---")

# Test noktaları
p1 = (0, 0)
p2 = (3, 4)
p3 = (6, 8)
p4 = (1, 1)

# Mesafe hesaplama
dist_12 = calculate_distance(p1, p2)
print(f"p1{p1} ile p2{p2} arası mesafe: {dist_12:.2f}")

dist_13 = calculate_distance(p1, p3)
print(f"p1{p1} ile p3{p3} arası mesafe: {dist_13:.2f}")

dist_23 = calculate_distance(p2, p3)
print(f"p2{p2} ile p3{p3} arası mesafe: {dist_23:.2f}")

# Orta nokta bulma
mid_12 = midpoint(p1, p2)
print(f"\np1 ve p2'nin orta noktası: {mid_12}")

mid_24 = midpoint(p2, p4)
print(f"p2 ve p4'ün orta noktası: {mid_24}")

# Collinearity kontrolü
print(f"\np1{p1}, p2{p2}, p3{p3} collinear mı? {is_collinear(p1, p2, p3)}")
print(f"p1{p1}, p2{p2}, p4{p4} collinear mı? {is_collinear(p1, p2, p4)}")

# Bonus: En yakın nokta çiftini bulma
points = [p1, p2, p3, p4]
min_distance = float('inf')
closest_pair = None

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = calculate_distance(points[i], points[j])
        if dist < min_distance:
            min_distance = dist
            closest_pair = (points[i], points[j])

print(f"\nEn yakın nokta çifti: {closest_pair[0]} ve {closest_pair[1]}")
print(f"Aralarındaki mesafe: {min_distance:.2f}")


# =============================================================================
# SORU 11: [Zor] Tuple ile Matrix İşlemleri
# =============================================================================
# Tuple'lardan oluşan matrix ile çalışın:
# matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
#
# 1. Her satırın toplamını hesaplayın
# 2. Her sütunun toplamını hesaplayın
# 3. Ana köşegen (diagonal) elemanlarını bulun
# 4. Matrix'in transpozunu alın
# 5. Matrix'in en büyük elemanını ve konumunu bulun

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Matrix: tuple'lardan oluşan tuple (satırlar)
- Satır toplamı: Her satır tuple'ını topla
- Sütun toplamı: Her sütun için elemanları topla
- Ana köşegen: matrix[i][i] elemanları
- Transpose: Satır-sütun yer değiştir
"""

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print("\n--- Matrix İşlemleri ---")
print("Matrix:")
for row in matrix:
    print(row)

# 1. Satır toplamları
print("\nSatır Toplamları:")
for i, row in enumerate(matrix):
    row_sum = sum(row)
    print(f"Satır {i}: {row_sum}")

# 2. Sütun toplamları
print("\nSütun Toplamları:")
num_cols = len(matrix[0])
for col in range(num_cols):
    col_sum = sum(matrix[row][col] for row in range(len(matrix)))
    print(f"Sütun {col}: {col_sum}")

# 3. Ana köşegen
diagonal = tuple(matrix[i][i] for i in range(len(matrix)))
print(f"\nAna köşegen: {diagonal}")
print(f"Köşegen toplamı: {sum(diagonal)}")

# 4. Transpose
transpose = tuple(tuple(matrix[row][col] for row in range(len(matrix)))
                  for col in range(num_cols))
print("\nTranspose:")
for row in transpose:
    print(row)

# 5. En büyük eleman ve konumu
max_value = float('-inf')
max_position = None

for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value > max_value:
            max_value = value
            max_position = (i, j)

print(f"\nEn büyük eleman: {max_value}")
print(f"Konumu: satır {max_position[0]}, sütun {max_position[1]}")

# Bonus: Her elemanın karesini alma
squared = tuple(tuple(x**2 for x in row) for row in matrix)
print("\nHer elemanın karesi:")
for row in squared:
    print(row)

# Bonus: Matrix düzleştirme (flatten)
flat = tuple(element for row in matrix for element in row)
print(f"\nDüzleştirilmiş: {flat}")


# =============================================================================
# SORU 12: [Challenge] Tuple ile Histogram Oluşturma
# =============================================================================
# Bir metin içindeki kelime sıklıklarını tuple listesi olarak gösterin:
# text = "python python java python javascript java python java"
#
# 1. Her kelimenin kaç kez geçtiğini bulun
# 2. Sonuçları (kelime, sıklık) tuple'ları olarak kaydedin
# 3. Sıklığa göre azalan sıralayın
# 4. En sık geçen 3 kelimeyi bulun
# 5. ASCII karakterler ile histogram çizin (her * bir tekrar)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Kelimeleri ayır ve say
- Dictionary ile sayma, sonra tuple listesine çevir
- sorted() ile sıklığa göre sırala
- Histogram için * karakterini tekrarla
"""

text = "python python java python javascript java python java python cpp java javascript"

print("\n--- Kelime Sıklığı Histogramı ---")
print(f"Metin: {text}\n")

# 1. Kelimeleri say
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# 2. Tuple listesine çevir
word_tuples = [(word, count) for word, count in word_count.items()]
print("Kelime-Sıklık Tuple'ları:")
print(word_tuples)

# 3. Sıklığa göre azalan sıralama
sorted_words = sorted(word_tuples, key=lambda x: x[1], reverse=True)
print(f"\nSıklığa göre sıralı: {sorted_words}")

# 4. En sık geçen 3 kelime
top_3 = sorted_words[:3]
print(f"\nEn sık 3 kelime:")
for word, count in top_3:
    print(f"  {word}: {count} kez")

# 5. Histogram çizimi
print("\n--- Histogram ---")
max_word_len = max(len(word) for word, _ in sorted_words)

for word, count in sorted_words:
    bar = "*" * count
    print(f"{word:<{max_word_len}} | {bar} ({count})")

# İstatistikler
total_words = len(words)
unique_words = len(word_count)
print(f"\n--- İstatistikler ---")
print(f"Toplam kelime: {total_words}")
print(f"Benzersiz kelime: {unique_words}")
print(f"En sık kelime: {sorted_words[0][0]} ({sorted_words[0][1]} kez)")
print(f"En az kelime: {sorted_words[-1][0]} ({sorted_words[-1][1]} kez)")

# Bonus: Yüzdelik hesaplama
print("\n--- Yüzdelik Dağılım ---")
for word, count in sorted_words:
    percentage = (count / total_words) * 100
    print(f"{word}: %{percentage:.1f}")


# =============================================================================
# SORU 13: [Challenge] Tuple ile Veri Gruplama ve Aggregation
# =============================================================================
# Çalışan verileri: (isim, departman, maaş)
# employees = [
#     ("Ali", "IT", 8000),
#     ("Ayşe", "HR", 6000),
#     ("Mehmet", "IT", 9000),
#     ("Zeynep", "Sales", 7000),
#     ("Can", "HR", 6500),
#     ("Elif", "IT", 8500),
#     ("Ahmet", "Sales", 7500)
# ]
#
# 1. Departmana göre grupla ve her departmanın:
#    - Toplam maaşını
#    - Ortalama maaşını
#    - Çalışan sayısını
#    - En yüksek ve en düşük maaşı hesapla
# 2. En yüksek ortalama maaşlı departmanı bul
# 3. Sonuçları güzel formatta yazdır

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Departmana göre gruplama yapıyoruz
- Her grup için istatistik hesaplıyoruz
- Dictionary ile gruplama, sonra tuple listesine çevirme
- Aggregation: sum, avg, count, min, max
"""

employees = [
    ("Ali", "IT", 8000),
    ("Ayşe", "HR", 6000),
    ("Mehmet", "IT", 9000),
    ("Zeynep", "Sales", 7000),
    ("Can", "HR", 6500),
    ("Elif", "IT", 8500),
    ("Ahmet", "Sales", 7500)
]

print("\n--- Çalışan Veri Analizi ---")
print(f"Toplam çalışan: {len(employees)}\n")

# Departmana göre gruplama
departments = {}

for name, dept, salary in employees:
    if dept not in departments:
        departments[dept] = []
    departments[dept].append((name, salary))

# Her departman için istatistikler
dept_stats = []

for dept, workers in departments.items():
    salaries = [salary for _, salary in workers]

    stats = (
        dept,
        len(workers),                    # Çalışan sayısı
        sum(salaries),                   # Toplam maaş
        sum(salaries) / len(workers),    # Ortalama maaş
        max(salaries),                   # En yüksek maaş
        min(salaries)                    # En düşük maaş
    )
    dept_stats.append(stats)

# Ortalama maaşa göre sırala
dept_stats_sorted = sorted(dept_stats, key=lambda x: x[3], reverse=True)

# Güzel formatta yazdırma
print("=" * 90)
print(f"{'Departman':<12} {'Çalışan':<10} {'Toplam':<15} {'Ortalama':<15} {'Max':<12} {'Min':<12}")
print("=" * 90)

for dept, count, total, avg, max_sal, min_sal in dept_stats_sorted:
    print(f"{dept:<12} {count:<10} {total:>13,} ₺  {avg:>13,.0f} ₺  {max_sal:>10,} ₺  {min_sal:>10,} ₺")

print("=" * 90)

# En yüksek ortalama maaşlı departman
best_dept = dept_stats_sorted[0]
print(f"\n🏆 En yüksek ortalama maaş: {best_dept[0]} Departmanı ({best_dept[3]:,.0f} ₺)")

# Genel istatistikler
all_salaries = [salary for _, _, salary in employees]
print(f"\n--- Genel İstatistikler ---")
print(f"Toplam maaş ödemesi: {sum(all_salaries):,} ₺")
print(f"Ortalama maaş: {sum(all_salaries)/len(all_salaries):,.0f} ₺")
print(f"En yüksek maaş: {max(all_salaries):,} ₺")
print(f"En düşük maaş: {min(all_salaries):,} ₺")

# Departman dağılımı
print(f"\n--- Departman Dağılımı ---")
for dept, count, _, _, _, _ in dept_stats_sorted:
    percentage = (count / len(employees)) * 100
    bar = "█" * int(percentage / 5)
    print(f"{dept:<12} | {bar} {percentage:.1f}%")


# =============================================================================
# SORU 14: [Challenge] Tuple ile Graph (Kenar Listesi)
# =============================================================================
# Bir graph'ı tuple listesi olarak temsil edin (kenar listesi):
# edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
#
# 1. Tüm benzersiz düğümleri (node) bulun
# 2. Her düğümün derece sayısını (kaç kenarı var) hesaplayın
# 3. En çok bağlantılı düğümü bulun
# 4. Verilen iki düğüm arasında direkt bağlantı var mı kontrol edin
# 5. Her düğümün komşularını listeleyin

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Graph yönsüz (undirected) varsayıyoruz
- Derece (degree): Bir düğümün kaç kenarı olduğu
- Adjacency: Bir düğümün komşuları
- Tuple ile graph temsili hafif ve okunabilir
"""

edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]

print("\n--- Graph Analizi (Kenar Listesi) ---")
print(f"Kenarlar: {edges}\n")

# 1. Benzersiz düğümleri bulma
nodes = set()
for edge in edges:
    nodes.add(edge[0])
    nodes.add(edge[1])

nodes = sorted(nodes)  # Sıralı liste
print(f"Düğümler: {nodes}")
print(f"Toplam düğüm sayısı: {len(nodes)}")
print(f"Toplam kenar sayısı: {len(edges)}")

# 2. Her düğümün derece sayısı
degree = {node: 0 for node in nodes}

for node1, node2 in edges:
    degree[node1] += 1
    degree[node2] += 1

print(f"\n--- Derece Dağılımı ---")
for node, deg in sorted(degree.items()):
    print(f"Düğüm {node}: derece {deg}")

# 3. En çok bağlantılı düğüm
max_degree_node = max(degree.items(), key=lambda x: x[1])
print(f"\nEn çok bağlantılı düğüm: {max_degree_node[0]} (derece: {max_degree_node[1]})")

# 4. İki düğüm arası direkt bağlantı kontrolü
def is_connected(node1, node2, edge_list):
    """İki düğüm arasında direkt kenar var mı?"""
    return (node1, node2) in edge_list or (node2, node1) in edge_list

print(f"\n--- Bağlantı Kontrolü ---")
print(f"A-B bağlantısı var mı? {is_connected('A', 'B', edges)}")
print(f"A-E bağlantısı var mı? {is_connected('A', 'E', edges)}")
print(f"B-C bağlantısı var mı? {is_connected('B', 'C', edges)}")

# 5. Her düğümün komşuları (adjacency list)
adjacency = {node: [] for node in nodes}

for node1, node2 in edges:
    adjacency[node1].append(node2)
    adjacency[node2].append(node1)  # Yönsüz graph

print(f"\n--- Komşuluk Listesi ---")
for node, neighbors in sorted(adjacency.items()):
    print(f"{node}: {sorted(neighbors)}")

# Bonus: Graph özellikleri
total_degree = sum(degree.values())
avg_degree = total_degree / len(nodes)
print(f"\n--- Graph Özellikleri ---")
print(f"Toplam derece: {total_degree}")
print(f"Ortalama derece: {avg_degree:.2f}")
print(f"Yoğunluk: {len(edges) / (len(nodes) * (len(nodes) - 1) / 2):.2%}")


# =============================================================================
# ALIŞTIRMALARIN SONU
# =============================================================================

print("\n" + "="*80)
print("TEBRİKLER! TÜM ALIŞTIRMALARI TAMAMLADINIZ!")
print("="*80)
print("\nBu bölümde şunları öğrendiniz:")
print("✓ Tuple oluşturma ve temel işlemler")
print("✓ Tuple immutability (değiştirilemezlik)")
print("✓ İndexleme ve slicing")
print("✓ Tuple metodları (count, index)")
print("✓ Tuple unpacking ve extended unpacking")
print("✓ Tuple ile çoklu değer döndürme")
print("✓ Named tuple kullanımı")
print("✓ Tuple ile sıralama ve karşılaştırma")
print("✓ Tuple vs List farkları")
print("✓ Gerçek dünya uygulamaları (veri analizi, koordinat, graph)")
print("\nSıradaki konu: 07-Dictionaries")
print("="*80)
