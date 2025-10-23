# Functions (Fonksiyonlar)

## İçindekiler
1. [Fonksiyonlar Nedir?](#fonksiyonlar-nedir)
2. [Fonksiyon Tanımlama ve Çağırma](#fonksiyon-tanımlama-ve-çağırma)
3. [Parametreler ve Argümanlar](#parametreler-ve-argümanlar)
4. [Return İfadesi](#return-ifadesi)
5. [Default Parametreler](#default-parametreler)
6. [*args ve **kwargs](#args-ve-kwargs)
7. [Lambda Fonksiyonları](#lambda-fonksiyonları)
8. [Scope (Kapsam)](#scope-kapsam)
9. [Recursion (Özyineleme)](#recursion-özyineleme)
10. [Docstrings](#docstrings)

---

## Fonksiyonlar Nedir?

Fonksiyonlar, belirli bir görevi yerine getiren, yeniden kullanılabilir kod bloklarıdır. Fonksiyonlar sayesinde kodunuzu organize edebilir, tekrardan kaçınabilir ve daha okunabilir programlar yazabilirsiniz.

**Fonksiyonların Avantajları:**
- Kod tekrarını önler (DRY - Don't Repeat Yourself)
- Kodu organize eder ve okunabilirliği artırır
- Test edilmesi ve debug edilmesi daha kolaydır
- Bakım ve güncelleme kolaylığı sağlar
- Modüler programlama yapmanızı sağlar

---

## Fonksiyon Tanımlama ve Çağırma

Python'da fonksiyon tanımlamak için `def` anahtar kelimesini kullanırız.

### Örnek 1: Basit Fonksiyon Tanımlama

```python
# Fonksiyon tanımlama
def greet():
    """Basit bir selamlama fonksiyonu"""
    print("Merhaba!")
    print("Python öğreniyorum.")

# Fonksiyonu çağırma
greet()
# Output:
# Merhaba!
# Python öğreniyorum.

# Fonksiyonu birden fazla kez çağırabiliriz
greet()
greet()
```

### Örnek 2: İsimle Selamlama

```python
def greet_person():
    """Kullanıcıya ismiyle selam verir"""
    name = "Ali"
    print(f"Merhaba {name}!")
    print("Nasılsın?")

greet_person()
# Output:
# Merhaba Ali!
# Nasılsın?
```

---

## Parametreler ve Argümanlar

Fonksiyonlara veri göndermek için parametreler kullanırız.

**Terminoloji:**
- **Parametre**: Fonksiyon tanımında belirtilen değişkenler
- **Argüman**: Fonksiyonu çağırırken gönderilen gerçek değerler

### Örnek 3: Tek Parametreli Fonksiyon

```python
def greet_user(name):
    """Parametreyle selamlama fonksiyonu"""
    print(f"Merhaba {name}!")

# Fonksiyonu farklı argümanlarla çağırma
greet_user("Ali")      # Merhaba Ali!
greet_user("Ayşe")     # Merhaba Ayşe!
greet_user("Mehmet")   # Merhaba Mehmet!
```

### Örnek 4: Birden Fazla Parametre

```python
def introduce(name, age, city):
    """Kişi hakkında bilgi verir"""
    print(f"Adı: {name}")
    print(f"Yaşı: {age}")
    print(f"Şehri: {city}")

# Pozisyonel argümanlar (sırası önemli)
introduce("Ali", 25, "İstanbul")
# Output:
# Adı: Ali
# Yaşı: 25
# Şehri: İstanbul

# Keyword argümanlar (sırası önemsiz)
introduce(city="Ankara", name="Ayşe", age=30)
# Output:
# Adı: Ayşe
# Yaşı: 30
# Şehri: Ankara

# Karışık kullanım (pozisyonel önce, keyword sonra)
introduce("Mehmet", age=28, city="İzmir")
```

### Örnek 5: Hesaplama Fonksiyonları

```python
def add(a, b):
    """İki sayıyı toplar"""
    result = a + b
    print(f"{a} + {b} = {result}")

def multiply(x, y):
    """İki sayıyı çarpar"""
    result = x * y
    print(f"{x} × {y} = {result}")

add(5, 3)        # 5 + 3 = 8
multiply(4, 7)   # 4 × 7 = 28
```

---

## Return İfadesi

`return` ifadesi, fonksiyonun bir değer döndürmesini sağlar. Return ifadesi olmayan fonksiyonlar `None` döndürür.

### Örnek 6: Return ile Değer Döndürme

```python
def add_numbers(a, b):
    """İki sayının toplamını döndürür"""
    return a + b

# Dönen değeri değişkene atama
result = add_numbers(10, 20)
print(f"Toplam: {result}")  # Toplam: 30

# Doğrudan kullanma
print(add_numbers(5, 15))   # 20

# Matematik işlemlerinde kullanma
total = add_numbers(3, 7) + add_numbers(2, 8)
print(f"Genel toplam: {total}")  # Genel toplam: 20
```

### Örnek 7: Birden Fazla Değer Döndürme

```python
def calculate(a, b):
    """İki sayının toplam, fark, çarpım ve bölümünü döndürür"""
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None

    return addition, subtraction, multiplication, division

# Tuple unpacking ile değerleri alma
toplam, fark, carpim, bolum = calculate(20, 4)

print(f"Toplam: {toplam}")           # 24
print(f"Fark: {fark}")               # 16
print(f"Çarpım: {carpim}")           # 80
print(f"Bölüm: {bolum}")             # 5.0

# Alternatif: Tuple olarak alma
sonuclar = calculate(15, 3)
print(sonuclar)  # (18, 12, 45, 5.0)
```

### Örnek 8: Koşullu Return

```python
def check_even(number):
    """Sayının çift mi tek mi olduğunu kontrol eder"""
    if number % 2 == 0:
        return "Çift"
    else:
        return "Tek"

print(check_even(10))  # Çift
print(check_even(7))   # Tek

def find_max(a, b, c):
    """Üç sayıdan en büyüğünü bulur"""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(f"En büyük: {find_max(10, 25, 15)}")  # En büyük: 25
```

---

## Default Parametreler

Parametrelere varsayılan değerler atayabilirsiniz. Fonksiyon çağrılırken bu parametreler isteğe bağlı hale gelir.

### Örnek 9: Default Parametre Kullanımı

```python
def greet(name, greeting="Merhaba"):
    """İsteğe bağlı selamlama mesajı ile karşılama"""
    print(f"{greeting}, {name}!")

# Default değer kullanılır
greet("Ali")  # Merhaba, Ali!

# Default değer override edilir
greet("Ayşe", "Günaydın")  # Günaydın, Ayşe!
greet("Mehmet", "İyi akşamlar")  # İyi akşamlar, Mehmet!
```

### Örnek 10: Birden Fazla Default Parametre

```python
def create_profile(name, age=18, city="İstanbul", country="Türkiye"):
    """Kullanıcı profili oluşturur"""
    profile = {
        "name": name,
        "age": age,
        "city": city,
        "country": country
    }
    return profile

# Sadece zorunlu parametre
p1 = create_profile("Ali")
print(p1)
# {'name': 'Ali', 'age': 18, 'city': 'İstanbul', 'country': 'Türkiye'}

# Bazı default değerleri override etme
p2 = create_profile("Ayşe", age=25, city="Ankara")
print(p2)
# {'name': 'Ayşe', 'age': 25, 'city': 'Ankara', 'country': 'Türkiye'}

# Tüm parametreleri belirtme
p3 = create_profile("Mehmet", 30, "İzmir", "Türkiye")
print(p3)
# {'name': 'Mehmet', 'age': 30, 'city': 'İzmir', 'country': 'Türkiye'}
```

### Örnek 11: Mutable Default Parameter Problemi

```python
# ❌ YANLIŞ KULLANIM - Mutable default parameter
def add_item_wrong(item, items=[]):
    """Dikkat! Bu fonksiyon beklenmedik davranış gösterir"""
    items.append(item)
    return items

list1 = add_item_wrong("elma")
print(list1)  # ['elma']

list2 = add_item_wrong("armut")
print(list2)  # ['elma', 'armut'] - Beklenmedik!

# ✅ DOĞRU KULLANIM - None kullanarak
def add_item_correct(item, items=None):
    """Doğru mutable default parameter kullanımı"""
    if items is None:
        items = []
    items.append(item)
    return items

list3 = add_item_correct("elma")
print(list3)  # ['elma']

list4 = add_item_correct("armut")
print(list4)  # ['armut'] - Beklenen davranış!
```

---

## *args ve **kwargs

Python'da fonksiyonlara değişken sayıda argüman göndermek için `*args` ve `**kwargs` kullanılır.

### Örnek 12: *args - Değişken Sayıda Pozisyonel Argüman

```python
def sum_all(*numbers):
    """Verilen tüm sayıları toplar"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))           # 6
print(sum_all(10, 20, 30, 40))    # 100
print(sum_all(5))                 # 5
print(sum_all())                  # 0

def print_items(*items):
    """Tüm öğeleri yazdırır"""
    print(f"Toplam {len(items)} öğe var:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

print_items("elma", "armut", "muz")
# Output:
# Toplam 3 öğe var:
# 1. elma
# 2. armut
# 3. muz
```

### Örnek 13: **kwargs - Değişken Sayıda Keyword Argüman

```python
def print_info(**info):
    """Verilen tüm bilgileri yazdırır"""
    print("Bilgiler:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print_info(name="Ali", age=25, city="İstanbul")
# Output:
# Bilgiler:
#   name: Ali
#   age: 25
#   city: İstanbul

print_info(brand="Tesla", model="Model 3", year=2024, color="Kırmızı")
# Output:
# Bilgiler:
#   brand: Tesla
#   model: Model 3
#   year: 2024
#   color: Kırmızı
```

### Örnek 14: *args ve **kwargs Birlikte Kullanımı

```python
def complete_function(required, *args, default="varsayılan", **kwargs):
    """Tüm parametre tiplerini gösteren örnek"""
    print(f"Zorunlu parametre: {required}")
    print(f"Default parametre: {default}")

    if args:
        print(f"Pozisyonel argümanlar: {args}")

    if kwargs:
        print(f"Keyword argümanlar: {kwargs}")

complete_function("zorunlu değer")
# Output:
# Zorunlu parametre: zorunlu değer
# Default parametre: varsayılan

complete_function("zorunlu", "ekstra1", "ekstra2", default="özel", x=10, y=20)
# Output:
# Zorunlu parametre: zorunlu
# Default parametre: özel
# Pozisyonel argümanlar: ('ekstra1', 'ekstra2')
# Keyword argümanlar: {'x': 10, 'y': 20}
```

### Örnek 15: Argümanları Unpacking İle Gönderme

```python
def calculate_total(price, quantity, tax=0.18):
    """Toplam tutarı hesaplar"""
    subtotal = price * quantity
    total = subtotal * (1 + tax)
    return total

# Normal kullanım
result = calculate_total(100, 5, 0.20)
print(f"Toplam: {result}")  # 600.0

# List/Tuple unpacking ile *
values = [100, 5]
result = calculate_total(*values)
print(f"Toplam: {result}")  # 590.0

# Dictionary unpacking ile **
params = {"price": 100, "quantity": 5, "tax": 0.20}
result = calculate_total(**params)
print(f"Toplam: {result}")  # 600.0
```

---

## Lambda Fonksiyonları

Lambda fonksiyonları, tek satırda tanımlanan isimsiz (anonymous) fonksiyonlardır. Genellikle kısa ve basit işlemler için kullanılır.

### Örnek 16: Basit Lambda Fonksiyonları

```python
# Normal fonksiyon
def square(x):
    return x ** 2

# Lambda fonksiyon
square_lambda = lambda x: x ** 2

print(square(5))         # 25
print(square_lambda(5))  # 25

# Birden fazla parametre
multiply = lambda x, y: x * y
print(multiply(3, 4))    # 12

# Karmaşık ifadeler
max_value = lambda a, b: a if a > b else b
print(max_value(10, 20)) # 20
```

### Örnek 17: Lambda ile Built-in Fonksiyonlar

```python
# map() ile kullanım
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter() ile kullanım
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

# sorted() ile kullanım
students = [
    {"name": "Ali", "grade": 85},
    {"name": "Ayşe", "grade": 92},
    {"name": "Mehmet", "grade": 78}
]

# Nota göre sıralama
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
print(sorted_students)
# [{'name': 'Ayşe', 'grade': 92}, {'name': 'Ali', 'grade': 85}, {'name': 'Mehmet', 'grade': 78}]
```

### Örnek 18: Lambda Fonksiyonlarının Sınırlamaları

```python
# ❌ Lambda ile yapılamaz (çok satırlı)
# calculate = lambda x:
#     if x > 0:
#         return x * 2
#     else:
#         return x * -1

# ✅ Normal fonksiyon kullanın
def calculate(x):
    if x > 0:
        return x * 2
    else:
        return x * -1

# Lambda: Basit, tek satırlık işlemler için idealdir
double = lambda x: x * 2
is_positive = lambda x: x > 0
greet = lambda name: f"Merhaba, {name}!"

print(double(5))           # 10
print(is_positive(-3))     # False
print(greet("Ali"))        # Merhaba, Ali!
```

---

## Scope (Kapsam)

Değişkenlerin erişilebilirlik alanına "scope" denir. Python'da dört scope seviyesi vardır:
- **Local (L)**: Fonksiyon içi
- **Enclosing (E)**: İç içe fonksiyonlarda dış fonksiyon
- **Global (G)**: Modül seviyesi
- **Built-in (B)**: Python'ın yerleşik isimleri

### Örnek 19: Local ve Global Scope

```python
# Global scope
global_var = "Global değişken"

def test_scope():
    # Local scope
    local_var = "Local değişken"
    print(f"Fonksiyon içinde - Global: {global_var}")
    print(f"Fonksiyon içinde - Local: {local_var}")

test_scope()
print(f"Fonksiyon dışında - Global: {global_var}")
# print(local_var)  # NameError: local_var tanımlı değil
```

### Örnek 20: Global Anahtar Kelimesi

```python
counter = 0  # Global değişken

def increment():
    global counter  # Global değişkeni değiştireceğimizi belirtiyoruz
    counter += 1
    print(f"Counter: {counter}")

increment()  # Counter: 1
increment()  # Counter: 2
increment()  # Counter: 3

print(f"Final counter: {counter}")  # Final counter: 3
```

### Örnek 21: Nonlocal Anahtar Kelimesi

```python
def outer_function():
    outer_var = "Dış fonksiyon"

    def inner_function():
        nonlocal outer_var  # Dış fonksiyonun değişkenini kullan
        outer_var = "Değiştirildi"
        print(f"İç fonksiyon: {outer_var}")

    print(f"Önce: {outer_var}")
    inner_function()
    print(f"Sonra: {outer_var}")

outer_function()
# Output:
# Önce: Dış fonksiyon
# İç fonksiyon: Değiştirildi
# Sonra: Değiştirildi
```

---

## Recursion (Özyineleme)

Bir fonksiyonun kendisini çağırmasına recursion denir. Recursion, bazı problemleri daha elegant şekilde çözmek için kullanılır.

### Örnek 22: Faktöriyel Hesaplama

```python
def factorial(n):
    """Faktöriyel hesaplama (recursive)"""
    # Base case (durma koşulu)
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 5! = 5 × 4 × 3 × 2 × 1 = 120
print(factorial(0))  # 0! = 1
print(factorial(1))  # 1! = 1

# Adım adım:
# factorial(5) = 5 × factorial(4)
#              = 5 × 4 × factorial(3)
#              = 5 × 4 × 3 × factorial(2)
#              = 5 × 4 × 3 × 2 × factorial(1)
#              = 5 × 4 × 3 × 2 × 1
#              = 120
```

### Örnek 23: Fibonacci Dizisi

```python
def fibonacci(n):
    """n. Fibonacci sayısını bulur (recursive)"""
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# İlk 10 Fibonacci sayısı
print("Fibonacci dizisi:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Output:
# F(0) = 0
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
# F(6) = 8
# F(7) = 13
# F(8) = 21
# F(9) = 34
```

### Örnek 24: Recursive vs Iterative

```python
# Recursive toplama
def sum_recursive(n):
    """1'den n'e kadar olan sayıların toplamı (recursive)"""
    if n <= 0:
        return 0
    return n + sum_recursive(n - 1)

# Iterative toplama
def sum_iterative(n):
    """1'den n'e kadar olan sayıların toplamı (iterative)"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_recursive(5))  # 15
print(sum_iterative(5))  # 15

# Not: Çoğu durumda iterative yaklaşım daha verimlidir
# Recursion daha elegant olabilir ama stack overflow riski vardır
```

---

## Docstrings

Docstring, fonksiyonların ne yaptığını açıklayan dokümantasyon string'leridir. Triple quotes (`"""` veya `'''`) kullanılarak yazılır.

### Örnek 25: Basit Docstring

```python
def calculate_area(width, height):
    """
    Dikdörtgenin alanını hesaplar.

    Args:
        width (float): Dikdörtgenin genişliği
        height (float): Dikdörtgenin yüksekliği

    Returns:
        float: Dikdörtgenin alanı
    """
    return width * height

# Docstring'i görüntüleme
print(calculate_area.__doc__)

# help() fonksiyonu ile
help(calculate_area)
```

### Örnek 26: Detaylı Docstring (Google Style)

```python
def calculate_bmi(weight, height):
    """
    Vücut Kitle İndeksini (BMI) hesaplar.

    BMI = kilo / (boy ^ 2)

    Args:
        weight (float): Kilogram cinsinden kilo
        height (float): Metre cinsinden boy

    Returns:
        float: Hesaplanan BMI değeri

    Raises:
        ValueError: Eğer kilo veya boy negatif veya sıfır ise

    Examples:
        >>> calculate_bmi(70, 1.75)
        22.86
        >>> calculate_bmi(80, 1.80)
        24.69
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Kilo ve boy pozitif olmalıdır")

    bmi = weight / (height ** 2)
    return round(bmi, 2)

print(calculate_bmi(70, 1.75))  # 22.86
```

### Örnek 27: NumPy Style Docstring

```python
def find_max_min(numbers):
    """
    Bir listedeki en büyük ve en küçük sayıyı bulur.

    Parameters
    ----------
    numbers : list
        Sayılardan oluşan liste

    Returns
    -------
    tuple
        (max, min) formatında tuple

    Notes
    -----
    Liste boş olmamalıdır.

    Examples
    --------
    >>> find_max_min([1, 5, 3, 9, 2])
    (9, 1)
    """
    if not numbers:
        return None, None

    return max(numbers), min(numbers)

print(find_max_min([1, 5, 3, 9, 2]))  # (9, 1)
```

---

## İleri Seviye Örnekler

### Örnek 28: Decorator (Basit)

```python
def timer_decorator(func):
    """Fonksiyonun çalışma süresini ölçer"""
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} fonksiyonu {end_time - start_time:.4f} saniye sürdü")
        return result

    return wrapper

@timer_decorator
def slow_function():
    """Yavaş çalışan örnek fonksiyon"""
    import time
    time.sleep(1)
    return "Tamamlandı"

result = slow_function()
# Output: slow_function fonksiyonu 1.0001 saniye sürdü
```

### Örnek 29: Closure

```python
def create_multiplier(n):
    """n ile çarpan bir fonksiyon oluşturur"""
    def multiplier(x):
        return x * n
    return multiplier

# Farklı çarpanlar oluşturma
times_2 = create_multiplier(2)
times_5 = create_multiplier(5)
times_10 = create_multiplier(10)

print(times_2(4))   # 8
print(times_5(4))   # 20
print(times_10(4))  # 40
```

### Örnek 30: Generator Function

```python
def countdown(n):
    """n'den 0'a geri sayar (generator)"""
    while n > 0:
        yield n
        n -= 1

# Generator kullanımı
for num in countdown(5):
    print(num)

# Output:
# 5
# 4
# 3
# 2
# 1

# Fibonacci generator
def fibonacci_generator(limit):
    """Fibonacci sayılarını üretir"""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

print(list(fibonacci_generator(10)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## Önemli Notlar

1. **Fonksiyon İsimlendirme**: Küçük harf ve alt çizgi kullanın (snake_case)
2. **Single Responsibility**: Bir fonksiyon bir iş yapmalı
3. **DRY Prensibi**: Kodu tekrarlamayın, fonksiyon yazın
4. **Docstring Kullanın**: Her fonksiyonu dokümante edin
5. **Default Parametreler**: Dikkatli kullanın (özellikle mutable objeler)
6. **Return**: Her zaman açık olun, fonksiyon ne döndürüyor?
7. **Recursion**: Durma koşulunu unutmayın (base case)
8. **Lambda**: Basit işlemler için, karmaşık mantık için normal fonksiyon
9. **Scope**: Global değişkenleri minimize edin
10. **Type Hints**: Modern Python'da tip belirtmeleri kullanın

---

## Özet

Bu bölümde öğrendikleriniz:
- Fonksiyon tanımlama ve çağırma
- Parametreler ve argümanlar (pozisyonel, keyword, default)
- Return ifadesi ve birden fazla değer döndürme
- *args ve **kwargs ile esnek parametreler
- Lambda fonksiyonları
- Scope (local, global, nonlocal)
- Recursion (özyineleme)
- Docstrings ile dokümantasyon
- İleri seviye kavramlar (decorators, closures, generators)

Şimdi `exercises.py` dosyasındaki alıştırmaları yaparak öğrendiklerinizi pekiştirebilirsiniz!
