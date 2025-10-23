# Variables and Data Types (Değişkenler ve Veri Tipleri)

## 📌 İçindekiler
1. [Değişkenler Nedir?](#değişkenler-nedir)
2. [Değişken İsimlendirme Kuralları](#değişken-isimlendirme-kuralları)
3. [Temel Veri Tipleri](#temel-veri-tipleri)
4. [Type Conversion (Tür Dönüşümü)](#type-conversion-tür-dönüşümü)
5. [Type Checking](#type-checking)
6. [Dinamik Typing](#dinamik-typing)

---

## Değişkenler Nedir?

Değişkenler, programımızda kullanmak üzere verileri bellekte saklamamızı sağlayan isimlendirilmiş konteynerlerdir. Python'da bir değişken oluşturmak için sadece bir isim ve değer atamamız yeterlidir.

### Örnek 1: Basit Değişken Tanımlama

```python
# Değişken tanımlama
name = "Ali"
age = 25
height = 1.75
is_student = True

print(name)        # Ali
print(age)         # 25
print(height)      # 1.75
print(is_student)  # True
```

### Örnek 2: Çoklu Değişken Atama

```python
# Aynı anda birden fazla değişken tanımlama
x, y, z = 10, 20, 30
print(x, y, z)  # 10 20 30

# Aynı değeri birden fazla değişkene atama
a = b = c = 100
print(a, b, c)  # 100 100 100
```

### Örnek 3: Değişken Değerini Değiştirme

```python
# Değişken değeri değiştirilebilir
counter = 0
print("İlk değer:", counter)  # 0

counter = 10
print("Yeni değer:", counter)  # 10

counter = counter + 5
print("Güncel değer:", counter)  # 15
```

---

## Değişken İsimlendirme Kuralları

Python'da değişken isimlendirirken dikkat etmemiz gereken kurallar vardır.

### ✅ Geçerli Kurallar:

1. Harf, rakam ve alt çizgi (_) kullanılabilir
2. Rakamla başlayamaz
3. Büyük-küçük harf duyarlıdır (case-sensitive)
4. Python anahtar kelimeleri kullanılamaz

### Örnek 4: İsimlendirme Örnekleri

```python
# Geçerli değişken isimleri
name = "Ali"
first_name = "Mehmet"
age1 = 25
_private = "gizli"
firstName = "Ayşe"  # camelCase
CONSTANT_VALUE = 100  # Sabitler için BÜYÜK HARF önerilir

# Geçersiz değişken isimleri (hata verir)
# 1name = "Ali"  # Rakamla başlayamaz
# first-name = "Ali"  # Tire kullanılamaz
# for = 10  # Anahtar kelime kullanılamaz
```

### Örnek 5: Case Sensitivity

```python
# Python büyük-küçük harf duyarlıdır
Name = "Ali"
name = "Mehmet"
NAME = "Ayşe"

print(Name)  # Ali
print(name)  # Mehmet
print(NAME)  # Ayşe
```

### İsimlendirme Stilleri:

```python
# Snake case (Python'da önerilen)
first_name = "Ali"
user_age = 25

# Camel case
firstName = "Ali"
userAge = 25

# Pascal case (Class isimleri için)
UserName = "Ali"

# Sabitler için
MAX_SIZE = 100
PI = 3.14159
```

---

## Temel Veri Tipleri

Python'da dört temel veri tipi vardır:

### 1. Integer (int) - Tam Sayılar

```python
# Tam sayılar
age = 25
year = 2025
negative = -42
big_number = 1000000

print(type(age))  # <class 'int'>

# Farklı sayı sistemleri
binary = 0b1010      # Binary (İkili) - 10
octal = 0o12         # Octal (Sekizli) - 10
hexadecimal = 0xA    # Hexadecimal (Onaltılı) - 10

print(binary, octal, hexadecimal)  # 10 10 10
```

### Örnek 6: Integer İşlemleri

```python
x = 10
y = 3

print(x + y)   # Toplama: 13
print(x - y)   # Çıkarma: 7
print(x * y)   # Çarpma: 30
print(x / y)   # Bölme: 3.333...
print(x // y)  # Tam bölme: 3
print(x % y)   # Mod (kalan): 1
print(x ** y)  # Üs alma: 1000
```

### 2. Float - Ondalıklı Sayılar

```python
# Ondalıklı sayılar
height = 1.75
temperature = -5.5
pi = 3.14159

print(type(height))  # <class 'float'>

# Bilimsel gösterim
scientific = 2.5e3  # 2.5 * 10^3 = 2500
print(scientific)   # 2500.0

small = 1.5e-3      # 1.5 * 10^-3 = 0.0015
print(small)        # 0.0015
```

### Örnek 7: Float Hassasiyet Problemi

```python
# Float hassasiyet sorunu
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 (Beklenen: 0.3)

# Çözüm: round() fonksiyonu
result = round(0.1 + 0.2, 2)
print(result)  # 0.3

# Veya Decimal modülü kullanılabilir
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.2')
print(result)  # 0.3
```

### 3. String (str) - Metin

```python
# String tanımlama
name = "Ali"
surname = 'Yılmaz'
message = """Çok satırlı
metin yazabilirsiniz"""

print(type(name))  # <class 'str'>
```

### Örnek 8: String İşlemleri

```python
first_name = "Ali"
last_name = "Yılmaz"

# String birleştirme
full_name = first_name + " " + last_name
print(full_name)  # Ali Yılmaz

# String tekrarlama
stars = "*" * 10
print(stars)  # **********

# String uzunluğu
length = len(full_name)
print(length)  # 10

# String indexing
print(full_name[0])   # A
print(full_name[-1])  # z

# String slicing
print(full_name[0:3])   # Ali
print(full_name[4:])    # Yılmaz
print(full_name[:3])    # Ali
```

### Örnek 9: String Metodları

```python
text = "Python Programming"

print(text.upper())       # PYTHON PROGRAMMING
print(text.lower())       # python programming
print(text.capitalize())  # Python programming
print(text.title())       # Python Programming

print(text.startswith("Python"))  # True
print(text.endswith("ing"))       # True

print(text.replace("Python", "Java"))  # Java Programming
print(text.split())  # ['Python', 'Programming']

# String formatting
name = "Ali"
age = 25

# Method 1: f-string (Python 3.6+)
message = f"Benim adım {name} ve {age} yaşındayım"
print(message)

# Method 2: format()
message = "Benim adım {} ve {} yaşındayım".format(name, age)
print(message)

# Method 3: % formatting (eski yöntem)
message = "Benim adım %s ve %d yaşındayım" % (name, age)
print(message)
```

### 4. Boolean (bool) - Mantıksal Değerler

```python
# Boolean değerler: True veya False
is_student = True
is_graduated = False
has_license = True

print(type(is_student))  # <class 'bool'>
```

### Örnek 10: Boolean İşlemleri

```python
x = True
y = False

# Mantıksal operatörler
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Karşılaştırma sonuçları
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True
print(5 != 3)   # True

# Boolean olarak değerlendirme
# Falsy değerler: False, 0, 0.0, "", [], {}, None
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("text"))  # True
print(bool([]))      # False
print(bool([1, 2]))  # True
```

---

## Type Conversion (Tür Dönüşümü)

Bir veri tipini başka bir veri tipine dönüştürebiliriz.

### Örnek 11: Integer Dönüşümleri

```python
# String to int
age_str = "25"
age_int = int(age_str)
print(age_int, type(age_int))  # 25 <class 'int'>

# Float to int (ondalık kısmı atar)
height = 1.75
height_int = int(height)
print(height_int)  # 1

# Boolean to int
print(int(True))   # 1
print(int(False))  # 0
```

### Örnek 12: Float Dönüşümleri

```python
# String to float
price_str = "19.99"
price_float = float(price_str)
print(price_float, type(price_float))  # 19.99 <class 'float'>

# Int to float
number = 10
number_float = float(number)
print(number_float)  # 10.0

# Boolean to float
print(float(True))   # 1.0
print(float(False))  # 0.0
```

### Örnek 13: String Dönüşümleri

```python
# Int to string
age = 25
age_str = str(age)
print(age_str, type(age_str))  # 25 <class 'str'>

# Float to string
price = 19.99
price_str = str(price)
print(price_str)  # 19.99

# Boolean to string
result = str(True)
print(result)  # True

# List to string (str() kullanarak)
numbers = [1, 2, 3]
numbers_str = str(numbers)
print(numbers_str)  # [1, 2, 3]
```

### Örnek 14: Boolean Dönüşümleri

```python
# Int to bool
print(bool(0))    # False
print(bool(1))    # True
print(bool(-5))   # True
print(bool(100))  # True

# String to bool
print(bool(""))      # False
print(bool("text"))  # True
print(bool("False")) # True (dikkat: string "False" da True'dur!)

# None to bool
print(bool(None))  # False
```

### Örnek 15: Hatalı Dönüşümler

```python
# Hatalı dönüşüm örnekleri
try:
    result = int("abc")  # ValueError
except ValueError as e:
    print("Hata:", e)

try:
    result = float("12.34.56")  # ValueError
except ValueError as e:
    print("Hata:", e)

# Doğru kullanım
number_str = "123abc"
if number_str.isdigit():
    number = int(number_str)
else:
    print("Geçersiz sayı formatı")
```

---

## Type Checking

Bir değişkenin tipini kontrol etmek için `type()` ve `isinstance()` fonksiyonlarını kullanırız.

### Örnek 16: type() Fonksiyonu

```python
name = "Ali"
age = 25
height = 1.75
is_student = True

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

# Type karşılaştırma
if type(age) == int:
    print("age bir integer'dır")

if type(name) == str:
    print("name bir string'dir")
```

### Örnek 17: isinstance() Fonksiyonu

```python
name = "Ali"
age = 25
height = 1.75

# isinstance() daha önerilen yöntemdir
print(isinstance(name, str))     # True
print(isinstance(age, int))      # True
print(isinstance(height, float)) # True

# Birden fazla tip kontrolü
print(isinstance(age, (int, float)))  # True
print(isinstance(name, (int, float))) # False

# Boolean, int'in bir alt sınıfıdır
is_active = True
print(isinstance(is_active, int))  # True
print(isinstance(is_active, bool)) # True
```

---

## Dinamik Typing

Python dinamik tipli bir dildir. Bu, bir değişkenin tipi runtime'da (çalışma zamanında) belirlendiği ve değiştirilebildiği anlamına gelir.

### Örnek 18: Dinamik Tip Değişimi

```python
# Değişken farklı tipte değerler alabilir
variable = 42
print(variable, type(variable))  # 42 <class 'int'>

variable = "Python"
print(variable, type(variable))  # Python <class 'str'>

variable = 3.14
print(variable, type(variable))  # 3.14 <class 'float'>

variable = True
print(variable, type(variable))  # True <class 'bool'>
```

### Örnek 19: Type Hints (Python 3.5+)

```python
# Type hints (tip ipuçları) - zorunlu değil, dokümantasyon amaçlı
name: str = "Ali"
age: int = 25
height: float = 1.75
is_student: bool = True

# Fonksiyonlarda tip ipuçları
def greet(name: str) -> str:
    return f"Merhaba, {name}!"

result = greet("Ali")
print(result)

# Type hints yanlış kullanılsa bile kod çalışır (runtime'da kontrol edilmez)
age: int = "25"  # Hata vermez ama tip ipucu ile uyuşmaz
print(age)  # 25

# Type checking için mypy gibi araçlar kullanılabilir
```

### Örnek 20: Gelişmiş Tip Kullanımı

```python
# None tipi
result = None
print(type(result))  # <class 'NoneType'>

# Complex sayılar
complex_num = 3 + 4j
print(type(complex_num))  # <class 'complex'>
print(complex_num.real)   # 3.0
print(complex_num.imag)   # 4.0

# Bytes
byte_data = b"Hello"
print(type(byte_data))  # <class 'bytes'>

# Range
numbers = range(5)
print(type(numbers))  # <class 'range'>
print(list(numbers))  # [0, 1, 2, 3, 4]
```

---

## 💡 Önemli Notlar

1. **Değişken İsimlendirme**: Anlamlı ve açıklayıcı isimler kullanın
2. **Snake Case**: Python'da değişkenler için `snake_case` kullanımı önerilir
3. **Sabitler**: Değişmeyen değerler için BÜYÜK_HARF kullanın
4. **Type Conversion**: Tip dönüşümlerinde hata kontrolü yapın
5. **Boolean Değerlendirme**: Python'da birçok değer falsy olabilir (0, "", [], None, vb.)
6. **Float Hassasiyeti**: Ondalıklı sayılarla çalışırken hassasiyet sorunlarına dikkat edin
7. **Type Hints**: Modern Python projelerinde tip ipuçları kullanımı önerilir

---

## 🎯 Özet

Bu bölümde öğrendikleriniz:
- ✅ Değişken tanımlama ve kullanma
- ✅ Değişken isimlendirme kuralları
- ✅ Temel veri tipleri (int, float, str, bool)
- ✅ Tip dönüşümleri
- ✅ Type checking yöntemleri
- ✅ Python'ın dinamik typing özelliği

Şimdi `exercises.py` dosyasındaki alıştırmaları yaparak öğrendiklerinizi pekiştirebilirsiniz!
