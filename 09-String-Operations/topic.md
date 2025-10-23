# String Operations (Metin İşlemleri)

## İçindekiler
1. [String Temel Kavramlar](#string-temel-kavramlar)
2. [String Metodları](#string-metodları)
3. [String Formatlama](#string-formatlama)
4. [String Slicing (Dilimleme)](#string-slicing)
5. [String Arama ve Değiştirme](#string-arama-ve-değiştirme)
6. [String Ayırma ve Birleştirme](#string-ayırma-ve-birleştirme)
7. [Regular Expressions (Regex) Temelleri](#regex-temelleri)

---

## String Temel Kavramlar

Python'da stringler (metinler) karakter dizileridir ve değiştirilemez (immutable) veri tipleridir. String işlemleri, metin verilerini manipüle etmek için kullanılan en yaygın operasyonlardır.

### Örnek 1: String Oluşturma ve Temel Özellikler

```python
# Farklı string oluşturma yöntemleri
tek_tirnak = 'Merhaba Dünya'
cift_tirnak = "Python Programlama"
uclu_tirnak = '''Çok satırlı
metin oluşturma'''

# String uzunluğu
metin = "Python"
print(f"Uzunluk: {len(metin)}")  # Çıktı: 6

# String'ler immutable'dır
# metin[0] = 'J'  # Bu hata verir!

# String birleştirme
ad = "Ahmet"
soyad = "Yılmaz"
tam_ad = ad + " " + soyad
print(tam_ad)  # Çıktı: Ahmet Yılmaz

# String tekrarlama
yildiz = "*" * 10
print(yildiz)  # Çıktı: **********
```

---

## String Metodları

Python, string manipülasyonu için zengin bir metod koleksiyonu sunar.

### Örnek 2: Büyük/Küçük Harf Dönüşümleri

```python
metin = "Python Programlama Dili"

# Büyük harfe çevirme
print(metin.upper())  # PYTHON PROGRAMLAMA DILI

# Küçük harfe çevirme
print(metin.lower())  # python programlama dili

# İlk harfi büyük yapma
print(metin.capitalize())  # Python programlama dili

# Her kelimenin ilk harfini büyük yapma
print(metin.title())  # Python Programlama Dili

# Büyük/küçük harf değiştirme
print("Hello WORLD".swapcase())  # hELLO world

# Türkçe karakterler için casefold kullanımı
turkce = "İSTANBUL"
print(turkce.lower())      # istanbul (i yerine ı olabilir)
print(turkce.casefold())   # istanbul (daha güvenli)
```

### Örnek 3: String Kontrol Metodları

```python
metin = "Python123"

# Alfabetik karakter kontrolü
print("abc".isalpha())      # True
print("abc123".isalpha())   # False

# Rakam kontrolü
print("12345".isdigit())    # True
print("123.45".isdigit())   # False
print("12345".isnumeric())  # True

# Alfanumerik kontrol
print(metin.isalnum())      # True
print("Python 123".isalnum())  # False (boşluk var)

# Boşluk karakteri kontrolü
print("   ".isspace())      # True
print("  a  ".isspace())    # False

# Büyük/küçük harf kontrolü
print("PYTHON".isupper())   # True
print("python".islower())   # True
print("Python".istitle())   # True

# Başlangıç ve bitiş kontrolü
url = "https://www.python.org"
print(url.startswith("https"))  # True
print(url.endswith(".org"))     # True
```

### Örnek 4: String Temizleme ve Düzenleme

```python
# Boşluk temizleme
metin = "   Python Programlama   "
print(metin.strip())   # "Python Programlama"
print(metin.lstrip())  # "Python Programlama   "
print(metin.rstrip())  # "   Python Programlama"

# Belirli karakterleri temizleme
url = "www.example.com"
print(url.strip("w.com"))  # "example"

# Belirli genişlikte metin hizalama
sayi = "42"
print(sayi.center(10, '*'))  # ****42****
print(sayi.ljust(10, '-'))   # 42--------
print(sayi.rjust(10, '0'))   # 0000000042

# Sekme karakterini boşluğa çevirme
metin_tab = "Python\tProgramlama"
print(metin_tab.expandtabs(4))  # Python    Programlama
```

### Örnek 5: String Arama ve Konumlama

```python
metin = "Python programlama dili, Python öğrenmek kolaydır"

# Alt string arama (index)
print(metin.index("Python"))     # 0 (ilk bulunan)
# print(metin.index("Java"))     # ValueError (bulunamazsa hata)

# Alt string arama (find) - daha güvenli
print(metin.find("Python"))      # 0
print(metin.find("Java"))        # -1 (bulunamazsa -1)

# Sağdan arama
print(metin.rfind("Python"))     # 26 (son bulunan)
print(metin.rindex("Python"))    # 26

# Kaç kez geçiyor
print(metin.count("Python"))     # 2
print(metin.count("python"))     # 0 (case-sensitive)

# Karakter pozisyonu
alfabe = "abcdefghijk"
print(alfabe.index('d'))         # 3
```

---

## String Formatlama

Python'da string formatlama için üç ana yöntem vardır: %-formatting, str.format() ve f-strings (en modern).

### Örnek 6: Eski Stil % Formatlama

```python
# Temel kullanım
ad = "Ayşe"
yas = 25
print("Benim adım %s ve %d yaşındayım" % (ad, yas))

# Farklı veri tipleri
print("Integer: %d" % 42)
print("Float: %f" % 3.14159)
print("Float (2 ondalık): %.2f" % 3.14159)  # 3.14
print("String: %s" % "Merhaba")
print("Hekzadesimal: %x" % 255)  # ff

# Genişlik ve hizalama
print("Sağa hizalı: %10s" % "Python")      # "    Python"
print("Sola hizalı: %-10s" % "Python")     # "Python    "
print("Sıfır doldurma: %05d" % 42)         # "00042"
```

### Örnek 7: str.format() Metodu

```python
# Temel kullanım
print("Merhaba, {}!".format("Dünya"))

# Pozisyonel argümanlar
print("{0} + {1} = {2}".format(5, 3, 8))
print("{2} - {1} = {0}".format(2, 5, 7))

# İsimlendirilmiş argümanlar
print("Ad: {name}, Yaş: {age}".format(name="Mehmet", age=30))

# Karışık kullanım
print("{0} {name} {1}".format("Merhaba", "!", name="Ahmet"))

# Format spesifikasyonları
pi = 3.14159265
print("Pi: {:.2f}".format(pi))              # 3.14
print("Pi: {:.4f}".format(pi))              # 3.1416
print("Yüzde: {:.1%}".format(0.875))        # 87.5%
print("Bilimsel: {:e}".format(1000000))     # 1.000000e+06

# Hizalama ve genişlik
print("{:>10}".format("Python"))     # "    Python"
print("{:<10}".format("Python"))     # "Python    "
print("{:^10}".format("Python"))     # "  Python  "
print("{:*^10}".format("Hi"))        # "****Hi****"

# Sayı formatlama
print("{:,}".format(1000000))        # "1,000,000"
print("{:_}".format(1000000))        # "1_000_000"
```

### Örnek 8: f-strings (Python 3.6+) - Önerilen Yöntem

```python
# Temel kullanım
ad = "Zeynep"
yas = 28
print(f"Benim adım {ad} ve {yas} yaşındayım")

# İfadeler ve hesaplamalar
a, b = 10, 20
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")

# Format spesifikasyonları
pi = 3.14159265
print(f"Pi: {pi:.2f}")                    # 3.14
print(f"Pi: {pi:.5f}")                    # 3.14159

# Hizalama
print(f"{'Python':>10}")                  # "    Python"
print(f"{'Python':<10}")                  # "Python    "
print(f"{'Python':^10}")                  # "  Python  "

# Sayı formatlama
sayi = 1234567.89
print(f"Virgüllü: {sayi:,}")              # "1,234,567.89"
print(f"İki ondalık: {sayi:.2f}")         # "1234567.89"

# Tarih formatlama
from datetime import datetime
simdi = datetime.now()
print(f"Tarih: {simdi:%Y-%m-%d}")
print(f"Saat: {simdi:%H:%M:%S}")

# Özel kullanımlar
deger = 42
print(f"Decimal: {deger:d}")              # 42
print(f"Binary: {deger:b}")               # 101010
print(f"Octal: {deger:o}")                # 52
print(f"Hex: {deger:x}")                  # 2a

# Debug (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")              # x=10, y=20, x+y=30
```

---

## String Slicing (Dilimleme)

String slicing, bir string'in belirli bölümlerini almak için kullanılır.

### Örnek 9: Temel Slicing İşlemleri

```python
metin = "Python Programlama"

# Temel indeksleme
print(metin[0])      # P (ilk karakter)
print(metin[-1])     # a (son karakter)
print(metin[-2])     # m (sondan ikinci)

# Basit slicing: [başlangıç:bitiş]
print(metin[0:6])    # "Python" (0'dan 6'ya kadar, 6 dahil değil)
print(metin[:6])     # "Python" (baştan 6'ya kadar)
print(metin[7:])     # "Programlama" (7'den sona kadar)
print(metin[:])      # "Python Programlama" (tüm string)

# Negatif indekslerle slicing
print(metin[-11:])   # "Programlama" (sondan 11 karakter)
print(metin[:-11])   # "Python " (sondan 11 karakter hariç)

# Adım (step) parametresi: [başlangıç:bitiş:adım]
print(metin[::2])    # "Pto rgalm" (her iki karakterde bir)
print(metin[1::2])   # "yhnPoralma" (1'den başlayıp ikişer)
print(metin[::-1])   # "amalmargorP nohtyP" (tersten)

# Pratik kullanımlar
# String'i tersine çevirme
print(metin[::-1])

# İlk 5 karakter
print(metin[:5])

# Son 5 karakter
print(metin[-5:])

# Ortadaki karakterleri alma
uzunluk = len(metin)
orta_baslangic = uzunluk // 2 - 2
orta_bitis = uzunluk // 2 + 2
print(metin[orta_baslangic:orta_bitis])
```

### Örnek 10: İleri Seviye Slicing

```python
# Karmaşık slicing örnekleri
alfabe = "abcdefghijklmnopqrstuvwxyz"

# Çift indeksli harfler
print(alfabe[::2])   # "acegikmoqsuwy"

# Tek indeksli harfler
print(alfabe[1::2])  # "bdfhjlnprtvxz"

# İlk 10 harfin tersi
print(alfabe[9::-1]) # "jihgfedcba"

# Son 10 harfin tersi
print(alfabe[-1:-11:-1])  # "zyxwvutsrq"

# Her üç karakterde bir
print(alfabe[::3])   # "adgjmpsvy"

# String'den karakter silme (slicing ile)
text = "Python Programlama"
# 7. indeksteki karakteri "silme"
yeni_text = text[:7] + text[8:]
print(yeni_text)     # "Python rogramlama"

# Belirli aralıktaki karakterleri alma
cumle = "Merhaba Dünya, Nasılsınız?"
kelimeler_arasi = cumle[8:13]  # "Dünya"
print(kelimeler_arasi)
```

---

## String Arama ve Değiştirme

String'lerde metin arama ve değiştirme işlemleri için çeşitli metodlar vardır.

### Örnek 11: Replace ve Translate İşlemleri

```python
# Basit replace
metin = "Python programlama, Python öğrenmek"
yeni_metin = metin.replace("Python", "Java")
print(yeni_metin)  # "Java programlama, Java öğrenmek"

# Sayıyla sınırlı replace
metin = "bir iki bir üç bir dört"
yeni = metin.replace("bir", "BİR", 2)  # İlk 2 değişim
print(yeni)  # "BİR iki BİR üç bir dört"

# Çoklu karakteri değiştirme - translate()
metin = "Python Programlama 2024"

# Çeviri tablosu oluşturma
ceviri_tablosu = str.maketrans("Python", "PYTHON")
print(metin.translate(ceviri_tablosu))

# Karakter silme
ceviri_tablosu = str.maketrans("", "", "aeiouAEIOU")  # Sesli harfleri sil
print(metin.translate(ceviri_tablosu))  # "Pythn Prgrmlm 2024"

# Karakter değiştirme ve silme
# 'o' -> '0', 'a' -> '@', sayıları sil
eski = "oa"
yeni = "0@"
sil = "0123456789"
ceviri = str.maketrans(eski, yeni, sil)
test = "Python programlama 2024"
print(test.translate(ceviri))  # "Pyth0n pr0gr@mlm@ "

# Türkçe karakterleri İngilizce karakterlere çevirme
turkce = "Çağla şeker yağmuru ığdır"
turkce_karakter = "çğıöşüÇĞİÖŞÜ"
ingilizce_karakter = "cgiosuCGIOSU"
ceviri = str.maketrans(turkce_karakter, ingilizce_karakter)
print(turkce.translate(ceviri))  # "Cagla seker yagmuru igdir"
```

### Örnek 12: String İçinde Arama ve Kontrol

```python
metin = "Python programlama dili öğrenmek için harika bir dildir"

# in operatörü ile kontrol
print("Python" in metin)      # True
print("Java" in metin)        # False
print("python" not in metin)  # True (küçük p)

# find() ve rfind()
print(metin.find("programlama"))    # 7
print(metin.find("Java"))           # -1
print(metin.rfind("dil"))           # 49 (son bulunan)

# index() - bulamazsa hata verir
try:
    print(metin.index("Python"))    # 0
    print(metin.index("Java"))      # ValueError
except ValueError:
    print("Aranan kelime bulunamadı!")

# count() - kaç kere geçiyor
print(metin.count("dil"))           # 2
print(metin.count("programlama"))   # 1

# Tüm pozisyonları bulma
kelime = "dil"
pozisyonlar = []
baslangic = 0
while True:
    pos = metin.find(kelime, baslangic)
    if pos == -1:
        break
    pozisyonlar.append(pos)
    baslangic = pos + 1
print(f"'{kelime}' kelimesi şu pozisyonlarda: {pozisyonlar}")
```

---

## String Ayırma ve Birleştirme

String'leri parçalara ayırmak ve birleştirmek için kullanılan metodlar.

### Örnek 13: Split ve Join İşlemleri

```python
# Basit split
cumle = "Python programlama dili"
kelimeler = cumle.split()  # Boşluklara göre ayır
print(kelimeler)  # ['Python', 'programlama', 'dili']

# Belirli ayırıcıya göre split
tarih = "2024-10-15"
parcalar = tarih.split("-")
print(parcalar)  # ['2024', '10', '15']

# Maksimum bölme sayısı
metin = "bir,iki,üç,dört,beş"
print(metin.split(",", 2))  # ['bir', 'iki', 'üç,dört,beş']

# rsplit() - sağdan bölme
print(metin.rsplit(",", 2))  # ['bir,iki,üç', 'dört', 'beş']

# splitlines() - satırlara göre ayırma
cok_satirli = """Birinci satır
İkinci satır
Üçüncü satır"""
satirlar = cok_satirli.splitlines()
print(satirlar)  # ['Birinci satır', 'İkinci satır', 'Üçüncü satır']

# partition() - üç parçaya ayırma
url = "https://www.example.com/page"
protokol, ayirac, geri_kalan = url.partition("://")
print(protokol)     # "https"
print(ayirac)       # "://"
print(geri_kalan)   # "www.example.com/page"

# rpartition() - sağdan üç parçaya ayırma
dosya = "belgeler/raporlar/rapor_2024.pdf"
yol, ayirac, dosya_adi = dosya.rpartition("/")
print(yol)          # "belgeler/raporlar"
print(dosya_adi)    # "rapor_2024.pdf"

# join() - birleştirme
kelimeler = ["Python", "harika", "bir", "dildir"]
cumle = " ".join(kelimeler)
print(cumle)  # "Python harika bir dildir"

# Farklı ayırıcılarla join
sayilar = ["1", "2", "3", "4", "5"]
print("-".join(sayilar))      # "1-2-3-4-5"
print(", ".join(sayilar))     # "1, 2, 3, 4, 5"
print("".join(sayilar))       # "12345"

# Liste comprehension ile join
rakamlar = [str(i) for i in range(1, 6)]
print(" + ".join(rakamlar))   # "1 + 2 + 3 + 4 + 5"
```

### Örnek 14: İleri Seviye String Manipülasyonu

```python
# CSV (Comma Separated Values) işleme
csv_satir = "Ahmet,Yılmaz,30,İstanbul"
veriler = csv_satir.split(",")
ad, soyad, yas, sehir = veriler
print(f"Ad: {ad}, Soyad: {soyad}, Yaş: {yas}, Şehir: {sehir}")

# Veri temizleme
kirli_veri = "  Python,  Java  , C++,   JavaScript "
temiz_liste = [item.strip() for item in kirli_veri.split(",")]
print(temiz_liste)  # ['Python', 'Java', 'C++', 'JavaScript']

# String'i karakterlere ayırma
kelime = "Python"
karakterler = list(kelime)
print(karakterler)  # ['P', 'y', 't', 'h', 'o', 'n']

# URL parse etme
url = "https://www.example.com:8080/path/to/page?param1=value1&param2=value2"
protokol, geri_kalan = url.split("://", 1)
host_ve_yol, sorgu = geri_kalan.split("?", 1)
print(f"Protokol: {protokol}")
print(f"Host ve Yol: {host_ve_yol}")
print(f"Sorgu: {sorgu}")

# Parametreleri parse etme
parametreler = {}
for param in sorgu.split("&"):
    anahtar, deger = param.split("=")
    parametreler[anahtar] = deger
print(parametreler)  # {'param1': 'value1', 'param2': 'value2'}

# Metin hizalama ve formatting
basliklar = ["Ad", "Yaş", "Şehir"]
veriler_listesi = [
    ["Ahmet", "30", "İstanbul"],
    ["Ayşe", "25", "Ankara"],
    ["Mehmet", "35", "İzmir"]
]

# Başlıkları yazdır
print(" | ".join([baslik.ljust(10) for baslik in basliklar]))
print("-" * 40)

# Verileri yazdır
for satir in veriler_listesi:
    print(" | ".join([veri.ljust(10) for veri in satir]))
```

---

## Regular Expressions (Regex) Temelleri

Regular expressions (düzenli ifadeler), metin desenlerini eşleştirmek için kullanılan güçlü bir araçtır.

### Örnek 15: Temel Regex İşlemleri

```python
import re

# Basit eşleştirme
metin = "Python programlama dili çok güçlüdür"
eslesme = re.search(r"programlama", metin)
if eslesme:
    print(f"Bulundu: {eslesme.group()} (pozisyon: {eslesme.start()})")

# findall() - tüm eşleşmeleri bulma
metin = "Python 3.9, Python 3.10, Python 3.11"
surumler = re.findall(r"Python \d+\.\d+", metin)
print(surumler)  # ['Python 3.9', 'Python 3.10', 'Python 3.11']

# match() - baştan eşleştirme
if re.match(r"Python", metin):
    print("String 'Python' ile başlıyor")

# split() - regex ile bölme
metin = "bir1iki2üç3dört4beş"
parcalar = re.split(r"\d+", metin)
print(parcalar)  # ['bir', 'iki', 'üç', 'dört', 'beş']

# sub() - regex ile değiştirme
metin = "Telefon: 0555-123-4567, Telefon: 0532-987-6543"
gizli = re.sub(r"\d", "*", metin)
print(gizli)  # "Telefon: ****-***-****, Telefon: ****-***-****"

# Gruplar ile çalışma
telefon = "İletişim: 0555-123-4567"
eslesme = re.search(r"(\d{4})-(\d{3})-(\d{4})", telefon)
if eslesme:
    print(f"Alan kodu: {eslesme.group(1)}")  # 0555
    print(f"Orta kısım: {eslesme.group(2)}")  # 123
    print(f"Son kısım: {eslesme.group(3)}")  # 4567
```

### Örnek 16: İleri Seviye Regex Kullanımı

```python
import re

# E-posta validasyonu
def email_dogrula(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(email_dogrula("test@example.com"))      # True
print(email_dogrula("invalid.email"))         # False

# Telefon numarası formatı
def telefon_formatla(telefon):
    # Sadece rakamları al
    rakamlar = re.sub(r'\D', '', telefon)

    # Format: (0555) 123-4567
    if len(rakamlar) == 10:
        return f"({rakamlar[:4]}) {rakamlar[4:7]}-{rakamlar[7:]}"
    return telefon

print(telefon_formatla("05551234567"))        # (0555) 123-4567
print(telefon_formatla("0555 123 45 67"))     # (0555) 123-4567

# URL'lerden bilgi çıkarma
url = "https://www.example.com:8080/path/to/page?id=123"
pattern = r'(https?)://([^:]+):?(\d+)?(/[^?]+)?(\?.*)?'
match = re.match(pattern, url)

if match:
    protokol = match.group(1)      # https
    domain = match.group(2)        # www.example.com
    port = match.group(3)          # 8080
    yol = match.group(4)           # /path/to/page
    sorgu = match.group(5)         # ?id=123

    print(f"Protokol: {protokol}")
    print(f"Domain: {domain}")
    print(f"Port: {port}")
    print(f"Yol: {yol}")
    print(f"Sorgu: {sorgu}")

# Kelime sınırları
metin = "Python programming, pythonic code, micropython"
# Tam kelime olarak "python" ara (case-insensitive)
eslesmeler = re.findall(r'\bpython\b', metin, re.IGNORECASE)
print(eslesmeler)  # ['Python', 'python']

# Lookahead ve lookbehind
metin = "100 TL, 200 USD, 300 EUR"
# TL'den önceki sayıları bul
tl_fiyatlar = re.findall(r'\d+(?= TL)', metin)
print(tl_fiyatlar)  # ['100']

# Named groups
tarih = "2024-10-15"
pattern = r'(?P<yil>\d{4})-(?P<ay>\d{2})-(?P<gun>\d{2})'
match = re.search(pattern, tarih)
if match:
    print(f"Yıl: {match.group('yil')}")    # 2024
    print(f"Ay: {match.group('ay')}")      # 10
    print(f"Gün: {match.group('gun')}")    # 15
```

### Örnek 17: Regex ile Metin Temizleme ve Validasyon

```python
import re

# HTML etiketlerini temizleme
html = "<p>Bu bir <b>HTML</b> metnidir.</p>"
temiz_metin = re.sub(r'<[^>]+>', '', html)
print(temiz_metin)  # "Bu bir HTML metnidir."

# Çoklu boşlukları tek boşluğa çevirme
metin = "Python    programlama     dili"
tek_bosluk = re.sub(r'\s+', ' ', metin)
print(tek_bosluk)  # "Python programlama dili"

# Sadece harf ve rakamları tutma
kirli = "Python@123#Programming!"
temiz = re.sub(r'[^a-zA-Z0-9\s]', '', kirli)
print(temiz)  # "Python123Programming"

# TC Kimlik No validasyonu (basit versiyon)
def tc_dogrula(tc):
    pattern = r'^[1-9]\d{10}$'  # 11 haneli, 0 ile başlamayan
    return bool(re.match(pattern, tc))

print(tc_dogrula("12345678901"))  # True (format olarak)
print(tc_dogrula("02345678901"))  # False (0 ile başlıyor)
print(tc_dogrula("123456789"))    # False (11 haneli değil)

# Şifre gücü kontrolü
def sifre_gucu_kontrol(sifre):
    # En az 8 karakter, 1 büyük harf, 1 küçük harf, 1 rakam, 1 özel karakter
    if len(sifre) < 8:
        return False

    patterns = [
        r'[A-Z]',      # Büyük harf
        r'[a-z]',      # Küçük harf
        r'\d',         # Rakam
        r'[!@#$%^&*(),.?":{}|<>]'  # Özel karakter
    ]

    return all(re.search(pattern, sifre) for pattern in patterns)

print(sifre_gucu_kontrol("Zayif123"))           # False (özel karakter yok)
print(sifre_gucu_kontrol("Guclu123!"))          # True

# Kredi kartı numarası maskeleme
def kredi_karti_maskele(kart_no):
    # Son 4 hane hariç hepsini * yap
    return re.sub(r'\d(?=\d{4})', '*', kart_no)

print(kredi_karti_maskele("1234-5678-9012-3456"))  # "****-****-****-3456"

# Dosya uzantısı çıkarma
dosyalar = ["document.pdf", "image.jpg", "script.py", "data.tar.gz"]
for dosya in dosyalar:
    match = re.search(r'\.([^.]+)$', dosya)
    if match:
        print(f"{dosya} -> Uzantı: {match.group(1)}")
```

### Örnek 18: Regex Compile ve Performance

```python
import re
import time

# Regex pattern'i compile etmek
# Aynı pattern'i birçok kez kullanacaksanız compile edin
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

emails = [
    "test@example.com",
    "invalid.email",
    "user@domain.co.uk",
    "another@test.org"
]

for email in emails:
    if email_pattern.match(email):
        print(f"{email} -> Geçerli")
    else:
        print(f"{email} -> Geçersiz")

# Performance karşılaştırması
test_metin = "Python programlama dili " * 1000

# Compile edilmemiş
start = time.time()
for _ in range(1000):
    re.findall(r'\bPython\b', test_metin)
sure1 = time.time() - start

# Compile edilmiş
compiled_pattern = re.compile(r'\bPython\b')
start = time.time()
for _ in range(1000):
    compiled_pattern.findall(test_metin)
sure2 = time.time() - start

print(f"Compile edilmemiş: {sure1:.4f} saniye")
print(f"Compile edilmiş: {sure2:.4f} saniye")
print(f"Performans artışı: %{((sure1-sure2)/sure1*100):.2f}")

# Flags kullanımı
metin = """Python Programlama
python öğreniyorum
PYTHON harika"""

# Case-insensitive arama
pattern = re.compile(r'python', re.IGNORECASE)
bulunanlar = pattern.findall(metin)
print(bulunanlar)  # ['Python', 'python', 'PYTHON']

# Multiline mode
metin_cok_satirli = """Başlık: Python
Başlık: Java
Başlık: C++"""

# Her satırın başındaki "Başlık:" ifadesini bul
pattern = re.compile(r'^Başlık:', re.MULTILINE)
bulunanlar = pattern.findall(metin_cok_satirli)
print(f"Bulunan başlık sayısı: {len(bulunanlar)}")  # 3
```

### Örnek 19: Regex ile Veri Çıkarma (Web Scraping Benzeri)

```python
import re

# Log dosyasından bilgi çıkarma
log_satirlari = """
2024-10-15 10:30:45 INFO User logged in: ahmet@example.com
2024-10-15 10:31:12 ERROR Database connection failed
2024-10-15 10:31:45 INFO User logged in: mehmet@example.com
2024-10-15 10:32:30 WARNING Low disk space: 5% remaining
"""

# Tarih ve saat çıkarma
tarihler = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log_satirlari)
print(f"Tarihler: {tarihler}")

# Log seviyelerini çıkarma
seviyeler = re.findall(r'(INFO|ERROR|WARNING)', log_satirlari)
print(f"Log seviyeleri: {seviyeler}")

# E-posta adreslerini çıkarma
emailler = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', log_satirlari)
print(f"E-postalar: {emailler}")

# Yapılandırılmış veri çıkarma
log_pattern = re.compile(
    r'(?P<tarih>\d{4}-\d{2}-\d{2}) '
    r'(?P<saat>\d{2}:\d{2}:\d{2}) '
    r'(?P<seviye>\w+) '
    r'(?P<mesaj>.*)'
)

for satir in log_satirlari.strip().split('\n'):
    match = log_pattern.search(satir)
    if match:
        print(f"Tarih: {match.group('tarih')}, "
              f"Seviye: {match.group('seviye')}, "
              f"Mesaj: {match.group('mesaj')}")

# Markdown linklerini parse etme
markdown_text = """
Bu bir [Python](https://www.python.org) öğrenme rehberidir.
Daha fazla bilgi için [burayı](https://docs.python.org) ziyaret edin.
"""

link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
linkler = re.findall(link_pattern, markdown_text)

for metin, url in linkler:
    print(f"Metin: {metin}, URL: {url}")

# IP adresi validasyonu ve çıkarma
metin = "Sunucu adresleri: 192.168.1.1, 10.0.0.1, 256.1.1.1"
ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
gecerli_ipler = re.findall(ip_pattern, metin)
print(f"Geçerli IP adresleri: {gecerli_ipler}")  # ['192.168.1.1', '10.0.0.1']
```

### Örnek 20: Pratik String İşleme Örnekleri

```python
import re

# 1. Slug oluşturma (URL-friendly string)
def slug_olustur(metin):
    # Türkçe karakterleri değiştir
    turkce_map = str.maketrans('çğıöşüÇĞİÖŞÜ', 'cgiosuCGIOSU')
    metin = metin.translate(turkce_map)

    # Küçük harfe çevir
    metin = metin.lower()

    # Özel karakterleri ve boşlukları - ile değiştir
    metin = re.sub(r'[^a-z0-9]+', '-', metin)

    # Başta ve sonda - varsa temizle
    metin = metin.strip('-')

    return metin

print(slug_olustur("Python Programlama Dili Öğreniyorum!"))
# "python-programlama-dili-ogreniyorum"

# 2. Kelime sayısını bulma (akıllı)
def kelime_say(metin):
    # Noktalama işaretlerini yok say, sadece kelimeleri say
    kelimeler = re.findall(r'\b[a-zA-ZçğıöşüÇĞİÖŞÜ]+\b', metin)
    return len(kelimeler)

cumle = "Python, harika bir programlama dilidir! Değil mi?"
print(f"Kelime sayısı: {kelime_say(cumle)}")  # 6

# 3. Metin özeti (ilk N kelime)
def metin_ozeti(metin, kelime_sayisi=10):
    kelimeler = metin.split()
    if len(kelimeler) <= kelime_sayisi:
        return metin
    return ' '.join(kelimeler[:kelime_sayisi]) + '...'

uzun_metin = """Python, yüksek seviyeli, yorumlamalı, genel amaçlı bir
programlama dilidir. Guido van Rossum tarafından geliştirilmiş ve
ilk kez 1991 yılında yayınlanmıştır."""

print(metin_ozeti(uzun_metin, 8))

# 4. Palindrome kontrolü (Tersten okunuşu aynı)
def palindrome_mu(metin):
    # Sadece harf ve rakamları al, küçük harfe çevir
    temiz = re.sub(r'[^a-zA-Z0-9]', '', metin).lower()
    return temiz == temiz[::-1]

print(palindrome_mu("A man a plan a canal Panama"))  # True
print(palindrome_mu("Python"))  # False

# 5. Camel Case'i Snake Case'e çevirme
def camel_to_snake(metin):
    # Büyük harften önce _ ekle
    metin = re.sub(r'(?<!^)(?=[A-Z])', '_', metin)
    return metin.lower()

print(camel_to_snake("getUserProfile"))      # "get_user_profile"
print(camel_to_snake("calculateTotalPrice")) # "calculate_total_price"

# 6. Snake Case'i Camel Case'e çevirme
def snake_to_camel(metin):
    bilesenler = metin.split('_')
    return bilesenler[0] + ''.join(x.title() for x in bilesenler[1:])

print(snake_to_camel("get_user_profile"))      # "getUserProfile"
print(snake_to_camel("calculate_total_price")) # "calculateTotalPrice"

# 7. String'deki rakamların toplamı
def rakam_toplami(metin):
    rakamlar = re.findall(r'\d+', metin)
    return sum(int(rakam) for rakam in rakamlar)

print(rakam_toplami("Python 3.9 + Django 4.2 = Harika"))  # 18

# 8. Tekrarlanan karakterleri temizleme
def tekrar_temizle(metin):
    return re.sub(r'(.)\1+', r'\1', metin)

print(tekrar_temizle("Hellllooo Wooorld!!!"))  # "Helo World!"

# 9. Stringi ters sırada kelimeler halinde yazdırma
def kelimeleri_ters_cevir(metin):
    return ' '.join(metin.split()[::-1])

print(kelimeleri_ters_cevir("Python programlama dilini seviyorum"))
# "seviyorum dilini programlama Python"

# 10. Metin içindeki en uzun kelimeyi bulma
def en_uzun_kelime(metin):
    kelimeler = re.findall(r'\b[a-zA-ZçğıöşüÇĞİÖŞÜ]+\b', metin)
    return max(kelimeler, key=len) if kelimeler else ""

cumle = "Python programlama dili mükemmel bir dildir"
print(f"En uzun kelime: {en_uzun_kelime(cumle)}")  # "programlama"
```

---

## Özet

String işlemleri Python programlamada en sık kullanılan operasyonlardandır. Bu dokümanda öğrendiğiniz konular:

1. **String Metodları**: upper(), lower(), strip(), find(), replace() vb.
2. **String Formatlama**: %-formatting, format(), f-strings
3. **String Slicing**: İndeksleme ve dilimleme teknikleri
4. **Arama ve Değiştirme**: find(), replace(), translate()
5. **Split ve Join**: String'leri bölme ve birleştirme
6. **Regular Expressions**: Karmaşık metin desenlerini eşleştirme

Bu konuları uygulamalı olarak pratik yaparak pekiştirebilirsiniz. String işlemleri, veri işleme, web scraping, metin analizi ve birçok alanda kullanılır.

---

## Kaynaklar

- Python Official Documentation: https://docs.python.org/3/library/stdtypes.html#string-methods
- Python re Module: https://docs.python.org/3/library/re.html
- Python String Formatting: https://docs.python.org/3/library/string.html
- Real Python String Tutorials: https://realpython.com/python-strings/
