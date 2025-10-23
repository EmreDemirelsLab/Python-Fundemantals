# Object-Oriented Programming (Nesne Yönelimli Programlama)

## İçindekiler
1. [OOP Nedir?](#oop-nedir)
2. [Class (Sınıf) Tanımlama](#class-sınıf-tanımlama)
3. [Object (Nesne) Oluşturma](#object-nesne-oluşturma)
4. [__init__ Constructor](#__init__-constructor)
5. [Instance Variables (Örnek Değişkenler)](#instance-variables-örnek-değişkenler)
6. [Instance Methods (Örnek Metodlar)](#instance-methods-örnek-metodlar)
7. [Class Variables (Sınıf Değişkenleri)](#class-variables-sınıf-değişkenleri)
8. [Class Methods ve Static Methods](#class-methods-ve-static-methods)
9. [Inheritance (Kalıtım)](#inheritance-kalıtım)
10. [Polymorphism (Çok Biçimlilik)](#polymorphism-çok-biçimlilik)
11. [Encapsulation (Kapsülleme)](#encapsulation-kapsülleme)
12. [Special Methods (Özel Metodlar)](#special-methods-özel-metodlar)
13. [Property Decorators](#property-decorators)

---

## OOP Nedir?

Object-Oriented Programming (OOP), programlamada nesneler kavramını merkeze alan bir programlama paradigmasıdır. Gerçek dünyayı modellemek için kullanılır ve kodun yeniden kullanılabilirliğini, modülerliğini ve bakımını kolaylaştırır.

**OOP'nin 4 Temel İlkesi:**
1. **Encapsulation (Kapsülleme)**: Veri ve metodları bir arada tutma
2. **Inheritance (Kalıtım)**: Mevcut sınıflardan yeni sınıflar türetme
3. **Polymorphism (Çok Biçimlilik)**: Aynı arayüzle farklı davranışlar sergileme
4. **Abstraction (Soyutlama)**: Karmaşıklığı gizleme, sadece gerekli bilgiyi gösterme

**OOP'nin Avantajları:**
- Kod tekrarını azaltır
- Daha organize ve modüler kod yapısı
- Gerçek dünya problemlerini modellemeyi kolaylaştırır
- Bakım ve güncelleme kolaylığı
- Takım çalışmasına uygun
- Test edilebilirlik

---

## Class (Sınıf) Tanımlama

Class, nesneler için bir şablon veya plan (blueprint) gibidir. Bir sınıf, o türdeki nesnelerin sahip olacağı özellikleri (attributes) ve davranışları (methods) tanımlar.

### Örnek 1: En Basit Sınıf

```python
# Boş bir sınıf tanımlama
class Person:
    """Basit bir Person sınıfı"""
    pass  # Geçici olarak boş bırakmak için

# Sınıftan nesne oluşturma
person1 = Person()
person2 = Person()

print(type(person1))  # <class '__main__.Person'>
print(isinstance(person1, Person))  # True
```

### Örnek 2: Attribute'lü Sınıf

```python
class Dog:
    """Köpek sınıfı - temel özellikler"""

    # Sınıf attribute'u (tüm nesneler için ortak)
    species = "Canis familiaris"

    def bark(self):
        """Köpek havlar"""
        print("Hav hav!")

# Nesne oluşturma
dog1 = Dog()
dog2 = Dog()

# Sınıf attribute'una erişim
print(dog1.species)  # Canis familiaris
print(Dog.species)   # Canis familiaris

# Method çağırma
dog1.bark()  # Hav hav!
```

---

## Object (Nesne) Oluşturma

Nesne, bir sınıfın somut bir örneğidir (instance). Sınıf şablondur, nesne ise o şablondan üretilen gerçek varlıktır.

### Örnek 3: Birden Fazla Nesne Oluşturma

```python
class Car:
    """Araba sınıfı"""

    def __init__(self, brand, model, year):
        """Constructor - nesne oluşturulurken çalışır"""
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """Araba bilgilerini gösterir"""
        print(f"{self.year} {self.brand} {self.model}")

# Farklı nesneler oluşturma
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Ford", "Mustang", 2022)

# Her nesne bağımsızdır
car1.display_info()  # 2020 Toyota Corolla
car2.display_info()  # 2021 Honda Civic
car3.display_info()  # 2022 Ford Mustang
```

---

## __init__ Constructor

`__init__` metodu, nesne oluşturulduğunda otomatik olarak çağrılan özel bir metoddur. Constructor (yapıcı metod) olarak bilinir ve nesnenin başlangıç durumunu ayarlamak için kullanılır.

### Örnek 4: Constructor ile Başlangıç Değerleri

```python
class Student:
    """Öğrenci sınıfı"""

    def __init__(self, name, age, student_id):
        """
        Öğrenci nesnesini başlatır

        Args:
            name (str): Öğrenci adı
            age (int): Öğrenci yaşı
            student_id (str): Öğrenci numarası
        """
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []  # Boş liste ile başlat

        print(f"Yeni öğrenci oluşturuldu: {name}")

    def add_grade(self, grade):
        """Not ekler"""
        self.grades.append(grade)

    def get_average(self):
        """Not ortalamasını hesaplar"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Nesne oluşturulurken __init__ otomatik çağrılır
student1 = Student("Ali Yılmaz", 20, "12345")
# Output: Yeni öğrenci oluşturuldu: Ali Yılmaz

student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

print(f"Ortalama: {student1.get_average():.2f}")  # 84.33
```

### Örnek 5: Default Parametreli Constructor

```python
class Book:
    """Kitap sınıfı"""

    def __init__(self, title, author, pages=0, isbn=None):
        """
        Kitap nesnesini başlatır

        Args:
            title (str): Kitap başlığı
            author (str): Yazar adı
            pages (int, optional): Sayfa sayısı. Defaults to 0.
            isbn (str, optional): ISBN numarası. Defaults to None.
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_read = False

    def mark_as_read(self):
        """Kitabı okundu olarak işaretle"""
        self.is_read = True

    def __str__(self):
        """String representasyonu"""
        status = "Okundu" if self.is_read else "Okunmadı"
        return f"'{self.title}' - {self.author} ({status})"

# Farklı şekillerde oluşturma
book1 = Book("1984", "George Orwell")
book2 = Book("Suç ve Ceza", "Dostoyevski", pages=671)
book3 = Book("Simyacı", "Paulo Coelho", pages=208, isbn="978-0062315007")

print(book1)  # '1984' - George Orwell (Okunmadı)
book1.mark_as_read()
print(book1)  # '1984' - George Orwell (Okundu)
```

---

## Instance Variables (Örnek Değişkenler)

Instance variables, her nesneye özgü değişkenlerdir. Her nesne kendi instance variable'larına sahiptir.

### Örnek 6: Instance Variables

```python
class BankAccount:
    """Banka hesabı sınıfı"""

    def __init__(self, owner, balance=0):
        """Hesap başlatma"""
        self.owner = owner        # Instance variable
        self.balance = balance    # Instance variable
        self.transactions = []    # Instance variable

    def deposit(self, amount):
        """Para yatırma"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"+{amount}")
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL")
        else:
            print("Geçersiz tutar!")

    def withdraw(self, amount):
        """Para çekme"""
        if amount > self.balance:
            print("Yetersiz bakiye!")
        elif amount > 0:
            self.balance -= amount
            self.transactions.append(f"-{amount}")
            print(f"{amount} TL çekildi. Yeni bakiye: {self.balance} TL")
        else:
            print("Geçersiz tutar!")

    def get_balance(self):
        """Bakiye sorgulama"""
        return self.balance

# Her hesap bağımsız instance variable'lara sahip
account1 = BankAccount("Ali Yılmaz", 1000)
account2 = BankAccount("Ayşe Kaya", 500)

account1.deposit(500)   # 500 TL yatırıldı. Yeni bakiye: 1500 TL
account2.withdraw(200)  # 200 TL çekildi. Yeni bakiye: 300 TL

print(f"{account1.owner}: {account1.balance} TL")  # Ali Yılmaz: 1500 TL
print(f"{account2.owner}: {account2.balance} TL")  # Ayşe Kaya: 300 TL
```

---

## Instance Methods (Örnek Metodlar)

Instance methods, nesneler üzerinde çalışan fonksiyonlardır. İlk parametreleri her zaman `self`'tir.

### Örnek 7: Instance Methods

```python
class Rectangle:
    """Dikdörtgen sınıfı"""

    def __init__(self, width, height):
        """Dikdörtgen başlatma"""
        self.width = width
        self.height = height

    def area(self):
        """Alan hesapla"""
        return self.width * self.height

    def perimeter(self):
        """Çevre hesapla"""
        return 2 * (self.width + self.height)

    def is_square(self):
        """Kare mi kontrol et"""
        return self.width == self.height

    def scale(self, factor):
        """Boyutları ölçekle"""
        self.width *= factor
        self.height *= factor

    def display_info(self):
        """Bilgileri göster"""
        print(f"Dikdörtgen: {self.width} x {self.height}")
        print(f"  Alan: {self.area()}")
        print(f"  Çevre: {self.perimeter()}")
        print(f"  Kare mi? {'Evet' if self.is_square() else 'Hayır'}")

# Kullanım
rect = Rectangle(10, 5)
rect.display_info()
# Output:
# Dikdörtgen: 10 x 5
#   Alan: 50
#   Çevre: 30
#   Kare mi? Hayır

rect.scale(2)  # 2 kat büyüt
rect.display_info()
# Output:
# Dikdörtgen: 20 x 10
#   Alan: 200
#   Çevre: 60
#   Kare mi? Hayır

square = Rectangle(5, 5)
print(f"Kare mi? {square.is_square()}")  # True
```

### Örnek 8: Metodların Birbirini Çağırması

```python
class Temperature:
    """Sıcaklık sınıfı"""

    def __init__(self, celsius=0):
        """Celsius olarak başlat"""
        self.celsius = celsius

    def to_fahrenheit(self):
        """Fahrenheit'a çevir"""
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        """Kelvin'e çevir"""
        return self.celsius + 273.15

    def set_fahrenheit(self, fahrenheit):
        """Fahrenheit değerini ayarla"""
        self.celsius = (fahrenheit - 32) * 5/9

    def display_all(self):
        """Tüm birimlerde göster"""
        print(f"Sıcaklık:")
        print(f"  {self.celsius:.2f} °C")
        print(f"  {self.to_fahrenheit():.2f} °F")
        print(f"  {self.to_kelvin():.2f} K")

# Kullanım
temp = Temperature(25)
temp.display_all()
# Output:
# Sıcaklık:
#   25.00 °C
#   77.00 °F
#   298.15 K

temp.set_fahrenheit(86)
temp.display_all()
# Output:
# Sıcaklık:
#   30.00 °C
#   86.00 °F
#   303.15 K
```

---

## Class Variables (Sınıf Değişkenleri)

Class variables, sınıfın tüm nesneleri tarafından paylaşılan değişkenlerdir. Sınıf seviyesinde tanımlanır.

### Örnek 9: Class Variables vs Instance Variables

```python
class Employee:
    """Çalışan sınıfı"""

    # Class variable - tüm çalışanlar için ortak
    company_name = "TechCorp"
    employee_count = 0
    raise_percentage = 1.05  # %5 zam

    def __init__(self, name, salary):
        """Çalışan başlatma"""
        # Instance variables - her çalışana özgü
        self.name = name
        self.salary = salary

        # Class variable'ı güncelle
        Employee.employee_count += 1

    def apply_raise(self):
        """Maaşa zam uygula"""
        self.salary = int(self.salary * Employee.raise_percentage)

    def display_info(self):
        """Bilgileri göster"""
        print(f"Çalışan: {self.name}")
        print(f"Şirket: {Employee.company_name}")
        print(f"Maaş: {self.salary} TL")

# Nesneler oluştur
emp1 = Employee("Ali Yılmaz", 10000)
emp2 = Employee("Ayşe Kaya", 12000)
emp3 = Employee("Mehmet Demir", 15000)

# Class variable tüm nesneler için ortaktır
print(f"Toplam çalışan: {Employee.employee_count}")  # 3
print(f"Şirket: {emp1.company_name}")  # TechCorp

# Class variable'ı değiştir (tüm nesneler etkilenir)
Employee.raise_percentage = 1.10  # %10 zam

emp1.apply_raise()
emp2.apply_raise()

emp1.display_info()
# Output:
# Çalışan: Ali Yılmaz
# Şirket: TechCorp
# Maaş: 11000 TL
```

### Örnek 10: Instance Variable ile Class Variable Karışımı

```python
class Pizza:
    """Pizza sınıfı"""

    # Class variables
    menu = {
        "Margherita": 50,
        "Pepperoni": 60,
        "Vegetarian": 55,
        "BBQ Chicken": 65
    }
    total_orders = 0

    def __init__(self, pizza_type, size="Medium"):
        """Pizza siparişi"""
        self.pizza_type = pizza_type
        self.size = size
        self.toppings = []

        Pizza.total_orders += 1
        self.order_number = Pizza.total_orders

    def add_topping(self, topping):
        """Malzeme ekle"""
        self.toppings.append(topping)

    def calculate_price(self):
        """Fiyat hesapla"""
        base_price = Pizza.menu.get(self.pizza_type, 50)

        # Boyuta göre çarpan
        size_multiplier = {
            "Small": 0.8,
            "Medium": 1.0,
            "Large": 1.3
        }

        price = base_price * size_multiplier.get(self.size, 1.0)
        price += len(self.toppings) * 5  # Her malzeme +5 TL

        return price

    def display_order(self):
        """Sipariş detayları"""
        print(f"Sipariş #{self.order_number}")
        print(f"  Pizza: {self.pizza_type} ({self.size})")
        if self.toppings:
            print(f"  Ekstra malzemeler: {', '.join(self.toppings)}")
        print(f"  Fiyat: {self.calculate_price()} TL")

# Siparişler
order1 = Pizza("Margherita", "Large")
order1.add_topping("Zeytin")
order1.add_topping("Mantar")

order2 = Pizza("Pepperoni", "Medium")
order2.add_topping("Biber")

order1.display_order()
# Output:
# Sipariş #1
#   Pizza: Margherita (Large)
#   Ekstra malzemeler: Zeytin, Mantar
#   Fiyat: 75.0 TL

order2.display_order()
# Output:
# Sipariş #2
#   Pizza: Pepperoni (Medium)
#   Ekstra malzemeler: Biber
#   Fiyat: 65 TL

print(f"\nToplam sipariş: {Pizza.total_orders}")  # 2
```

---

## Class Methods ve Static Methods

Class methods ve static methods, sınıfla ilgili ancak instance'a bağlı olmayan metodlardır.

### Örnek 11: Class Methods (@classmethod)

```python
class Date:
    """Tarih sınıfı"""

    def __init__(self, day, month, year):
        """Tarih başlatma"""
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        """String'den tarih oluştur (factory method)"""
        day, month, year = map(int, date_string.split('-'))
        return cls(day, month, year)

    @classmethod
    def today(cls):
        """Bugünün tarihini döndür"""
        import datetime
        today = datetime.date.today()
        return cls(today.day, today.month, today.year)

    def display(self):
        """Tarihi göster"""
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

# Normal kullanım
date1 = Date(25, 10, 2024)
print(date1.display())  # 25/10/2024

# Class method ile oluşturma
date2 = Date.from_string("15-03-2024")
print(date2.display())  # 15/03/2024

# Bugünün tarihi
date3 = Date.today()
print(date3.display())  # Bugünün tarihi
```

### Örnek 12: Static Methods (@staticmethod)

```python
class MathOperations:
    """Matematiksel işlemler sınıfı"""

    @staticmethod
    def add(a, b):
        """Toplama (static method)"""
        return a + b

    @staticmethod
    def is_even(number):
        """Çift mi kontrol et"""
        return number % 2 == 0

    @staticmethod
    def factorial(n):
        """Faktöriyel hesapla"""
        if n == 0 or n == 1:
            return 1
        return n * MathOperations.factorial(n - 1)

    @staticmethod
    def is_prime(number):
        """Asal sayı mı kontrol et"""
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

# Static method'lar nesne oluşturmadan çağrılabilir
print(f"5 + 3 = {MathOperations.add(5, 3)}")  # 8
print(f"10 çift mi? {MathOperations.is_even(10)}")  # True
print(f"5! = {MathOperations.factorial(5)}")  # 120
print(f"17 asal mı? {MathOperations.is_prime(17)}")  # True

# Nesne üzerinden de çağrılabilir (ama gerekli değil)
math = MathOperations()
print(math.add(10, 20))  # 30
```

### Örnek 13: Instance, Class ve Static Methods Karşılaştırması

```python
class Calculator:
    """Hesap makinesi sınıfı - üç metod tipini gösterir"""

    # Class variable
    pi = 3.14159

    def __init__(self, name):
        """Instance başlatma"""
        self.name = name  # Instance variable
        self.history = []  # İşlem geçmişi

    # Instance method - self kullanır
    def add_to_history(self, operation):
        """İşlem geçmişine ekle"""
        self.history.append(operation)
        return operation

    # Class method - cls kullanır
    @classmethod
    def circle_area(cls, radius):
        """Daire alanı hesapla (class method)"""
        return cls.pi * radius ** 2

    # Static method - self/cls kullanmaz
    @staticmethod
    def is_positive(number):
        """Pozitif mi kontrol et (static method)"""
        return number > 0

    def calculate(self, a, b, operation):
        """Hesaplama yap ve geçmişe ekle"""
        if operation == "add":
            result = a + b
        elif operation == "multiply":
            result = a * b
        else:
            result = None

        self.add_to_history(f"{a} {operation} {b} = {result}")
        return result

# Instance method kullanımı
calc = Calculator("Hesap Makinesi 1")
calc.calculate(5, 3, "add")
calc.calculate(4, 7, "multiply")
print(calc.history)  # ['5 add 3 = 8', '4 multiply 7 = 28']

# Class method kullanımı (nesne olmadan)
area = Calculator.circle_area(5)
print(f"Daire alanı: {area:.2f}")  # 78.54

# Static method kullanımı (nesne olmadan)
print(f"10 pozitif mi? {Calculator.is_positive(10)}")  # True
print(f"-5 pozitif mi? {Calculator.is_positive(-5)}")  # False
```

---

## Inheritance (Kalıtım)

Inheritance, bir sınıfın başka bir sınıftan özellik ve davranışları devralmasıdır. Kod tekrarını önler ve hiyerarşik ilişkiler kurar.

### Örnek 14: Basit Kalıtım

```python
# Parent class (Base class)
class Animal:
    """Hayvan base class"""

    def __init__(self, name, age):
        """Hayvan başlatma"""
        self.name = name
        self.age = age

    def speak(self):
        """Ses çıkar"""
        return "Hayvan ses çıkarıyor"

    def info(self):
        """Bilgi göster"""
        return f"{self.name}, {self.age} yaşında"

# Child class (Derived class)
class Dog(Animal):
    """Köpek - Animal'dan türetildi"""

    def speak(self):
        """Ses çıkar (override edildi)"""
        return "Hav hav!"

    def fetch(self):
        """Köpeğe özgü davranış"""
        return f"{self.name} topu getiriyor"

class Cat(Animal):
    """Kedi - Animal'dan türetildi"""

    def speak(self):
        """Ses çıkar (override edildi)"""
        return "Miyav!"

    def scratch(self):
        """Kediye özgü davranış"""
        return f"{self.name} tırmalıyor"

# Kullanım
dog = Dog("Karabaş", 3)
cat = Cat("Pamuk", 2)

print(dog.info())    # Karabaş, 3 yaşında (parent'tan geldi)
print(dog.speak())   # Hav hav! (override edildi)
print(dog.fetch())   # Karabaş topu getiriyor

print(cat.info())    # Pamuk, 2 yaşında (parent'tan geldi)
print(cat.speak())   # Miyav! (override edildi)
print(cat.scratch()) # Pamuk tırmalıyor

# isinstance kontrolü
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (Dog, Animal'dan türedi)
print(isinstance(dog, Cat))     # False
```

### Örnek 15: super() Kullanımı

```python
class Vehicle:
    """Araç base class"""

    def __init__(self, brand, model, year):
        """Araç başlatma"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0

    def drive(self, distance):
        """Araç sürdür"""
        self.odometer += distance
        return f"{distance} km yol gidildi"

    def info(self):
        """Araç bilgisi"""
        return f"{self.year} {self.brand} {self.model} - {self.odometer} km"

class ElectricVehicle(Vehicle):
    """Elektrikli araç - Vehicle'dan türetildi"""

    def __init__(self, brand, model, year, battery_capacity):
        """Elektrikli araç başlatma"""
        # Parent constructor'ı çağır
        super().__init__(brand, model, year)

        # Child'a özgü attribute
        self.battery_capacity = battery_capacity
        self.battery_level = 100

    def charge(self):
        """Bataryayı şarj et"""
        self.battery_level = 100
        return "Batarya tam şarj edildi"

    def info(self):
        """Araç bilgisi (override + extend)"""
        # Parent metodunu çağır ve genişlet
        base_info = super().info()
        return f"{base_info}\nBatarya: {self.battery_level}% ({self.battery_capacity} kWh)"

# Kullanım
tesla = ElectricVehicle("Tesla", "Model 3", 2024, 75)
print(tesla.info())
# Output:
# 2024 Tesla Model 3 - 0 km
# Batarya: 100% (75 kWh)

tesla.drive(150)
print(tesla.drive(150))  # 150 km yol gidildi
print(tesla.charge())     # Batarya tam şarj edildi
print(tesla.info())
# Output:
# 2024 Tesla Model 3 - 150 km
# Batarya: 100% (75 kWh)
```

### Örnek 16: Multi-Level Inheritance

```python
class LivingBeing:
    """Canlı varlık"""

    def __init__(self, name):
        self.name = name
        self.alive = True

    def breathe(self):
        return f"{self.name} nefes alıyor"

class Mammal(LivingBeing):
    """Memeli hayvan"""

    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} doğum yapıyor"

class Human(Mammal):
    """İnsan"""

    def __init__(self, name, fur_color, language):
        super().__init__(name, fur_color)
        self.language = language

    def speak(self):
        return f"{self.name} {self.language} konuşuyor"

    def introduce(self):
        """Kendini tanıt"""
        return f"Merhaba, ben {self.name}. {self.language} konuşuyorum."

# Kullanım
person = Human("Ali", "Kahverengi", "Türkçe")

# Tüm seviyelerdeki metodlara erişim
print(person.breathe())     # LivingBeing'den
print(person.give_birth())  # Mammal'dan
print(person.speak())       # Human'dan
print(person.introduce())   # Human'dan
```

---

## Polymorphism (Çok Biçimlilik)

Polymorphism, aynı arayüzün farklı sınıflarda farklı şekillerde uygulanmasıdır. Aynı metod ismi, farklı davranışlar sergileyebilir.

### Örnek 17: Method Overriding ile Polymorphism

```python
class Shape:
    """Şekil base class"""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Alan hesapla (override edilmeli)"""
        raise NotImplementedError("Alt sınıflar bu metodu implement etmeli")

    def perimeter(self):
        """Çevre hesapla (override edilmeli)"""
        raise NotImplementedError("Alt sınıflar bu metodu implement etmeli")

class Circle(Shape):
    """Daire"""

    def __init__(self, radius):
        super().__init__("Daire")
        self.radius = radius

    def area(self):
        """Daire alanı"""
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        """Daire çevresi"""
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    """Dikdörtgen"""

    def __init__(self, width, height):
        super().__init__("Dikdörtgen")
        self.width = width
        self.height = height

    def area(self):
        """Dikdörtgen alanı"""
        return self.width * self.height

    def perimeter(self):
        """Dikdörtgen çevresi"""
        return 2 * (self.width + self.height)

class Triangle(Shape):
    """Üçgen"""

    def __init__(self, base, height, side1, side2):
        super().__init__("Üçgen")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        """Üçgen alanı"""
        return (self.base * self.height) / 2

    def perimeter(self):
        """Üçgen çevresi"""
        return self.base + self.side1 + self.side2

# Polymorphism - aynı arayüz, farklı davranışlar
shapes = [
    Circle(5),
    Rectangle(10, 6),
    Triangle(8, 5, 6, 7)
]

# Tüm şekiller için aynı metod çağrılıyor, farklı sonuçlar alınıyor
for shape in shapes:
    print(f"{shape.name}:")
    print(f"  Alan: {shape.area():.2f}")
    print(f"  Çevre: {shape.perimeter():.2f}")
    print()

# Output:
# Daire:
#   Alan: 78.54
#   Çevre: 31.42
#
# Dikdörtgen:
#   Alan: 60.00
#   Çevre: 32.00
#
# Üçgen:
#   Alan: 20.00
#   Çevre: 21.00
```

### Örnek 18: Duck Typing

```python
class Duck:
    """Ördek"""

    def speak(self):
        return "Vak vak!"

    def fly(self):
        return "Ördek uçuyor"

class Airplane:
    """Uçak"""

    def speak(self):
        return "Vınnnnn!"

    def fly(self):
        return "Uçak uçuyor"

class Penguin:
    """Penguen"""

    def speak(self):
        return "Quack!"

    # Penguenler uçamaz, fly metodu yok

def make_it_fly(thing):
    """
    Duck typing - tip kontrolü yapmıyor
    Sadece fly() metoduna sahip olması yeterli
    """
    try:
        print(thing.speak())
        print(thing.fly())
    except AttributeError:
        print(f"{thing.__class__.__name__} uçamıyor!")

# Test
duck = Duck()
plane = Airplane()
penguin = Penguin()

make_it_fly(duck)     # Vak vak! / Ördek uçuyor
make_it_fly(plane)    # Vınnnnn! / Uçak uçuyor
make_it_fly(penguin)  # Quack! / Penguin uçamıyor!
```

---

## Encapsulation (Kapsülleme)

Encapsulation, verileri ve metodları bir arada tutma ve dış erişimden koruma prensibidir. Python'da naming convention ile sağlanır:
- `public`: Herkes erişebilir (normal isimler)
- `_protected`: Sınıf ve alt sınıflar erişebilir (tek alt çizgi)
- `__private`: Sadece sınıf erişebilir (çift alt çizgi)

### Örnek 19: Public, Protected, Private Attributes

```python
class BankAccount:
    """Banka hesabı - encapsulation örneği"""

    def __init__(self, owner, balance):
        self.owner = owner              # Public
        self._account_number = "1234"   # Protected (convention)
        self.__balance = balance        # Private (name mangling)
        self.__pin = "0000"             # Private

    # Public method
    def deposit(self, amount):
        """Para yatır"""
        if amount > 0:
            self.__balance += amount
            return True
        return False

    # Public method
    def withdraw(self, amount, pin):
        """Para çek (PIN ile)"""
        if not self.__verify_pin(pin):
            return "Hatalı PIN!"

        if amount > self.__balance:
            return "Yetersiz bakiye!"

        self.__balance -= amount
        return f"{amount} TL çekildi"

    # Public method
    def get_balance(self, pin):
        """Bakiye sorgula (PIN ile)"""
        if self.__verify_pin(pin):
            return self.__balance
        return "Hatalı PIN!"

    # Private method
    def __verify_pin(self, pin):
        """PIN doğrula (private)"""
        return pin == self.__pin

    # Public method
    def change_pin(self, old_pin, new_pin):
        """PIN değiştir"""
        if self.__verify_pin(old_pin):
            self.__pin = new_pin
            return "PIN değiştirildi"
        return "Hatalı PIN!"

# Kullanım
account = BankAccount("Ali Yılmaz", 1000)

# Public attribute - erişilebilir
print(account.owner)  # Ali Yılmaz

# Protected attribute - erişilebilir ama yapılmamalı (convention)
print(account._account_number)  # 1234

# Private attribute - name mangling ile erişilebilir ama yapılmamalı
# print(account.__balance)  # AttributeError
# print(account._BankAccount__balance)  # 1000 (name mangling)

# Public metodlar ile erişim
account.deposit(500)
print(account.get_balance("0000"))  # 1500
print(account.withdraw(200, "0000"))  # 200 TL çekildi
print(account.withdraw(200, "1111"))  # Hatalı PIN!

account.change_pin("0000", "1234")
print(account.get_balance("1234"))  # 1300
```

### Örnek 20: Getter ve Setter Methods

```python
class Person:
    """Kişi sınıfı - getter/setter örneği"""

    def __init__(self, name, age):
        self.__name = name  # Private
        self.__age = age    # Private

    # Getter methods
    def get_name(self):
        """İsim getter"""
        return self.__name

    def get_age(self):
        """Yaş getter"""
        return self.__age

    # Setter methods
    def set_name(self, name):
        """İsim setter (validasyon ile)"""
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Geçersiz isim!")

    def set_age(self, age):
        """Yaş setter (validasyon ile)"""
        if isinstance(age, int) and 0 <= age <= 150:
            self.__age = age
        else:
            raise ValueError("Geçersiz yaş!")

    def display(self):
        """Bilgileri göster"""
        return f"{self.__name}, {self.__age} yaşında"

# Kullanım
person = Person("Ali", 25)

# Getter ile okuma
print(person.get_name())  # Ali
print(person.get_age())   # 25

# Setter ile yazma
person.set_name("Ahmet")
person.set_age(30)
print(person.display())   # Ahmet, 30 yaşında

# Validasyon çalışıyor
try:
    person.set_age(200)  # ValueError
except ValueError as e:
    print(e)  # Geçersiz yaş!
```

---

## Special Methods (Özel Metodlar)

Special methods (magic methods/dunder methods), Python'da çift alt çizgi ile başlayan ve biten özel metodlardır. Operator overloading ve built-in fonksiyonlarla çalışmayı sağlar.

### Örnek 21: __str__ ve __repr__

```python
class Book:
    """Kitap sınıfı - string representation"""

    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        """
        User-friendly string representation
        print() ve str() için kullanılır
        """
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """
        Developer-friendly representation
        Nesneyi yeniden oluşturmak için kullanılabilir
        """
        return f"Book('{self.title}', '{self.author}', {self.year}, {self.pages})"

# Kullanım
book = Book("1984", "George Orwell", 1949, 328)

print(str(book))   # '1984' by George Orwell (__str__)
print(repr(book))  # Book('1984', 'George Orwell', 1949, 328) (__repr__)
print(book)        # '1984' by George Orwell (__str__ öncelikli)

# __repr__ ile nesneyi yeniden oluşturma
book2 = eval(repr(book))
print(book2)       # '1984' by George Orwell
```

### Örnek 22: Comparison Methods

```python
class Product:
    """Ürün sınıfı - karşılaştırma metodları"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        """Eşitlik (==)"""
        return self.price == other.price

    def __lt__(self, other):
        """Küçüktür (<)"""
        return self.price < other.price

    def __le__(self, other):
        """Küçük eşit (<=)"""
        return self.price <= other.price

    def __gt__(self, other):
        """Büyüktür (>)"""
        return self.price > other.price

    def __ge__(self, other):
        """Büyük eşit (>=)"""
        return self.price >= other.price

    def __ne__(self, other):
        """Eşit değil (!=)"""
        return self.price != other.price

    def __str__(self):
        return f"{self.name}: {self.price} TL"

# Kullanım
laptop = Product("Laptop", 15000)
phone = Product("Phone", 8000)
tablet = Product("Tablet", 8000)

print(laptop > phone)    # True
print(phone < laptop)    # True
print(phone == tablet)   # True (fiyat aynı)
print(phone != laptop)   # True

# Sıralama
products = [laptop, phone, tablet, Product("Monitor", 5000)]
sorted_products = sorted(products)  # __lt__ kullanılır

print("Fiyata göre sıralı:")
for product in sorted_products:
    print(f"  {product}")
# Output:
# Fiyata göre sıralı:
#   Monitor: 5000 TL
#   Phone: 8000 TL
#   Tablet: 8000 TL
#   Laptop: 15000 TL
```

### Örnek 23: Arithmetic Methods

```python
class Vector2D:
    """2D vektör sınıfı - aritmetik operatörler"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Toplama (+)"""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Çıkarma (-)"""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Skaler çarpma (*)"""
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """Skaler bölme (/)"""
        return Vector2D(self.x / scalar, self.y / scalar)

    def __abs__(self):
        """Mutlak değer (büyüklük)"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

# Kullanım
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

v3 = v1 + v2  # __add__
print(v3)     # Vector2D(4, 6)

v4 = v1 - v2  # __sub__
print(v4)     # Vector2D(2, 2)

v5 = v1 * 3   # __mul__
print(v5)     # Vector2D(9, 12)

v6 = v1 / 2   # __truediv__
print(v6)     # Vector2D(1.5, 2.0)

print(f"Büyüklük: {abs(v1)}")  # 5.0 (__abs__)
```

### Örnek 24: Container Methods

```python
class ShoppingCart:
    """Alışveriş sepeti - container methods"""

    def __init__(self):
        self.items = []

    def add(self, item, price):
        """Ürün ekle"""
        self.items.append({"item": item, "price": price})

    def __len__(self):
        """Ürün sayısı (len())"""
        return len(self.items)

    def __getitem__(self, index):
        """Indeksleme (cart[0])"""
        return self.items[index]

    def __setitem__(self, index, value):
        """Indeksle atama (cart[0] = ...)"""
        self.items[index] = value

    def __delitem__(self, index):
        """Indeksle silme (del cart[0])"""
        del self.items[index]

    def __contains__(self, item_name):
        """in operatörü ('Laptop' in cart)"""
        return any(item["item"] == item_name for item in self.items)

    def __iter__(self):
        """İterasyon (for item in cart)"""
        return iter(self.items)

    def total(self):
        """Toplam fiyat"""
        return sum(item["price"] for item in self.items)

    def __str__(self):
        return f"ShoppingCart with {len(self)} items (Total: {self.total()} TL)"

# Kullanım
cart = ShoppingCart()
cart.add("Laptop", 15000)
cart.add("Mouse", 150)
cart.add("Keyboard", 500)

print(len(cart))        # 3 (__len__)
print(cart[0])          # {'item': 'Laptop', 'price': 15000} (__getitem__)
print("Mouse" in cart)  # True (__contains__)

# İterasyon
for item in cart:  # __iter__
    print(f"  {item['item']}: {item['price']} TL")

print(cart)  # ShoppingCart with 3 items (Total: 15650 TL)

# Silme
del cart[1]  # __delitem__
print(cart)  # ShoppingCart with 2 items (Total: 15500 TL)
```

### Örnek 25: Context Manager (__enter__, __exit__)

```python
class FileManager:
    """Dosya yöneticisi - context manager"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """with bloğuna girerken çalışır"""
        print(f"Dosya açılıyor: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """with bloğundan çıkarken çalışır"""
        if self.file:
            self.file.close()
            print(f"Dosya kapatıldı: {self.filename}")

        # Exception handling
        if exc_type is not None:
            print(f"Hata oluştu: {exc_val}")

        return False  # Exception'ı yeniden fırlat

# Kullanım
# with FileManager("test.txt", "w") as f:
#     f.write("Merhaba Dünya!")
#     f.write("\nPython OOP")
# # __exit__ otomatik çağrılır

# Built-in with statement ile karşılaştırma
# with open("test.txt", "r") as f:
#     content = f.read()
#     print(content)
```

---

## Property Decorators

Property decorators, attribute'lara getter, setter ve deleter metodları ekleyerek kontrollü erişim sağlar.

### Örnek 26: @property Decorator

```python
class Temperature:
    """Sıcaklık sınıfı - property decorator"""

    def __init__(self, celsius=0):
        self._celsius = celsius  # Protected attribute

    @property
    def celsius(self):
        """Celsius getter"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Celsius setter (validasyon ile)"""
        if value < -273.15:
            raise ValueError("Sıcaklık mutlak sıfırın altında olamaz!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Fahrenheit getter (hesaplanıyor)"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Fahrenheit setter (celsius'a çevriliyor)"""
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        """Kelvin getter (hesaplanıyor)"""
        return self._celsius + 273.15

# Kullanım - attribute gibi erişilir ama metodlar çalışır
temp = Temperature(25)

# Property getter
print(f"Celsius: {temp.celsius}")      # 25
print(f"Fahrenheit: {temp.fahrenheit}")  # 77.0
print(f"Kelvin: {temp.kelvin}")         # 298.15

# Property setter
temp.celsius = 30
print(f"Yeni celsius: {temp.celsius}")  # 30

temp.fahrenheit = 86
print(f"Celsius (F'den): {temp.celsius}")  # 30.0

# Validasyon
try:
    temp.celsius = -300  # ValueError
except ValueError as e:
    print(e)  # Sıcaklık mutlak sıfırın altında olamaz!
```

### Örnek 27: Property ile Hesaplanan Attributeler

```python
class Circle:
    """Daire sınıfı - computed properties"""

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Yarıçap getter"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Yarıçap setter (validasyon)"""
        if value <= 0:
            raise ValueError("Yarıçap pozitif olmalı!")
        self._radius = value

    @property
    def diameter(self):
        """Çap (hesaplanıyor)"""
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        """Çap setter (yarıçapa çevriliyor)"""
        if value <= 0:
            raise ValueError("Çap pozitif olmalı!")
        self._radius = value / 2

    @property
    def area(self):
        """Alan (hesaplanıyor, sadece getter)"""
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        """Çevre (hesaplanıyor, sadece getter)"""
        return 2 * 3.14159 * self._radius

# Kullanım
circle = Circle(5)

print(f"Yarıçap: {circle.radius}")          # 5
print(f"Çap: {circle.diameter}")            # 10
print(f"Alan: {circle.area:.2f}")           # 78.54
print(f"Çevre: {circle.circumference:.2f}") # 31.42

# Yarıçapı değiştir
circle.radius = 10
print(f"Yeni alan: {circle.area:.2f}")      # 314.16

# Çapı değiştir (yarıçap da değişir)
circle.diameter = 30
print(f"Yarıçap: {circle.radius}")          # 15.0
print(f"Alan: {circle.area:.2f}")           # 706.86

# Alan setter yok (read-only)
# circle.area = 100  # AttributeError
```

### Örnek 28: Property ile Validasyon

```python
class Person:
    """Kişi sınıfı - property ile validasyon"""

    def __init__(self, name, age, email):
        self.name = name    # Setter çağrılır
        self.age = age      # Setter çağrılır
        self.email = email  # Setter çağrılır

    @property
    def name(self):
        """İsim getter"""
        return self._name

    @name.setter
    def name(self, value):
        """İsim setter (validasyon)"""
        if not isinstance(value, str):
            raise TypeError("İsim string olmalı!")
        if len(value) < 2:
            raise ValueError("İsim en az 2 karakter olmalı!")
        self._name = value.strip().title()

    @property
    def age(self):
        """Yaş getter"""
        return self._age

    @age.setter
    def age(self, value):
        """Yaş setter (validasyon)"""
        if not isinstance(value, int):
            raise TypeError("Yaş tam sayı olmalı!")
        if not 0 <= value <= 150:
            raise ValueError("Yaş 0-150 arasında olmalı!")
        self._age = value

    @property
    def email(self):
        """Email getter"""
        return self._email

    @email.setter
    def email(self, value):
        """Email setter (validasyon)"""
        if not isinstance(value, str):
            raise TypeError("Email string olmalı!")
        if "@" not in value or "." not in value:
            raise ValueError("Geçersiz email formatı!")
        self._email = value.lower()

    @property
    def is_adult(self):
        """Yetişkin mi? (computed property)"""
        return self._age >= 18

    def __str__(self):
        return f"{self._name} ({self._age}) - {self._email}"

# Kullanım
person = Person("ali yılmaz", 25, "Ali@Example.COM")
print(person)  # Ali Yılmaz (25) - ali@example.com
print(f"Yetişkin mi? {person.is_adult}")  # True

# Validasyon çalışıyor
try:
    person.age = 200  # ValueError
except ValueError as e:
    print(e)

try:
    person.email = "invalid-email"  # ValueError
except ValueError as e:
    print(e)

# Property ile güvenli güncelleme
person.name = "ayşe kaya"
person.age = 17
print(person)  # Ayşe Kaya (17) - ali@example.com
print(f"Yetişkin mi? {person.is_adult}")  # False
```

---

## Önemli Notlar

1. **Class İsimlendirme**: PascalCase kullanın (ClassName)
2. **self**: Her instance method'un ilk parametresi
3. **__init__**: Constructor, nesne oluşturulurken çalışır
4. **Inheritance**: super() ile parent class'a erişim
5. **Encapsulation**: Private attribute'lar için `__` prefix
6. **Polymorphism**: Aynı arayüz, farklı implementasyonlar
7. **Special Methods**: Operator overloading için `__method__`
8. **Property**: Getter/setter için @property decorator
9. **Class vs Instance**: Class variable tüm nesneler için ortak
10. **Documentation**: Her class ve method için docstring yazın

---

## Özet

Bu bölümde öğrendikleriniz:
- Class ve Object kavramları
- Constructor (__init__) ve instance variables
- Instance methods, class methods, static methods
- Class variables ve instance variables farkı
- Inheritance (kalıtım) ve super() kullanımı
- Polymorphism (çok biçimlilik) ve method overriding
- Encapsulation (kapsülleme) ve erişim seviyeleri
- Special methods (__str__, __repr__, __add__, vb.)
- Property decorators ile kontrollü erişim
- OOP prensipleri ve best practices

Şimdi `exercises.py` dosyasındaki alıştırmaları yaparak OOP becerilerinizi geliştirebilirsiniz!
