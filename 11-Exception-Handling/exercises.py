"""
EXCEPTION HANDLING EXERCISES
Her alıştırma sorusu, TODO bölümü ve detaylı çözümden oluşmaktadır.
Zorluk seviyesi: Kolay -> Orta -> Zor
"""

# =====================================================
# EXERCISE 1: Güvenli Sayı Dönüşümü (KOLAY)
# =====================================================
"""
Soru:
Kullanıcıdan alınan string değeri integer'a dönüştüren ve hata durumunda
uygun mesaj veren bir fonksiyon yazın.

İpuçları:
- int() fonksiyonu ValueError fırlatabilir
- Kullanıcıya açıklayıcı mesaj verin
- None veya varsayılan değer dönebilirsiniz

TODO: Aşağıdaki fonksiyonu tamamlayın
"""

def safe_int_conversion(value, default=0):
    """
    String değeri integer'a dönüştürür

    Args:
        value: Dönüştürülecek değer
        default: Hata durumunda dönülecek değer

    Returns:
        Integer değer veya default değer
    """
    # TODO: Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def safe_int_conversion_solution(value, default=0):
    """
    String değeri integer'a güvenli şekilde dönüştürür
    """
    try:
        # String'i integer'a dönüştürmeyi dene
        result = int(value)
        return result
    except ValueError:
        # Dönüşüm başarısız olursa bilgi ver ve default döndür
        print(f"Uyarı: '{value}' sayıya dönüştürülemedi. Varsayılan değer kullanılıyor: {default}")
        return default
    except TypeError:
        # Yanlış tip gönderilmişse
        print(f"Uyarı: Geçersiz tip. Varsayılan değer kullanılıyor: {default}")
        return default


# Test
print("=== Exercise 1 Test ===")
print(safe_int_conversion_solution("123"))      # 123
print(safe_int_conversion_solution("abc"))      # 0 (default)
print(safe_int_conversion_solution("45.7"))     # 0 (default)
print(safe_int_conversion_solution(None, -1))   # -1
print()


# =====================================================
# EXERCISE 2: Güvenli Liste Erişimi (KOLAY)
# =====================================================
"""
Soru:
Verilen listeye güvenli şekilde erişen bir fonksiyon yazın.
Geçersiz indeks durumunda None döndürün.

İpuçları:
- IndexError'u yakalayın
- Negatif indeksler geçerlidir
- Liste boşsa da IndexError oluşabilir

TODO: Aşağıdaki fonksiyonu tamamlayın
"""

def safe_list_access(lst, index):
    """
    Listeye güvenli şekilde erişir

    Args:
        lst: Liste
        index: Erişilecek indeks

    Returns:
        Element veya None
    """
    # TODO: Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def safe_list_access_solution(lst, index):
    """
    Listeye güvenli şekilde erişir ve hataları yönetir
    """
    try:
        # Listeye erişmeyi dene
        return lst[index]
    except IndexError:
        # İndeks geçersizse None döndür
        print(f"Uyarı: İndeks {index} geçersiz. Liste uzunluğu: {len(lst)}")
        return None
    except TypeError:
        # lst liste değilse
        print("Hata: İlk parametre bir liste olmalı")
        return None


# Test
print("=== Exercise 2 Test ===")
my_list = [10, 20, 30, 40, 50]
print(safe_list_access_solution(my_list, 2))     # 30
print(safe_list_access_solution(my_list, -1))    # 50
print(safe_list_access_solution(my_list, 10))    # None
print(safe_list_access_solution(my_list, 100))   # None
print()


# =====================================================
# EXERCISE 3: Güvenli Bölme İşlemi (KOLAY)
# =====================================================
"""
Soru:
İki sayıyı bölen ve olası hataları yöneten bir fonksiyon yazın.
- ZeroDivisionError
- TypeError
- ValueError

İpuçları:
- Sıfıra bölme kontrolü yapın
- Tip kontrolü yapın
- Hata durumunda bilgilendirici mesaj verin

TODO: Aşağıdaki fonksiyonu tamamlayın
"""

def safe_divide(a, b):
    """
    İki sayıyı güvenli şekilde böler

    Args:
        a: Bölünen
        b: Bölen

    Returns:
        Bölme sonucu veya None
    """
    # TODO: Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def safe_divide_solution(a, b):
    """
    İki sayıyı güvenli şekilde böler ve tüm olası hataları yönetir
    """
    try:
        # Bölme işlemini gerçekleştir
        result = a / b
        return result
    except ZeroDivisionError:
        # Sıfıra bölme hatası
        print("Hata: Sıfıra bölme yapılamaz!")
        return None
    except TypeError:
        # Yanlış tip (string vb.)
        print(f"Hata: Geçersiz tipler. a: {type(a).__name__}, b: {type(b).__name__}")
        return None
    except Exception as e:
        # Beklenmeyen hatalar
        print(f"Beklenmeyen hata: {type(e).__name__} - {e}")
        return None


# Test
print("=== Exercise 3 Test ===")
print(safe_divide_solution(10, 2))      # 5.0
print(safe_divide_solution(10, 0))      # None (ZeroDivisionError)
print(safe_divide_solution("10", 2))    # None (TypeError)
print(safe_divide_solution(10, "2"))    # None (TypeError)
print()


# =====================================================
# EXERCISE 4: Dictionary Güvenli Erişim (ORTA)
# =====================================================
"""
Soru:
Nested dictionary'lere güvenli şekilde erişen bir fonksiyon yazın.
Fonksiyon bir key path'i (liste halinde) almalı ve değeri döndürmeli.

Örnek: get_nested_value({"a": {"b": {"c": 10}}}, ["a", "b", "c"]) -> 10

İpuçları:
- KeyError'u yakalayın
- TypeError'u yakalayın (dict değilse)
- Her seviyeyi kontrol edin

TODO: Aşağıdaki fonksiyonu tamamlayın
"""

def get_nested_value(data, key_path, default=None):
    """
    Nested dictionary'den güvenli şekilde değer alır

    Args:
        data: Dictionary
        key_path: Key'lerin listesi (örn: ["user", "address", "city"])
        default: Bulunamazsa dönülecek değer

    Returns:
        Bulunan değer veya default
    """
    # TODO: Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def get_nested_value_solution(data, key_path, default=None):
    """
    Nested dictionary'den güvenli şekilde değer alır
    Her seviyede KeyError ve TypeError kontrolü yapar
    """
    try:
        # Başlangıç değeri
        current = data

        # Her key için iterasyon
        for key in key_path:
            current = current[key]

        return current

    except KeyError as e:
        # Key bulunamadı
        print(f"Uyarı: Key bulunamadı: {e}")
        return default
    except TypeError:
        # Bir seviyede dict yerine başka tip var
        print("Uyarı: Dictionary yapısında hata var")
        return default
    except Exception as e:
        # Beklenmeyen hatalar
        print(f"Beklenmeyen hata: {e}")
        return default


# Test
print("=== Exercise 4 Test ===")
test_data = {
    "user": {
        "name": "Ahmet",
        "address": {
            "city": "İstanbul",
            "zip": "34000"
        },
        "age": 25
    }
}

print(get_nested_value_solution(test_data, ["user", "name"]))                    # Ahmet
print(get_nested_value_solution(test_data, ["user", "address", "city"]))        # İstanbul
print(get_nested_value_solution(test_data, ["user", "phone"], "N/A"))           # N/A
print(get_nested_value_solution(test_data, ["user", "age", "invalid"], "N/A"))  # N/A
print()


# =====================================================
# EXERCISE 5: Dosya İşlemleri (ORTA)
# =====================================================
"""
Soru:
Bir dosyayı okuyup içeriğini döndüren, tüm olası hataları yöneten
ve finally ile dosyayı kapatan bir fonksiyon yazın.

İpuçları:
- FileNotFoundError
- PermissionError
- UnicodeDecodeError
- Finally bloğu ile dosyayı kapatın

TODO: Aşağıdaki fonksiyonu tamamlayın
"""

def read_file_safe(filename, encoding='utf-8'):
    """
    Dosyayı güvenli şekilde okur

    Args:
        filename: Dosya adı
        encoding: Encoding (varsayılan: utf-8)

    Returns:
        Dosya içeriği veya None
    """
    # TODO: Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def read_file_safe_solution(filename, encoding='utf-8'):
    """
    Dosyayı güvenli şekilde okur ve tüm hataları yönetir
    Finally bloğu ile dosyanın kapatılmasını garanti eder
    """
    file_handle = None
    try:
        # Dosyayı aç
        file_handle = open(filename, 'r', encoding=encoding)

        # İçeriği oku
        content = file_handle.read()

        print(f"Dosya başarıyla okundu: {filename}")
        return content

    except FileNotFoundError:
        print(f"Hata: Dosya bulunamadı: {filename}")
        return None
    except PermissionError:
        print(f"Hata: Dosyaya erişim izni yok: {filename}")
        return None
    except UnicodeDecodeError as e:
        print(f"Hata: Encoding hatası: {e}")
        return None
    except Exception as e:
        print(f"Beklenmeyen hata: {type(e).__name__} - {e}")
        return None
    finally:
        # Dosya açıksa kapat
        if file_handle:
            file_handle.close()
            print(f"Dosya kapatıldı: {filename}")


# Test
print("=== Exercise 5 Test ===")
# Var olmayan dosya
read_file_safe_solution("nonexistent.txt")
print()


# =====================================================
# EXERCISE 6: Yaş Doğrulama ve Custom Exception (ORTA)
# =====================================================
"""
Soru:
Yaş doğrulama için özel exception sınıfları oluşturun ve kullanın:
- NegativeAgeError: Negatif yaş için
- InvalidAgeError: 0-150 dışı yaşlar için
- AgeTypeError: Yanlış tip için

İpuçları:
- Exception sınıfından türetin
- Her exception'da bilgilendirici mesaj olsun
- Yaş doğrulama fonksiyonu uygun exception'ı fırlatsın

TODO: Aşağıdaki sınıfları ve fonksiyonu tamamlayın
"""

# TODO: Custom exception sınıflarını oluşturun
class NegativeAgeError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class AgeTypeError(Exception):
    pass


def validate_age(age):
    """
    Yaşı doğrular ve geçersizse exception fırlatır

    Args:
        age: Doğrulanacak yaş

    Returns:
        True (geçerliyse)

    Raises:
        AgeTypeError: Tip yanlışsa
        NegativeAgeError: Negatif yaş
        InvalidAgeError: Geçersiz yaş aralığı
    """
    # TODO: Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
class NegativeAgeError_Solution(Exception):
    """Negatif yaş hatası"""
    def __init__(self, age):
        self.age = age
        super().__init__(f"Yaş negatif olamaz: {age}")


class InvalidAgeError_Solution(Exception):
    """Geçersiz yaş aralığı hatası"""
    def __init__(self, age):
        self.age = age
        super().__init__(f"Geçersiz yaş: {age}. Yaş 0-150 arasında olmalıdır.")


class AgeTypeError_Solution(Exception):
    """Yaş tipi hatası"""
    def __init__(self, value):
        self.value = value
        self.type_name = type(value).__name__
        super().__init__(f"Yaş bir sayı olmalıdır. Alınan tip: {self.type_name}")


def validate_age_solution(age):
    """
    Yaşı doğrular ve uygun exception'ı fırlatır
    """
    # Tip kontrolü
    if not isinstance(age, (int, float)):
        raise AgeTypeError_Solution(age)

    # Negatif kontrol
    if age < 0:
        raise NegativeAgeError_Solution(age)

    # Aralık kontrolü
    if age > 150:
        raise InvalidAgeError_Solution(age)

    return True


# Test
print("=== Exercise 6 Test ===")
test_ages = [25, -5, 200, "abc", 30.5, 0, 150]

for test_age in test_ages:
    try:
        validate_age_solution(test_age)
        print(f"✓ Geçerli yaş: {test_age}")
    except NegativeAgeError_Solution as e:
        print(f"✗ {e}")
    except InvalidAgeError_Solution as e:
        print(f"✗ {e}")
    except AgeTypeError_Solution as e:
        print(f"✗ {e}")

print()


# =====================================================
# EXERCISE 7: Retry Mekanizması (ORTA-ZOR)
# =====================================================
"""
Soru:
Başarısız olan bir işlemi belirli sayıda tekrar deneyen bir decorator yazın.
Her denemede exception loglanmalı ve belirli bir bekleme süresi olmalı.

İpuçları:
- Decorator kullanın
- time.sleep() ile bekleme ekleyin
- Deneme sayısını parametreleştirin
- Son denemede de başarısız olursa exception'ı fırlat

TODO: Aşağıdaki decorator'ı tamamlayın
"""

import time

def retry(max_attempts=3, delay=1):
    """
    Başarısız işlemleri tekrar deneyen decorator

    Args:
        max_attempts: Maksimum deneme sayısı
        delay: Denemeler arası bekleme süresi (saniye)
    """
    # TODO: Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def retry_solution(max_attempts=3, delay=1):
    """
    Başarısız işlemleri belirli sayıda tekrar deneyen decorator
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Deneme {attempt}/{max_attempts}...")
                    result = func(*args, **kwargs)
                    print(f"✓ İşlem başarılı!")
                    return result

                except Exception as e:
                    last_exception = e
                    print(f"✗ Hata: {type(e).__name__} - {e}")

                    if attempt < max_attempts:
                        print(f"  {delay} saniye bekleniyor...")
                        time.sleep(delay)
                    else:
                        print(f"  Tüm denemeler başarısız!")

            # Tüm denemeler başarısız, son exception'ı fırlat
            raise last_exception

        return wrapper
    return decorator


# Test fonksiyonu
class UnstableService:
    """Bazen başarılı, bazen başarısız olan bir servis simülasyonu"""
    def __init__(self, success_after=3):
        self.attempt_count = 0
        self.success_after = success_after

    @retry_solution(max_attempts=5, delay=0.5)
    def unreliable_operation(self):
        """Belirli sayıda denemeden sonra başarılı olan işlem"""
        self.attempt_count += 1

        if self.attempt_count < self.success_after:
            raise ConnectionError(f"Bağlantı hatası (deneme: {self.attempt_count})")

        return "İşlem başarılı!"


# Test
print("=== Exercise 7 Test ===")
service = UnstableService(success_after=3)
try:
    result = service.unreliable_operation()
    print(f"Sonuç: {result}")
except Exception as e:
    print(f"Nihai hata: {e}")

print()


# =====================================================
# EXERCISE 8: Context Manager ile Resource Yönetimi (ZOR)
# =====================================================
"""
Soru:
Bir veritabanı bağlantısını simüle eden ve exception durumunda
otomatik rollback yapan bir context manager yazın.

İpuçları:
- __enter__ ve __exit__ metodlarını implement edin
- __exit__ metodunda exception bilgisine erişin
- Exception varsa rollback, yoksa commit yapın

TODO: Aşağıdaki sınıfı tamamlayın
"""

class DatabaseTransaction:
    """Veritabanı transaction context manager"""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
        self.transaction_started = False

    def __enter__(self):
        # TODO: Kodunuzu buraya yazın
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Kodunuzu buraya yazın
        pass


# ÇÖZÜM:
class DatabaseTransaction_Solution:
    """
    Veritabanı transaction'larını yöneten context manager
    Exception durumunda otomatik rollback yapar
    """

    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
        self.transaction_started = False
        self.operations = []

    def __enter__(self):
        """Context'e girildiğinde çalışır"""
        print(f"[DB] {self.db_name} veritabanına bağlanılıyor...")
        self.connected = True

        print(f"[DB] Transaction başlatılıyor...")
        self.transaction_started = True

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context'ten çıkılırken çalışır"""
        try:
            if exc_type is not None:
                # Exception oluştuysa rollback yap
                print(f"\n[DB] Hata oluştu: {exc_type.__name__}")
                print(f"[DB] Rollback yapılıyor...")
                self.operations.clear()
                print(f"[DB] Rollback tamamlandı")
            else:
                # Exception yoksa commit yap
                print(f"\n[DB] Commit yapılıyor...")
                print(f"[DB] {len(self.operations)} işlem kaydedildi")
                print(f"[DB] Commit tamamlandı")

        finally:
            # Her durumda bağlantıyı kapat
            if self.connected:
                print(f"[DB] Bağlantı kapatılıyor...")
                self.connected = False

        # False döndürürsek exception propagate olur
        # True döndürürsek exception suppress edilir
        return False  # Exception'ı propagate et

    def execute(self, query):
        """Sorgu çalıştırma simülasyonu"""
        if not self.transaction_started:
            raise RuntimeError("Transaction başlatılmamış!")

        print(f"[DB] Sorgu çalıştırılıyor: {query}")
        self.operations.append(query)

        # Tehlikeli sorguları simüle et
        if "DELETE FROM users" in query:
            raise ValueError("Tehlikeli sorgu engellendi!")

        return f"Sonuç: {len(self.operations)} satır etkilendi"


# Test
print("=== Exercise 8 Test ===")

# Başarılı transaction
print("--- Başarılı Transaction ---")
try:
    with DatabaseTransaction_Solution("MyDatabase") as db:
        db.execute("INSERT INTO users VALUES (1, 'Ahmet')")
        db.execute("INSERT INTO users VALUES (2, 'Mehmet')")
        db.execute("UPDATE users SET active = true")
except Exception as e:
    print(f"Hata yakalandı: {e}")

print("\n--- Başarısız Transaction ---")
# Başarısız transaction (rollback)
try:
    with DatabaseTransaction_Solution("MyDatabase") as db:
        db.execute("INSERT INTO users VALUES (3, 'Ayşe')")
        db.execute("DELETE FROM users")  # Bu hata verecek
        db.execute("INSERT INTO users VALUES (4, 'Fatma')")
except Exception as e:
    print(f"Hata yakalandı: {e}")

print()


# =====================================================
# EXERCISE 9: Exception Chaining ve Logging (ZOR)
# =====================================================
"""
Soru:
Katmanlı bir uygulama simüle edin (Data -> Business -> API katmanları).
Her katmanda uygun exception'ı fırlatın ve exception chaining kullanın.
Ayrıca detaylı logging yapın.

İpuçları:
- Her katman için özel exception sınıfları oluşturun
- "raise ... from ..." kullanarak exception chain'i koruyun
- __cause__ ile orijinal hataya erişin

TODO: Aşağıdaki katmanlı sistemi oluşturun
"""

# TODO: Exception sınıflarını ve katmanları oluşturun


# ÇÖZÜM:
class DataLayerError(Exception):
    """Data katmanı hataları"""
    pass


class BusinessLayerError(Exception):
    """Business katmanı hataları"""
    pass


class APILayerError(Exception):
    """API katmanı hataları"""
    pass


class DataLayer:
    """Veri erişim katmanı"""

    @staticmethod
    def get_user_from_db(user_id):
        """Veritabanından kullanıcı getir (simülasyon)"""
        try:
            # Veritabanı hatası simülasyonu
            if user_id < 0:
                raise ValueError(f"Geçersiz user_id: {user_id}")

            if user_id > 1000:
                raise ConnectionError("Veritabanı bağlantısı koptu")

            # Kullanıcı bulunamadı
            if user_id == 999:
                raise KeyError(f"User ID {user_id} bulunamadı")

            # Başarılı
            return {"id": user_id, "name": f"User_{user_id}", "email": f"user{user_id}@example.com"}

        except (ValueError, ConnectionError, KeyError) as e:
            # Alt seviye hatayı DataLayerError'a çevir
            raise DataLayerError(
                f"Veri erişim hatası: User ID {user_id}"
            ) from e


class BusinessLayer:
    """İş mantığı katmanı"""

    @staticmethod
    def get_user_profile(user_id):
        """Kullanıcı profilini getir"""
        try:
            # Data katmanından veri al
            user_data = DataLayer.get_user_from_db(user_id)

            # İş mantığı uygulaması
            if not user_data.get("email"):
                raise ValueError("Kullanıcının email'i yok")

            profile = {
                "user_id": user_data["id"],
                "display_name": user_data["name"].upper(),
                "contact": user_data["email"]
            }

            return profile

        except DataLayerError as e:
            # Data katmanı hatasını business hatasına çevir
            raise BusinessLayerError(
                f"İş mantığı hatası: Profil oluşturulamadı"
            ) from e


class APILayer:
    """API katmanı"""

    @staticmethod
    def get_user_endpoint(user_id):
        """API endpoint: Kullanıcı getir"""
        try:
            # Business katmanından veri al
            profile = BusinessLayer.get_user_profile(user_id)

            return {
                "status": "success",
                "data": profile
            }

        except BusinessLayerError as e:
            # Business katmanı hatasını API hatasına çevir
            raise APILayerError(
                f"API Hatası: İstek işlenemedi"
            ) from e


def detailed_error_logger(user_id):
    """Detaylı hata loglama"""
    try:
        response = APILayer.get_user_endpoint(user_id)
        print(f"✓ Başarılı: {response}")
        return response

    except APILayerError as e:
        print(f"\n{'='*60}")
        print(f"HATA DETAYLARI - User ID: {user_id}")
        print(f"{'='*60}")

        # Exception chain'i takip et
        current_error = e
        level = 1

        while current_error:
            print(f"\nSeviye {level}: {type(current_error).__name__}")
            print(f"  Mesaj: {current_error}")

            # Bir sonraki seviye
            if hasattr(current_error, '__cause__'):
                current_error = current_error.__cause__
                level += 1
            else:
                break

        print(f"\n{'='*60}")
        return None


# Test
print("=== Exercise 9 Test ===")

print("--- Test 1: Başarılı ---")
detailed_error_logger(42)

print("\n--- Test 2: Geçersiz ID ---")
detailed_error_logger(-5)

print("\n--- Test 3: Kullanıcı Bulunamadı ---")
detailed_error_logger(999)

print("\n--- Test 4: Bağlantı Hatası ---")
detailed_error_logger(1001)

print()


# =====================================================
# EXERCISE 10: Input Validation Framework (ZOR)
# =====================================================
"""
Soru:
Kullanıcı input'larını doğrulayan kapsamlı bir framework oluşturun:
- Farklı validation türleri (type, range, format, custom)
- Her validation için özel exception
- Birden fazla hata durumunda tüm hataları toplama
- Detaylı hata raporlama

TODO: Validation framework'ünü oluşturun
"""

# TODO: Kodunuzu buraya yazın


# ÇÖZÜM:
class ValidationError(Exception):
    """Base validation exception"""
    pass


class TypeValidationError(ValidationError):
    """Tip doğrulama hatası"""
    pass


class RangeValidationError(ValidationError):
    """Aralık doğrulama hatası"""
    pass


class FormatValidationError(ValidationError):
    """Format doğrulama hatası"""
    pass


class RequiredFieldError(ValidationError):
    """Zorunlu alan hatası"""
    pass


class ValidationResult:
    """Validation sonucu"""

    def __init__(self):
        self.is_valid = True
        self.errors = []

    def add_error(self, field, error):
        """Hata ekle"""
        self.is_valid = False
        self.errors.append({"field": field, "error": str(error)})

    def __str__(self):
        if self.is_valid:
            return "✓ Tüm validasyonlar başarılı"

        error_msg = "✗ Validation hataları:\n"
        for err in self.errors:
            error_msg += f"  - {err['field']}: {err['error']}\n"
        return error_msg


class Validator:
    """Input validation framework"""

    @staticmethod
    def validate_required(value, field_name):
        """Zorunlu alan kontrolü"""
        if value is None or value == "":
            raise RequiredFieldError(f"{field_name} zorunludur")

    @staticmethod
    def validate_type(value, expected_type, field_name):
        """Tip kontrolü"""
        if not isinstance(value, expected_type):
            raise TypeValidationError(
                f"{field_name} {expected_type.__name__} tipinde olmalıdır. "
                f"Alınan tip: {type(value).__name__}"
            )

    @staticmethod
    def validate_range(value, min_val, max_val, field_name):
        """Aralık kontrolü"""
        if not (min_val <= value <= max_val):
            raise RangeValidationError(
                f"{field_name} {min_val} ile {max_val} arasında olmalıdır. "
                f"Alınan değer: {value}"
            )

    @staticmethod
    def validate_email(email, field_name):
        """Email format kontrolü"""
        if "@" not in email or "." not in email.split("@")[-1]:
            raise FormatValidationError(
                f"{field_name} geçerli bir email formatında değil: {email}"
            )

    @staticmethod
    def validate_length(value, min_len, max_len, field_name):
        """Uzunluk kontrolü"""
        length = len(value)
        if not (min_len <= length <= max_len):
            raise RangeValidationError(
                f"{field_name} uzunluğu {min_len}-{max_len} arasında olmalıdır. "
                f"Alınan uzunluk: {length}"
            )


class UserRegistrationForm:
    """Kullanıcı kayıt formu validation örneği"""

    def __init__(self, data):
        self.data = data
        self.result = ValidationResult()

    def validate(self):
        """Tüm alanları doğrula"""
        # Username validation
        self._validate_field(
            "username",
            [
                lambda: Validator.validate_required(self.data.get("username"), "Kullanıcı Adı"),
                lambda: Validator.validate_type(self.data.get("username"), str, "Kullanıcı Adı"),
                lambda: Validator.validate_length(self.data.get("username"), 3, 20, "Kullanıcı Adı"),
            ]
        )

        # Email validation
        self._validate_field(
            "email",
            [
                lambda: Validator.validate_required(self.data.get("email"), "Email"),
                lambda: Validator.validate_type(self.data.get("email"), str, "Email"),
                lambda: Validator.validate_email(self.data.get("email"), "Email"),
            ]
        )

        # Age validation
        self._validate_field(
            "age",
            [
                lambda: Validator.validate_required(self.data.get("age"), "Yaş"),
                lambda: Validator.validate_type(self.data.get("age"), int, "Yaş"),
                lambda: Validator.validate_range(self.data.get("age"), 18, 100, "Yaş"),
            ]
        )

        # Password validation
        self._validate_field(
            "password",
            [
                lambda: Validator.validate_required(self.data.get("password"), "Şifre"),
                lambda: Validator.validate_type(self.data.get("password"), str, "Şifre"),
                lambda: Validator.validate_length(self.data.get("password"), 8, 50, "Şifre"),
            ]
        )

        return self.result

    def _validate_field(self, field_name, validators):
        """Tek alan için tüm validasyonları çalıştır"""
        for validator_func in validators:
            try:
                validator_func()
            except ValidationError as e:
                self.result.add_error(field_name, e)
                break  # İlk hatada dur


# Test
print("=== Exercise 10 Test ===")

# Test 1: Geçerli data
print("--- Test 1: Geçerli Kayıt ---")
valid_data = {
    "username": "ahmet_yilmaz",
    "email": "ahmet@example.com",
    "age": 25,
    "password": "securepassword123"
}
form1 = UserRegistrationForm(valid_data)
result1 = form1.validate()
print(result1)

# Test 2: Çoklu hata
print("--- Test 2: Çoklu Hatalar ---")
invalid_data = {
    "username": "ab",  # Çok kısa
    "email": "invalid-email",  # Geçersiz format
    "age": 15,  # Yaş küçük
    "password": "123"  # Çok kısa
}
form2 = UserRegistrationForm(invalid_data)
result2 = form2.validate()
print(result2)

# Test 3: Eksik alanlar
print("--- Test 3: Eksik Alanlar ---")
incomplete_data = {
    "username": "ahmet",
    # email yok
    "age": 25,
    # password yok
}
form3 = UserRegistrationForm(incomplete_data)
result3 = form3.validate()
print(result3)

# Test 4: Tip hataları
print("--- Test 4: Tip Hataları ---")
wrong_types = {
    "username": 12345,  # String olmalı
    "email": "valid@email.com",
    "age": "25",  # Integer olmalı
    "password": ["password"]  # String olmalı
}
form4 = UserRegistrationForm(wrong_types)
result4 = form4.validate()
print(result4)

print()


# =====================================================
# EXERCISE 11: Async Exception Handling Simulation (İLERİ SEVİYE)
# =====================================================
"""
Soru:
Asenkron işlemleri simüle eden ve exception'ları yöneten bir sistem yazın.
Birden fazla işlem paralel çalışacak ve hatalar toplanacak.

İpuçları:
- Multiple operation'ları simüle edin
- Her operation başarılı/başarısız olabilir
- Tüm sonuçları ve hataları toplayın
- Partial success durumunu yönetin

TODO: Async simulation sistemini oluşturun
"""

import random


# ÇÖZÜM:
class OperationResult:
    """İşlem sonucu"""

    def __init__(self, operation_id, success, result=None, error=None):
        self.operation_id = operation_id
        self.success = success
        self.result = result
        self.error = error

    def __str__(self):
        if self.success:
            return f"Op-{self.operation_id}: ✓ Başarılı - {self.result}"
        return f"Op-{self.operation_id}: ✗ Hata - {self.error}"


class AsyncOperationSimulator:
    """Asenkron işlem simülatörü"""

    def __init__(self, name, success_rate=0.7):
        self.name = name
        self.success_rate = success_rate

    def execute(self, operation_id):
        """Tek işlem çalıştır"""
        try:
            # Rastgele başarı/başarısızlık
            if random.random() > self.success_rate:
                # Farklı hata türleri simüle et
                error_types = [
                    ConnectionError("Bağlantı zaman aşımı"),
                    ValueError("Geçersiz veri formatı"),
                    RuntimeError("Servis geçici olarak kullanılamıyor"),
                ]
                raise random.choice(error_types)

            # Başarılı sonuç
            result = f"{self.name} işlemi tamamlandı"
            return OperationResult(operation_id, True, result=result)

        except Exception as e:
            return OperationResult(
                operation_id,
                False,
                error=f"{type(e).__name__}: {e}"
            )


class BatchOperationManager:
    """Toplu işlem yöneticisi"""

    def __init__(self, fail_fast=False):
        self.fail_fast = fail_fast
        self.results = []

    def execute_batch(self, operations, operation_count):
        """Birden fazla işlemi çalıştır"""
        print(f"Toplam {operation_count} işlem başlatılıyor...")
        print(f"Mod: {'Fail-Fast' if self.fail_fast else 'Collect-All-Results'}\n")

        for i in range(operation_count):
            operation = random.choice(operations)
            print(f"İşlem {i+1} çalıştırılıyor ({operation.name})...")

            result = operation.execute(i+1)
            self.results.append(result)

            print(f"  {result}")

            # Fail-fast modda ilk hatada dur
            if self.fail_fast and not result.success:
                print(f"\n⚠ Fail-fast modu: İşlem {i+1} başarısız, durduruluyor!")
                raise RuntimeError(f"Batch işlem başarısız: {result.error}")

        return self.get_summary()

    def get_summary(self):
        """Özet bilgi"""
        total = len(self.results)
        successful = sum(1 for r in self.results if r.success)
        failed = total - successful

        summary = {
            "total": total,
            "successful": successful,
            "failed": failed,
            "success_rate": f"{(successful/total*100):.1f}%" if total > 0 else "0%",
            "results": self.results
        }

        return summary


# Test
print("=== Exercise 11 Test ===")

# İşlem tipleri oluştur
operations = [
    AsyncOperationSimulator("Veritabanı", success_rate=0.8),
    AsyncOperationSimulator("API Çağrısı", success_rate=0.6),
    AsyncOperationSimulator("Dosya İşleme", success_rate=0.9),
]

# Test 1: Collect-all-results modu
print("--- Test 1: Tüm Sonuçları Topla ---")
manager1 = BatchOperationManager(fail_fast=False)
try:
    summary1 = manager1.execute_batch(operations, operation_count=10)
    print(f"\n📊 ÖZET:")
    print(f"  Toplam: {summary1['total']}")
    print(f"  Başarılı: {summary1['successful']}")
    print(f"  Başarısız: {summary1['failed']}")
    print(f"  Başarı Oranı: {summary1['success_rate']}")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("\n" + "="*60 + "\n")

# Test 2: Fail-fast modu
print("--- Test 2: Fail-Fast Modu ---")
manager2 = BatchOperationManager(fail_fast=True)
try:
    summary2 = manager2.execute_batch(operations, operation_count=10)
    print(f"\n📊 ÖZET:")
    print(f"  Tüm işlemler başarılı!")
    print(f"  Toplam: {summary2['total']}")
except RuntimeError as e:
    print(f"\n❌ Batch işlem başarısız!")
    summary2 = manager2.get_summary()
    print(f"📊 Kısmi Özet:")
    print(f"  Tamamlanan: {summary2['total']}")
    print(f"  Başarılı: {summary2['successful']}")
    print(f"  Başarısız: {summary2['failed']}")

print()


# =====================================================
# EXERCISE 12: Exception Hierarchy ve Polymorphism (İLERİ SEVİYE)
# =====================================================
"""
Soru:
Bir e-ticaret sistemi için kapsamlı exception hierarchy'si oluşturun:
- Ödeme hataları
- Stok hataları
- Kullanıcı hataları
Her exception türü için özel handling ve logging

TODO: E-ticaret exception hierarchy'sini oluşturun
"""

# ÇÖZÜM:
from datetime import datetime
from typing import Optional


# Base exception
class ECommerceException(Exception):
    """E-ticaret sistemi base exception"""

    def __init__(self, message, error_code=None, user_message=None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code or "E000"
        self.user_message = user_message or message
        self.timestamp = datetime.now()

    def log(self):
        """Exception'ı logla"""
        log_entry = f"""
[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}]
Exception: {type(self).__name__}
Code: {self.error_code}
Message: {self.message}
User Message: {self.user_message}
"""
        return log_entry


# Payment exceptions
class PaymentException(ECommerceException):
    """Ödeme hataları base class"""
    pass


class PaymentDeclinedException(PaymentException):
    """Ödeme reddedildi"""

    def __init__(self, card_last4, reason):
        super().__init__(
            message=f"Kart (*{card_last4}) ile ödeme reddedildi: {reason}",
            error_code="PAY001",
            user_message="Ödemeniz reddedildi. Lütfen başka bir kart deneyin."
        )
        self.card_last4 = card_last4
        self.reason = reason


class InsufficientFundsException(PaymentException):
    """Yetersiz bakiye"""

    def __init__(self, required, available):
        super().__init__(
            message=f"Yetersiz bakiye: Gerekli {required} TL, Mevcut {available} TL",
            error_code="PAY002",
            user_message="Kartınızda yetersiz bakiye bulunmaktadır."
        )
        self.required = required
        self.available = available


# Inventory exceptions
class InventoryException(ECommerceException):
    """Stok hataları base class"""
    pass


class OutOfStockException(InventoryException):
    """Stok tükendi"""

    def __init__(self, product_id, product_name):
        super().__init__(
            message=f"Ürün stokta yok: {product_name} (ID: {product_id})",
            error_code="INV001",
            user_message=f"Üzgünüz, '{product_name}' şu an stokta bulunmamaktadır."
        )
        self.product_id = product_id
        self.product_name = product_name


class InsufficientStockException(InventoryException):
    """Yetersiz stok"""

    def __init__(self, product_name, requested, available):
        super().__init__(
            message=f"Yetersiz stok: {product_name} - İstenen: {requested}, Mevcut: {available}",
            error_code="INV002",
            user_message=f"'{product_name}' için yalnızca {available} adet stok bulunmaktadır."
        )
        self.product_name = product_name
        self.requested = requested
        self.available = available


# User exceptions
class UserException(ECommerceException):
    """Kullanıcı hataları base class"""
    pass


class UserNotAuthenticatedException(UserException):
    """Kullanıcı giriş yapmamış"""

    def __init__(self):
        super().__init__(
            message="Kullanıcı kimlik doğrulaması yapılmamış",
            error_code="USR001",
            user_message="Bu işlem için giriş yapmanız gerekmektedir."
        )


class InvalidAddressException(UserException):
    """Geçersiz adres"""

    def __init__(self, reason):
        super().__init__(
            message=f"Geçersiz teslimat adresi: {reason}",
            error_code="USR002",
            user_message="Teslimat adresiniz geçersiz. Lütfen kontrol ediniz."
        )
        self.reason = reason


# Order management system
class Order:
    """Sipariş sınıfı"""

    def __init__(self, order_id, user_id, items):
        self.order_id = order_id
        self.user_id = user_id
        self.items = items  # [(product_id, product_name, quantity, price), ...]
        self.total = sum(item[2] * item[3] for item in items)
        self.status = "pending"


class OrderProcessor:
    """Sipariş işleyici"""

    def __init__(self):
        self.inventory = {
            "P001": {"name": "Laptop", "stock": 5, "price": 10000},
            "P002": {"name": "Mouse", "stock": 0, "price": 100},
            "P003": {"name": "Keyboard", "stock": 3, "price": 500},
        }
        self.user_balance = {"U001": 5000, "U002": 50000}

    def process_order(self, order, user_authenticated=True, address_valid=True):
        """Siparişi işle"""
        errors = []

        try:
            # 1. Kullanıcı doğrulama
            if not user_authenticated:
                raise UserNotAuthenticatedException()

            # 2. Adres kontrolü
            if not address_valid:
                raise InvalidAddressException("Eksik bilgiler")

            # 3. Stok kontrolü
            for product_id, product_name, quantity, price in order.items:
                if product_id not in self.inventory:
                    raise OutOfStockException(product_id, product_name)

                available = self.inventory[product_id]["stock"]
                if available == 0:
                    raise OutOfStockException(product_id, product_name)

                if available < quantity:
                    raise InsufficientStockException(product_name, quantity, available)

            # 4. Ödeme kontrolü
            user_balance = self.user_balance.get(order.user_id, 0)
            if user_balance < order.total:
                raise InsufficientFundsException(order.total, user_balance)

            # 5. İşlemi tamamla
            print(f"✓ Sipariş başarıyla işlendi: {order.order_id}")
            print(f"  Toplam: {order.total} TL")
            order.status = "completed"
            return True

        except ECommerceException as e:
            # E-ticaret exception'larını logla
            print(f"\n❌ Sipariş İşlenemedi: {order.order_id}")
            print(e.log())
            print(f"Kullanıcıya gösterilecek mesaj: {e.user_message}\n")
            order.status = "failed"
            return False


# Test
print("=== Exercise 12 Test ===")

processor = OrderProcessor()

# Test 1: Başarılı sipariş
print("--- Test 1: Başarılı Sipariş ---")
order1 = Order(
    "ORD001",
    "U002",
    [
        ("P001", "Laptop", 1, 10000),
        ("P003", "Keyboard", 2, 500),
    ]
)
processor.process_order(order1)

# Test 2: Kimlik doğrulama hatası
print("--- Test 2: Kimlik Doğrulama Hatası ---")
order2 = Order("ORD002", "U001", [("P001", "Laptop", 1, 10000)])
processor.process_order(order2, user_authenticated=False)

# Test 3: Stok tükendi
print("--- Test 3: Stok Tükendi ---")
order3 = Order("ORD003", "U002", [("P002", "Mouse", 1, 100)])
processor.process_order(order3)

# Test 4: Yetersiz stok
print("--- Test 4: Yetersiz Stok ---")
order4 = Order("ORD004", "U002", [("P003", "Keyboard", 5, 500)])
processor.process_order(order4)

# Test 5: Yetersiz bakiye
print("--- Test 5: Yetersiz Bakiye ---")
order5 = Order("ORD005", "U001", [("P001", "Laptop", 1, 10000)])
processor.process_order(order5)

# Test 6: Geçersiz adres
print("--- Test 6: Geçersiz Adres ---")
order6 = Order("ORD006", "U002", [("P003", "Keyboard", 1, 500)])
processor.process_order(order6, address_valid=False)

print("\n" + "="*60)
print("TÜM ALIŞTURMALAR TAMAMLANDI!")
print("="*60)
