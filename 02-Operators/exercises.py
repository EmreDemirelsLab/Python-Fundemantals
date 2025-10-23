"""
OPERATORS - ALIŞTIRMALAR
=========================

Her soruyu çözmeye çalışın. Takılırsanız, her sorunun altındaki
ÇÖZÜM bölümünü inceleyebilirsiniz.

Zorluk Seviyeleri:
[Kolay] - Temel kavramları test eder
[Orta] - Birden fazla kavramı birleştirir
[Zor] - Daha karmaşık problemler
[Challenge] - Dünya standartlarında zorlayıcı sorular
"""

# =============================================================================
# SORU 1: [Kolay] Temel Aritmetik İşlemler
# =============================================================================
# İki sayı tanımlayın: a = 17, b = 5
# Tüm aritmetik operatörleri (+, -, *, /, //, %, **) kullanarak
# sonuçları yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- / operatörü normal bölme (float döner)
- // operatörü tam bölme (floor division)
- % operatörü mod (kalan)
- ** operatörü üs alma
"""

a = 17
b = 5

print("\n--- Temel Aritmetik İşlemler ---")
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")      # 22
print(f"a - b = {a - b}")      # 12
print(f"a * b = {a * b}")      # 85
print(f"a / b = {a / b}")      # 3.4
print(f"a // b = {a // b}")    # 3
print(f"a % b = {a % b}")      # 2
print(f"a ** b = {a ** b}")    # 1419857


# =============================================================================
# SORU 2: [Kolay] Karşılaştırma Operatörleri
# =============================================================================
# İki sayı tanımlayın: x = 10, y = 20
# Tüm karşılaştırma operatörlerini (==, !=, >, <, >=, <=) kullanarak
# sonuçları yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Karşılaştırma operatörleri her zaman boolean döndürür
- == eşitlik, != eşitsizlik kontrolü yapar
- Zincir karşılaştırma da yapılabilir: a < b < c
"""

x = 10
y = 20

print("\n--- Karşılaştırma Operatörleri ---")
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")     # False
print(f"x != y: {x != y}")     # True
print(f"x > y: {x > y}")       # False
print(f"x < y: {x < y}")       # True
print(f"x >= y: {x >= y}")     # False
print(f"x <= y: {x <= y}")     # True

# Bonus: Zincir karşılaştırma
print(f"\n5 < x < 15: {5 < x < 15}")        # True
print(f"0 < x <= 10: {0 < x <= 10}")        # True


# =============================================================================
# SORU 3: [Kolay] Mantıksal Operatörler
# =============================================================================
# İki boolean değişken oluşturun: p = True, q = False
# and, or, not operatörlerini kullanarak tüm kombinasyonları yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- and: Her ikisi de True ise True
- or: En az biri True ise True
- not: Değeri tersine çevirir
"""

p = True
q = False

print("\n--- Mantıksal Operatörler ---")
print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")       # False
print(f"p or q: {p or q}")         # True
print(f"not p: {not p}")           # False
print(f"not q: {not q}")           # True
print(f"p and not q: {p and not q}")   # True
print(f"not p or q: {not p or q}")     # False


# =============================================================================
# SORU 4: [Kolay] Atama Operatörleri
# =============================================================================
# Bir değişken oluşturun: counter = 10
# +=, -=, *=, /= operatörlerini sırayla kullanarak değişkenin
# değerini güncelleyin ve her adımda yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- += : counter = counter + değer
- -= : counter = counter - değer
- *= : counter = counter * değer
- /= : counter = counter / değer
"""

counter = 10
print("\n--- Atama Operatörleri ---")
print(f"Başlangıç: {counter}")

counter += 5
print(f"counter += 5: {counter}")    # 15

counter -= 3
print(f"counter -= 3: {counter}")    # 12

counter *= 2
print(f"counter *= 2: {counter}")    # 24

counter /= 4
print(f"counter /= 4: {counter}")    # 6.0


# =============================================================================
# SORU 5: [Orta] Hesap Makinesi
# =============================================================================
# Kullanıcıdan iki sayı ve bir işlem alın (simüle edilmiş):
# num1 = 15, num2 = 4, operation = "+"
# operation'a göre (+, -, *, /, //, %, **) işlem yapın ve sonucu yazdırın
# if-elif kullanabilirsiniz

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Kullanıcı girdisine göre farklı işlemler yapıyoruz
- if-elif-else yapısı kullanarak işlem seçimi yapıyoruz
- Bölme için 0'a bölme kontrolü yapmak iyi bir pratiktir
"""

num1 = 15
num2 = 4
operation = "+"

print("\n--- Hesap Makinesi ---")
print(f"Sayı 1: {num1}")
print(f"Sayı 2: {num2}")
print(f"İşlem: {operation}")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Hata: Sıfıra bölme!"
elif operation == "//":
    if num2 != 0:
        result = num1 // num2
    else:
        result = "Hata: Sıfıra bölme!"
elif operation == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Hata: Sıfıra bölme!"
elif operation == "**":
    result = num1 ** num2
else:
    result = "Hata: Geçersiz işlem!"

print(f"Sonuç: {result}")

# Bonus: Dictionary kullanarak daha temiz çözüm
operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Hata: Sıfıra bölme!",
    "//": lambda x, y: x // y if y != 0 else "Hata: Sıfıra bölme!",
    "%": lambda x, y: x % y if y != 0 else "Hata: Sıfıra bölme!",
    "**": lambda x, y: x ** y,
}

if operation in operations:
    result = operations[operation](num1, num2)
    print(f"Sonuç (dict metodu): {result}")


# =============================================================================
# SORU 6: [Orta] Yaş Kategorisi Belirleme
# =============================================================================
# Bir yaş değişkeni oluşturun: age = 25
# Karşılaştırma ve mantıksal operatörler kullanarak yaş kategorisini belirleyin:
# - 0-12: Çocuk
# - 13-17: Ergen
# - 18-64: Yetişkin
# - 65+: Yaşlı
# Kategoriyi yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Zincir karşılaştırma kullanıyoruz: 0 <= age < 13
- Mantıksal operatörlerle aralık kontrolü yapabiliriz
- if-elif yapısı ile kategorileri kontrol ediyoruz
"""

age = 25

print("\n--- Yaş Kategorisi ---")
print(f"Yaş: {age}")

if 0 <= age < 13:
    category = "Çocuk"
elif 13 <= age < 18:
    category = "Ergen"
elif 18 <= age < 65:
    category = "Yetişkin"
elif age >= 65:
    category = "Yaşlı"
else:
    category = "Geçersiz yaş"

print(f"Kategori: {category}")

# Alternatif: Mantıksal operatörler ile
if age >= 0 and age < 13:
    print("Alternatif: Çocuk")
elif age >= 13 and age < 18:
    print("Alternatif: Ergen")
elif age >= 18 and age < 65:
    print("Alternatif: Yetişkin")
elif age >= 65:
    print("Alternatif: Yaşlı")


# =============================================================================
# SORU 7: [Orta] Üyelik Operatörleri
# =============================================================================
# Bir alışveriş listesi oluşturun: shopping_list = ["ekmek", "süt", "yumurta", "peynir"]
# Kullanıcının aradığı ürünün listede olup olmadığını kontrol edin:
# - "süt" var mı?
# - "çikolata" var mı?
# - "EKMEK" var mı? (case-insensitive kontrol yapın)

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- in operatörü liste, tuple, string vb. yapılarda üyelik kontrolü yapar
- not in operatörü üye olmadığını kontrol eder
- String'lerde case-insensitive kontrol için lower() kullanılır
"""

shopping_list = ["ekmek", "süt", "yumurta", "peynir"]

print("\n--- Alışveriş Listesi Kontrolü ---")
print(f"Liste: {shopping_list}")

# Süt var mı?
item1 = "süt"
if item1 in shopping_list:
    print(f"✓ {item1} listede var")
else:
    print(f"✗ {item1} listede yok")

# Çikolata var mı?
item2 = "çikolata"
if item2 in shopping_list:
    print(f"✓ {item2} listede var")
else:
    print(f"✗ {item2} listede yok")

# EKMEK var mı? (case-insensitive)
item3 = "EKMEK"
# Liste elemanlarını lowercase'e çevirip kontrol et
shopping_list_lower = [item.lower() for item in shopping_list]
if item3.lower() in shopping_list_lower:
    print(f"✓ {item3} listede var (case-insensitive)")
else:
    print(f"✗ {item3} listede yok")

# Bonus: Birden fazla ürün kontrolü
search_items = ["ekmek", "çikolata", "süt"]
found = [item for item in search_items if item in shopping_list]
not_found = [item for item in search_items if item not in shopping_list]
print(f"\nBulunan ürünler: {found}")
print(f"Bulunamayan ürünler: {not_found}")


# =============================================================================
# SORU 8: [Orta] is vs == Farkı
# =============================================================================
# Şu değişkenleri oluşturun:
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a
#
# Her kombinasyon için hem == hem de is operatörü ile karşılaştırın
# Sonuçları ve farkları açıklayın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- == operatörü değer eşitliğini kontrol eder
- is operatörü obje eşitliğini (identity) kontrol eder
- a ve b aynı değerlere sahip ama farklı objeler
- c, a'nın referansını tutuyor, aynı obje
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("\n--- is vs == Operatörleri ---")
print(f"a = {a}, id: {id(a)}")
print(f"b = {b}, id: {id(b)}")
print(f"c = {c}, id: {id(c)}")

print("\na == b:", a == b)    # True (aynı değer)
print("a is b:", a is b)      # False (farklı objeler)

print("\na == c:", a == c)    # True (aynı değer)
print("a is c:", a is c)      # True (aynı obje)

print("\nb == c:", b == c)    # True (aynı değer)
print("b is c:", b is c)      # False (farklı objeler)

# c'yi değiştir ve etkisini gör
print("\n--- c'yi değiştirme ---")
c.append(4)
print(f"c.append(4) sonrası:")
print(f"a = {a}")  # [1, 2, 3, 4] - değişti!
print(f"b = {b}")  # [1, 2, 3] - değişmedi
print(f"c = {c}")  # [1, 2, 3, 4]


# =============================================================================
# SORU 9: [Zor] Çift/Tek Sayı ve Pozitif/Negatif Kontrolü
# =============================================================================
# Bir sayı listesi oluşturun: numbers = [-10, -3, 0, 5, 12, 17, 24]
# Her sayı için şunları kontrol edin:
# - Çift mi, tek mi?
# - Pozitif mi, negatif mi, sıfır mı?
# Sonuçları düzenli bir formatta yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Mod operatörü (%) ile çift/tek kontrolü: n % 2 == 0
- Karşılaştırma operatörleri ile pozitif/negatif kontrolü
- Mantıksal operatörlerle birleştirerek kategorize ediyoruz
"""

numbers = [-10, -3, 0, 5, 12, 17, 24]

print("\n--- Sayı Analizi ---")
print(f"{'Sayı':<10} {'Çift/Tek':<15} {'Pozitif/Negatif':<20}")
print("-" * 45)

for num in numbers:
    # Çift/Tek kontrolü
    if num % 2 == 0:
        parity = "Çift"
    else:
        parity = "Tek"

    # Pozitif/Negatif kontrolü
    if num > 0:
        sign = "Pozitif"
    elif num < 0:
        sign = "Negatif"
    else:
        sign = "Sıfır"

    print(f"{num:<10} {parity:<15} {sign:<20}")

# Bonus: İstatistikler
even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = sum(1 for n in numbers if n % 2 != 0)
positive_count = sum(1 for n in numbers if n > 0)
negative_count = sum(1 for n in numbers if n < 0)
zero_count = sum(1 for n in numbers if n == 0)

print(f"\n{'='*45}")
print(f"Çift sayılar: {even_count}")
print(f"Tek sayılar: {odd_count}")
print(f"Pozitif sayılar: {positive_count}")
print(f"Negatif sayılar: {negative_count}")
print(f"Sıfır: {zero_count}")


# =============================================================================
# SORU 10: [Zor] Yıl Kontrolü (Artık Yıl)
# =============================================================================
# Bir yıl değişkeni oluşturun: year = 2024
# Mantıksal operatörler kullanarak artık yıl olup olmadığını kontrol edin
#
# Artık yıl kuralları:
# - 4'e tam bölünüyorsa artık yıldır
# - ANCAK 100'e tam bölünüyorsa artık yıl DEĞİLDİR
# - ANCAK 400'e tam bölünüyorsa artık yıldır
#
# Örnekler: 2000 (artık), 1900 (değil), 2024 (artık), 2023 (değil)

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Mod operatörü ile tam bölünme kontrolü yapıyoruz
- Mantıksal operatörlerle (and, or) kuralları birleştiriyoruz
- Öncelik sırası önemli: parantez kullanıyoruz
"""

year = 2024

print("\n--- Artık Yıl Kontrolü ---")
print(f"Yıl: {year}")

# Method 1: Adım adım kontrol
is_leap = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
    else:
        is_leap = True

print(f"Artık yıl mı? (Method 1): {is_leap}")

# Method 2: Tek satırda (önerilen)
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"Artık yıl mı? (Method 2): {is_leap}")

# Test örnekleri
test_years = [2000, 1900, 2024, 2023, 2100, 2400]
print("\nTest Yılları:")
for y in test_years:
    leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    status = "Artık yıl" if leap else "Normal yıl"
    print(f"  {y}: {status}")


# =============================================================================
# SORU 11: [Zor] Operatör Önceliği
# =============================================================================
# Aşağıdaki ifadelerin sonucunu tahmin edin, sonra kontrol edin:
# 1. 2 + 3 * 4
# 2. (2 + 3) * 4
# 3. 10 - 3 - 2
# 4. 2 ** 3 ** 2
# 5. True or False and False
# 6. (True or False) and False
# 7. 5 > 3 and 10 < 20 or 15 > 25

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Çarpma, toplamadan önce gelir
- Üs alma sağdan sola işlenir
- and, or'dan önce gelir
- Parantez her şeyden önce gelir
- Karşılaştırma, mantıksal operatörlerden önce gelir
"""

print("\n--- Operatör Önceliği ---")

# 1. Çarpma önce
expr1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {expr1}")  # 14 (önce 3*4=12, sonra 2+12=14)

# 2. Parantez önce
expr2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {expr2}")  # 20 (önce 2+3=5, sonra 5*4=20)

# 3. Soldan sağa
expr3 = 10 - 3 - 2
print(f"10 - 3 - 2 = {expr3}")  # 5 (önce 10-3=7, sonra 7-2=5)

# 4. Üs alma sağdan sola
expr4 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {expr4}")  # 512 (önce 3**2=9, sonra 2**9=512)

# 5. and önce, or sonra
expr5 = True or False and False
print(f"True or False and False = {expr5}")  # True (önce False and False=False, sonra True or False=True)

# 6. Parantez önce
expr6 = (True or False) and False
print(f"(True or False) and False = {expr6}")  # False (önce True or False=True, sonra True and False=False)

# 7. Karmaşık
expr7 = 5 > 3 and 10 < 20 or 15 > 25
print(f"5 > 3 and 10 < 20 or 15 > 25 = {expr7}")  # True
# Adım adım: (5>3)=True, (10<20)=True, (15>25)=False
#            True and True or False
#            True or False
#            True


# =============================================================================
# SORU 12: [Zor] Short-Circuit Evaluation
# =============================================================================
# Short-circuit evaluation'ı gösterin:
# 1. False and expensive_function() - fonksiyon çağrılmaz
# 2. True or expensive_function() - fonksiyon çağrılmaz
# Bir sayaç ile fonksiyon kaç kez çağrıldığını gösterin

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- and operatörü: İlk False'da durur, sağ tarafı değerlendirmez
- or operatörü: İlk True'da durur, sağ tarafı değerlendirmez
- Bu davranış performans için önemli ve bazen hata önleme için kullanılır
"""

call_count = 0

def expensive_function():
    """Pahalı bir işlemi simüle eder"""
    global call_count
    call_count += 1
    print(f"  [expensive_function çağrıldı - {call_count}. kez]")
    return True

print("\n--- Short-Circuit Evaluation ---")

# Test 1: False and ... (fonksiyon çağrılmaz)
print("Test 1: False and expensive_function()")
call_count = 0
result = False and expensive_function()
print(f"  Sonuç: {result}, Çağrı sayısı: {call_count}")  # 0

# Test 2: True or ... (fonksiyon çağrılmaz)
print("\nTest 2: True or expensive_function()")
call_count = 0
result = True or expensive_function()
print(f"  Sonuç: {result}, Çağrı sayısı: {call_count}")  # 0

# Test 3: True and ... (fonksiyon çağrılır)
print("\nTest 3: True and expensive_function()")
call_count = 0
result = True and expensive_function()
print(f"  Sonuç: {result}, Çağrı sayısı: {call_count}")  # 1

# Test 4: False or ... (fonksiyon çağrılır)
print("\nTest 4: False or expensive_function()")
call_count = 0
result = False or expensive_function()
print(f"  Sonuç: {result}, Çağrı sayısı: {call_count}")  # 1

# Pratik kullanım: Güvenli değer erişimi
print("\n--- Pratik Kullanım ---")
data = None

# Hatalı: data.upper() -> AttributeError
# result = data.upper()

# Doğru: Short-circuit kullanımı
result = data and data.upper()
print(f"data and data.upper(): {result}")  # None (hata vermez)

data = "hello"
result = data and data.upper()
print(f"data and data.upper(): {result}")  # HELLO


# =============================================================================
# SORU 13: [Challenge] Bitwise ile Çift/Tek ve Swap
# =============================================================================
# Bitwise operatörler kullanarak:
# 1. Bir sayının çift mi tek mi olduğunu kontrol edin (% kullanmadan)
# 2. İki sayıyı swap edin (geçici değişken kullanmadan, XOR ile)
# 3. Bir sayıyı 2 ile çarpın (bitwise shift kullanarak)
# 4. Bir sayıyı 4'e bölün (bitwise shift kullanarak)

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Bitwise & ile son bit kontrolü: n & 1 (0 ise çift, 1 ise tek)
- XOR swap: a ^= b, b ^= a, a ^= b
- Left shift (<<): 2 ile çarpma
- Right shift (>>): 2 ile bölme
"""

print("\n--- Bitwise Operatörler ---")

# 1. Çift/Tek kontrolü
def is_even_bitwise(n):
    """Bitwise AND ile çift kontrolü"""
    return (n & 1) == 0

numbers = [10, 15, 22, 37, 100]
print("Çift/Tek Kontrolü (Bitwise):")
for num in numbers:
    status = "Çift" if is_even_bitwise(num) else "Tek"
    print(f"  {num}: {status} (binary: {bin(num)})")

# 2. XOR Swap
print("\nXOR Swap:")
x = 25
y = 50
print(f"Başlangıç: x={x}, y={y}")
print(f"  x binary: {bin(x)}")
print(f"  y binary: {bin(y)}")

x = x ^ y  # x = 25 XOR 50
y = x ^ y  # y = (25 XOR 50) XOR 50 = 25
x = x ^ y  # x = (25 XOR 50) XOR 25 = 50

print(f"Swap sonrası: x={x}, y={y}")

# Alternatif: Tek satırda
a, b = 100, 200
a ^= b
b ^= a
a ^= b
print(f"XOR swap: a={a}, b={b}")

# 3. 2 ile çarpma (left shift)
print("\n2 ile Çarpma (Left Shift):")
num = 10
for i in range(4):
    result = num << i
    print(f"  {num} << {i} = {result} (= {num} * {2**i})")

# 4. 2 ile bölme (right shift)
print("\n2 ile Bölme (Right Shift):")
num = 100
for i in range(4):
    result = num >> i
    print(f"  {num} >> {i} = {result} (= {num} // {2**i})")

# Bonus: Hızlı çarpma/bölme karşılaştırması
import time

num = 1000000
iterations = 10000000

# Normal çarpma
start = time.time()
for _ in range(iterations):
    result = num * 2
normal_time = time.time() - start

# Bitwise çarpma
start = time.time()
for _ in range(iterations):
    result = num << 1
bitwise_time = time.time() - start

print(f"\nPerformans Karşılaştırması ({iterations} iterasyon):")
print(f"  Normal çarpma: {normal_time:.4f} saniye")
print(f"  Bitwise shift: {bitwise_time:.4f} saniye")
print(f"  Hız artışı: {normal_time/bitwise_time:.2f}x")


# =============================================================================
# SORU 14: [Challenge] Operatörlerle BMI Hesaplama ve Kategori
# =============================================================================
# Vücut Kitle İndeksi (BMI) hesaplayıcısı yazın:
# - Kilo (kg) ve boy (m) bilgisi alın
# - BMI = kilo / (boy ** 2)
# - Kategorileri belirleyin:
#   * BMI < 18.5: Zayıf
#   * 18.5 <= BMI < 25: Normal
#   * 25 <= BMI < 30: Fazla Kilolu
#   * 30 <= BMI < 35: Obez (1. Derece)
#   * 35 <= BMI < 40: Obez (2. Derece)
#   * BMI >= 40: Obez (3. Derece - Morbid)
# Sonucu renkli ve detaylı yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- ** operatörü ile üs alma (boy^2)
- / operatörü ile bölme
- Zincir karşılaştırma ile kategori belirleme
- f-string ile formatlı çıktı
"""

def calculate_bmi(weight, height):
    """BMI hesaplar ve kategori belirler"""
    # BMI hesaplama
    bmi = weight / (height ** 2)

    # Kategori belirleme
    if bmi < 18.5:
        category = "Zayıf"
        emoji = "⚠️"
        advice = "Kilo almanız önerilir"
    elif 18.5 <= bmi < 25:
        category = "Normal"
        emoji = "✅"
        advice = "İdeal kiloda sınız"
    elif 25 <= bmi < 30:
        category = "Fazla Kilolu"
        emoji = "⚠️"
        advice = "Kilo vermeniz önerilir"
    elif 30 <= bmi < 35:
        category = "Obez (1. Derece)"
        emoji = "❗"
        advice = "Doktor kontrolü önerilir"
    elif 35 <= bmi < 40:
        category = "Obez (2. Derece)"
        emoji = "❗❗"
        advice = "Mutlaka doktora başvurun"
    else:  # bmi >= 40
        category = "Obez (3. Derece - Morbid)"
        emoji = "🚨"
        advice = "Acil doktor kontrolü gerekli"

    return bmi, category, emoji, advice


print("\n--- BMI Hesaplayıcı ---")

# Test örnekleri
test_cases = [
    (50, 1.70, "Ayşe"),
    (75, 1.75, "Mehmet"),
    (90, 1.80, "Ali"),
    (120, 1.65, "Fatma"),
]

print(f"{'İsim':<10} {'Kilo':<8} {'Boy':<8} {'BMI':<10} {'Kategori':<25} {'Tavsiye':<30}")
print("=" * 100)

for weight, height, name in test_cases:
    bmi, category, emoji, advice = calculate_bmi(weight, height)
    print(f"{name:<10} {weight:<8} {height:<8.2f} {bmi:<10.2f} {emoji} {category:<23} {advice:<30}")

# Detaylı örnek
print("\n" + "="*100)
print("DETAYLI BMI RAPORU")
print("="*100)

weight = 85
height = 1.75
name = "Kullanıcı"

bmi, category, emoji, advice = calculate_bmi(weight, height)

print(f"\nKişi: {name}")
print(f"Kilo: {weight} kg")
print(f"Boy: {height} m")
print(f"\n{emoji} BMI: {bmi:.2f}")
print(f"{emoji} Kategori: {category}")
print(f"{emoji} Tavsiye: {advice}")

# İdeal kilo aralığı hesaplama
ideal_bmi_min = 18.5
ideal_bmi_max = 24.9
ideal_weight_min = ideal_bmi_min * (height ** 2)
ideal_weight_max = ideal_bmi_max * (height ** 2)

print(f"\n📊 İdeal Kilo Aralığınız: {ideal_weight_min:.1f} - {ideal_weight_max:.1f} kg")

# Kilo değişimi önerisi
if bmi < 18.5:
    target_weight = ideal_bmi_min * (height ** 2)
    weight_change = target_weight - weight
    print(f"💪 {abs(weight_change):.1f} kg almanız önerilir")
elif bmi > 25:
    target_weight = ideal_bmi_max * (height ** 2)
    weight_change = target_weight - weight
    print(f"💪 {abs(weight_change):.1f} kg vermeniz önerilir")


# =============================================================================
# SORU 15: [Challenge] Gelişmiş Mantıksal İfade Değerlendirici
# =============================================================================
# Bir kullanıcı yetkilendirme sistemi yazın:
# Kullanıcı bilgileri:
# - age: yaş
# - is_member: üye mi?
# - has_premium: premium üyeliği var mı?
# - login_count: kaç kez giriş yapmış?
# - is_verified: doğrulanmış mı?
#
# Erişim kuralları:
# 1. VIP Erişim: (Premium üye VE doğrulanmış) VEYA (10+ giriş VE üye)
# 2. Standart Erişim: Üye VE 18+ yaş VE doğrulanmış
# 3. Deneme Erişimi: Üye değil AMA 18+ yaş
# 4. Erişim Yok: Diğer durumlar
#
# Farklı kullanıcı profilleri test edin

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Karmaşık mantıksal ifadeleri and, or, not ile oluşturuyoruz
- Parantez ile öncelik belirliyoruz
- Karşılaştırma operatörleri ile koşul kontrolü yapıyoruz
- Her koşulu ayrı değişkende tutarak okunabilirlik artırıyoruz
"""

def check_access(age, is_member, has_premium, login_count, is_verified, name="User"):
    """Kullanıcı erişim seviyesini belirler"""

    print(f"\n--- {name} için Erişim Kontrolü ---")
    print(f"Yaş: {age}")
    print(f"Üye: {is_member}")
    print(f"Premium: {has_premium}")
    print(f"Giriş Sayısı: {login_count}")
    print(f"Doğrulanmış: {is_verified}")

    # VIP Erişim kontrolü
    vip_condition1 = has_premium and is_verified
    vip_condition2 = login_count >= 10 and is_member
    has_vip_access = vip_condition1 or vip_condition2

    # Standart Erişim kontrolü
    has_standard_access = is_member and age >= 18 and is_verified

    # Deneme Erişim kontrolü
    has_trial_access = not is_member and age >= 18

    # Erişim seviyesi belirleme
    if has_vip_access:
        access_level = "VIP Erişim"
        emoji = "👑"
        features = ["Tüm özellikler", "Reklamsız", "Öncelikli destek", "Özel içerik"]
    elif has_standard_access:
        access_level = "Standart Erişim"
        emoji = "✅"
        features = ["Temel özellikler", "Topluluk erişimi", "Standart destek"]
    elif has_trial_access:
        access_level = "Deneme Erişimi"
        emoji = "🔓"
        features = ["Sınırlı özellikler", "3 günlük deneme"]
    else:
        access_level = "Erişim Yok"
        emoji = "🚫"
        features = ["Lütfen kaydolun veya giriş yapın"]

    print(f"\n{emoji} Erişim Seviyesi: {access_level}")
    print(f"Özellikler:")
    for feature in features:
        print(f"  • {feature}")

    # Detaylı analiz
    print(f"\nKoşul Analizi:")
    print(f"  VIP (Premium VE Doğrulanmış): {vip_condition1}")
    print(f"  VIP (10+ Giriş VE Üye): {vip_condition2}")
    print(f"  VIP Toplam: {has_vip_access}")
    print(f"  Standart: {has_standard_access}")
    print(f"  Deneme: {has_trial_access}")

    return access_level


# Test senaryoları
print("\n" + "="*80)
print("KULLANICI YETKİLENDİRME SİSTEMİ")
print("="*80)

# Senaryo 1: VIP kullanıcı (premium + verified)
check_access(
    age=25,
    is_member=True,
    has_premium=True,
    login_count=5,
    is_verified=True,
    name="VIP Kullanıcı"
)

# Senaryo 2: VIP kullanıcı (10+ login + member)
check_access(
    age=30,
    is_member=True,
    has_premium=False,
    login_count=15,
    is_verified=False,
    name="Aktif Kullanıcı"
)

# Senaryo 3: Standart kullanıcı
check_access(
    age=22,
    is_member=True,
    has_premium=False,
    login_count=3,
    is_verified=True,
    name="Standart Kullanıcı"
)

# Senaryo 4: Deneme kullanıcısı
check_access(
    age=20,
    is_member=False,
    has_premium=False,
    login_count=0,
    is_verified=False,
    name="Yeni Ziyaretçi"
)

# Senaryo 5: Erişim yok (yaş küçük)
check_access(
    age=16,
    is_member=False,
    has_premium=False,
    login_count=0,
    is_verified=False,
    name="Genç Ziyaretçi"
)

# Senaryo 6: Erişim yok (üye ama doğrulanmamış)
check_access(
    age=25,
    is_member=True,
    has_premium=False,
    login_count=2,
    is_verified=False,
    name="Doğrulanmamış Üye"
)

# Özet tablo
print("\n" + "="*80)
print("ERİŞİM SEVİYELERİ ÖZETİ")
print("="*80)
print("\n1. 👑 VIP Erişim:")
print("   • (Premium ÜYELİK VE Doğrulanmış) VEYA")
print("   • (10+ Giriş VE Üye)")
print("\n2. ✅ Standart Erişim:")
print("   • Üye VE 18+ Yaş VE Doğrulanmış")
print("\n3. 🔓 Deneme Erişimi:")
print("   • Üye DEĞİL AMA 18+ Yaş")
print("\n4. 🚫 Erişim Yok:")
print("   • Diğer tüm durumlar")


# =============================================================================
# ALIŞTIRMALARIN SONU
# =============================================================================

print("\n" + "="*80)
print("TEBRİKLER! TÜM ALIŞTIRMALARI TAMAMLADINIZ!")
print("="*80)
print("\nBu bölümde şunları öğrendiniz:")
print("✓ Aritmetik operatörler (+, -, *, /, //, %, **)")
print("✓ Karşılaştırma operatörleri (==, !=, >, <, >=, <=)")
print("✓ Mantıksal operatörler (and, or, not)")
print("✓ Atama operatörleri (=, +=, -=, vb.)")
print("✓ Kimlik operatörleri (is, is not)")
print("✓ Üyelik operatörleri (in, not in)")
print("✓ Bitwise operatörler (&, |, ^, ~, <<, >>)")
print("✓ Operatör önceliği ve short-circuit evaluation")
print("\nSıradaki konu: 03-Control-Structures")
print("="*80)
