"""
FUNCTIONS (FONKSİYONLAR) - ALIŞTIRMALAR
========================================

Her soruyu çözmeye çalışın. Takılırsanız, her sorunun altındaki
ÇÖZÜM bölümünü inceleyebilirsiniz.

Zorluk Seviyeleri:
[Kolay] - Temel kavramları test eder
[Orta] - Birden fazla kavramı birleştirir
[Zor] - Daha karmaşık problemler
[Challenge] - Dünya standartlarında zorlayıcı sorular
"""

# =============================================================================
# SORU 1: [Kolay] Basit Fonksiyon Tanımlama
# =============================================================================
# İsminizi yazdıran bir fonksiyon yazın.
# Fonksiyon adı: print_name
# Parametresiz olmalı ve ekrana "Benim adım X" yazdırmalı

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- def anahtar kelimesi ile fonksiyon tanımlanır
- Fonksiyon adı küçük harfle ve snake_case kullanılır
- İki nokta üst üste ile fonksiyon bloğu başlar
- Fonksiyon bloğu girintilidir (indentation)
"""

def print_name():
    """İsmi yazdıran basit fonksiyon"""
    print("Benim adım Ahmet")

# Fonksiyonu çağırma
print_name()


# =============================================================================
# SORU 2: [Kolay] Parametreli Fonksiyon
# =============================================================================
# Bir isim parametresi alan ve o kişiye özel mesaj yazdıran fonksiyon yazın.
# Fonksiyon adı: greet_person
# Parametre: name
# Çıktı: "Merhaba, {name}! Hoş geldin."

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Parantez içinde parametre tanımlanır
- Parametre fonksiyon içinde değişken gibi kullanılır
- f-string ile string formatlama yapılabilir
"""

def greet_person(name):
    """Kişiye özel selamlama mesajı gösterir"""
    print(f"Merhaba, {name}! Hoş geldin.")

# Test
greet_person("Ali")
greet_person("Ayşe")
greet_person("Mehmet")


# =============================================================================
# SORU 3: [Kolay] Return İfadesi
# =============================================================================
# İki sayıyı toplayan ve sonucu döndüren fonksiyon yazın.
# Fonksiyon adı: add
# Parametreler: a, b
# Return: a + b

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- return ifadesi fonksiyondan değer döndürür
- Döndürülen değer bir değişkene atanabilir
- Return olmayan fonksiyonlar None döndürür
"""

def add(a, b):
    """İki sayının toplamını döndürür"""
    return a + b

# Test
result = add(5, 3)
print(f"5 + 3 = {result}")  # 8

print(f"10 + 20 = {add(10, 20)}")  # 30


# =============================================================================
# SORU 4: [Kolay] Birden Fazla İşlem
# =============================================================================
# İki sayı için dört işlemi yapan fonksiyonlar yazın:
# - subtract(a, b): Çıkarma
# - multiply(a, b): Çarpma
# - divide(a, b): Bölme (0'a bölünme kontrolü yapın)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Her işlem için ayrı fonksiyon yazılır
- Bölme işleminde payda kontrolü önemlidir
- if-else ile koşul kontrolü yapılır
"""

def subtract(a, b):
    """İki sayının farkını döndürür"""
    return a - b

def multiply(a, b):
    """İki sayının çarpımını döndürür"""
    return a * b

def divide(a, b):
    """İki sayının bölümünü döndürür"""
    if b == 0:
        return "Hata: Sıfıra bölme yapılamaz!"
    return a / b

# Test
print(f"10 - 3 = {subtract(10, 3)}")      # 7
print(f"5 × 4 = {multiply(5, 4)}")        # 20
print(f"15 ÷ 3 = {divide(15, 3)}")        # 5.0
print(f"10 ÷ 0 = {divide(10, 0)}")        # Hata mesajı


# =============================================================================
# SORU 5: [Orta] Default Parametreler
# =============================================================================
# Dikdörtgenin alanını hesaplayan fonksiyon yazın.
# Fonksiyon adı: calculate_rectangle_area
# Parametreler: width (zorunlu), height (default=10)
# Return: width × height

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Default parametreler = ile atanır
- Default parametreler sonda olmalıdır
- Çağrırken default parametreler isteğe bağlıdır
"""

def calculate_rectangle_area(width, height=10):
    """
    Dikdörtgenin alanını hesaplar.

    Args:
        width (float): Genişlik
        height (float, optional): Yükseklik. Defaults to 10.

    Returns:
        float: Alan
    """
    return width * height

# Test
print(f"Alan (5, default): {calculate_rectangle_area(5)}")       # 50
print(f"Alan (5, 8): {calculate_rectangle_area(5, 8)}")          # 40
print(f"Alan (width=7, height=3): {calculate_rectangle_area(width=7, height=3)}")  # 21


# =============================================================================
# SORU 6: [Orta] Birden Fazla Return Değeri
# =============================================================================
# Bir dairenin hem alanını hem çevresini hesaplayan fonksiyon yazın.
# Fonksiyon adı: circle_properties
# Parametre: radius
# Return: (area, circumference) tuple
# Formüller: alan = π × r², çevre = 2 × π × r (π = 3.14159)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Birden fazla değer tuple olarak döndürülür
- Tuple unpacking ile ayrı değişkenlere atanabilir
- math modülünden pi değeri kullanılabilir
"""

def circle_properties(radius):
    """
    Dairenin alan ve çevresini hesaplar.

    Args:
        radius (float): Yarıçap

    Returns:
        tuple: (alan, çevre)
    """
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference

# Test
r = 5
alan, cevre = circle_properties(r)
print(f"Yarıçap {r} olan dairenin:")
print(f"  Alanı: {alan:.2f}")
print(f"  Çevresi: {cevre:.2f}")

# Alternatif: math modülü ile
import math

def circle_properties_v2(radius):
    """math.pi kullanarak daha hassas hesaplama"""
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

alan2, cevre2 = circle_properties_v2(5)
print(f"\nmath.pi ile:")
print(f"  Alanı: {alan2:.2f}")
print(f"  Çevresi: {cevre2:.2f}")


# =============================================================================
# SORU 7: [Orta] *args Kullanımı
# =============================================================================
# Verilen tüm sayıların ortalamasını hesaplayan fonksiyon yazın.
# Fonksiyon adı: calculate_average
# Parametreler: *numbers (değişken sayıda)
# Return: Ortalama (hiç sayı verilmezse 0)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- *args tüm pozisyonel argümanları tuple olarak toplar
- len() ile eleman sayısı bulunur
- sum() ile toplam hesaplanır
- Boş durumu kontrol etmek önemlidir
"""

def calculate_average(*numbers):
    """
    Verilen sayıların ortalamasını hesaplar.

    Args:
        *numbers: Değişken sayıda sayı

    Returns:
        float: Ortalama
    """
    if len(numbers) == 0:
        return 0

    total = sum(numbers)
    return total / len(numbers)

# Test
print(f"Ortalama (10, 20, 30): {calculate_average(10, 20, 30)}")           # 20.0
print(f"Ortalama (5, 15, 25, 35): {calculate_average(5, 15, 25, 35)}")    # 20.0
print(f"Ortalama (100): {calculate_average(100)}")                        # 100.0
print(f"Ortalama (): {calculate_average()}")                              # 0


# =============================================================================
# SORU 8: [Orta] **kwargs Kullanımı
# =============================================================================
# Kullanıcı bilgilerini formatlı şekilde yazdıran fonksiyon yazın.
# Fonksiyon adı: print_user_info
# Parametreler: **user_data
# Çıktı: Her key-value çiftini "Key: Value" formatında yazdırmalı

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- **kwargs tüm keyword argümanları dictionary olarak toplar
- items() ile key-value çiftleri üzerinde iterasyon
- title() ile keyleri düzgün formatlayabiliriz
"""

def print_user_info(**user_data):
    """
    Kullanıcı bilgilerini yazdırır.

    Args:
        **user_data: Kullanıcı bilgileri (key=value formatında)
    """
    print("Kullanıcı Bilgileri:")
    print("-" * 30)
    for key, value in user_data.items():
        # Key'i daha okunabilir yap
        formatted_key = key.replace('_', ' ').title()
        print(f"{formatted_key}: {value}")

# Test
print_user_info(
    name="Ali Yılmaz",
    age=25,
    city="İstanbul",
    email="ali@example.com",
    phone="555-1234"
)

print("\n")

print_user_info(
    product_name="Laptop",
    brand="Dell",
    price=15000,
    in_stock=True
)


# =============================================================================
# SORU 9: [Orta] Lambda Fonksiyonu
# =============================================================================
# Aşağıdaki görevleri lambda fonksiyonları kullanarak yapın:
# 1. Bir sayının karesini alan lambda
# 2. İki sayının maksimumunu bulan lambda
# 3. Bir string'in uzunluğunu döndüren lambda
# Bu lambda'ları kullanarak örnekler gösterin.

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Lambda: lambda parametreler: ifade
- Tek satırlık, basit fonksiyonlar için idealdir
- Genellikle map, filter, sorted gibi fonksiyonlarla kullanılır
- Karmaşık mantık için normal fonksiyon tercih edilmelidir
"""

# 1. Kare alma
square = lambda x: x ** 2
print(f"5'in karesi: {square(5)}")  # 25

# 2. Maksimum bulma
maximum = lambda a, b: a if a > b else b
print(f"Max(10, 20): {maximum(10, 20)}")  # 20

# 3. String uzunluğu
str_length = lambda s: len(s)
print(f"'Python' uzunluğu: {str_length('Python')}")  # 6

# Lambda ile map örneği
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Sayılar: {numbers}")
print(f"Kareler: {squared_numbers}")

# Lambda ile filter örneği
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Çift sayılar: {even_numbers}")

# Lambda ile sorted örneği
words = ["python", "java", "c", "javascript", "go"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"Uzunluğa göre sıralı: {sorted_by_length}")


# =============================================================================
# SORU 10: [Zor] Recursion - Faktöriyel
# =============================================================================
# Faktöriyel hesaplayan recursive fonksiyon yazın.
# Fonksiyon adı: factorial
# Parametre: n (pozitif tam sayı)
# Return: n! (n faktöriyel)
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# 0! = 1 (tanım gereği)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Recursive fonksiyon kendini çağıran fonksiyondur
- Base case (durma koşulu) olmalıdır
- Recursive case her çağrıda problemi küçültmeli
- Stack overflow'dan kaçınmak için sınır kontrolü önemlidir
"""

def factorial(n):
    """
    Faktöriyel hesaplar (recursive).

    Args:
        n (int): Pozitif tam sayı

    Returns:
        int: n faktöriyel

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    # Base case: 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)

# Test
print("Faktöriyel Hesaplama:")
for i in range(8):
    print(f"{i}! = {factorial(i)}")

# Adım adım açıklama
print("\n5! hesaplama adımları:")
print("factorial(5) = 5 × factorial(4)")
print("             = 5 × 4 × factorial(3)")
print("             = 5 × 4 × 3 × factorial(2)")
print("             = 5 × 4 × 3 × 2 × factorial(1)")
print("             = 5 × 4 × 3 × 2 × 1")
print("             = 120")


# =============================================================================
# SORU 11: [Zor] Recursion - Fibonacci
# =============================================================================
# Fibonacci sayısını bulan recursive fonksiyon yazın.
# Fonksiyon adı: fibonacci
# Parametre: n (pozitif tam sayı)
# Return: n. Fibonacci sayısı
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Fibonacci: Her sayı, kendinden önceki iki sayının toplamıdır
- İki base case vardır: F(0) = 0, F(1) = 1
- Recursive durum: F(n) = F(n-1) + F(n-2)
- Not: Bu yöntem büyük n değerleri için yavaştır (exponential zaman)
"""

def fibonacci(n):
    """
    n. Fibonacci sayısını bulur (recursive).

    Args:
        n (int): Sıra numarası

    Returns:
        int: n. Fibonacci sayısı
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test
print("\nFibonacci Dizisi:")
for i in range(15):
    print(f"F({i}) = {fibonacci(i)}")

# Bonus: İteratif (daha verimli) versiyon
def fibonacci_iterative(n):
    """Fibonacci - iterative versiyon (daha hızlı)"""
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print("\nİteratif vs Recursive karşılaştırma:")
print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci_iterative(10) = {fibonacci_iterative(10)}")


# =============================================================================
# SORU 12: [Zor] Scope Anlama
# =============================================================================
# Global ve local scope'u gösterin:
# 1. Global bir counter değişkeni (başlangıç: 0)
# 2. increment() fonksiyonu: counter'ı 1 artırır ve yazdırır
# 3. reset() fonksiyonu: counter'ı 0'a sıfırlar
# 4. get_counter() fonksiyonu: counter değerini döndürür

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Global değişkenler modül seviyesinde tanımlanır
- global anahtar kelimesi ile global değişken değiştirilebilir
- global kullanmadan global değişken sadece okunabilir
- Best practice: Global değişken kullanımını minimize edin
"""

# Global değişken
counter = 0

def increment():
    """Counter'ı 1 artırır"""
    global counter  # Global değişkeni değiştireceğiz
    counter += 1
    print(f"Counter artırıldı: {counter}")

def reset():
    """Counter'ı sıfırlar"""
    global counter
    counter = 0
    print("Counter sıfırlandı")

def get_counter():
    """Counter değerini döndürür"""
    # global anahtar kelimesi gerekmiyor (sadece okuyoruz)
    return counter

# Test
print(f"\nBaşlangıç counter: {get_counter()}")
increment()  # 1
increment()  # 2
increment()  # 3
print(f"Şu anki counter: {get_counter()}")
reset()      # 0
print(f"Sıfırlandıktan sonra: {get_counter()}")


# =============================================================================
# SORU 13: [Zor] Docstring Yazımı
# =============================================================================
# Üçgenin alanını hesaplayan fonksiyon yazın ve detaylı docstring ekleyin.
# Fonksiyon adı: triangle_area
# Parametreler: base (taban), height (yükseklik)
# Return: Alan
# Docstring Google style kullanarak yazın (Args, Returns, Examples bölümleri)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Docstring fonksiyonun hemen altına triple quotes ile yazılır
- Google, NumPy, reStructuredText gibi farklı stiller vardır
- Args: Parametreleri açıklar
- Returns: Dönüş değerini açıklar
- Examples: Kullanım örnekleri (doctests için de kullanılır)
- Raises: Olası exception'ları belirtir
"""

def triangle_area(base, height):
    """
    Üçgenin alanını hesaplar.

    Üçgenin alanı taban ile yüksekliğin çarpımının yarısına eşittir.
    Alan = (taban × yükseklik) / 2

    Args:
        base (float): Üçgenin taban uzunluğu (pozitif olmalı)
        height (float): Üçgenin yüksekliği (pozitif olmalı)

    Returns:
        float: Üçgenin alanı

    Raises:
        ValueError: Eğer taban veya yükseklik negatif veya sıfır ise

    Examples:
        >>> triangle_area(10, 5)
        25.0

        >>> triangle_area(6, 8)
        24.0

        >>> triangle_area(12.5, 8.4)
        52.5
    """
    # Validasyon
    if base <= 0 or height <= 0:
        raise ValueError("Taban ve yükseklik pozitif olmalıdır")

    # Hesaplama
    area = (base * height) / 2
    return area

# Test
print("\nÜçgen Alanı Hesaplama:")
print(f"Taban: 10, Yükseklik: 5 → Alan: {triangle_area(10, 5)}")
print(f"Taban: 6, Yükseklik: 8 → Alan: {triangle_area(6, 8)}")

# Docstring'i görüntüleme
print("\nFonksiyon dokümantasyonu:")
print(triangle_area.__doc__)

# help() ile detaylı bilgi
# help(triangle_area)


# =============================================================================
# SORU 14: [Challenge] Çok Amaçlı Hesap Makinesi
# =============================================================================
# Gelişmiş bir hesap makinesi fonksiyonu yazın.
# Fonksiyon adı: calculator
# Parametreler: operation (string: "add", "subtract", "multiply", "divide", "power")
#               *args (değişken sayıda sayı)
# Return: İşlem sonucu
# Özellikler:
# - "add": Tüm sayıları topla
# - "subtract": İlk sayıdan diğerlerini çıkar
# - "multiply": Tüm sayıları çarp
# - "divide": İlk sayıyı diğerlerine böl (0'a bölme kontrolü)
# - "power": İlk sayının ikinci sayı kuvvetini al
# - Geçersiz işlem için hata mesajı

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- String karşılaştırma ile işlem tipi belirlenir
- *args ile değişken sayıda parametre alınır
- Her işlem için ayrı mantık yazılır
- Edge case'leri kontrol edilir (boş argüman, sıfıra bölme, vb.)
- Okunabilirlik için her işlem ayrı if-elif bloğunda
"""

def calculator(operation, *args):
    """
    Çok amaçlı hesap makinesi.

    Args:
        operation (str): İşlem tipi ("add", "subtract", "multiply", "divide", "power")
        *args: Değişken sayıda sayı

    Returns:
        float/str: İşlem sonucu veya hata mesajı

    Examples:
        >>> calculator("add", 1, 2, 3, 4, 5)
        15

        >>> calculator("multiply", 2, 3, 4)
        24

        >>> calculator("power", 2, 3)
        8
    """
    # Argüman kontrolü
    if len(args) == 0:
        return "Hata: En az bir sayı gerekli"

    # İşlem tipine göre hesaplama
    if operation == "add":
        # Toplama: Tüm sayıları topla
        return sum(args)

    elif operation == "subtract":
        # Çıkarma: İlk sayıdan diğerlerini çıkar
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    elif operation == "multiply":
        # Çarpma: Tüm sayıları çarp
        result = 1
        for num in args:
            result *= num
        return result

    elif operation == "divide":
        # Bölme: İlk sayıyı diğerlerine böl
        # Sıfıra bölme kontrolü
        if any(num == 0 for num in args[1:]):
            return "Hata: Sıfıra bölme yapılamaz"

        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    elif operation == "power":
        # Üs alma: İlk sayının ikinci sayı kuvveti
        if len(args) < 2:
            return "Hata: Üs alma için en az 2 sayı gerekli"
        return args[0] ** args[1]

    else:
        return f"Hata: Geçersiz işlem '{operation}'"

# Test
print("\nÇok Amaçlı Hesap Makinesi:")
print("-" * 50)

print(f"Toplama (1, 2, 3, 4, 5): {calculator('add', 1, 2, 3, 4, 5)}")
print(f"Çıkarma (100, 20, 10): {calculator('subtract', 100, 20, 10)}")
print(f"Çarpma (2, 3, 4, 5): {calculator('multiply', 2, 3, 4, 5)}")
print(f"Bölme (100, 2, 5): {calculator('divide', 100, 2, 5)}")
print(f"Üs (2, 10): {calculator('power', 2, 10)}")
print(f"Geçersiz işlem: {calculator('modulo', 10, 3)}")
print(f"Sıfıra bölme: {calculator('divide', 10, 0)}")


# =============================================================================
# SORU 15: [Challenge] Memoization ile Fibonacci
# =============================================================================
# Fibonacci hesaplamasını optimize edin.
# Memoization (önbellekleme) tekniği kullanarak daha önce hesaplanan
# değerleri saklayın ve tekrar hesaplamayın.
# Fonksiyon adı: fibonacci_memo
# İpucu: Bir cache dictionary'si kullanın

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Memoization: Hesaplanan sonuçları cache'leyerek performans artırma
- Dictionary ile önceki sonuçlar saklanır
- Recursive çağrılar azalır (exponential → linear zaman)
- Closure veya global dictionary kullanılabilir
"""

# Yöntem 1: Global cache dictionary
fibonacci_cache = {}

def fibonacci_memo(n):
    """
    Memoization ile optimize edilmiş Fibonacci.

    Args:
        n (int): Sıra numarası

    Returns:
        int: n. Fibonacci sayısı
    """
    # Cache'de varsa direkt döndür
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Hesapla ve cache'e kaydet
    result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    fibonacci_cache[n] = result

    return result

# Test
print("\nMemoization ile Fibonacci:")
import time

# Büyük bir değer dene
n = 35

# Memoized versiyon
start = time.time()
result_memo = fibonacci_memo(n)
time_memo = time.time() - start
print(f"fibonacci_memo({n}) = {result_memo}")
print(f"Süre: {time_memo:.6f} saniye")

# Normal recursive versiyon ile karşılaştırma
# Not: n=35 için normal versiyon çok yavaş olabilir
start = time.time()
result_normal = fibonacci(n)
time_normal = time.time() - start
print(f"\nfibonacci({n}) = {result_normal}")
print(f"Süre: {time_normal:.6f} saniye")
print(f"\nHızlanma: {time_normal / time_memo:.2f}x daha hızlı!")

# Yöntem 2: Python'un functools.lru_cache decorator'ı
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    """LRU cache decorator ile Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

print("\nLRU Cache ile:")
start = time.time()
result_lru = fibonacci_lru(n)
time_lru = time.time() - start
print(f"fibonacci_lru({n}) = {result_lru}")
print(f"Süre: {time_lru:.6f} saniye")


# =============================================================================
# SORU 16: [Challenge] Decorator Fonksiyonu
# =============================================================================
# Bir fonksiyonun çalışma süresini ölçen decorator yazın.
# Decorator adı: measure_time
# Fonksiyonun çalışma süresini saniye cinsinden yazdırmalı

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Decorator: Bir fonksiyonu wrap eden (saran) fonksiyondur
- @syntax ile kullanılır
- Wrapper fonksiyon orijinal fonksiyonun yerine çalışır
- *args, **kwargs ile tüm parametreleri ileteriz
- time.time() ile zaman ölçümü yapılır
"""

import time

def measure_time(func):
    """
    Fonksiyonun çalışma süresini ölçen decorator.

    Args:
        func: Süre ölçülecek fonksiyon

    Returns:
        function: Wrapper fonksiyon
    """
    def wrapper(*args, **kwargs):
        # Başlangıç zamanı
        start_time = time.time()

        # Orijinal fonksiyonu çalıştır
        result = func(*args, **kwargs)

        # Bitiş zamanı
        end_time = time.time()

        # Süreyi hesapla ve yazdır
        duration = end_time - start_time
        print(f"\n[Süre Ölçümü] {func.__name__}() → {duration:.6f} saniye")

        return result

    return wrapper

# Decorator kullanımı
@measure_time
def slow_function():
    """Yavaş çalışan örnek fonksiyon"""
    time.sleep(1)
    return "Tamamlandı"

@measure_time
def calculate_sum(n):
    """1'den n'e kadar topla"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

@measure_time
def fibonacci_slow(n):
    """Yavaş fibonacci (ölçüm için)"""
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)

# Test
print("\nDecorator Testi:")
print("-" * 50)

result1 = slow_function()
print(f"Sonuç: {result1}")

result2 = calculate_sum(1000000)
print(f"Sonuç: {result2}")

# Not: fibonacci_slow çok yavaş olacağı için küçük değer
# result3 = fibonacci_slow(20)
# print(f"Sonuç: {result3}")


# =============================================================================
# SORU 17: [Challenge] Closure (Kapatma)
# =============================================================================
# Bir sayaç oluşturan factory fonksiyonu yazın.
# Fonksiyon adı: create_counter
# Parametre: start (başlangıç değeri, default=0)
# Return: increment, decrement, get_value fonksiyonlarını içeren dict
# Her counter bağımsız olmalı (closure kullanımı)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Closure: İç fonksiyonun dış fonksiyonun değişkenlerine erişmesi
- nonlocal: Dış fonksiyonun değişkenini değiştirmek için
- Her create_counter çağrısı bağımsız bir counter oluşturur
- Dictionary döndürerek birden fazla fonksiyonu paketleyebiliriz
"""

def create_counter(start=0):
    """
    Bağımsız bir counter oluşturur (closure).

    Args:
        start (int, optional): Başlangıç değeri. Defaults to 0.

    Returns:
        dict: increment, decrement, get_value fonksiyonlarını içeren dict
    """
    # Closure değişkeni
    count = start

    def increment(amount=1):
        """Counter'ı artırır"""
        nonlocal count
        count += amount
        return count

    def decrement(amount=1):
        """Counter'ı azaltır"""
        nonlocal count
        count -= amount
        return count

    def get_value():
        """Mevcut değeri döndürür"""
        return count

    def reset():
        """Counter'ı başlangıç değerine sıfırlar"""
        nonlocal count
        count = start
        return count

    # Fonksiyonları dictionary olarak döndür
    return {
        "increment": increment,
        "decrement": decrement,
        "get_value": get_value,
        "reset": reset
    }

# Test
print("\nClosure Counter:")
print("-" * 50)

# İlk counter
counter1 = create_counter(0)
print(f"Counter 1 başlangıç: {counter1['get_value']()}")
counter1["increment"]()
counter1["increment"]()
counter1["increment"]()
print(f"Counter 1 (3x artırma): {counter1['get_value']()}")

# İkinci counter (bağımsız)
counter2 = create_counter(100)
print(f"\nCounter 2 başlangıç: {counter2['get_value']()}")
counter2["decrement"](5)
counter2["decrement"](10)
print(f"Counter 2 (5 ve 10 azaltma): {counter2['get_value']()}")

# Counter 1 etkilenmedi
print(f"\nCounter 1 hala: {counter1['get_value']()}")

# Reset test
counter1["reset"]()
print(f"Counter 1 reset: {counter1['get_value']()}")


# =============================================================================
# SORU 18: [Challenge] Recursive Dizin Gezme
# =============================================================================
# Bir sayı listesindeki tüm elemanların toplamını bulan recursive fonksiyon yazın.
# Ancak liste içinde başka listeler de olabilir (nested lists).
# Fonksiyon adı: sum_nested
# Parametre: data (sayılar ve/veya listeler içeren liste)
# Return: Tüm sayıların toplamı
# Örnek: sum_nested([1, [2, 3], [4, [5, 6]]]) → 21

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Nested (iç içe) veri yapılarını işlemek için recursion idealdir
- isinstance() ile tip kontrolü yapılır
- Liste ise: recursive çağrı
- Sayı ise: direkt topla ekle
- Her seviyede toplama işlemi yapılır
"""

def sum_nested(data):
    """
    İç içe listelerdeki tüm sayıları toplar.

    Args:
        data (list): Sayılar ve/veya listeler içeren liste

    Returns:
        int/float: Toplam

    Examples:
        >>> sum_nested([1, 2, 3])
        6

        >>> sum_nested([1, [2, 3], [4, [5, 6]]])
        21

        >>> sum_nested([[1, 2], [3, [4, 5]], 6])
        21
    """
    total = 0

    for item in data:
        # Eğer item bir liste ise, recursive çağrı
        if isinstance(item, list):
            total += sum_nested(item)
        # Eğer sayı ise, direkt ekle
        elif isinstance(item, (int, float)):
            total += item

    return total

# Test
print("\nNested List Toplama:")
print("-" * 50)

test_cases = [
    [1, 2, 3, 4, 5],
    [1, [2, 3], [4, [5, 6]]],
    [[1, 2], [3, [4, 5]], 6],
    [[[1]], [[2, [3]]], 4],
    [10, [20, [30, [40, [50]]]]]
]

for test in test_cases:
    result = sum_nested(test)
    print(f"{test} → {result}")

# Bonus: Düzleştirme (flatten) fonksiyonu
def flatten(data):
    """İç içe listeyi düzleştirir"""
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print("\nDüzleştirme Örnekleri:")
for test in test_cases:
    flattened = flatten(test)
    print(f"{test} → {flattened}")


# =============================================================================
# SORU 19: [Challenge] Fonksiyon Kompozisyonu
# =============================================================================
# Birden fazla fonksiyonu birleştiren (compose) bir fonksiyon yazın.
# Fonksiyon adı: compose
# Parametreler: *functions (değişken sayıda fonksiyon)
# Return: Tüm fonksiyonları sağdan sola uygulayan yeni fonksiyon
# Örnek: compose(f, g, h)(x) → f(g(h(x)))

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Function composition: Fonksiyonları birleştirme
- Matematiksel notasyon: (f ∘ g)(x) = f(g(x))
- Sağdan sola uygulanır
- Functional programming konsepti
- Closure kullanılır
"""

def compose(*functions):
    """
    Birden fazla fonksiyonu birleştirir (sağdan sola).

    Args:
        *functions: Birleştirilecek fonksiyonlar

    Returns:
        function: Kompozit fonksiyon

    Examples:
        >>> double = lambda x: x * 2
        >>> add_five = lambda x: x + 5
        >>> f = compose(double, add_five)
        >>> f(3)  # double(add_five(3)) = double(8) = 16
        16
    """
    def composed(x):
        # Sağdan sola uygula
        result = x
        for func in reversed(functions):
            result = func(result)
        return result

    return composed

# Test fonksiyonları
def add_10(x):
    """10 ekle"""
    return x + 10

def multiply_2(x):
    """2 ile çarp"""
    return x * 2

def square(x):
    """Karesi al"""
    return x ** 2

# Test
print("\nFonksiyon Kompozisyonu:")
print("-" * 50)

# Tek tek
x = 3
print(f"Başlangıç: {x}")
step1 = add_10(x)
print(f"add_10({x}) = {step1}")
step2 = multiply_2(step1)
print(f"multiply_2({step1}) = {step2}")
step3 = square(step2)
print(f"square({step2}) = {step3}")

# Kompozisyon ile
f = compose(square, multiply_2, add_10)
result = f(3)
print(f"\nKompoze: square(multiply_2(add_10(3))) = {result}")

# Farklı kombinasyonlar
print("\nFarklı Kombinasyonlar:")
f1 = compose(add_10, multiply_2)
print(f"add_10(multiply_2(5)) = {f1(5)}")  # 10 + (5*2) = 20

f2 = compose(multiply_2, add_10)
print(f"multiply_2(add_10(5)) = {f2(5)}")  # (5+10)*2 = 30

# Lambda ile
f3 = compose(
    lambda x: x ** 2,
    lambda x: x + 5,
    lambda x: x * 2
)
print(f"Kompoze lambda: {f3(3)}")  # ((3*2)+5)^2 = 11^2 = 121


# =============================================================================
# SORU 20: [Challenge] Currying
# =============================================================================
# Currying tekniğini uygulayan bir fonksiyon yazın.
# Curry: Çok parametreli bir fonksiyonu tek parametreli fonksiyonlar
# zincirine dönüştürme.
# Örnek: add(a, b) → curried_add(a)(b)
# curry(add, 2)(3) → 5

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Currying: Çok parametreli fonksiyonu tek parametreli zincirine dönüştürme
- Functional programming konsepti
- Partial application için kullanışlıdır
- Closure ile implementasyon
"""

def curry(func, *initial_args):
    """
    Fonksiyonu curry'ler (partial application).

    Args:
        func: Curry'lenecek fonksiyon
        *initial_args: Ön tanımlı argümanlar

    Returns:
        function: Curry'lenmiş fonksiyon
    """
    def curried(*args):
        # Tüm argümanları birleştir
        all_args = initial_args + args

        # Eğer yeterli argüman varsa, fonksiyonu çağır
        # Değilse, yeni bir curried fonksiyon döndür
        try:
            return func(*all_args)
        except TypeError:
            # Hala yeterli argüman yok, devam et
            return curry(func, *all_args)

    return curried

# Test fonksiyonları
def add(a, b):
    """İki sayıyı toplar"""
    return a + b

def multiply(a, b, c):
    """Üç sayıyı çarpar"""
    return a * b * c

def greet(greeting, name, punctuation):
    """Selamlama mesajı oluşturur"""
    return f"{greeting}, {name}{punctuation}"

# Test
print("\nCurrying:")
print("-" * 50)

# Basit curry
add_5 = curry(add, 5)
print(f"add_5(3) = {add_5(3)}")  # 8
print(f"add_5(10) = {add_5(10)}")  # 15

# Çoklu parametre
multiply_2 = curry(multiply, 2)
print(f"\nmultiply_2(3)(4) = {multiply_2(3, 4)}")  # 24

multiply_2_3 = curry(multiply, 2, 3)
print(f"multiply_2_3(5) = {multiply_2_3(5)}")  # 30

# String fonksiyonu
say_hello = curry(greet, "Merhaba")
print(f"\nsay_hello('Ali')('!') = {say_hello('Ali', '!')}")

say_hello_ali = curry(greet, "Merhaba", "Ali")
print(f"say_hello_ali('!') = {say_hello_ali('!')}")

# Alternatif: Manuel currying
def add_curried(a):
    """Manuel curry örneği"""
    def add_b(b):
        return a + b
    return add_b

print("\nManuel Currying:")
result = add_curried(5)(3)
print(f"add_curried(5)(3) = {result}")  # 8

# functools.partial ile (Python'un built-in çözümü)
from functools import partial

add_5_partial = partial(add, 5)
print(f"\nfunctools.partial:")
print(f"add_5_partial(3) = {add_5_partial(3)}")  # 8


# =============================================================================
# ALIŞTIRMALARIN SONU
# =============================================================================

print("\n" + "="*60)
print("TEBRİKLER! TÜM FONKSİYON ALIŞTIRMALARINI TAMAMLADINIZ!")
print("="*60)
print("\nBu bölümde şunları öğrendiniz:")
print("✓ Fonksiyon tanımlama ve çağırma")
print("✓ Parametreler ve argümanlar (pozisyonel, keyword, default)")
print("✓ Return ifadesi ve birden fazla değer döndürme")
print("✓ *args ve **kwargs ile esnek parametreler")
print("✓ Lambda fonksiyonları")
print("✓ Scope (local, global, nonlocal)")
print("✓ Recursion (özyineleme)")
print("✓ Docstrings ile dokümantasyon")
print("✓ İleri seviye: Decorators, Closures, Memoization")
print("✓ Functional programming: Composition, Currying")
print("\nSıradaki konu: 05-Lists")
print("="*60)
