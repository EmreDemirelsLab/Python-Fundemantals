# Operators (Operatörler)

## 📌 İçindekiler
1. [Aritmetik Operatörler](#aritmetik-operatörler)
2. [Karşılaştırma Operatörleri](#karşılaştırma-operatörleri)
3. [Mantıksal Operatörler](#mantıksal-operatörler)
4. [Atama Operatörleri](#atama-operatörleri)
5. [Kimlik Operatörleri](#kimlik-operatörleri)
6. [Üyelik Operatörleri](#üyelik-operatörleri)
7. [Bitwise Operatörler](#bitwise-operatörler)
8. [Operatör Önceliği](#operatör-önceliği)

---

## Aritmetik Operatörler

Matematiksel işlemler yapmak için kullanılır.

### Temel Aritmetik Operatörler

| Operatör | İşlem | Örnek | Sonuç |
|----------|-------|-------|--------|
| + | Toplama | 5 + 3 | 8 |
| - | Çıkarma | 5 - 3 | 2 |
| * | Çarpma | 5 * 3 | 15 |
| / | Bölme | 5 / 2 | 2.5 |
| // | Tam Bölme | 5 // 2 | 2 |
| % | Mod (Kalan) | 5 % 2 | 1 |
| ** | Üs Alma | 5 ** 2 | 25 |

### Örnek 1: Temel İşlemler

```python
a = 10
b = 3

print("Toplama:", a + b)          # 13
print("Çıkarma:", a - b)          # 7
print("Çarpma:", a * b)           # 30
print("Bölme:", a / b)            # 3.333...
print("Tam Bölme:", a // b)       # 3
print("Mod (Kalan):", a % b)      # 1
print("Üs Alma:", a ** b)         # 1000
```

### Örnek 2: Negatif Sayılarla İşlemler

```python
x = -10
y = 3

print("Negatif toplama:", x + y)      # -7
print("Negatif çarpma:", x * y)       # -30
print("Negatif bölme:", x / y)        # -3.333...
print("Negatif tam bölme:", x // y)   # -4 (dikkat!)
print("Negatif mod:", x % y)          # 2 (dikkat!)

# Tam bölme her zaman aşağı yuvarlar (floor)
print("\nPositif tam bölme: 7 // 2 =", 7 // 2)      # 3
print("Negatif tam bölme: -7 // 2 =", -7 // 2)      # -4
```

### Örnek 3: Float ve Integer İşlemleri

```python
# Integer + Integer = Integer
result1 = 5 + 3
print(result1, type(result1))  # 8 <class 'int'>

# Integer + Float = Float
result2 = 5 + 3.0
print(result2, type(result2))  # 8.0 <class 'float'>

# Bölme her zaman float döndürür (Python 3)
result3 = 10 / 5
print(result3, type(result3))  # 2.0 <class 'float'>

# Tam bölme integer döndürebilir
result4 = 10 // 3
print(result4, type(result4))  # 3 <class 'int'>
```

### Örnek 4: String ve Sayılarla İşlemler

```python
# String toplama (concatenation)
text1 = "Hello"
text2 = "World"
result = text1 + " " + text2
print(result)  # Hello World

# String çarpma (repetition)
stars = "*" * 10
print(stars)  # **********

# String ve sayı direkt toplanamaz
# print("Age: " + 25)  # TypeError!

# Doğru kullanım:
age = 25
print("Age: " + str(age))     # Age: 25
print(f"Age: {age}")          # Age: 25
```

### Örnek 5: Liste ve Tuple İşlemleri

```python
# Liste toplama
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # [1, 2, 3, 4, 5, 6]

# Liste çarpma
numbers = [0] * 5
print(numbers)  # [0, 0, 0, 0, 0]

# Tuple işlemleri
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # (1, 2, 3, 4)
```

---

## Karşılaştırma Operatörleri

İki değeri karşılaştırır ve boolean (True/False) döndürür.

| Operatör | Açıklama | Örnek | Sonuç |
|----------|----------|-------|--------|
| == | Eşit mi? | 5 == 5 | True |
| != | Eşit değil mi? | 5 != 3 | True |
| > | Büyük mü? | 5 > 3 | True |
| < | Küçük mü? | 5 < 3 | False |
| >= | Büyük veya eşit mi? | 5 >= 5 | True |
| <= | Küçük veya eşit mi? | 5 <= 3 | False |

### Örnek 6: Sayı Karşılaştırmaları

```python
x = 10
y = 5

print("x == y:", x == y)    # False
print("x != y:", x != y)    # True
print("x > y:", x > y)      # True
print("x < y:", x < y)      # False
print("x >= y:", x >= y)    # True
print("x <= y:", x <= y)    # False

# Zincir karşılaştırma
age = 25
print(18 <= age < 65)       # True
print(10 < x < 20)          # True (10 < 10 < 20)
```

### Örnek 7: String Karşılaştırmaları

```python
# String'ler lexicographic (alfabetik) olarak karşılaştırılır
name1 = "Alice"
name2 = "Bob"

print(name1 == name2)       # False
print(name1 < name2)        # True (A, B'den önce gelir)

# Büyük-küçük harf duyarlı
print("python" == "Python")  # False
print("python" == "python")  # True

# Case-insensitive karşılaştırma
print("python".lower() == "Python".lower())  # True

# String uzunluğu karşılaştırma
print(len("hello") > len("hi"))  # True
```

### Örnek 8: Liste ve Tuple Karşılaştırmaları

```python
# Listeler eleman eleman karşılaştırılır
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(list1 == list2)       # True
print(list1 == list3)       # False
print(list1 < list3)        # True (3 < 4)

# İlk farklı eleman karşılaştırılır
print([1, 2, 3] < [1, 3, 0])  # True (2 < 3)
print([1, 2] < [1, 2, 0])     # True (daha kısa)
```

---

## Mantıksal Operatörler

Boolean değerleri birleştirmek için kullanılır.

| Operatör | Açıklama | Örnek | Sonuç |
|----------|----------|-------|--------|
| and | Her ikisi de True ise True | True and False | False |
| or | En az biri True ise True | True or False | True |
| not | Değeri tersine çevirir | not True | False |

### Örnek 9: Temel Mantıksal İşlemler

```python
# and operatörü (VE)
print(True and True)     # True
print(True and False)    # False
print(False and False)   # False

# or operatörü (VEYA)
print(True or True)      # True
print(True or False)     # True
print(False or False)    # False

# not operatörü (DEĞİL)
print(not True)          # False
print(not False)         # True
```

### Örnek 10: Pratik Mantıksal İşlemler

```python
age = 25
has_license = True
has_car = False

# Araç kullanabilir mi?
can_drive = age >= 18 and has_license
print("Araç kullanabilir mi?", can_drive)  # True

# Araç ihtiyacı var mı?
needs_car = has_license and not has_car
print("Araç ihtiyacı var mı?", needs_car)  # True

# Birden fazla koşul
is_adult = age >= 18
is_senior = age >= 65
is_working_age = is_adult and not is_senior
print("Çalışma yaşında mı?", is_working_age)  # True
```

### Örnek 11: Short-Circuit Evaluation

```python
# and operatörü: İlk False'da durur
print("Test 1:", False and print("Bu çalışmaz"))  # False (print çalışmaz)

# or operatörü: İlk True'da durur
print("Test 2:", True or print("Bu çalışmaz"))    # True (print çalışmaz)

# Pratik kullanım: Güvenli değer kontrolü
value = None
# result = value.upper()  # AttributeError!
result = value and value.upper()  # None (hata vermez)
print("Sonuç:", result)

# Varsayılan değer
name = ""
display_name = name or "Misafir"
print("Hoş geldin,", display_name)  # Hoş geldin, Misafir
```

### Örnek 12: Karmaşık Mantıksal İfadeler

```python
# Parantez kullanımı
a, b, c = True, False, True

result1 = a and b or c
print("a and b or c:", result1)  # True

result2 = a and (b or c)
print("a and (b or c):", result2)  # True

result3 = (a and b) or c
print("(a and b) or c:", result3)  # True

# DeMorgan Kuralları
x, y = True, False
print("not (x and y):", not (x and y))              # True
print("(not x) or (not y):", (not x) or (not y))    # True (eşdeğer)

print("not (x or y):", not (x or y))                # False
print("(not x) and (not y):", (not x) and (not y))  # False (eşdeğer)
```

---

## Atama Operatörleri

Değişkenlere değer atamak ve güncellemek için kullanılır.

| Operatör | Örnek | Eşdeğer |
|----------|-------|---------|
| = | x = 5 | x = 5 |
| += | x += 3 | x = x + 3 |
| -= | x -= 3 | x = x - 3 |
| *= | x *= 3 | x = x * 3 |
| /= | x /= 3 | x = x / 3 |
| //= | x //= 3 | x = x // 3 |
| %= | x %= 3 | x = x % 3 |
| **= | x **= 3 | x = x ** 3 |
| &= | x &= 3 | x = x & 3 |
| \|= | x \|= 3 | x = x \| 3 |
| ^= | x ^= 3 | x = x ^ 3 |
| >>= | x >>= 3 | x = x >> 3 |
| <<= | x <<= 3 | x = x << 3 |

### Örnek 13: Temel Atama Operatörleri

```python
# Basit atama
x = 10
print("x =", x)  # 10

# Toplama ataması
x += 5  # x = x + 5
print("x += 5:", x)  # 15

# Çıkarma ataması
x -= 3  # x = x - 3
print("x -= 3:", x)  # 12

# Çarpma ataması
x *= 2  # x = x * 2
print("x *= 2:", x)  # 24

# Bölme ataması
x /= 4  # x = x / 4
print("x /= 4:", x)  # 6.0

# Mod ataması
x = 17
x %= 5  # x = x % 5
print("x %= 5:", x)  # 2
```

### Örnek 14: Çoklu Atama

```python
# Aynı değeri birden fazla değişkene atama
a = b = c = 0
print(a, b, c)  # 0 0 0

# Farklı değerleri atama (tuple unpacking)
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# Liste unpacking
numbers = [10, 20, 30]
first, second, third = numbers
print(first, second, third)  # 10 20 30

# * operatörü ile kalan elemanları alma
a, *rest, b = [1, 2, 3, 4, 5]
print(a)     # 1
print(rest)  # [2, 3, 4]
print(b)     # 5
```

---

## Kimlik Operatörleri

İki değişkenin aynı objeye referans verip vermediğini kontrol eder.

| Operatör | Açıklama | Örnek |
|----------|----------|-------|
| is | Aynı obje mi? | x is y |
| is not | Farklı obje mi? | x is not y |

### Örnek 15: is vs ==

```python
# == değer eşitliğini kontrol eder
# is obje eşitliğini (identity) kontrol eder

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b:", a == b)      # True (aynı değerler)
print("a is b:", a is b)      # False (farklı objeler)
print("a is c:", a is c)      # True (aynı obje)

# None kontrolü (daima 'is' kullan)
value = None
print(value is None)          # True (doğru)
print(value == None)          # True (çalışır ama önerilmez)

# Boolean kontrolü
flag = True
print(flag is True)           # True (küçük değerler cache'lenir)

# Integer caching (-5 to 256)
x = 256
y = 256
print(x is y)                 # True (cached)

m = 257
n = 257
print(m is n)                 # False (not cached)
```

---

## Üyelik Operatörleri

Bir değerin sequence içinde olup olmadığını kontrol eder.

| Operatör | Açıklama | Örnek |
|----------|----------|-------|
| in | İçinde var mı? | x in list |
| not in | İçinde yok mu? | x not in list |

### Örnek 16: Liste ve Tuple'da Üyelik

```python
numbers = [1, 2, 3, 4, 5]

print(3 in numbers)           # True
print(10 in numbers)          # False
print(10 not in numbers)      # True

# Tuple
colors = ("red", "green", "blue")
print("red" in colors)        # True
print("yellow" in colors)     # False
```

### Örnek 17: String'de Üyelik

```python
text = "Hello World"

print("Hello" in text)        # True
print("hello" in text)        # False (case-sensitive)
print("xyz" in text)          # False
print("World" not in text)    # False

# Substring kontrolü
email = "user@example.com"
print("@" in email)           # True
print(email.endswith(".com")) # True
```

### Örnek 18: Dictionary'de Üyelik

```python
person = {
    "name": "Ali",
    "age": 25,
    "city": "Istanbul"
}

# Key kontrolü (varsayılan)
print("name" in person)       # True
print("email" in person)      # False

# Value kontrolü
print("Ali" in person.values())      # True
print(25 in person.values())         # True

# Key-value çifti kontrolü
print(("name", "Ali") in person.items())  # True
```

---

## Bitwise Operatörler

Sayıların binary (ikili) gösteriminde bit düzeyinde işlem yapar.

| Operatör | Açıklama | Örnek | Sonuç |
|----------|----------|-------|--------|
| & | AND | 5 & 3 | 1 |
| \| | OR | 5 \| 3 | 7 |
| ^ | XOR | 5 ^ 3 | 6 |
| ~ | NOT | ~5 | -6 |
| << | Left shift | 5 << 1 | 10 |
| >> | Right shift | 5 >> 1 | 2 |

### Örnek 19: Bitwise Temel İşlemler

```python
a = 5   # Binary: 0101
b = 3   # Binary: 0011

# AND (&): Her iki bit de 1 ise 1
result = a & b  # 0101 & 0011 = 0001 = 1
print(f"{a} & {b} = {result}")

# OR (|): En az bir bit 1 ise 1
result = a | b  # 0101 | 0011 = 0111 = 7
print(f"{a} | {b} = {result}")

# XOR (^): Bitler farklı ise 1
result = a ^ b  # 0101 ^ 0011 = 0110 = 6
print(f"{a} ^ {b} = {result}")

# NOT (~): Bitleri tersine çevirir
result = ~a     # ~0101 = -6 (two's complement)
print(f"~{a} = {result}")

# Left Shift (<<): Sola kaydırma (2 ile çarpma)
result = a << 1  # 0101 << 1 = 1010 = 10
print(f"{a} << 1 = {result}")

# Right Shift (>>): Sağa kaydırma (2 ile bölme)
result = a >> 1  # 0101 >> 1 = 0010 = 2
print(f"{a} >> 1 = {result}")
```

### Örnek 20: Bitwise Pratik Kullanımlar

```python
# Çift/tek kontrolü
def is_even(n):
    return (n & 1) == 0

print("10 çift mi?", is_even(10))  # True
print("7 çift mi?", is_even(7))    # False

# Hızlı çarpma/bölme (2'nin katları için)
num = 10
print(f"{num} * 2 = {num << 1}")   # 20
print(f"{num} * 4 = {num << 2}")   # 40
print(f"{num} / 2 = {num >> 1}")   # 5
print(f"{num} / 4 = {num >> 2}")   # 2

# İki sayıyı swap etme (XOR trick)
x, y = 10, 20
print(f"Başlangıç: x={x}, y={y}")
x = x ^ y
y = x ^ y
x = x ^ y
print(f"Swap sonrası: x={x}, y={y}")

# Bit set kontrolü
flags = 0b1010  # 10 in binary
mask = 0b0010   # 2 in binary

# 2. bit set mi?
is_set = (flags & mask) != 0
print(f"2. bit set mi? {is_set}")  # True
```

---

## Operatör Önceliği

Operatörlerin hangi sırada değerlendirileceğini belirler (yüksekten düşüğe):

1. **()** - Parantezler
2. **\*\*** - Üs alma
3. **~, +, -** - Unary NOT, plus, minus
4. **\*, /, //, %** - Çarpma, bölme, tam bölme, mod
5. **+, -** - Toplama, çıkarma
6. **<<, >>** - Bitwise shift
7. **&** - Bitwise AND
8. **^** - Bitwise XOR
9. **|** - Bitwise OR
10. **==, !=, >, <, >=, <=, is, is not, in, not in** - Karşılaştırma
11. **not** - Mantıksal NOT
12. **and** - Mantıksal AND
13. **or** - Mantıksal OR

### Örnek 21: Operatör Önceliği Örnekleri

```python
# Matematiksel öncelik
result = 2 + 3 * 4
print(result)  # 14 (önce çarpma, sonra toplama)

result = (2 + 3) * 4
print(result)  # 20 (parantez önce)

# Üs alma önceliği
result = 2 ** 3 ** 2
print(result)  # 512 (sağdan sola: 3^2=9, 2^9=512)

result = (2 ** 3) ** 2
print(result)  # 64 (önce 2^3=8, sonra 8^2=64)

# Karşılaştırma ve mantıksal
result = 5 > 3 and 10 < 20
print(result)  # True (önce karşılaştırma, sonra and)

result = not 5 > 10 or 3 < 7
print(result)  # True

# Karışık örnek
x = 10
result = x > 5 and x < 15 or x == 20
print(result)  # True
# Değerlendirme sırası: (x > 5) and (x < 15) or (x == 20)
```

---

## 💡 Önemli Notlar

1. **Bölme İşlemi**: Python 3'te `/` her zaman float döndürür
2. **Tam Bölme**: `//` operatörü her zaman aşağı yuvarlar (floor)
3. **is vs ==**: `is` obje eşitliği, `==` değer eşitliği kontrol eder
4. **Short-Circuit**: `and` ve `or` operatörleri gerektiğinde erken durur
5. **Zincir Karşılaştırma**: `a < b < c` şeklinde kullanılabilir
6. **Bitwise Operatörler**: Performans kritik uygulamalarda kullanışlıdır
7. **Parantez Kullanımı**: Öncelik karmaşıksa parantez kullanın

---

## 🎯 Özet

Bu bölümde öğrendikleriniz:
- ✅ Aritmetik operatörler (+, -, *, /, //, %, **)
- ✅ Karşılaştırma operatörleri (==, !=, >, <, >=, <=)
- ✅ Mantıksal operatörler (and, or, not)
- ✅ Atama operatörleri (=, +=, -=, vb.)
- ✅ Kimlik operatörleri (is, is not)
- ✅ Üyelik operatörleri (in, not in)
- ✅ Bitwise operatörler (&, |, ^, ~, <<, >>)
- ✅ Operatör önceliği

Şimdi `exercises.py` dosyasındaki alıştırmaları yaparak öğrendiklerinizi pekiştirebilirsiniz!
