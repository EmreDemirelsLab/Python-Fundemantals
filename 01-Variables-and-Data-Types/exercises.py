"""
VARIABLES AND DATA TYPES - ALIŞTIRMALAR
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
# SORU 1: [Kolay] Değişken Tanımlama
# =============================================================================
# Kendi bilgilerinizi içeren değişkenler oluşturun:
# - Adınız (string)
# - Yaşınız (integer)
# - Boyunuz metre cinsinden (float)
# - Öğrenci olup olmadığınız (boolean)
# Sonra hepsini ekrana yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- String değerler tek veya çift tırnak içinde yazılır
- Integer tam sayıları temsil eder
- Float ondalıklı sayıları temsil eder
- Boolean True veya False değerlerini alır (büyük harfle başlar!)
"""

my_name = "Ahmet Yılmaz"
my_age = 22
my_height = 1.78
is_student = True

print("Adım:", my_name)
print("Yaşım:", my_age)
print("Boyum:", my_height)
print("Öğrenci miyim?:", is_student)

# Alternatif: f-string kullanarak
print(f"\nAdım {my_name}, {my_age} yaşındayım ve boyum {my_height}m")


# =============================================================================
# SORU 2: [Kolay] Tip Kontrolü
# =============================================================================
# Yukarıda oluşturduğunuz her değişkenin tipini type() fonksiyonu ile
# kontrol edin ve ekrana yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- type() fonksiyonu bir değişkenin veya değerin veri tipini döndürür
- Dönen değer <class 'tip_adı'> formatındadır
"""

print("\n--- Tip Kontrolleri ---")
print("my_name tipi:", type(my_name))        # <class 'str'>
print("my_age tipi:", type(my_age))          # <class 'int'>
print("my_height tipi:", type(my_height))    # <class 'float'>
print("is_student tipi:", type(is_student))  # <class 'bool'>


# =============================================================================
# SORU 3: [Kolay] Matematiksel İşlemler
# =============================================================================
# İki sayı değişkeni oluşturun (a = 15, b = 4) ve şu işlemleri yapın:
# - Toplama
# - Çıkarma
# - Çarpma
# - Bölme
# - Tam bölme (floor division)
# - Mod (kalan)
# - Üs alma

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- / operatörü normal bölme yapar ve float döndürür
- // operatörü tam bölme yapar (ondalık kısmı atar)
- % operatörü bölme işleminden kalanı verir
- ** operatörü üs alma yapar
"""

a = 15
b = 4

print("\n--- Matematiksel İşlemler ---")
print(f"{a} + {b} =", a + b)      # 19
print(f"{a} - {b} =", a - b)      # 11
print(f"{a} * {b} =", a * b)      # 60
print(f"{a} / {b} =", a / b)      # 3.75
print(f"{a} // {b} =", a // b)    # 3
print(f"{a} % {b} =", a % b)      # 3
print(f"{a} ** {b} =", a ** b)    # 50625


# =============================================================================
# SORU 4: [Kolay] String Birleştirme
# =============================================================================
# first_name ve last_name adında iki değişken oluşturun.
# Bu iki değişkeni birleştirerek full_name değişkeni oluşturun.
# Aralarında boşluk olduğundan emin olun.

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- String'ler + operatörü ile birleştirilebilir (concatenation)
- Araya boşluk eklemek için " " kullanılır
- Alternatif olarak f-string, format() veya join() kullanılabilir
"""

first_name = "Mehmet"
last_name = "Demir"

# Method 1: + operatörü
full_name = first_name + " " + last_name
print("\n--- String Birleştirme ---")
print("Tam adı:", full_name)

# Method 2: f-string (önerilen)
full_name = f"{first_name} {last_name}"
print("Tam adı (f-string):", full_name)

# Method 3: format()
full_name = "{} {}".format(first_name, last_name)
print("Tam adı (format):", full_name)

# Method 4: join()
full_name = " ".join([first_name, last_name])
print("Tam adı (join):", full_name)


# =============================================================================
# SORU 5: [Orta] Tip Dönüşümü
# =============================================================================
# Kullanıcıdan yaş bilgisini string olarak alın (age_str = "25")
# Bu string'i integer'a çevirin, 5 ekleyin ve sonucu yazdırın
# Sonra bu sonucu tekrar string'e çevirin ve "Yaşınız: X" şeklinde yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- int() fonksiyonu string'i integer'a çevirir
- String ile integer + ile birleştirilemez, önce dönüşüm gerekir
- str() fonksiyonu integer'ı string'e çevirir
- f-string kullanarak otomatik dönüşüm de yapılabilir
"""

age_str = "25"
print("\n--- Tip Dönüşümü ---")
print("Orijinal:", age_str, "- Tipi:", type(age_str))

# String'i integer'a çevir
age_int = int(age_str)
print("Integer'a çevrildi:", age_int, "- Tipi:", type(age_int))

# 5 ekle
new_age = age_int + 5
print("5 eklendi:", new_age)

# Tekrar string'e çevir ve yazdır
result = "Yaşınız: " + str(new_age)
print(result)

# Alternatif: f-string (otomatik dönüşüm)
result = f"Yaşınız: {new_age}"
print(result)


# =============================================================================
# SORU 6: [Orta] Boolean Mantığı
# =============================================================================
# İki boolean değişken oluşturun: has_license = True, has_car = False
# Şu durumları kontrol edin ve sonuçları yazdırın:
# - Her ikisi de True mu?
# - En az biri True mu?
# - has_license True ama has_car False mu?

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- and operatörü: Her ikisi de True ise True döner
- or operatörü: En az biri True ise True döner
- not operatörü: Değeri tersine çevirir
- Karışık mantıksal ifadeler parantez ile gruplandırılabilir
"""

has_license = True
has_car = False

print("\n--- Boolean Mantığı ---")
print("Ehliyetim var:", has_license)
print("Arabam var:", has_car)

# Her ikisi de True mu?
both_true = has_license and has_car
print("\nHer ikisi de var mı?:", both_true)  # False

# En az biri True mu?
at_least_one = has_license or has_car
print("En az biri var mı?:", at_least_one)  # True

# has_license True ama has_car False mu?
specific_case = has_license and not has_car
print("Ehliyetim var ama arabam yok mu?:", specific_case)  # True


# =============================================================================
# SORU 7: [Orta] String İşlemleri
# =============================================================================
# Bir email adresi string'i oluşturun: "AHMET.YILMAZ@EMAIL.COM"
# Şunları yapın:
# 1. Tamamını küçük harfe çevirin
# 2. @ işaretinin konumunu bulun
# 3. Kullanıcı adını (@ öncesi) ve domain'i (@ sonrası) ayırın
# 4. Kullanıcı adındaki . işaretini boşlukla değiştirin

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- lower() metodu string'i küçük harfe çevirir
- find() metodu belirtilen karakterin indeksini döndürür
- split() metodu string'i belirtilen ayırıcıya göre böler
- replace() metodu karakter/string değiştirir
- String slicing ile belirli kısımlar alınabilir
"""

email = "AHMET.YILMAZ@EMAIL.COM"
print("\n--- String İşlemleri ---")
print("Orijinal email:", email)

# 1. Küçük harfe çevir
email_lower = email.lower()
print("Küçük harf:", email_lower)

# 2. @ işaretinin konumu
at_position = email_lower.find('@')
print("@ işaretinin konumu:", at_position)

# 3. Kullanıcı adı ve domain'i ayır
# Method 1: split() kullanarak
parts = email_lower.split('@')
username = parts[0]
domain = parts[1]
print("Kullanıcı adı:", username)
print("Domain:", domain)

# Method 2: slicing kullanarak
username_alt = email_lower[:at_position]
domain_alt = email_lower[at_position + 1:]
print("Kullanıcı adı (slicing):", username_alt)
print("Domain (slicing):", domain_alt)

# 4. Kullanıcı adındaki . işaretini boşlukla değiştir
username_formatted = username.replace('.', ' ')
print("Formatlanmış kullanıcı adı:", username_formatted)

# Tam isim olarak yazdır (title case)
full_name = username_formatted.title()
print("Tam isim:", full_name)


# =============================================================================
# SORU 8: [Orta] Değişken Değiştirme (Swap)
# =============================================================================
# İki değişken oluşturun: x = 10, y = 20
# Bu iki değişkenin değerlerini yer değiştirin (swap)
# Python'a özgü yöntemi kullanın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Python'da tuple unpacking kullanarak değişken swap çok kolaydır
- Geleneksel yöntemde geçici değişken (temp) gerekir
- Python yöntemi daha temiz ve okunabilirdir
"""

x = 10
y = 20

print("\n--- Değişken Swap ---")
print("Başlangıç - x:", x, "y:", y)

# Python yöntemi (tuple unpacking)
x, y = y, x
print("Swap sonrası - x:", x, "y:", y)

# Geleneksel yöntem (referans için)
a = 100
b = 200
print("\nGeleneksel yöntem - a:", a, "b:", b)
temp = a
a = b
b = temp
print("Swap sonrası - a:", a, "b:", b)

# Matematiksel yöntem (sadece sayılar için)
m = 5
n = 15
print("\nMatematiksel yöntem - m:", m, "n:", n)
m = m + n  # m = 20
n = m - n  # n = 5
m = m - n  # m = 15
print("Swap sonrası - m:", m, "n:", n)


# =============================================================================
# SORU 9: [Zor] Çoklu Tip Dönüşümü ve Doğrulama
# =============================================================================
# Kullanıcıdan alınmış string değerler var (gerçekte input ile alınmış gibi):
# price_str = "99.99"
# quantity_str = "5"
# discount_str = "15"  (yüzde cinsinden)
#
# Bunları kullanarak:
# 1. Toplam fiyatı hesaplayın (price * quantity)
# 2. İndirimi uygulayın
# 3. Sonucu 2 ondalık basamakla gösterin
# 4. Sonucu güzel bir formatta yazdırın

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- String'leri uygun tiplere dönüştürmeliyiz
- İndirim hesaplaması: toplam * (1 - discount/100)
- round() fonksiyonu ondalık basamak sayısını belirler
- f-string ile formatlama yapabiliriz: {değer:.2f} (2 ondalık basamak)
"""

price_str = "99.99"
quantity_str = "5"
discount_str = "15"

print("\n--- Fiyat Hesaplama ---")

# 1. String'leri dönüştür
price = float(price_str)
quantity = int(quantity_str)
discount = float(discount_str)

print(f"Birim fiyat: ${price}")
print(f"Miktar: {quantity}")
print(f"İndirim: %{discount}")

# 2. Toplam fiyat (indirim öncesi)
subtotal = price * quantity
print(f"\nAra toplam: ${subtotal}")

# 3. İndirim tutarı
discount_amount = subtotal * (discount / 100)
print(f"İndirim tutarı: ${discount_amount:.2f}")

# 4. İndirim sonrası toplam
total = subtotal - discount_amount
# Alternatif: total = subtotal * (1 - discount/100)
print(f"İndirimli toplam: ${total:.2f}")

# Bonus: Detaylı makbuz formatı
print("\n" + "="*40)
print("           SATIN ALMA MAKBUZU")
print("="*40)
print(f"Birim Fiyat:        ${price:>10.2f}")
print(f"Miktar:             {quantity:>10}")
print(f"Ara Toplam:         ${subtotal:>10.2f}")
print(f"İndirim (%{discount}):     -${discount_amount:>10.2f}")
print("-"*40)
print(f"TOPLAM:             ${total:>10.2f}")
print("="*40)


# =============================================================================
# SORU 10: [Zor] Veri Tipi Validasyonu
# =============================================================================
# Bir fonksiyon yazın: validate_input(value, expected_type)
# Bu fonksiyon verilen value'nun expected_type tipinde olup olmadığını kontrol etsin
# Eğer doğru tipse "Geçerli" mesajı, değilse tip dönüşümü yapmaya çalışsın
# Dönüşüm mümkün değilse hata mesajı versin

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- isinstance() fonksiyonu tip kontrolü yapar
- try-except bloğu ile hata yakalama yapılır
- Dinamik tip dönüşümü için dönüştürücü fonksiyon çağrılır
"""

def validate_input(value, expected_type):
    """
    Verilen değerin beklenen tipte olup olmadığını kontrol eder.
    Değilse, dönüştürmeyi dener.
    """
    # Önce tip kontrolü
    if isinstance(value, expected_type):
        print(f"✓ '{value}' zaten {expected_type.__name__} tipinde")
        return value

    # Tip dönüşümü dene
    try:
        if expected_type == int:
            converted = int(value)
        elif expected_type == float:
            converted = float(value)
        elif expected_type == str:
            converted = str(value)
        elif expected_type == bool:
            # String'den bool'a özel dönüşüm
            if isinstance(value, str):
                if value.lower() in ['true', '1', 'yes']:
                    converted = True
                elif value.lower() in ['false', '0', 'no']:
                    converted = False
                else:
                    raise ValueError("Boolean'a dönüştürülemez")
            else:
                converted = bool(value)
        else:
            raise ValueError(f"Desteklenmeyen tip: {expected_type}")

        print(f"→ '{value}' ({type(value).__name__}) → '{converted}' ({expected_type.__name__}) dönüştürüldü")
        return converted

    except (ValueError, TypeError) as e:
        print(f"✗ Hata: '{value}' {expected_type.__name__} tipine dönüştürülemedi")
        print(f"  Sebep: {e}")
        return None


# Test örnekleri
print("\n--- Veri Tipi Validasyonu ---")
validate_input(42, int)                    # Zaten int
validate_input("42", int)                  # String'den int'e dönüşür
validate_input("3.14", float)              # String'den float'a dönüşür
validate_input(100, str)                   # Int'ten string'e dönüşür
validate_input("True", bool)               # String'den bool'a dönüşür
validate_input("abc", int)                 # Hata: dönüştürülemez
validate_input([1, 2, 3], int)             # Hata: dönüştürülemez


# =============================================================================
# SORU 11: [Zor] Hassas Ondalık Hesaplama
# =============================================================================
# Float'ların hassasiyet problemini gösterin ve çözün:
# 1. 0.1 + 0.1 + 0.1 işleminin sonucunu gösterin
# 2. Sonucun 0.3'e eşit olup olmadığını kontrol edin
# 3. Decimal modülü kullanarak aynı işlemi yapın ve farkı gösterin
# 4. İki float sayının "yaklaşık eşit" olup olmadığını kontrol eden bir yöntem gösterin

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Float'lar binary gösterimde tam olarak ifade edilemeyebilir
- Decimal modülü finansal hesaplamalar için daha uygundur
- math.isclose() fonksiyonu yaklaşık eşitlik kontrolü yapar
- Tolerans değeri (epsilon) ile karşılaştırma yapılabilir
"""

from decimal import Decimal, getcontext
import math

print("\n--- Float Hassasiyet Problemi ---")

# 1. Float işlemi
result_float = 0.1 + 0.1 + 0.1
print(f"Float işlemi: 0.1 + 0.1 + 0.1 = {result_float}")
print(f"Tam gösterim: {result_float:.20f}")

# 2. Eşitlik kontrolü
is_equal = (result_float == 0.3)
print(f"\nSonuç 0.3'e eşit mi? {is_equal}")  # False!
print(f"Beklenen: 0.3")
print(f"Gerçek:   {result_float}")

# 3. Decimal modülü kullanımı
print("\n--- Decimal Çözümü ---")
getcontext().prec = 28  # Hassasiyet ayarı

result_decimal = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(f"Decimal işlemi: 0.1 + 0.1 + 0.1 = {result_decimal}")
is_equal_decimal = (result_decimal == Decimal('0.3'))
print(f"Sonuç 0.3'e eşit mi? {is_equal_decimal}")  # True!

# 4. Yaklaşık eşitlik kontrolü
print("\n--- Yaklaşık Eşitlik Kontrolü ---")

# Method 1: math.isclose() (Python 3.5+)
is_close = math.isclose(result_float, 0.3, rel_tol=1e-9)
print(f"math.isclose() ile: {is_close}")  # True

# Method 2: Manuel epsilon kontrolü
epsilon = 1e-10
is_approx_equal = abs(result_float - 0.3) < epsilon
print(f"Epsilon kontrolü ile: {is_approx_equal}")  # True

# Method 3: round() kullanımı
rounded = round(result_float, 2)
print(f"round() ile: {rounded == 0.3}")  # True

# Pratik örnek: Fiyat hesaplaması
print("\n--- Pratik Örnek: Fiyat Hesaplaması ---")
price1 = 10.10
price2 = 20.20
price3 = 30.30
total_float = price1 + price2 + price3
print(f"Float toplam: ${total_float:.2f}")

# Decimal ile daha güvenli
price1_d = Decimal('10.10')
price2_d = Decimal('20.20')
price3_d = Decimal('30.30')
total_decimal = price1_d + price2_d + price3_d
print(f"Decimal toplam: ${total_decimal}")


# =============================================================================
# SORU 12: [Challenge] Akıllı Tip Dönüştürücü
# =============================================================================
# Bir smart_convert() fonksiyonu yazın:
# - String input alır
# - Otomatik olarak en uygun veri tipine dönüştürmeye çalışır
# - Mümkün olan tipleri şu sırada denesin: int → float → bool → str
# - Dönüştürülen değeri ve tipini döndürsün
#
# Örnekler:
# "42" → 42 (int)
# "3.14" → 3.14 (float)
# "True" → True (bool)
# "Hello" → "Hello" (str - dönüştürülemediği için aynı kalır)

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Tip dönüşümlerini sırayla deniyoruz
- Her başarısız denemede bir sonraki tipe geçiyoruz
- Boolean kontrolü özel: belirli string değerlerini kabul eder
- Son çare olarak string olarak bırakıyoruz
"""

def smart_convert(value):
    """
    String input'u otomatik olarak en uygun veri tipine dönüştürür.

    Args:
        value (str): Dönüştürülecek string değer

    Returns:
        tuple: (dönüştürülmüş_değer, tip_adı)
    """
    if not isinstance(value, str):
        return value, type(value).__name__

    original = value
    value = value.strip()  # Baştaki ve sondaki boşlukları temizle

    # 1. Integer'a dönüşüm dene
    try:
        # Nokta içeriyorsa ve ondalık kısmı 0 ise
        if '.' in value:
            float_val = float(value)
            if float_val.is_integer():
                result = int(float_val)
                return result, "int"
        else:
            result = int(value)
            return result, "int"
    except ValueError:
        pass

    # 2. Float'a dönüşüm dene
    try:
        result = float(value)
        return result, "float"
    except ValueError:
        pass

    # 3. Boolean'a dönüşüm dene
    if value.lower() in ['true', 't', 'yes', 'y', '1']:
        return True, "bool"
    elif value.lower() in ['false', 'f', 'no', 'n', '0']:
        return False, "bool"

    # 4. Hiçbiri olmadıysa string olarak bırak
    return original, "str"


# Test fonksiyonu
def test_smart_convert():
    test_cases = [
        "42",
        "3.14",
        "2.0",
        "True",
        "false",
        "yes",
        "NO",
        "Hello World",
        "  123  ",
        "-99",
        "1.23e2",  # Bilimsel gösterim
        "0xFF",    # Hexadecimal (string kalacak, int() hexadecimal parse etmez strip edildiğinde)
    ]

    print("\n--- Akıllı Tip Dönüştürücü ---")
    print(f"{'Input':<20} {'Output':<20} {'Type':<10}")
    print("-" * 50)

    for test in test_cases:
        result, result_type = smart_convert(test)
        print(f"{test!r:<20} {str(result):<20} {result_type:<10}")


test_smart_convert()


# =============================================================================
# SORU 13: [Challenge] Çoklu Dönüştürme ve Validasyon
# =============================================================================
# Bir FormValidator sınıfı oluşturun (OOP henüz öğrenmediyseniz fonksiyonlarla yapabilirsiniz):
# Form alanları ve beklenen tipleri ile initialize edin:
# {
#     "name": str,
#     "age": int,
#     "email": str,
#     "balance": float,
#     "is_active": bool
# }
#
# validate() metodu:
# - Verilen değerleri kontrol etsin
# - Tip dönüşümü yapabiliyorsa yapsın
# - Yapamıyorsa hata bildirsin
# - Email için basit format kontrolü yapsın (@ içermeli)
# - Age için aralık kontrolü yapsın (0-150)
# - Balance negatif olamaz
#
# Örnek kullanım:
# validator.validate({
#     "name": "Ali Veli",
#     "age": "25",
#     "email": "ali@example.com",
#     "balance": "1000.50",
#     "is_active": "True"
# })

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- Class-based yaklaşım daha organize ve genişletilebilir
- Her field için tip kontrolü ve dönüşüm yapıyoruz
- Ek validasyon kuralları ekliyoruz (email format, age range, balance)
- Detaylı hata mesajları döndürüyoruz
"""

class FormValidator:
    """
    Form verilerini valide eden ve tip dönüşümü yapan sınıf.
    """

    def __init__(self, schema):
        """
        Args:
            schema (dict): Alan adları ve beklenen tipleri içeren sözlük
        """
        self.schema = schema
        self.errors = []

    def validate(self, data):
        """
        Form verilerini valide eder.

        Args:
            data (dict): Valide edilecek form verileri

        Returns:
            tuple: (başarılı_mı, temizlenmiş_veri, hatalar)
        """
        self.errors = []
        cleaned_data = {}

        # Her schema alanı için kontrol yap
        for field_name, expected_type in self.schema.items():
            if field_name not in data:
                self.errors.append(f"'{field_name}' alanı eksik")
                continue

            value = data[field_name]

            # Tip dönüşümü ve validasyon
            converted_value = self._convert_and_validate(
                field_name, value, expected_type
            )

            if converted_value is not None:
                cleaned_data[field_name] = converted_value

        # Başarılı mı?
        success = len(self.errors) == 0
        return success, cleaned_data, self.errors

    def _convert_and_validate(self, field_name, value, expected_type):
        """
        Tek bir alanı dönüştürür ve valide eder.
        """
        # Zaten doğru tipteyse direkt kabul et
        if isinstance(value, expected_type):
            converted = value
        else:
            # Tip dönüşümü dene
            try:
                if expected_type == bool:
                    # Boolean özel durum
                    if isinstance(value, str):
                        if value.lower() in ['true', '1', 'yes']:
                            converted = True
                        elif value.lower() in ['false', '0', 'no']:
                            converted = False
                        else:
                            raise ValueError("Boolean değeri geçersiz")
                    else:
                        converted = bool(value)
                else:
                    converted = expected_type(value)
            except (ValueError, TypeError) as e:
                self.errors.append(
                    f"'{field_name}': {expected_type.__name__} tipine dönüştürülemedi"
                )
                return None

        # Ek validasyonlar
        if field_name == "email":
            if "@" not in converted or "." not in converted:
                self.errors.append(f"'{field_name}': Geçersiz email formatı")
                return None

        elif field_name == "age":
            if not (0 <= converted <= 150):
                self.errors.append(f"'{field_name}': Yaş 0-150 arasında olmalı")
                return None

        elif field_name == "balance":
            if converted < 0:
                self.errors.append(f"'{field_name}': Bakiye negatif olamaz")
                return None

        return converted

    def get_errors(self):
        """Hata mesajlarını döndürür."""
        return self.errors


# Test fonksiyonu
def test_form_validator():
    print("\n--- Form Validator ---\n")

    # Schema tanımla
    schema = {
        "name": str,
        "age": int,
        "email": str,
        "balance": float,
        "is_active": bool
    }

    validator = FormValidator(schema)

    # Test case 1: Geçerli veri
    print("Test 1: Geçerli Veri")
    print("-" * 50)
    test_data = {
        "name": "Ali Veli",
        "age": "25",
        "email": "ali@example.com",
        "balance": "1000.50",
        "is_active": "True"
    }

    success, cleaned, errors = validator.validate(test_data)
    if success:
        print("✓ Validasyon başarılı!")
        print("Temizlenmiş veri:")
        for key, value in cleaned.items():
            print(f"  {key}: {value} ({type(value).__name__})")
    else:
        print("✗ Validasyon başarısız!")
        for error in errors:
            print(f"  - {error}")

    # Test case 2: Geçersiz veri
    print("\n\nTest 2: Geçersiz Veri")
    print("-" * 50)
    test_data_invalid = {
        "name": "Mehmet Yılmaz",
        "age": "200",  # Yaş aralık dışı
        "email": "invalid-email",  # Geçersiz format
        "balance": "-100",  # Negatif
        "is_active": "maybe"  # Geçersiz boolean
    }

    success, cleaned, errors = validator.validate(test_data_invalid)
    if success:
        print("✓ Validasyon başarılı!")
    else:
        print("✗ Validasyon başarısız!")
        print("Hatalar:")
        for error in errors:
            print(f"  - {error}")

    # Test case 3: Eksik alan
    print("\n\nTest 3: Eksik Alan")
    print("-" * 50)
    test_data_missing = {
        "name": "Ayşe Kaya",
        "age": "30",
        "email": "ayse@example.com"
        # balance ve is_active eksik
    }

    success, cleaned, errors = validator.validate(test_data_missing)
    if success:
        print("✓ Validasyon başarılı!")
    else:
        print("✗ Validasyon başarısız!")
        print("Hatalar:")
        for error in errors:
            print(f"  - {error}")


test_form_validator()


# =============================================================================
# SORU 14: [Challenge] Memory-Efficient Değişken Yönetimi
# =============================================================================
# Python'da değişkenlerin bellekte nasıl saklandığını gösterin:
# 1. id() fonksiyonunu kullanarak iki değişkenin aynı objeyi gösterip göstermediğini kontrol edin
# 2. Small integer caching (-5 to 256) davranışını gösterin
# 3. String interning davranışını gösterin
# 4. is ve == operatörlerinin farkını gösterin

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- id() fonksiyonu objenin bellekteki adresini döndürür
- Python küçük integer'ları (-5 to 256) cache'ler (performans için)
- String interning: Bazı string'ler otomatik olarak interned edilir
- is operatörü: Aynı obje mi? (identity check)
- == operatörü: Değerler eşit mi? (equality check)
"""

import sys

print("\n--- Memory ve Object Identity ---\n")

# 1. Integer caching
print("1. Integer Caching (-5 to 256)")
print("-" * 50)

a = 256
b = 256
print(f"a = 256, b = 256")
print(f"a is b: {a is b}")  # True (cached)
print(f"id(a): {id(a)}, id(b): {id(b)}")

x = 257
y = 257
print(f"\nx = 257, y = 257")
print(f"x is y: {x is y}")  # False (not cached)
print(f"id(x): {id(x)}, id(y): {id(y)}")

# 2. String interning
print("\n\n2. String Interning")
print("-" * 50)

s1 = "python"
s2 = "python"
print(f"s1 = 'python', s2 = 'python'")
print(f"s1 is s2: {s1 is s2}")  # True (interned)
print(f"id(s1): {id(s1)}, id(s2): {id(s2)}")

# Boşluk içeren string'ler interned edilmeyebilir
s3 = "hello world"
s4 = "hello world"
print(f"\ns3 = 'hello world', s4 = 'hello world'")
print(f"s3 is s4: {s3 is s4}")  # Implementation dependent
print(f"id(s3): {id(s3)}, id(s4): {id(s4)}")

# 3. List (mutable) davranışı
print("\n\n3. Mutable Objects (List)")
print("-" * 50)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 = [1, 2, 3], list2 = [1, 2, 3]")
print(f"list1 == list2: {list1 == list2}")  # True (aynı değer)
print(f"list1 is list2: {list1 is list2}")  # False (farklı objeler)
print(f"id(list1): {id(list1)}, id(list2): {id(list2)}")

# Reference
list3 = list1
print(f"\nlist3 = list1")
print(f"list3 is list1: {list3 is list1}")  # True (aynı obje)
list3.append(4)
print(f"list3.append(4)")
print(f"list1: {list1}")  # [1, 2, 3, 4] - değişti!
print(f"list3: {list3}")  # [1, 2, 3, 4]

# 4. is vs ==
print("\n\n4. 'is' vs '==' Operatörleri")
print("-" * 50)

# None kontrolü (daima 'is' kullan)
value = None
print(f"value = None")
print(f"value is None: {value is None}")  # Doğru kullanım
print(f"value == None: {value == None}")  # Çalışır ama önerilmez

# Boolean kontrolü
flag = True
print(f"\nflag = True")
print(f"flag is True: {flag is True}")    # Doğru kullanım
print(f"flag == True: {flag == True}")    # Çalışır ama bazen karmaşık

# 5. sys.getsizeof() - Obje boyutu
print("\n\n5. Object Size")
print("-" * 50)

int_small = 1
int_big = 10**100
str_short = "hi"
str_long = "hello" * 1000
list_empty = []
list_full = list(range(1000))

print(f"int (1): {sys.getsizeof(int_small)} bytes")
print(f"int (10^100): {sys.getsizeof(int_big)} bytes")
print(f"str ('hi'): {sys.getsizeof(str_short)} bytes")
print(f"str ('hello'*1000): {sys.getsizeof(str_long)} bytes")
print(f"list (empty): {sys.getsizeof(list_empty)} bytes")
print(f"list (1000 items): {sys.getsizeof(list_full)} bytes")


# =============================================================================
# SORU 15: [Challenge] Dinamik Tip Sistemi Analizi
# =============================================================================
# Python'ın dinamik tip sistemini analiz eden bir araç yazın:
# - analyze_variable() fonksiyonu bir değişken alsın
# - Şu bilgileri raporlasın:
#   * Tip adı
#   * Bellekteki adresi (id)
#   * Boyutu (bytes)
#   * Mutable mi immutable mi?
#   * Hangi metodlara sahip? (önemli olanları listeleyin)
#   * Hashable mi?

# TODO: Kodunuzu buraya yazın



# ÇÖZÜM:
"""
Açıklama:
- type() ile tip bilgisi
- id() ile bellek adresi
- sys.getsizeof() ile boyut
- Mutable/immutable kontrolü için bilinen tipler
- dir() ile tüm attribute ve metodlar
- hash() ile hashable kontrolü
"""

import sys

def analyze_variable(var, var_name="variable"):
    """
    Bir değişkeni detaylı şekilde analiz eder.

    Args:
        var: Analiz edilecek değişken
        var_name (str): Değişken adı (görüntüleme için)
    """
    print(f"\n{'='*60}")
    print(f"VARIABLE ANALYSIS: {var_name}")
    print(f"{'='*60}")

    # 1. Değer ve Tip
    print(f"\nDeğer: {repr(var)}")
    var_type = type(var)
    print(f"Tip: {var_type.__name__} ({var_type})")

    # 2. Bellek Adresi
    print(f"ID (Memory Address): {id(var)}")
    print(f"ID (Hex): {hex(id(var))}")

    # 3. Boyut
    size = sys.getsizeof(var)
    print(f"Boyut: {size} bytes")

    # 4. Mutable/Immutable
    immutable_types = (int, float, str, tuple, frozenset, bytes, bool, type(None))
    is_immutable = isinstance(var, immutable_types)
    mutability = "Immutable" if is_immutable else "Mutable"
    print(f"Mutability: {mutability}")

    # 5. Hashable kontrolü
    try:
        hash_value = hash(var)
        print(f"Hashable: Yes (hash: {hash_value})")
    except TypeError:
        print(f"Hashable: No")

    # 6. Önemli metodlar
    print(f"\nÖnemli Metodlar/Attribute'lar:")

    # Public metodları filtrele (__ ile başlamayanlar)
    all_attrs = dir(var)
    public_methods = [attr for attr in all_attrs if not attr.startswith('_')]

    # Kategorize et
    special_methods = [attr for attr in all_attrs if attr.startswith('__') and attr.endswith('__')]

    if public_methods:
        print(f"  Public metodlar ({len(public_methods)}): {', '.join(public_methods[:10])}")
        if len(public_methods) > 10:
            print(f"    ... ve {len(public_methods) - 10} tane daha")

    # Bazı özel metodları göster
    important_special = ['__add__', '__len__', '__getitem__', '__setitem__', '__iter__', '__str__', '__repr__']
    present_special = [m for m in important_special if m in special_methods]
    if present_special:
        print(f"  Özel metodlar: {', '.join(present_special)}")

    # 7. Ekstra bilgiler (tipe göre)
    print(f"\nTipe Özgü Bilgiler:")

    if isinstance(var, (list, tuple, str, dict, set)):
        print(f"  Uzunluk: {len(var)}")

    if isinstance(var, (int, float)):
        print(f"  Sayısal değer: {var}")
        if isinstance(var, float):
            print(f"  Integer mi?: {var.is_integer()}")

    if isinstance(var, str):
        print(f"  Alphanumeric: {var.isalnum()}")
        print(f"  Digit: {var.isdigit()}")
        print(f"  Upper: {var.isupper()}")
        print(f"  Lower: {var.islower()}")

    if isinstance(var, bool):
        print(f"  Boolean değeri: {var}")
        print(f"  Integer karşılığı: {int(var)}")

    # 8. Tip hiyerarşisi
    print(f"\nTip Hiyerarşisi:")
    mro = var_type.__mro__ if hasattr(var_type, '__mro__') else [var_type]
    for i, base_type in enumerate(mro):
        indent = "  " * i
        print(f"{indent}↳ {base_type.__name__}")


# Test örnekleri
print("\n" + "="*60)
print("DİNAMİK TİP SİSTEMİ ANALİZİ")
print("="*60)

# Farklı tiplerden örnekler
analyze_variable(42, "integer")
analyze_variable(3.14, "float")
analyze_variable("Python", "string")
analyze_variable([1, 2, 3], "list")
analyze_variable((1, 2, 3), "tuple")
analyze_variable({"name": "Ali", "age": 25}, "dict")
analyze_variable({1, 2, 3}, "set")
analyze_variable(True, "boolean")
analyze_variable(None, "none")

# Bonus: Karşılaştırma
print("\n" + "="*60)
print("KARŞILAŞTIRMA: List vs Tuple")
print("="*60)

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(f"\nList boyutu: {sys.getsizeof(my_list)} bytes")
print(f"Tuple boyutu: {sys.getsizeof(my_tuple)} bytes")
print(f"Fark: {sys.getsizeof(my_list) - sys.getsizeof(my_tuple)} bytes")
print("\nSonuç: Tuple daha hafiftir (immutable olduğu için daha az overhead)")


# =============================================================================
# ALIŞTIRMALARIN SONU
# =============================================================================

print("\n" + "="*60)
print("TEBRİKLER! TÜM ALIŞTIRMALARI TAMAMLADINIZ!")
print("="*60)
print("\nBu bölümde şunları öğrendiniz:")
print("✓ Değişken tanımlama ve isimlendirme kuralları")
print("✓ Temel veri tipleri (int, float, str, bool)")
print("✓ Tip dönüşümleri ve validasyon")
print("✓ Type checking yöntemleri")
print("✓ Python'ın dinamik typing özelliği")
print("✓ Memory yönetimi ve object identity")
print("✓ Float hassasiyeti ve Decimal kullanımı")
print("\nSıradaki konu: 02-Operators")
print("="*60)
