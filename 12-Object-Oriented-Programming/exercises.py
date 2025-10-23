"""
OBJECT-ORIENTED PROGRAMMING (NESNE YÖNELİMLİ PROGRAMLAMA) - ALIŞTIRMALAR
==========================================================================

Her soruyu çözmeye çalışın. Takılırsanız, her sorunun altındaki
ÇÖZÜM bölümünü inceleyebilirsiniz.

Zorluk Seviyeleri:
[Kolay] - Temel kavramları test eder
[Orta] - Birden fazla kavramı birleştirir
[Zor] - Daha karmaşık problemler
[Challenge] - Dünya standartlarında zorlayıcı sorular
"""

# =============================================================================
# SORU 1: [Kolay] Basit Class Tanımlama
# =============================================================================
# Bir Person sınıfı oluşturun.
# Attributes: name, age, city
# Method: introduce() - "Merhaba, ben {name}. {age} yaşındayım ve {city}'de yaşıyorum."
# __init__ ile attribute'ları başlatın

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- class anahtar kelimesi ile sınıf tanımlanır
- __init__ constructor, nesne oluşturulurken çalışır
- self parametresi, nesnenin kendisini temsil eder
- Instance variables self.attribute_name şeklinde tanımlanır
"""

class Person:
    """Kişi sınıfı - basit örnek"""

    def __init__(self, name, age, city):
        """
        Kişi nesnesini başlatır

        Args:
            name (str): Kişinin adı
            age (int): Kişinin yaşı
            city (str): Kişinin yaşadığı şehir
        """
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        """Kişi kendini tanıtır"""
        return f"Merhaba, ben {self.name}. {self.age} yaşındayım ve {self.city}'de yaşıyorum."

# Test
person1 = Person("Ali Yılmaz", 25, "İstanbul")
person2 = Person("Ayşe Kaya", 30, "Ankara")

print(person1.introduce())
# Output: Merhaba, ben Ali Yılmaz. 25 yaşındayım ve İstanbul'de yaşıyorum.

print(person2.introduce())
# Output: Merhaba, ben Ayşe Kaya. 30 yaşındayım ve Ankara'de yaşıyorum.


# =============================================================================
# SORU 2: [Kolay] Instance Methods
# =============================================================================
# Bir Rectangle (Dikdörtgen) sınıfı oluşturun.
# Attributes: width, height
# Methods:
#   - area() -> Alan hesapla
#   - perimeter() -> Çevre hesapla
#   - is_square() -> Kare mi kontrol et (width == height)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Instance methods nesne üzerinde çalışan fonksiyonlardır
- İlk parametre her zaman self'tir
- self.attribute ile instance variable'lara erişilir
- return ile değer döndürülür
"""

class Rectangle:
    """Dikdörtgen sınıfı"""

    def __init__(self, width, height):
        """Dikdörtgen başlatma"""
        self.width = width
        self.height = height

    def area(self):
        """Alan hesaplar"""
        return self.width * self.height

    def perimeter(self):
        """Çevre hesaplar"""
        return 2 * (self.width + self.height)

    def is_square(self):
        """Kare mi kontrol eder"""
        return self.width == self.height

    def __str__(self):
        """String representasyonu"""
        return f"Rectangle({self.width}x{self.height})"

# Test
rect1 = Rectangle(10, 5)
print(f"{rect1} - Alan: {rect1.area()}, Çevre: {rect1.perimeter()}")
# Output: Rectangle(10x5) - Alan: 50, Çevre: 30
print(f"Kare mi? {rect1.is_square()}")  # False

rect2 = Rectangle(7, 7)
print(f"{rect2} - Alan: {rect2.area()}, Çevre: {rect2.perimeter()}")
# Output: Rectangle(7x7) - Alan: 49, Çevre: 28
print(f"Kare mi? {rect2.is_square()}")  # True


# =============================================================================
# SORU 3: [Kolay] Class Variables
# =============================================================================
# Bir Dog sınıfı oluşturun.
# Class variable: species = "Canis familiaris"
# Instance variables: name, age, breed
# Methods:
#   - bark() -> "{name} havlıyor: Hav hav!"
#   - description() -> "{name}, {age} yaşında bir {breed}"

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Class variables sınıf seviyesinde tanımlanır
- Tüm nesneler tarafından paylaşılır
- ClassName.variable veya self.variable ile erişilir
- Instance variables her nesneye özgüdür
"""

class Dog:
    """Köpek sınıfı"""

    # Class variable - tüm köpekler için ortak
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        """Köpek başlatma"""
        # Instance variables - her köpeğe özgü
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        """Köpek havlar"""
        return f"{self.name} havlıyor: Hav hav!"

    def description(self):
        """Köpek tanımı"""
        return f"{self.name}, {self.age} yaşında bir {self.breed}"

    def __str__(self):
        return f"{self.name} ({self.species})"

# Test
dog1 = Dog("Karabaş", 3, "Golden Retriever")
dog2 = Dog("Pamuk", 5, "Husky")

print(dog1.bark())  # Karabaş havlıyor: Hav hav!
print(dog1.description())  # Karabaş, 3 yaşında bir Golden Retriever
print(f"Tür: {Dog.species}")  # Canis familiaris

# Her iki köpek de aynı türe sahip
print(f"{dog1.name} türü: {dog1.species}")  # Canis familiaris
print(f"{dog2.name} türü: {dog2.species}")  # Canis familiaris


# =============================================================================
# SORU 4: [Orta] Bank Account System
# =============================================================================
# Bir BankAccount sınıfı oluşturun.
# Attributes: account_holder, balance (başlangıç 0)
# Methods:
#   - deposit(amount) -> Para yatır, balance güncelle
#   - withdraw(amount) -> Para çek (yetersiz bakiye kontrolü)
#   - get_balance() -> Bakiyeyi döndür
#   - transfer(amount, other_account) -> Başka hesaba para transfer et

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Encapsulation: Bakiye korunuyor, sadece metodlarla değiştirilebilir
- Validasyon: Para çekerken bakiye kontrolü
- Nesne etkileşimi: transfer metodunda iki nesne birlikte çalışıyor
"""

class BankAccount:
    """Banka hesabı sınıfı"""

    def __init__(self, account_holder, balance=0):
        """
        Hesap başlatma

        Args:
            account_holder (str): Hesap sahibi
            balance (float): Başlangıç bakiyesi (default: 0)
        """
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []  # İşlem geçmişi

    def deposit(self, amount):
        """Para yatırma"""
        if amount <= 0:
            return "Geçersiz tutar!"

        self.balance += amount
        self.transactions.append(f"Yatırma: +{amount} TL")
        return f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL"

    def withdraw(self, amount):
        """Para çekme"""
        if amount <= 0:
            return "Geçersiz tutar!"

        if amount > self.balance:
            return "Yetersiz bakiye!"

        self.balance -= amount
        self.transactions.append(f"Çekme: -{amount} TL")
        return f"{amount} TL çekildi. Yeni bakiye: {self.balance} TL"

    def get_balance(self):
        """Bakiye sorgulama"""
        return self.balance

    def transfer(self, amount, other_account):
        """Başka hesaba transfer"""
        if amount <= 0:
            return "Geçersiz tutar!"

        if amount > self.balance:
            return "Yetersiz bakiye!"

        # Kendi hesabından çek
        self.balance -= amount
        self.transactions.append(f"Transfer: -{amount} TL → {other_account.account_holder}")

        # Diğer hesaba yatır
        other_account.balance += amount
        other_account.transactions.append(f"Transfer: +{amount} TL ← {self.account_holder}")

        return f"{amount} TL {other_account.account_holder}'a transfer edildi"

    def show_transactions(self):
        """İşlem geçmişini göster"""
        print(f"{self.account_holder} - İşlem Geçmişi:")
        for transaction in self.transactions:
            print(f"  {transaction}")

    def __str__(self):
        return f"{self.account_holder}: {self.balance} TL"

# Test
account1 = BankAccount("Ali Yılmaz", 1000)
account2 = BankAccount("Ayşe Kaya", 500)

print(account1.deposit(500))   # 500 TL yatırıldı. Yeni bakiye: 1500 TL
print(account1.withdraw(200))  # 200 TL çekildi. Yeni bakiye: 1300 TL
print(account1.transfer(300, account2))  # 300 TL Ayşe Kaya'a transfer edildi

print(f"\n{account1}")  # Ali Yılmaz: 1000 TL
print(f"{account2}")    # Ayşe Kaya: 800 TL

print()
account1.show_transactions()
print()
account2.show_transactions()


# =============================================================================
# SORU 5: [Orta] Class Methods ve Static Methods
# =============================================================================
# Bir Employee sınıfı oluşturun.
# Class variable: raise_percent = 1.04 (4% zam)
# Instance variables: name, salary
# Methods:
#   - apply_raise() -> Maaşa zam uygula (instance method)
#   - set_raise_percent(percent) -> Zam oranını değiştir (class method)
#   - is_workday(day) -> İş günü mü kontrol et (static method, Pzt-Cum: True)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Instance method: self parametresi, nesne üzerinde çalışır
- Class method: @classmethod, cls parametresi, sınıf üzerinde çalışır
- Static method: @staticmethod, self/cls yok, utility fonksiyon gibi
"""

class Employee:
    """Çalışan sınıfı"""

    # Class variable
    raise_percent = 1.04  # 4% zam
    employee_count = 0

    def __init__(self, name, salary):
        """Çalışan başlatma"""
        self.name = name
        self.salary = salary

        # Class variable'ı güncelle
        Employee.employee_count += 1

    # Instance method
    def apply_raise(self):
        """Maaşa zam uygula"""
        old_salary = self.salary
        self.salary = int(self.salary * Employee.raise_percent)
        return f"{self.name} - Eski: {old_salary} TL → Yeni: {self.salary} TL"

    # Class method
    @classmethod
    def set_raise_percent(cls, percent):
        """
        Zam oranını değiştir

        Args:
            percent (float): Yeni zam oranı (örn: 1.10 = %10)
        """
        cls.raise_percent = percent
        return f"Zam oranı %{(percent - 1) * 100:.0f} olarak güncellendi"

    # Class method - factory method
    @classmethod
    def from_string(cls, emp_str):
        """
        String'den çalışan oluştur
        Format: "İsim-Maaş"
        """
        name, salary = emp_str.split('-')
        return cls(name, int(salary))

    # Static method
    @staticmethod
    def is_workday(day):
        """
        İş günü mü kontrol et

        Args:
            day (str): Gün adı (Pazartesi, Salı, vb.)

        Returns:
            bool: İş günü ise True
        """
        workdays = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
        return day in workdays

    def __str__(self):
        return f"{self.name}: {self.salary} TL"

# Test
emp1 = Employee("Ali Yılmaz", 10000)
emp2 = Employee("Ayşe Kaya", 12000)

print(f"Toplam çalışan: {Employee.employee_count}")  # 2

# Instance method
print(emp1.apply_raise())  # Ali Yılmaz - Eski: 10000 TL → Yeni: 10400 TL

# Class method
print(Employee.set_raise_percent(1.10))  # Zam oranı %10 olarak güncellendi
print(emp2.apply_raise())  # Ayşe Kaya - Eski: 12000 TL → Yeni: 13200 TL

# Factory method
emp3 = Employee.from_string("Mehmet Demir-15000")
print(emp3)  # Mehmet Demir: 15000 TL

# Static method
print(f"Pazartesi iş günü mü? {Employee.is_workday('Pazartesi')}")  # True
print(f"Cumartesi iş günü mü? {Employee.is_workday('Cumartesi')}")  # False


# =============================================================================
# SORU 6: [Orta] Inheritance (Kalıtım)
# =============================================================================
# Bir Vehicle (Araç) base class oluşturun.
# Attributes: brand, model, year
# Methods: start(), stop(), info()
#
# Vehicle'dan Car ve Motorcycle sınıfları türetin.
# Car: ek attribute -> doors (kapı sayısı)
# Motorcycle: ek attribute -> engine_capacity (motor hacmi)
# Her ikisi de info() metodunu override etsin

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Inheritance: class Child(Parent) şeklinde tanımlanır
- super().__init__() ile parent constructor çağrılır
- Method overriding: Child class'ta aynı isimli metod yeniden tanımlanır
- isinstance() ile tip kontrolü yapılır
"""

# Parent class (Base class)
class Vehicle:
    """Araç base class"""

    def __init__(self, brand, model, year):
        """Araç başlatma"""
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        """Aracı çalıştır"""
        if self.is_running:
            return f"{self.brand} {self.model} zaten çalışıyor"
        self.is_running = True
        return f"{self.brand} {self.model} çalıştırıldı"

    def stop(self):
        """Aracı durdur"""
        if not self.is_running:
            return f"{self.brand} {self.model} zaten durmuş"
        self.is_running = False
        return f"{self.brand} {self.model} durduruldu"

    def info(self):
        """Araç bilgisi"""
        return f"{self.year} {self.brand} {self.model}"

# Child class 1
class Car(Vehicle):
    """Araba - Vehicle'dan türetildi"""

    def __init__(self, brand, model, year, doors):
        """Araba başlatma"""
        # Parent constructor'ı çağır
        super().__init__(brand, model, year)

        # Child'a özgü attribute
        self.doors = doors

    def info(self):
        """Araba bilgisi (override edildi)"""
        # Parent metodunu çağır ve genişlet
        base_info = super().info()
        return f"{base_info} ({self.doors} kapılı araba)"

    def honk(self):
        """Korna çal (araba'ya özgü)"""
        return "Düüüt düüüt!"

# Child class 2
class Motorcycle(Vehicle):
    """Motosiklet - Vehicle'dan türetildi"""

    def __init__(self, brand, model, year, engine_capacity):
        """Motosiklet başlatma"""
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity  # cc cinsinden

    def info(self):
        """Motosiklet bilgisi (override edildi)"""
        base_info = super().info()
        return f"{base_info} ({self.engine_capacity}cc motosiklet)"

    def wheelie(self):
        """Tek teker (motosiklet'e özgü)"""
        return "Tek teker yapıyorum! Vııınnn!"

# Test
car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Yamaha", "R1", 2022, 998)

print(car.info())  # 2020 Toyota Corolla (4 kapılı araba)
print(car.start())  # Toyota Corolla çalıştırıldı
print(car.honk())   # Düüüt düüüt!

print()
print(motorcycle.info())  # 2022 Yamaha R1 (998cc motosiklet)
print(motorcycle.start())  # Yamaha R1 çalıştırıldı
print(motorcycle.wheelie())  # Tek teker yapıyorum! Vııınnn!

# isinstance kontrolü
print(f"\nCar, Vehicle mi? {isinstance(car, Vehicle)}")  # True
print(f"Motorcycle, Vehicle mi? {isinstance(motorcycle, Vehicle)}")  # True
print(f"Car, Motorcycle mi? {isinstance(car, Motorcycle)}")  # False


# =============================================================================
# SORU 7: [Zor] Polymorphism (Çok Biçimlilik)
# =============================================================================
# Bir Shape (Şekil) base class oluşturun.
# Methods: area(), perimeter() (NotImplementedError fırlatsın)
#
# Shape'den türetin:
# - Circle(radius)
# - Square(side)
# - Triangle(base, height, side1, side2, side3)
#
# Her biri area() ve perimeter() metodlarını implement etsin.
# Bir fonksiyon yazın: print_shape_info(shape) -> Polymorphism göstersin

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Abstract base class: Base metodlar NotImplementedError fırlatır
- Polymorphism: Aynı arayüz (area, perimeter), farklı implementasyonlar
- Duck typing: print_shape_info fonksiyonu tip kontrolü yapmıyor
- Her shape farklı hesaplama yapar ama aynı arayüzü kullanır
"""

import math

# Base class (Abstract)
class Shape:
    """Şekil base class - abstract"""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Alan hesapla (alt sınıflar implement etmeli)"""
        raise NotImplementedError("Alt sınıflar area() metodunu implement etmeli")

    def perimeter(self):
        """Çevre hesapla (alt sınıflar implement etmeli)"""
        raise NotImplementedError("Alt sınıflar perimeter() metodunu implement etmeli")

# Child class 1
class Circle(Shape):
    """Daire"""

    def __init__(self, radius):
        super().__init__("Daire")
        self.radius = radius

    def area(self):
        """Daire alanı: π × r²"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Daire çevresi: 2 × π × r"""
        return 2 * math.pi * self.radius

# Child class 2
class Square(Shape):
    """Kare"""

    def __init__(self, side):
        super().__init__("Kare")
        self.side = side

    def area(self):
        """Kare alanı: kenar²"""
        return self.side ** 2

    def perimeter(self):
        """Kare çevresi: 4 × kenar"""
        return 4 * self.side

# Child class 3
class Triangle(Shape):
    """Üçgen"""

    def __init__(self, base, height, side1, side2, side3):
        super().__init__("Üçgen")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """Üçgen alanı: (taban × yükseklik) / 2"""
        return (self.base * self.height) / 2

    def perimeter(self):
        """Üçgen çevresi: kenar1 + kenar2 + kenar3"""
        return self.side1 + self.side2 + self.side3

# Polymorphic fonksiyon
def print_shape_info(shape):
    """
    Şekil bilgilerini yazdırır (Polymorphism)

    Args:
        shape: Shape veya alt sınıflarından bir nesne
    """
    print(f"{shape.name}:")
    print(f"  Alan: {shape.area():.2f}")
    print(f"  Çevre: {shape.perimeter():.2f}")
    print()

# Test - Polymorphism gösterimi
shapes = [
    Circle(5),
    Square(4),
    Triangle(6, 4, 5, 5, 6)
]

print("=== POLYMORPHİSM ÖRNEĞİ ===\n")

# Aynı arayüz, farklı davranışlar
for shape in shapes:
    print_shape_info(shape)  # Her shape farklı hesaplama yapar

# Manuel test
circle = Circle(7)
print(f"Daire (r=7):")
print(f"  Alan: {circle.area():.2f}")  # 153.94
print(f"  Çevre: {circle.perimeter():.2f}")  # 43.98


# =============================================================================
# SORU 8: [Zor] Encapsulation (Kapsülleme)
# =============================================================================
# Bir CreditCard sınıfı oluşturun.
# Private attributes: __card_number, __pin, __balance, __credit_limit
# Public methods:
#   - verify_pin(pin) -> PIN kontrolü
#   - get_balance(pin) -> Bakiye sorgula
#   - purchase(amount, pin) -> Alışveriş yap
#   - pay_bill(amount) -> Fatura öde
# Encapsulation prensiplerine uygun olmalı

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Private attributes: __ prefix ile tanımlanır (name mangling)
- Encapsulation: Veriler korunur, sadece metodlarla erişilir
- Validasyon: Her işlemde PIN kontrolü ve limit kontrolü
- Security: Hassas veriler (PIN, kart no) direkt erişilemez
"""

class CreditCard:
    """Kredi kartı sınıfı - encapsulation örneği"""

    def __init__(self, card_number, pin, credit_limit):
        """
        Kredi kartı başlatma

        Args:
            card_number (str): Kart numarası
            pin (str): PIN kodu
            credit_limit (float): Kredi limiti
        """
        # Private attributes
        self.__card_number = card_number
        self.__pin = pin
        self.__balance = 0  # Borç
        self.__credit_limit = credit_limit
        self.__transactions = []

    def __verify_pin(self, pin):
        """PIN doğrula (private method)"""
        return pin == self.__pin

    def get_masked_card_number(self):
        """Maskeli kart numarası (güvenli)"""
        # Son 4 hane göster
        return "**** **** **** " + self.__card_number[-4:]

    def get_balance(self, pin):
        """Bakiye sorgula (PIN ile)"""
        if not self.__verify_pin(pin):
            return "Hatalı PIN!"
        return self.__balance

    def get_available_credit(self, pin):
        """Kullanılabilir kredi (PIN ile)"""
        if not self.__verify_pin(pin):
            return "Hatalı PIN!"
        return self.__credit_limit - self.__balance

    def purchase(self, amount, pin):
        """Alışveriş yap"""
        if not self.__verify_pin(pin):
            return "Hatalı PIN!"

        if amount <= 0:
            return "Geçersiz tutar!"

        # Limit kontrolü
        if self.__balance + amount > self.__credit_limit:
            return f"Limit aşıldı! Kullanılabilir: {self.__credit_limit - self.__balance} TL"

        # İşlemi gerçekleştir
        self.__balance += amount
        self.__transactions.append(f"Alışveriş: {amount} TL")
        return f"{amount} TL alışveriş yapıldı. Güncel borç: {self.__balance} TL"

    def pay_bill(self, amount):
        """Fatura öde (PIN gerekmez)"""
        if amount <= 0:
            return "Geçersiz tutar!"

        if amount > self.__balance:
            # Fazla ödeme yapılabilir
            overpayment = amount - self.__balance
            self.__balance = 0
            return f"Borç ödendi. Fazla ödeme: {overpayment} TL (iade edilecek)"

        self.__balance -= amount
        self.__transactions.append(f"Ödeme: {amount} TL")
        return f"{amount} TL ödeme yapıldı. Kalan borç: {self.__balance} TL"

    def change_pin(self, old_pin, new_pin):
        """PIN değiştir"""
        if not self.__verify_pin(old_pin):
            return "Hatalı PIN!"

        if len(new_pin) != 4 or not new_pin.isdigit():
            return "PIN 4 haneli rakam olmalı!"

        self.__pin = new_pin
        return "PIN başarıyla değiştirildi"

    def get_transactions(self, pin):
        """İşlem geçmişi (PIN ile)"""
        if not self.__verify_pin(pin):
            return "Hatalı PIN!"
        return self.__transactions.copy()  # Kopya döndür (güvenlik)

    def __str__(self):
        return f"Kart: {self.get_masked_card_number()}"

# Test
card = CreditCard("1234567890123456", "1234", 10000)

print(card)  # Kart: **** **** **** 3456
print(f"Kullanılabilir kredi: {card.get_available_credit('1234')} TL")  # 10000 TL

# Alışveriş
print(card.purchase(3000, "1234"))  # 3000 TL alışveriş yapıldı
print(card.purchase(2000, "1234"))  # 2000 TL alışveriş yapıldı

# Bakiye kontrolü
print(f"Borç: {card.get_balance('1234')} TL")  # 5000 TL

# Yanlış PIN
print(card.get_balance("0000"))  # Hatalı PIN!

# Ödeme
print(card.pay_bill(2000))  # 2000 TL ödeme yapıldı. Kalan borç: 3000 TL

# Limit aşımı
print(card.purchase(8000, "1234"))  # Limit aşıldı!

# İşlem geçmişi
transactions = card.get_transactions("1234")
print("\nİşlem Geçmişi:")
for t in transactions:
    print(f"  {t}")

# Private attribute'a erişim denemesi
# print(card.__pin)  # AttributeError
# print(card._CreditCard__pin)  # 1234 (name mangling - yapılmamalı!)


# =============================================================================
# SORU 9: [Zor] Special Methods (__str__, __repr__, __eq__, vb.)
# =============================================================================
# Bir Book sınıfı oluşturun.
# Attributes: title, author, year, pages
# Special methods:
#   - __str__ -> Kullanıcı dostu string
#   - __repr__ -> Developer string (nesneyi yeniden oluşturabilir)
#   - __eq__ -> Eşitlik kontrolü (title ve author aynıysa eşit)
#   - __lt__ -> Küçüktür (sayfa sayısına göre)
#   - __len__ -> Sayfa sayısı

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- __str__: print() ve str() için, kullanıcı dostu
- __repr__: repr() için, developer dostu, nesneyi yeniden oluşturabilir
- __eq__: == operatörü için
- __lt__: < operatörü için (diğer karşılaştırmalar türetilebilir)
- __len__: len() fonksiyonu için
"""

class Book:
    """Kitap sınıfı - special methods örneği"""

    def __init__(self, title, author, year, pages):
        """Kitap başlatma"""
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        """
        User-friendly string representation
        print() ve str() için kullanılır
        """
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        """
        Developer-friendly representation
        Nesneyi yeniden oluşturmak için kullanılabilir
        """
        return f"Book('{self.title}', '{self.author}', {self.year}, {self.pages})"

    def __eq__(self, other):
        """
        Eşitlik kontrolü (==)
        Title ve author aynıysa kitaplar eşit
        """
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        """
        Küçüktür (<)
        Sayfa sayısına göre karşılaştırma
        """
        return self.pages < other.pages

    def __le__(self, other):
        """Küçük eşit (<=)"""
        return self.pages <= other.pages

    def __gt__(self, other):
        """Büyüktür (>)"""
        return self.pages > other.pages

    def __ge__(self, other):
        """Büyük eşit (>=)"""
        return self.pages >= other.pages

    def __len__(self):
        """
        len() fonksiyonu için
        Sayfa sayısını döndürür
        """
        return self.pages

# Test
book1 = Book("1984", "George Orwell", 1949, 328)
book2 = Book("Hayvan Çiftliği", "George Orwell", 1945, 112)
book3 = Book("1984", "George Orwell", 2020, 350)  # Yeni baskı

# __str__ ve __repr__
print(str(book1))   # '1984' by George Orwell (1949)
print(repr(book1))  # Book('1984', 'George Orwell', 1949, 328)

# __eq__
print(f"\nbook1 == book3? {book1 == book3}")  # True (title ve author aynı)
print(f"book1 == book2? {book1 == book2}")    # False

# __lt__, __gt__
print(f"\nbook2 < book1? {book2 < book1}")    # True (112 < 328)
print(f"book1 > book2? {book1 > book2}")      # True

# __len__
print(f"\nlen(book1): {len(book1)} sayfa")    # 328 sayfa

# Sıralama (sorted __lt__ kullanır)
books = [book1, book2, book3]
sorted_books = sorted(books)

print("\nSayfa sayısına göre sıralı:")
for book in sorted_books:
    print(f"  {book} - {len(book)} sayfa")

# __repr__ ile nesneyi yeniden oluşturma
book4 = eval(repr(book1))
print(f"\nYeniden oluşturulan: {book4}")


# =============================================================================
# SORU 10: [Zor] Property Decorator
# =============================================================================
# Bir Temperature sınıfı oluşturun.
# Private attribute: __celsius
# Properties:
#   - celsius (getter/setter) -> Validasyon ile (-273.15'den küçük olamaz)
#   - fahrenheit (getter/setter) -> Otomatik dönüşüm
#   - kelvin (getter) -> Sadece okuma
# Property decorator kullanın

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- @property: Getter tanımlar, attribute gibi erişilir
- @attr.setter: Setter tanımlar, validasyon eklenebilir
- Computed properties: fahrenheit ve kelvin hesaplanıyor
- Encapsulation: __celsius private, sadece property ile erişilir
"""

class Temperature:
    """Sıcaklık sınıfı - property decorator örneği"""

    def __init__(self, celsius=0):
        """Sıcaklık başlatma"""
        self.__celsius = celsius  # Private attribute

    @property
    def celsius(self):
        """
        Celsius getter
        Attribute gibi erişilir: temp.celsius
        """
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        """
        Celsius setter (validasyon ile)
        Attribute gibi atanır: temp.celsius = 25
        """
        if value < -273.15:
            raise ValueError("Sıcaklık mutlak sıfırın altında olamaz! (-273.15°C)")
        self.__celsius = value

    @property
    def fahrenheit(self):
        """
        Fahrenheit getter (computed property)
        Celsius'tan otomatik hesaplanır
        """
        return (self.__celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """
        Fahrenheit setter
        Celsius'a çevrilir ve kaydedilir
        """
        celsius = (value - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("Sıcaklık mutlak sıfırın altında olamaz!")
        self.__celsius = celsius

    @property
    def kelvin(self):
        """
        Kelvin getter (computed property, read-only)
        Sadece getter var, setter yok (read-only)
        """
        return self.__celsius + 273.15

    def display_all(self):
        """Tüm birimlerde göster"""
        print(f"Sıcaklık:")
        print(f"  {self.celsius:.2f} °C")
        print(f"  {self.fahrenheit:.2f} °F")
        print(f"  {self.kelvin:.2f} K")

    def __str__(self):
        return f"{self.celsius:.2f}°C / {self.fahrenheit:.2f}°F / {self.kelvin:.2f}K"

# Test
temp = Temperature(25)

# Property getter - attribute gibi erişim
print(f"Celsius: {temp.celsius}°C")        # 25°C
print(f"Fahrenheit: {temp.fahrenheit}°F")  # 77.0°F
print(f"Kelvin: {temp.kelvin}K")           # 298.15K

print("\n" + "="*50 + "\n")

# Property setter - attribute gibi atama
temp.celsius = 30
print(f"Yeni celsius: {temp.celsius}°C")   # 30°C

temp.fahrenheit = 86
print(f"Celsius (F'den): {temp.celsius}°C")  # 30.0°C

print("\n" + "="*50 + "\n")

# Tüm birimlerde göster
temp.display_all()

print("\n" + "="*50 + "\n")

# Validasyon çalışıyor
try:
    temp.celsius = -300  # Mutlak sıfırın altı
except ValueError as e:
    print(f"Hata: {e}")

# Read-only property (kelvin sadece okunabilir)
# temp.kelvin = 300  # AttributeError: can't set attribute

print(temp)  # __str__ metodu


# =============================================================================
# SORU 11: [Challenge] Library Management System
# =============================================================================
# Bir kütüphane yönetim sistemi oluşturun.
#
# LibraryBook sınıfı:
#   - title, author, isbn, copies_available
#   - checkout(), return_book() metodları
#
# Member sınıfı:
#   - name, member_id, borrowed_books (liste)
#   - borrow_book(book), return_book(book)
#
# Library sınıfı:
#   - books (dict), members (dict)
#   - add_book(), add_member()
#   - lend_book(member_id, isbn), return_book(member_id, isbn)
#   - show_available_books()

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Composition: Library, Book ve Member nesnelerini içerir
- Encapsulation: Her sınıf kendi verilerini yönetir
- Interaction: Nesneler birbirleriyle etkileşir
- Real-world example: Gerçek dünya problemi modellemesi
"""

class LibraryBook:
    """Kütüphane kitabı sınıfı"""

    def __init__(self, title, author, isbn, copies_available):
        """Kitap başlatma"""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available
        self.total_copies = copies_available

    def checkout(self):
        """Kitap ödünç al"""
        if self.copies_available > 0:
            self.copies_available -= 1
            return True
        return False

    def return_book(self):
        """Kitap iade et"""
        if self.copies_available < self.total_copies:
            self.copies_available += 1
            return True
        return False

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {self.copies_available}/{self.total_copies} mevcut"


class Member:
    """Kütüphane üyesi sınıfı"""

    def __init__(self, name, member_id):
        """Üye başlatma"""
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # ISBN listesi

    def borrow_book(self, isbn):
        """Kitap ödünç al"""
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)
            return True
        return False

    def return_book(self, isbn):
        """Kitap iade et"""
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True
        return False

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) - {len(self.borrowed_books)} kitap ödünç almış"


class Library:
    """Kütüphane sınıfı - composition örneği"""

    def __init__(self, name):
        """Kütüphane başlatma"""
        self.name = name
        self.books = {}      # ISBN -> LibraryBook
        self.members = {}    # member_id -> Member

    def add_book(self, book):
        """Kütüphaneye kitap ekle"""
        if book.isbn in self.books:
            # Zaten var, kopya sayısını artır
            self.books[book.isbn].total_copies += book.total_copies
            self.books[book.isbn].copies_available += book.copies_available
            return f"'{book.title}' kitabından {book.total_copies} kopya daha eklendi"
        else:
            self.books[book.isbn] = book
            return f"'{book.title}' kütüphaneye eklendi"

    def add_member(self, member):
        """Kütüphaneye üye ekle"""
        if member.member_id in self.members:
            return f"Üye zaten kayıtlı: {member.name}"
        self.members[member.member_id] = member
        return f"Yeni üye kaydedildi: {member.name}"

    def lend_book(self, member_id, isbn):
        """Üyeye kitap ödünç ver"""
        # Üye kontrolü
        if member_id not in self.members:
            return "Üye bulunamadı!"

        # Kitap kontrolü
        if isbn not in self.books:
            return "Kitap bulunamadı!"

        member = self.members[member_id]
        book = self.books[isbn]

        # Müsaitlik kontrolü
        if not book.checkout():
            return f"'{book.title}' şu anda müsait değil"

        # Üyeye kaydet
        member.borrow_book(isbn)
        return f"'{book.title}' {member.name} tarafından ödünç alındı"

    def return_book(self, member_id, isbn):
        """Üyeden kitap iade al"""
        # Üye kontrolü
        if member_id not in self.members:
            return "Üye bulunamadı!"

        # Kitap kontrolü
        if isbn not in self.books:
            return "Kitap bulunamadı!"

        member = self.members[member_id]
        book = self.books[isbn]

        # Üyenin kitabı var mı?
        if not member.return_book(isbn):
            return f"{member.name} bu kitabı ödünç almamış!"

        # Kütüphaneye iade et
        book.return_book()
        return f"'{book.title}' {member.name} tarafından iade edildi"

    def show_available_books(self):
        """Mevcut kitapları göster"""
        print(f"\n{self.name} - Mevcut Kitaplar:")
        print("=" * 70)
        available = False
        for book in self.books.values():
            if book.copies_available > 0:
                print(f"  {book}")
                available = True
        if not available:
            print("  Mevcut kitap yok")

    def show_members(self):
        """Üyeleri göster"""
        print(f"\n{self.name} - Üyeler:")
        print("=" * 70)
        for member in self.members.values():
            print(f"  {member}")
            if member.borrowed_books:
                for isbn in member.borrowed_books:
                    book = self.books.get(isbn)
                    if book:
                        print(f"    - {book.title}")

# Test
library = Library("Şehir Kütüphanesi")

# Kitap ekle
book1 = LibraryBook("1984", "George Orwell", "ISBN-001", 3)
book2 = LibraryBook("Suç ve Ceza", "Dostoyevski", "ISBN-002", 2)
book3 = LibraryBook("Simyacı", "Paulo Coelho", "ISBN-003", 1)

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

# Üye ekle
member1 = Member("Ali Yılmaz", "M001")
member2 = Member("Ayşe Kaya", "M002")

print(library.add_member(member1))
print(library.add_member(member2))

# Kitap ödünç al
print("\n" + "="*70)
print(library.lend_book("M001", "ISBN-001"))  # Ali -> 1984
print(library.lend_book("M001", "ISBN-002"))  # Ali -> Suç ve Ceza
print(library.lend_book("M002", "ISBN-003"))  # Ayşe -> Simyacı

# Mevcut kitapları göster
library.show_available_books()

# Üyeleri göster
library.show_members()

# Kitap iade et
print("\n" + "="*70)
print(library.return_book("M001", "ISBN-001"))  # Ali 1984'ü iade etti

# Güncel durum
library.show_available_books()


# =============================================================================
# SORU 12: [Challenge] Multi-Level Inheritance
# =============================================================================
# Bir çalışan hiyerarşisi oluşturun:
#
# Person (base):
#   - name, age, email
#
# Employee (Person'dan türer):
#   - employee_id, salary, department
#   - give_raise(percent)
#
# Manager (Employee'dan türer):
#   - team_members (liste)
#   - add_team_member(), remove_team_member()
#   - get_team_salary_total()
#
# Her seviyede __str__ metodunu override edin

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Multi-level inheritance: Person -> Employee -> Manager
- super().__init__() ile her seviyede parent constructor çağrılır
- Method overriding: Her seviye __str__ metodunu override ediyor
- Composition: Manager, Employee nesnelerini içerir (team_members)
"""

# Level 1: Base class
class Person:
    """Kişi base class"""

    def __init__(self, name, age, email):
        """Kişi başlatma"""
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.age}) - {self.email}"


# Level 2: Employee
class Employee(Person):
    """Çalışan - Person'dan türetildi"""

    # Class variable
    employee_count = 0

    def __init__(self, name, age, email, employee_id, salary, department):
        """Çalışan başlatma"""
        # Parent constructor
        super().__init__(name, age, email)

        # Employee attributes
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

        Employee.employee_count += 1

    def give_raise(self, percent):
        """Maaşa zam uygula"""
        old_salary = self.salary
        self.salary = int(self.salary * (1 + percent / 100))
        return f"{self.name} - Maaş: {old_salary} TL -> {self.salary} TL (%{percent} zam)"

    def __str__(self):
        # Parent __str__ kullan ve genişlet
        person_info = super().__str__()
        return f"{person_info}\nÇalışan ID: {self.employee_id}, Maaş: {self.salary} TL, Departman: {self.department}"


# Level 3: Manager
class Manager(Employee):
    """Yönetici - Employee'dan türetildi"""

    def __init__(self, name, age, email, employee_id, salary, department, team_name):
        """Yönetici başlatma"""
        # Parent constructor
        super().__init__(name, age, email, employee_id, salary, department)

        # Manager attributes
        self.team_name = team_name
        self.team_members = []  # Employee listesi

    def add_team_member(self, employee):
        """Takıma üye ekle"""
        if not isinstance(employee, Employee):
            return "Sadece Employee nesneleri eklenebilir!"

        if employee in self.team_members:
            return f"{employee.name} zaten takımda!"

        self.team_members.append(employee)
        return f"{employee.name} {self.team_name} takımına eklendi"

    def remove_team_member(self, employee):
        """Takımdan üye çıkar"""
        if employee in self.team_members:
            self.team_members.remove(employee)
            return f"{employee.name} {self.team_name} takımından çıkarıldı"
        return f"{employee.name} takımda değil!"

    def get_team_salary_total(self):
        """Takımın toplam maaş maliyeti (yönetici dahil değil)"""
        return sum(emp.salary for emp in self.team_members)

    def show_team(self):
        """Takım üyelerini göster"""
        print(f"\n{self.team_name} Takımı (Yönetici: {self.name})")
        print("=" * 60)
        for emp in self.team_members:
            print(f"  {emp.name} ({emp.department}) - {emp.salary} TL")
        print(f"\nToplam Maaş: {self.get_team_salary_total()} TL")

    def __str__(self):
        # Parent __str__ kullan ve genişlet
        employee_info = super().__str__()
        return f"{employee_info}\nYönetici - Takım: {self.team_name} ({len(self.team_members)} üye)"


# Test
print("=== MULTI-LEVEL INHERITANCE ===\n")

# Person nesnesi
person = Person("Zeynep Demir", 22, "zeynep@example.com")
print("Person:")
print(person)
print()

# Employee nesnesi
emp1 = Employee("Ali Yılmaz", 28, "ali@example.com", "E001", 15000, "IT")
emp2 = Employee("Ayşe Kaya", 25, "ayse@example.com", "E002", 12000, "IT")
emp3 = Employee("Mehmet Öz", 30, "mehmet@example.com", "E003", 14000, "IT")

print("Employee:")
print(emp1)
print()

# Manager nesnesi
manager = Manager("Fatma Aksoy", 35, "fatma@example.com", "M001", 25000, "IT", "Development Team")

print("Manager:")
print(manager)
print()

# Takım oluştur
print(manager.add_team_member(emp1))
print(manager.add_team_member(emp2))
print(manager.add_team_member(emp3))

# Takımı göster
manager.show_team()

# Zam ver
print("\n" + "="*60)
print(emp1.give_raise(10))  # %10 zam
print(emp2.give_raise(15))  # %15 zam

# Güncel takım
manager.show_team()

# isinstance kontrolü
print("\n" + "="*60)
print(f"manager, Manager mi? {isinstance(manager, Manager)}")      # True
print(f"manager, Employee mi? {isinstance(manager, Employee)}")    # True
print(f"manager, Person mi? {isinstance(manager, Person)}")        # True
print(f"emp1, Manager mi? {isinstance(emp1, Manager)}")            # False


# =============================================================================
# SORU 13: [Challenge] Operator Overloading
# =============================================================================
# Bir Money sınıfı oluşturun (para birimi ile).
# Attributes: amount, currency
# Special methods:
#   - __add__, __sub__ -> Para toplama/çıkarma (aynı para birimi gerekli)
#   - __mul__, __truediv__ -> Skaler çarpma/bölme
#   - __eq__, __lt__, __gt__ -> Karşılaştırma
#   - __str__, __repr__
#   - __abs__ -> Mutlak değer

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Operator overloading: Operatörleri (+, -, *, /, ==, <, >) yeniden tanımlama
- __add__, __sub__: Aritmetik operatörler
- __eq__, __lt__, __gt__: Karşılaştırma operatörleri
- __abs__: Mutlak değer (abs())
- Validasyon: Para birimi kontrolü
"""

class Money:
    """Para sınıfı - operator overloading"""

    def __init__(self, amount, currency="TRY"):
        """
        Para başlatma

        Args:
            amount (float): Tutar
            currency (str): Para birimi (TRY, USD, EUR, vb.)
        """
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        """Toplama (+)"""
        if not isinstance(other, Money):
            raise TypeError("Money nesnesi ile toplanabilir")

        if self.currency != other.currency:
            raise ValueError(f"Farklı para birimleri toplanamaz: {self.currency} ve {other.currency}")

        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        """Çıkarma (-)"""
        if not isinstance(other, Money):
            raise TypeError("Money nesnesi ile çıkarılabilir")

        if self.currency != other.currency:
            raise ValueError(f"Farklı para birimleri çıkarılamaz: {self.currency} ve {other.currency}")

        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, scalar):
        """Skaler çarpma (*)"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Sadece sayı ile çarpılabilir")

        return Money(self.amount * scalar, self.currency)

    def __rmul__(self, scalar):
        """Sağdan çarpma (scalar * money)"""
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        """Skaler bölme (/)"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Sadece sayıya bölünebilir")

        if scalar == 0:
            raise ValueError("Sıfıra bölünemez")

        return Money(self.amount / scalar, self.currency)

    def __eq__(self, other):
        """Eşitlik (==)"""
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        """Küçüktür (<)"""
        if not isinstance(other, Money):
            raise TypeError("Money nesnesi ile karşılaştırılabilir")

        if self.currency != other.currency:
            raise ValueError(f"Farklı para birimleri karşılaştırılamaz")

        return self.amount < other.amount

    def __le__(self, other):
        """Küçük eşit (<=)"""
        return self == other or self < other

    def __gt__(self, other):
        """Büyüktür (>)"""
        if not isinstance(other, Money):
            raise TypeError("Money nesnesi ile karşılaştırılabilir")

        if self.currency != other.currency:
            raise ValueError(f"Farklı para birimleri karşılaştırılamaz")

        return self.amount > other.amount

    def __ge__(self, other):
        """Büyük eşit (>=)"""
        return self == other or self > other

    def __abs__(self):
        """Mutlak değer"""
        return Money(abs(self.amount), self.currency)

    def __str__(self):
        """User-friendly string"""
        return f"{self.amount:.2f} {self.currency}"

    def __repr__(self):
        """Developer-friendly string"""
        return f"Money({self.amount}, '{self.currency}')"

# Test
print("\n=== OPERATOR OVERLOADING ===\n")

# Para nesneleri oluştur
money1 = Money(100, "TRY")
money2 = Money(50, "TRY")
money3 = Money(75, "USD")

# __str__ ve __repr__
print(str(money1))   # 100.00 TRY
print(repr(money1))  # Money(100, 'TRY')

# Aritmetik işlemler
print("\nAritmetik İşlemler:")
print(f"{money1} + {money2} = {money1 + money2}")  # 150.00 TRY
print(f"{money1} - {money2} = {money1 - money2}")  # 50.00 TRY
print(f"{money1} * 2 = {money1 * 2}")              # 200.00 TRY
print(f"2 * {money1} = {2 * money1}")              # 200.00 TRY
print(f"{money1} / 4 = {money1 / 4}")              # 25.00 TRY

# Karşılaştırma
print("\nKarşılaştırma:")
print(f"{money1} == {money2}? {money1 == money2}")  # False
print(f"{money1} > {money2}? {money1 > money2}")    # True
print(f"{money1} < {money2}? {money1 < money2}")    # False

# Mutlak değer
money4 = Money(-50, "TRY")
print(f"\nabs({money4}) = {abs(money4)}")  # 50.00 TRY

# Hata durumları
print("\nHata Durumları:")
try:
    result = money1 + money3  # Farklı para birimleri
except ValueError as e:
    print(f"Hata: {e}")

try:
    result = money1 > money3  # Farklı para birimleri
except ValueError as e:
    print(f"Hata: {e}")


# =============================================================================
# SORU 14: [Challenge] Composition vs Inheritance
# =============================================================================
# Bir şirket organizasyonu modelleyin.
#
# Address sınıfı: street, city, country
# Phone sınıfı: country_code, number
#
# Company sınıfı:
#   - Composition ile Address ve Phone içersin
#   - name, address, phones (liste)
#   - add_phone(), get_main_address()
#
# Employee sınıfı:
#   - name, address, phones (liste)
#   - company (Company referansı)

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Composition: "has-a" ilişkisi (Company has Address, has Phones)
- Aggregation: Employee, Company'ye referans tutuyor
- Encapsulation: Her sınıf kendi verilerini yönetiyor
- Real-world modeling: Gerçek dünya ilişkilerini modelleme
"""

class Address:
    """Adres sınıfı"""

    def __init__(self, street, city, country):
        """Adres başlatma"""
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

    def __repr__(self):
        return f"Address('{self.street}', '{self.city}', '{self.country}')"


class Phone:
    """Telefon sınıfı"""

    def __init__(self, country_code, number, phone_type="mobile"):
        """Telefon başlatma"""
        self.country_code = country_code
        self.number = number
        self.phone_type = phone_type  # mobile, home, work

    def __str__(self):
        return f"+{self.country_code} {self.number} ({self.phone_type})"

    def __repr__(self):
        return f"Phone({self.country_code}, '{self.number}', '{self.phone_type}')"


class Company:
    """Şirket sınıfı - composition örneği"""

    def __init__(self, name, address):
        """
        Şirket başlatma

        Args:
            name (str): Şirket adı
            address (Address): Şirket adresi
        """
        self.name = name
        self.address = address  # Composition: Company HAS-A Address
        self.phones = []        # Phone listesi
        self.employees = []     # Employee listesi

    def add_phone(self, phone):
        """Telefon ekle"""
        if not isinstance(phone, Phone):
            raise TypeError("Phone nesnesi gerekli")
        self.phones.append(phone)

    def get_main_address(self):
        """Ana adres"""
        return self.address

    def add_employee(self, employee):
        """Çalışan ekle"""
        if employee not in self.employees:
            self.employees.append(employee)

    def __str__(self):
        phones_str = ", ".join(str(p) for p in self.phones)
        return f"{self.name}\n  Adres: {self.address}\n  Telefonlar: {phones_str}"


class Employee:
    """Çalışan sınıfı - aggregation örneği"""

    def __init__(self, name, address, company=None):
        """
        Çalışan başlatma

        Args:
            name (str): Çalışan adı
            address (Address): Çalışan adresi
            company (Company, optional): Çalıştığı şirket
        """
        self.name = name
        self.address = address  # Composition: Employee HAS-A Address
        self.company = company  # Aggregation: Employee referansı Company'ye
        self.phones = []        # Phone listesi

        # Şirkete kendini ekle
        if company:
            company.add_employee(self)

    def add_phone(self, phone):
        """Telefon ekle"""
        if not isinstance(phone, Phone):
            raise TypeError("Phone nesnesi gerekli")
        self.phones.append(phone)

    def __str__(self):
        company_name = self.company.name if self.company else "Şirket yok"
        phones_str = ", ".join(str(p) for p in self.phones)
        return f"{self.name} ({company_name})\n  Adres: {self.address}\n  Telefonlar: {phones_str}"


# Test
print("\n=== COMPOSİTİON vs İNHERİTANCE ===\n")

# Şirket oluştur
company_address = Address("Levent", "İstanbul", "Türkiye")
company = Company("TechCorp", company_address)
company.add_phone(Phone(90, "212-555-0000", "work"))
company.add_phone(Phone(90, "212-555-0001", "work"))

print("Şirket:")
print(company)
print()

# Çalışanlar oluştur
emp1_address = Address("Kadıköy", "İstanbul", "Türkiye")
emp1 = Employee("Ali Yılmaz", emp1_address, company)
emp1.add_phone(Phone(90, "532-555-1111", "mobile"))

emp2_address = Address("Çankaya", "Ankara", "Türkiye")
emp2 = Employee("Ayşe Kaya", emp2_address, company)
emp2.add_phone(Phone(90, "555-555-2222", "mobile"))

print("Çalışan 1:")
print(emp1)
print()

print("Çalışan 2:")
print(emp2)
print()

# Şirketin çalışanları
print(f"{company.name} Çalışanları:")
print("=" * 50)
for emp in company.employees:
    print(f"  {emp.name} - {emp.address.city}")


# =============================================================================
# SORU 15: [Challenge] Design Pattern - Singleton
# =============================================================================
# Singleton pattern uygulayın.
# DatabaseConnection sınıfı oluşturun:
#   - Sadece bir instance oluşturulabilsin
#   - __new__ metodunu override edin
#   - connect(), disconnect(), execute_query() metodları

# TODO: Kodunuzu buraya yazın




# ÇÖZÜM:
"""
Açıklama:
- Singleton pattern: Bir sınıftan sadece bir nesne oluşturulabilir
- __new__ metodu override edilir
- Class variable ile instance saklanır
- Use case: Database bağlantısı, logger, configuration
"""

class DatabaseConnection:
    """Database connection - Singleton pattern"""

    # Class variable - tek instance
    _instance = None
    _initialized = False

    def __new__(cls):
        """
        __new__ metodu override - sadece bir instance oluştur
        """
        if cls._instance is None:
            print("Yeni database connection oluşturuluyor...")
            cls._instance = super().__new__(cls)
        else:
            print("Mevcut database connection kullanılıyor...")
        return cls._instance

    def __init__(self):
        """
        __init__ her çağrıda çalışır ama __new__ sadece bir kez
        """
        # İlk kez mi başlatılıyor?
        if not DatabaseConnection._initialized:
            print("Database bağlantısı başlatılıyor...")
            self.host = "localhost"
            self.port = 5432
            self.database = "mydb"
            self.connected = False
            self.queries_executed = 0
            DatabaseConnection._initialized = True

    def connect(self):
        """Veritabanına bağlan"""
        if self.connected:
            return "Zaten bağlı!"

        print(f"Bağlanılıyor: {self.host}:{self.port}/{self.database}")
        self.connected = True
        return "Bağlantı başarılı"

    def disconnect(self):
        """Bağlantıyı kes"""
        if not self.connected:
            return "Bağlantı yok!"

        print("Bağlantı kesiliyor...")
        self.connected = False
        return "Bağlantı kesildi"

    def execute_query(self, query):
        """Sorgu çalıştır"""
        if not self.connected:
            return "Hata: Önce bağlan!"

        self.queries_executed += 1
        return f"Sorgu çalıştırıldı: {query} (Toplam: {self.queries_executed})"

    def get_stats(self):
        """İstatistikleri göster"""
        return {
            "connected": self.connected,
            "queries_executed": self.queries_executed,
            "host": self.host,
            "database": self.database
        }

    def __str__(self):
        status = "Bağlı" if self.connected else "Bağlı değil"
        return f"DatabaseConnection ({status}) - {self.queries_executed} sorgu çalıştırıldı"


# Test
print("\n=== SİNGLETON PATTERN ===\n")

# İlk instance
db1 = DatabaseConnection()
print(db1.connect())

# İkinci instance (aslında aynı nesne)
db2 = DatabaseConnection()
print(db2.connect())  # Zaten bağlı!

# Aynı nesne mi?
print(f"\ndb1 is db2? {db1 is db2}")  # True
print(f"id(db1) == id(db2)? {id(db1) == id(db2)}")  # True

# db2 üzerinden sorgu çalıştır
print(db2.execute_query("SELECT * FROM users"))
print(db2.execute_query("SELECT * FROM products"))

# db1 üzerinden istatistikleri gör (aynı nesne!)
print(f"\ndb1 stats: {db1.get_stats()}")
print(f"db2 stats: {db2.get_stats()}")

print(db1)
print(db2)

# Bağlantıyı kes
print(db1.disconnect())


# =============================================================================
# ALIŞTIRMALARIN SONU
# =============================================================================

print("\n" + "="*70)
print("TEBRİKLER! TÜM OOP ALIŞTIRMALARINI TAMAMLADINIZ!")
print("="*70)
print("\nBu bölümde şunları öğrendiniz:")
print("✓ Class ve Object kavramları")
print("✓ __init__ constructor ve instance variables")
print("✓ Instance methods, class methods, static methods")
print("✓ Class variables ve instance variables farkı")
print("✓ Inheritance (kalıtım) ve super() kullanımı")
print("✓ Polymorphism (çok biçimlilik)")
print("✓ Encapsulation (kapsülleme) ve private attributes")
print("✓ Special methods (__str__, __repr__, __eq__, vb.)")
print("✓ Operator overloading (__add__, __sub__, vb.)")
print("✓ Property decorators (@property)")
print("✓ Composition vs Inheritance")
print("✓ Design Patterns (Singleton)")
print("✓ Real-world applications (Bank, Library, Company)")
print("\nArtık Python OOP konusunda uzman seviyesiniz!")
print("="*70)
