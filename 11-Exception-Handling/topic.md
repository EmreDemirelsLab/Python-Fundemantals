# Exception Handling (İstisna Yönetimi)

## İçindekiler
1. [Exception Nedir?](#exception-nedir)
2. [Try/Except Yapısı](#tryexcept-yapısı)
3. [Birden Fazla Exception Yakalamak](#birden-fazla-exception-yakalamak)
4. [Else ve Finally Blokları](#else-ve-finally-blokları)
5. [Exception Bilgisine Erişmek](#exception-bilgisine-erişmek)
6. [Yaygın Exception Türleri](#yaygın-exception-türleri)
7. [Exception Fırlatmak (Raise)](#exception-fırlatmak)
8. [Özel Exception Sınıfları](#özel-exception-sınıfları)
9. [Exception Chaining](#exception-chaining)
10. [Best Practices](#best-practices)

---

## Exception Nedir?

**Exception (İstisna)**, programın çalışması sırasında oluşan ve normal akışı bozan hatalardır. Python'da exception'lar object'lerdir ve tüm exception'lar `BaseException` sınıfından türetilir.

Exception handling, programın beklenmedik durumlarla karşılaştığında çökmesini önler ve hataları kontrollü bir şekilde yönetmemizi sağlar.

### Örnek 1: Exception Olmadan

```python
# Exception handling olmadan - Program çökecek
def divide(a, b):
    return a / b

result = divide(10, 0)  # ZeroDivisionError: division by zero
print("Bu satır çalışmayacak")
```

**Açıklama:** Bu kod çalıştırıldığında `ZeroDivisionError` hatası oluşur ve program sonlanır. Sonraki satırlar çalışmaz.

---

## Try/Except Yapısı

`try/except` bloğu, hata oluşabilecek kodları güvenli bir şekilde çalıştırmamızı sağlar.

### Söz Dizimi

```python
try:
    # Hata oluşabilecek kod
    risky_code()
except ExceptionType:
    # Hata oluştuğunda çalışacak kod
    handle_error()
```

### Örnek 2: Temel Try/Except

```python
# Try/except ile güvenli bölme
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Hata: Sıfıra bölme yapılamaz!")
        return None

# Kullanım
print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Hata mesajı + None
print("Program devam ediyor")  # Bu satır çalışır
```

**Açıklama:** Exception yakalandığında program çökmez, `except` bloğu çalışır ve program normal akışına devam eder.

### Örnek 3: Genel Exception Yakalamak

```python
# Tüm exception'ları yakalamak (dikkatli kullanılmalı)
def risky_operation(data):
    try:
        # Farklı hatalar oluşabilir
        number = int(data)
        result = 100 / number
        items = [1, 2, 3]
        print(items[number])
        return result
    except Exception as e:
        print(f"Bir hata oluştu: {type(e).__name__}")
        print(f"Hata mesajı: {e}")
        return None

# Test
risky_operation("abc")    # ValueError: invalid literal
risky_operation("0")      # ZeroDivisionError
risky_operation("10")     # IndexError: list index out of range
```

**Açıklama:** `Exception` tüm exception türlerini yakalar. Ancak hangi hatanın oluştuğunu belirlemek için daha spesifik exception'lar kullanmak daha iyidir.

---

## Birden Fazla Exception Yakalamak

Farklı exception türlerini ayrı ayrı veya birlikte yakalayabiliriz.

### Örnek 4: Çoklu Exception Blokları

```python
# Her exception türü için ayrı işlem
def process_user_input(value, index):
    my_list = [10, 20, 30, 40, 50]

    try:
        number = int(value)
        result = my_list[index] / number
        return result
    except ValueError:
        print("Hata: Geçerli bir sayı giriniz!")
        return None
    except ZeroDivisionError:
        print("Hata: Sıfıra bölme yapılamaz!")
        return None
    except IndexError:
        print(f"Hata: İndeks 0-{len(my_list)-1} arasında olmalı!")
        return None
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")
        return None

# Test
print(process_user_input("5", 2))      # 6.0 (30/5)
print(process_user_input("abc", 2))    # ValueError
print(process_user_input("0", 2))      # ZeroDivisionError
print(process_user_input("5", 10))     # IndexError
```

### Örnek 5: Birden Fazla Exception'ı Birlikte Yakalamak

```python
# Aynı şekilde işlenecek exception'ları gruplamak
def calculate(operation, a, b):
    try:
        if operation == "divide":
            return a / b
        elif operation == "power":
            return a ** b
        elif operation == "list_access":
            items = [a, b]
            return items[a]
    except (ZeroDivisionError, ValueError, TypeError) as e:
        print(f"Matematik/Tip hatası: {type(e).__name__}")
        return None
    except (IndexError, KeyError) as e:
        print(f"Erişim hatası: {type(e).__name__}")
        return None

# Test
print(calculate("divide", 10, 0))        # ZeroDivisionError
print(calculate("list_access", 5, 10))   # IndexError
```

**Açıklama:** Parantez içinde birden fazla exception türü belirterek aynı işlemi uygulayabiliriz.

---

## Else ve Finally Blokları

### Else Bloğu

`else` bloğu, `try` bloğunda **hiçbir exception oluşmazsa** çalışır.

### Finally Bloğu

`finally` bloğu, **her durumda** (exception olsa da olmasa da) çalışır. Genellikle temizlik işlemleri için kullanılır.

### Örnek 6: Else ve Finally Kullanımı

```python
# Dosya işlemleri örneği
def read_file_safely(filename):
    file_handle = None
    try:
        print("Dosya açılıyor...")
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print("Dosya başarıyla okundu")
        return content
    except FileNotFoundError:
        print(f"Hata: '{filename}' dosyası bulunamadı!")
        return None
    except PermissionError:
        print(f"Hata: '{filename}' dosyasına erişim izni yok!")
        return None
    else:
        print("İşlem hatasız tamamlandı")
        # Bu blok sadece exception olmadığında çalışır
        print(f"Dosya boyutu: {len(content)} karakter")
    finally:
        print("Finally bloğu çalışıyor...")
        if file_handle:
            file_handle.close()
            print("Dosya kapatıldı")
        print("Temizlik işlemleri tamamlandı")

# Test
print("=== Başarılı Okuma ===")
# Not: Test için gerçek bir dosya oluşturabilirsiniz
# content = read_file_safely("example.txt")

print("\n=== Başarısız Okuma ===")
content = read_file_safely("nonexistent.txt")
```

### Örnek 7: Finally ile Kaynak Yönetimi

```python
# Veritabanı bağlantısı simülasyonu
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def connect(self):
        print(f"{self.db_name} veritabanına bağlanılıyor...")
        self.connected = True

    def execute_query(self, query):
        if not self.connected:
            raise ConnectionError("Veritabanı bağlı değil!")
        if "DELETE *" in query:
            raise ValueError("Tehlikeli sorgu!")
        return f"Sorgu çalıştırıldı: {query}"

    def disconnect(self):
        print(f"{self.db_name} bağlantısı kapatılıyor...")
        self.connected = False

def perform_database_operation(query):
    db = DatabaseConnection("MyDatabase")
    try:
        db.connect()
        result = db.execute_query(query)
        print(result)
        return result
    except ValueError as e:
        print(f"Sorgu hatası: {e}")
        return None
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")
        return None
    else:
        print("Sorgu başarıyla tamamlandı")
    finally:
        # Bağlantı her durumda kapatılır
        if db.connected:
            db.disconnect()
        print("Kaynak temizlendi")

# Test
print("=== Normal Sorgu ===")
perform_database_operation("SELECT * FROM users")

print("\n=== Hatalı Sorgu ===")
perform_database_operation("DELETE * FROM users")
```

**Açıklama:** `finally` bloğu, exception olsa da olmasa da çalışır. Bu özellik, dosya kapatma, bağlantı kesme gibi temizlik işlemleri için kritiktir.

---

## Exception Bilgisine Erişmek

Exception object'ine `as` anahtar kelimesiyle erişebiliriz.

### Örnek 8: Exception Detayları

```python
# Exception bilgilerini detaylı incelemek
import sys
import traceback

def detailed_exception_handling():
    try:
        numbers = [1, 2, 3]
        result = numbers[5] / 0
    except Exception as e:
        # Exception türü
        print(f"Exception Türü: {type(e).__name__}")

        # Exception mesajı
        print(f"Exception Mesajı: {str(e)}")

        # Exception argümanları
        print(f"Exception Args: {e.args}")

        # Traceback bilgisi
        print("\nDetaylı Traceback:")
        traceback.print_exc()

        # Sistem bilgisi
        print(f"\nSistem Bilgisi: {sys.exc_info()[0]}")

detailed_exception_handling()
```

### Örnek 9: Exception Bilgilerini Loglama

```python
# Exception'ları loglama örneği
from datetime import datetime

def log_exception(func):
    """Exception'ları dosyaya kaydeden decorator"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Exception bilgilerini topla
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_type = type(e).__name__
            error_message = str(e)

            # Log mesajı oluştur
            log_entry = f"""
{'='*50}
Zaman: {timestamp}
Fonksiyon: {func.__name__}
Exception: {error_type}
Mesaj: {error_message}
Args: {args}
Kwargs: {kwargs}
{'='*50}
"""
            print("LOG ENTRY:", log_entry)

            # Gerçek uygulamada dosyaya yazılabilir
            # with open('error.log', 'a') as f:
            #     f.write(log_entry)

            raise  # Exception'ı tekrar fırlat

@log_exception
def divide_numbers(a, b):
    return a / b

# Test
try:
    result = divide_numbers(10, 0)
except ZeroDivisionError:
    print("Exception loglandı ve yakalandı")
```

**Açıklama:** Exception bilgilerini yakalayıp loglayarak hata ayıklama sürecini kolaylaştırabiliriz.

---

## Yaygın Exception Türleri

Python'da sık karşılaşılan exception türleri:

### Örnek 10: Yaygın Exception'lar

```python
# Farklı exception türlerini göstermek
def demonstrate_common_exceptions():

    # 1. ValueError - Yanlış değer
    print("1. ValueError:")
    try:
        number = int("abc")
    except ValueError as e:
        print(f"   Hata: {e}")

    # 2. TypeError - Yanlış tip
    print("\n2. TypeError:")
    try:
        result = "text" + 5
    except TypeError as e:
        print(f"   Hata: {e}")

    # 3. IndexError - Geçersiz indeks
    print("\n3. IndexError:")
    try:
        my_list = [1, 2, 3]
        item = my_list[10]
    except IndexError as e:
        print(f"   Hata: {e}")

    # 4. KeyError - Geçersiz anahtar
    print("\n4. KeyError:")
    try:
        my_dict = {"name": "Ahmet"}
        age = my_dict["age"]
    except KeyError as e:
        print(f"   Hata: {e}")

    # 5. AttributeError - Geçersiz attribute
    print("\n5. AttributeError:")
    try:
        my_list = [1, 2, 3]
        my_list.append_all([4, 5])  # Böyle bir method yok
    except AttributeError as e:
        print(f"   Hata: {e}")

    # 6. FileNotFoundError - Dosya bulunamadı
    print("\n6. FileNotFoundError:")
    try:
        with open("nonexistent.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"   Hata: {e}")

    # 7. ZeroDivisionError - Sıfıra bölme
    print("\n7. ZeroDivisionError:")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"   Hata: {e}")

    # 8. ImportError - İmport hatası
    print("\n8. ImportError:")
    try:
        import nonexistent_module
    except ImportError as e:
        print(f"   Hata: {e}")

    # 9. NameError - Tanımsız değişken
    print("\n9. NameError:")
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"   Hata: {e}")

    # 10. RuntimeError - Çalışma zamanı hatası
    print("\n10. RuntimeError:")
    try:
        raise RuntimeError("Özel çalışma zamanı hatası")
    except RuntimeError as e:
        print(f"   Hata: {e}")

demonstrate_common_exceptions()
```

**Açıklama:** Her exception türü farklı bir hata durumunu temsil eder. Uygun exception'ı yakalamak, hatayı daha iyi yönetmemizi sağlar.

---

## Exception Fırlatmak (Raise)

`raise` anahtar kelimesiyle manuel olarak exception fırlatabiliriz.

### Örnek 11: Raise Kullanımı

```python
# Exception fırlatmak
def validate_age(age):
    """Yaş doğrulama fonksiyonu"""
    if not isinstance(age, int):
        raise TypeError("Yaş bir tam sayı olmalıdır!")

    if age < 0:
        raise ValueError("Yaş negatif olamaz!")

    if age > 150:
        raise ValueError("Geçersiz yaş: 150'den büyük olamaz!")

    return True

def register_user(name, age):
    """Kullanıcı kayıt fonksiyonu"""
    try:
        validate_age(age)
        print(f"Kullanıcı kaydedildi: {name}, {age} yaşında")
        return True
    except TypeError as e:
        print(f"Tip Hatası: {e}")
        return False
    except ValueError as e:
        print(f"Değer Hatası: {e}")
        return False

# Test
register_user("Ahmet", 25)      # Başarılı
register_user("Mehmet", "25")   # TypeError
register_user("Ayşe", -5)       # ValueError
register_user("Fatma", 200)     # ValueError
```

### Örnek 12: Exception'ı Yeniden Fırlatmak

```python
# Exception'ı yakalayıp tekrar fırlatmak
def process_payment(amount):
    """Ödeme işleme fonksiyonu"""
    try:
        if amount <= 0:
            raise ValueError("Ödeme tutarı pozitif olmalıdır!")

        # Ödeme işlemi simülasyonu
        if amount > 10000:
            raise Exception("Büyük tutarlar için onay gerekli!")

        print(f"Ödeme işlendi: {amount} TL")
        return True

    except ValueError as e:
        print(f"Doğrulama hatası: {e}")
        raise  # Exception'ı tekrar fırlat
    except Exception as e:
        print(f"İşlem hatası: {e}")
        # Loglama yapılabilir
        raise  # Exception'ı tekrar fırlat

def handle_payment(amount):
    """Üst seviye ödeme yönetimi"""
    try:
        process_payment(amount)
    except ValueError:
        print("ValueError üst seviyede yakalandı")
    except Exception:
        print("Genel exception üst seviyede yakalandı")

# Test
print("=== Test 1 ===")
handle_payment(100)

print("\n=== Test 2 ===")
handle_payment(-50)

print("\n=== Test 3 ===")
handle_payment(15000)
```

**Açıklama:** `raise` tek başına kullanıldığında, yakalanan exception'ı tekrar fırlatır. Bu, exception'ı logladıktan sonra üst seviyeye iletmek için kullanışlıdır.

---

## Özel Exception Sınıfları

Kendi exception sınıflarımızı oluşturarak daha anlamlı hata yönetimi yapabiliriz.

### Örnek 13: Özel Exception Sınıfları

```python
# Özel exception sınıfları oluşturmak
class BankException(Exception):
    """Banka işlemleri için temel exception"""
    pass

class InsufficientFundsException(BankException):
    """Yetersiz bakiye exception'ı"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortage = amount - balance
        super().__init__(
            f"Yetersiz bakiye! Bakiye: {balance} TL, "
            f"İstenen: {amount} TL, Eksik: {self.shortage} TL"
        )

class InvalidAccountException(BankException):
    """Geçersiz hesap exception'ı"""
    def __init__(self, account_number):
        self.account_number = account_number
        super().__init__(f"Geçersiz hesap numarası: {account_number}")

class DailyLimitExceededException(BankException):
    """Günlük limit aşımı exception'ı"""
    def __init__(self, limit, requested):
        self.limit = limit
        self.requested = requested
        super().__init__(
            f"Günlük limit aşıldı! Limit: {limit} TL, "
            f"Talep: {requested} TL"
        )

class BankAccount:
    """Banka hesabı sınıfı"""
    DAILY_LIMIT = 5000

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.daily_withdrawal = 0

    def withdraw(self, amount):
        """Para çekme"""
        # Hesap kontrolü
        if len(self.account_number) != 10:
            raise InvalidAccountException(self.account_number)

        # Günlük limit kontrolü
        if self.daily_withdrawal + amount > self.DAILY_LIMIT:
            raise DailyLimitExceededException(
                self.DAILY_LIMIT,
                self.daily_withdrawal + amount
            )

        # Bakiye kontrolü
        if amount > self.balance:
            raise InsufficientFundsException(self.balance, amount)

        # İşlemi gerçekleştir
        self.balance -= amount
        self.daily_withdrawal += amount
        print(f"Para çekildi: {amount} TL, Kalan bakiye: {self.balance} TL")
        return True

# Kullanım örneği
def perform_withdrawal(account, amount):
    try:
        account.withdraw(amount)
    except InvalidAccountException as e:
        print(f"Hesap Hatası: {e}")
    except InsufficientFundsException as e:
        print(f"Bakiye Hatası: {e}")
        print(f"Ek bilgi - Eksik tutar: {e.shortage} TL")
    except DailyLimitExceededException as e:
        print(f"Limit Hatası: {e}")
        print(f"Ek bilgi - Kalan limit: {e.limit - (e.requested - amount)} TL")
    except BankException as e:
        print(f"Genel Banka Hatası: {e}")

# Test
print("=== Geçerli İşlem ===")
account1 = BankAccount("1234567890", 1000)
perform_withdrawal(account1, 500)

print("\n=== Yetersiz Bakiye ===")
perform_withdrawal(account1, 1000)

print("\n=== Günlük Limit Aşımı ===")
account2 = BankAccount("1234567890", 10000)
perform_withdrawal(account2, 6000)

print("\n=== Geçersiz Hesap ===")
account3 = BankAccount("123", 1000)
perform_withdrawal(account3, 100)
```

**Açıklama:** Özel exception sınıfları oluşturarak:
- Daha açıklayıcı hata mesajları verebiliriz
- Exception'a ek bilgiler ekleyebiliriz
- Exception hiyerarşisi oluşturabiliriz
- Kod okunabilirliğini artırabiliriz

---

## Exception Chaining

Python 3'te exception'lar birbirine zincirlenebilir (`from` anahtar kelimesi).

### Örnek 14: Exception Chaining

```python
# Exception chaining (zincirleme)
class ConfigurationError(Exception):
    """Konfigürasyon hatası"""
    pass

class DatabaseError(Exception):
    """Veritabanı hatası"""
    pass

def load_config(filename):
    """Konfigürasyon dosyası yükleme"""
    try:
        with open(filename, 'r') as f:
            config = f.read()

        if not config:
            raise ValueError("Konfigürasyon dosyası boş!")

        return config
    except FileNotFoundError as e:
        # Orijinal exception'ı yeni exception'a zincirle
        raise ConfigurationError(
            f"Konfigürasyon yüklenemedi: {filename}"
        ) from e
    except ValueError as e:
        raise ConfigurationError(
            "Geçersiz konfigürasyon içeriği"
        ) from e

def initialize_database(config):
    """Veritabanı başlatma"""
    try:
        # Konfigürasyon yükle
        settings = load_config(config)

        # Veritabanı bağlantısı simülasyonu
        if "database" not in settings:
            raise KeyError("Veritabanı ayarı bulunamadı")

        print("Veritabanı başarıyla başlatıldı")
        return True

    except ConfigurationError as e:
        # ConfigurationError'ı DatabaseError'a zincirle
        raise DatabaseError(
            "Veritabanı başlatılamadı"
        ) from e
    except KeyError as e:
        raise DatabaseError(
            "Gerekli ayarlar eksik"
        ) from e

# Kullanım
try:
    initialize_database("nonexistent_config.ini")
except DatabaseError as e:
    print(f"Hata: {e}")
    print(f"Hata Türü: {type(e).__name__}")

    # Zincirlenmiş exception'a erişim
    if e.__cause__:
        print(f"\nNedeni: {e.__cause__}")
        print(f"Neden Türü: {type(e.__cause__).__name__}")

        # İkinci seviye zincir
        if e.__cause__.__cause__:
            print(f"\nKök Neden: {e.__cause__.__cause__}")
            print(f"Kök Neden Türü: {type(e.__cause__.__cause__).__name__}")
```

### Örnek 15: Exception Chaining ile Detaylı Hata İzleme

```python
# Katmanlı exception handling
class ValidationError(Exception):
    """Doğrulama hatası"""
    pass

class BusinessLogicError(Exception):
    """İş mantığı hatası"""
    pass

class APIError(Exception):
    """API hatası"""
    pass

def validate_email(email):
    """Email doğrulama"""
    if "@" not in email:
        raise ValueError(f"Geçersiz email formatı: {email}")
    return True

def create_user(username, email):
    """Kullanıcı oluşturma"""
    try:
        # Email doğrulama
        validate_email(email)

        # Kullanıcı adı kontrolü
        if len(username) < 3:
            raise ValueError("Kullanıcı adı en az 3 karakter olmalı")

        print(f"Kullanıcı oluşturuldu: {username}")
        return {"username": username, "email": email}

    except ValueError as e:
        raise ValidationError(
            f"Kullanıcı doğrulama başarısız: {username}"
        ) from e

def register_user_api(username, email):
    """API endpoint simülasyonu"""
    try:
        user = create_user(username, email)

        # İş mantığı kontrolü
        if username == "admin":
            raise PermissionError("'admin' kullanıcı adı rezerve edilmiş")

        return {"status": "success", "user": user}

    except ValidationError as e:
        raise BusinessLogicError(
            "Kayıt işlemi başarısız"
        ) from e
    except PermissionError as e:
        raise BusinessLogicError(
            "Yetki hatası"
        ) from e

def handle_api_request(username, email):
    """API istek yöneticisi"""
    try:
        return register_user_api(username, email)
    except BusinessLogicError as e:
        raise APIError(
            f"API hatası: Kullanıcı kaydedilemedi"
        ) from e

# Test ve hata zincirini görüntüleme
def test_with_error_chain(username, email):
    try:
        result = handle_api_request(username, email)
        print(f"Başarılı: {result}")
    except APIError as e:
        print("=== HATA ZİNCİRİ ===")
        current_error = e
        level = 1

        while current_error:
            print(f"\nSeviye {level}:")
            print(f"  Tür: {type(current_error).__name__}")
            print(f"  Mesaj: {current_error}")

            # Bir sonraki seviye
            current_error = current_error.__cause__
            level += 1

# Test senaryoları
print("=== Test 1: Geçersiz Email ===")
test_with_error_chain("ahmet", "invalid-email")

print("\n\n=== Test 2: Kısa Kullanıcı Adı ===")
test_with_error_chain("ab", "user@example.com")

print("\n\n=== Test 3: Rezerve Kullanıcı Adı ===")
test_with_error_chain("admin", "admin@example.com")

print("\n\n=== Test 4: Başarılı ===")
test_with_error_chain("ahmet", "ahmet@example.com")
```

**Açıklama:** Exception chaining ile:
- Hatanın nereden kaynaklandığını izleyebiliriz
- Orijinal hata bilgisini kaybetmeden yeni exception'lar fırlatabiliriz
- Katmanlı uygulamalarda hata akışını takip edebiliriz

---

## Best Practices

### 1. Spesifik Exception'ları Yakalayın

```python
# ❌ Kötü: Çok genel
try:
    result = int(input_value) / divisor
except:  # Tüm hataları yakalar, KeyboardInterrupt bile!
    print("Bir hata oluştu")

# ✅ İyi: Spesifik
try:
    result = int(input_value) / divisor
except ValueError:
    print("Geçersiz sayı formatı")
except ZeroDivisionError:
    print("Sıfıra bölme hatası")
```

### 2. Exception'ları Sessizce Yutmayın

```python
# ❌ Kötü: Silent failure
try:
    risky_operation()
except Exception:
    pass  # Hata göz ardı edilir!

# ✅ İyi: En azından logla
try:
    risky_operation()
except Exception as e:
    logger.error(f"İşlem başarısız: {e}")
    # veya raise ile tekrar fırlat
```

### 3. Finally ile Kaynakları Temizleyin

```python
# ✅ İyi: Finally ile temizlik
file = None
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Dosya bulunamadı")
finally:
    if file:
        file.close()

# ✅ Daha İyi: Context manager kullan
try:
    with open("data.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Dosya bulunamadı")
```

### 4. Exception'larda Anlamlı Mesajlar Kullanın

```python
# ❌ Kötü: Belirsiz mesaj
if age < 0:
    raise ValueError("Hata")

# ✅ İyi: Açıklayıcı mesaj
if age < 0:
    raise ValueError(
        f"Yaş negatif olamaz. Girilen değer: {age}"
    )
```

### 5. Özel Exception'lar Oluşturun

```python
# ✅ İyi: Domain-specific exceptions
class PaymentError(Exception):
    """Ödeme işlemlerinde oluşan hatalar"""
    pass

class PaymentDeclinedError(PaymentError):
    """Ödeme reddedildi"""
    pass

class InsufficientFundsError(PaymentError):
    """Yetersiz bakiye"""
    pass
```

### 6. EAFP Prensibini Kullanın

EAFP: "Easier to Ask for Forgiveness than Permission" (İzin istemektense özür dilemek daha kolay)

```python
# LBYL (Look Before You Leap) - Pythonic değil
if key in my_dict:
    value = my_dict[key]
else:
    value = None

# ✅ EAFP - Pythonic
try:
    value = my_dict[key]
except KeyError:
    value = None

# ✅ Veya daha basit
value = my_dict.get(key)  # KeyError yerine None döner
```

### 7. Çok Fazla İç İçe Try/Except Kullanmayın

```python
# ❌ Kötü: İç içe try/except
try:
    try:
        try:
            risky_operation()
        except TypeError:
            handle_type_error()
    except ValueError:
        handle_value_error()
except Exception:
    handle_general_error()

# ✅ İyi: Düz yapı
try:
    risky_operation()
except TypeError:
    handle_type_error()
except ValueError:
    handle_value_error()
except Exception:
    handle_general_error()
```

### 8. Exception'ları Dokümante Edin

```python
def process_data(data):
    """
    Veriyi işler ve sonucu döner.

    Args:
        data: İşlenecek veri

    Returns:
        İşlenmiş veri

    Raises:
        ValueError: Veri geçersiz formatsa
        TypeError: Veri yanlış tipte ise
        ProcessingError: İşleme hatası oluşursa
    """
    if not isinstance(data, dict):
        raise TypeError("Veri dict tipinde olmalı")

    if "required_field" not in data:
        raise ValueError("'required_field' alanı gerekli")

    # İşleme devam et...
```

---

## Özet

### Exception Handling Temel Kavramlar:

1. **Try/Except**: Hataları yakalamak için temel yapı
2. **Else**: Exception oluşmazsa çalışan blok
3. **Finally**: Her durumda çalışan blok (temizlik işlemleri için)
4. **Raise**: Exception fırlatmak için
5. **Custom Exceptions**: Özel exception sınıfları oluşturmak
6. **Exception Chaining**: Exception'ları birbirine bağlamak

### Yaygın Exception Türleri:

- `ValueError`: Yanlış değer
- `TypeError`: Yanlış tip
- `IndexError`: Geçersiz indeks
- `KeyError`: Geçersiz anahtar
- `FileNotFoundError`: Dosya bulunamadı
- `ZeroDivisionError`: Sıfıra bölme
- `AttributeError`: Geçersiz attribute
- `ImportError`: Import hatası
- `NameError`: Tanımsız değişken

### Best Practices:

1. Spesifik exception'ları yakalayın
2. Exception'ları sessizce yutmayın
3. Finally ile kaynakları temizleyin
4. Anlamlı hata mesajları kullanın
5. Özel exception sınıfları oluşturun
6. EAFP prensibini benimseyin
7. Exception'ları dokümante edin
8. İç içe try/except kullanmaktan kaçının

Exception handling, robust ve güvenilir programlar yazmak için kritik bir beceridir. Doğru kullanıldığında, programlarınızın beklenmedik durumlarla başa çıkmasını ve kullanıcı deneyimini iyileştirmenizi sağlar.
