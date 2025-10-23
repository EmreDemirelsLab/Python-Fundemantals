"""
STRING OPERATIONS EXERCISES
Python String İşlemleri Alıştırmaları

Bu dosya, Python'da string (metin) işlemleri konusunda pratik yapmak için
tasarlanmış alıştırmalar içerir. Her soru, TODO bölümü ve detaylı çözüm içerir.

Zorluk Seviyeleri:
- Kolay (Easy): 1-5
- Orta (Medium): 6-10
- Zor (Challenge): 11-15
"""

# ============================================================================
# KOLAY SEVİYE (EASY LEVEL)
# ============================================================================

# Alıştırma 1: String Bilgileri
# String'in uzunluğunu, ilk karakterini, son karakterini ve ortadaki
# karakteri bulan bir fonksiyon yazın.
print("=" * 70)
print("Alıştırma 1: String Bilgileri")
print("=" * 70)

# TODO: string_bilgileri fonksiyonunu tamamlayın
# Parametre: metin (string)
# Dönüş: Dictionary - {'uzunluk': int, 'ilk': str, 'son': str, 'orta': str}

def string_bilgileri(metin):
    """
    String hakkında temel bilgileri döndürür.

    Args:
        metin (str): Analiz edilecek metin

    Returns:
        dict: String bilgilerini içeren dictionary
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def string_bilgileri_cozum(metin):
    """
    String hakkında temel bilgileri döndürür.

    Mantık:
    1. len() ile string uzunluğunu buluyoruz
    2. İndeksleme ile ilk karakter: metin[0]
    3. Negatif indeksleme ile son karakter: metin[-1]
    4. Ortadaki karakter için uzunluk // 2 indeksini kullanıyoruz
    """
    uzunluk = len(metin)
    ilk_karakter = metin[0] if uzunluk > 0 else ""
    son_karakter = metin[-1] if uzunluk > 0 else ""
    orta_karakter = metin[uzunluk // 2] if uzunluk > 0 else ""

    return {
        'uzunluk': uzunluk,
        'ilk': ilk_karakter,
        'son': son_karakter,
        'orta': orta_karakter
    }


# Test
test_metin = "Python"
sonuc = string_bilgileri_cozum(test_metin)
print(f"Metin: '{test_metin}'")
print(f"Sonuç: {sonuc}")
print(f"Beklenen: {{'uzunluk': 6, 'ilk': 'P', 'son': 'n', 'orta': 'h'}}\n")


# ============================================================================
# Alıştırma 2: String Temizleme
# Bir string'in başındaki ve sonundaki boşlukları temizleyen, tüm harfleri
# küçük yapan ve çoklu boşlukları tek boşluğa çeviren fonksiyon yazın.
print("=" * 70)
print("Alıştırma 2: String Temizleme")
print("=" * 70)

# TODO: temizle fonksiyonunu tamamlayın

def temizle(metin):
    """
    String'i temizler ve normalize eder.

    Args:
        metin (str): Temizlenecek metin

    Returns:
        str: Temizlenmiş metin
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def temizle_cozum(metin):
    """
    String'i temizler ve normalize eder.

    Mantık:
    1. strip() ile başta ve sondaki boşlukları temizliyoruz
    2. lower() ile tüm harfleri küçük yapıyoruz
    3. split() + join() ile çoklu boşlukları tek boşluğa çeviriyoruz
       - split() boşluklardan böler ve boş stringleri atlar
       - ' '.join() parçaları tek boşlukla birleştirir
    """
    # Başta ve sondaki boşlukları temizle
    metin = metin.strip()

    # Küçük harfe çevir
    metin = metin.lower()

    # Çoklu boşlukları tek boşluğa çevir
    # split() parametresiz kullanılırsa tüm boşlukları ayırır
    metin = ' '.join(metin.split())

    return metin


# Test
test_metin = "   PYTHON    PROGRAMLAMA   DİLİ   "
sonuc = temizle_cozum(test_metin)
print(f"Orijinal: '{test_metin}'")
print(f"Sonuç: '{sonuc}'")
print(f"Beklenen: 'python programlama dili'\n")


# ============================================================================
# Alıştırma 3: String Ters Çevirme
# Bir string'i farklı şekillerde ters çeviren fonksiyonlar yazın:
# 1. Karakterleri ters çevir
# 2. Kelimeleri ters çevir (sırayı)
# 3. Her kelimeyi kendi içinde ters çevir
print("=" * 70)
print("Alıştırma 3: String Ters Çevirme")
print("=" * 70)

# TODO: ters_cevir fonksiyonlarını tamamlayın

def karakterleri_ters_cevir(metin):
    """Tüm karakterleri ters çevirir."""
    # Kodunuzu buraya yazın
    pass


def kelimeleri_ters_cevir(metin):
    """Kelimelerin sırasını ters çevirir."""
    # Kodunuzu buraya yazın
    pass


def her_kelimeyi_ters_cevir(metin):
    """Her kelimeyi kendi içinde ters çevirir."""
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def karakterleri_ters_cevir_cozum(metin):
    """
    Tüm karakterleri ters çevirir.

    Mantık:
    - Slicing ile [::-1] kullanarak string'i ters çeviriyoruz
    - -1 adımı, sondan başa doğru gitmeyi sağlar
    """
    return metin[::-1]


def kelimeleri_ters_cevir_cozum(metin):
    """
    Kelimelerin sırasını ters çevirir.

    Mantık:
    1. split() ile kelimelere ayırıyoruz
    2. [::-1] ile liste sırasını ters çeviriyoruz
    3. join() ile tekrar birleştiriyoruz
    """
    kelimeler = metin.split()
    return ' '.join(kelimeler[::-1])


def her_kelimeyi_ters_cevir_cozum(metin):
    """
    Her kelimeyi kendi içinde ters çevirir.

    Mantık:
    1. split() ile kelimelere ayırıyoruz
    2. List comprehension ile her kelimeyi ters çeviriyoruz
    3. join() ile tekrar birleştiriyoruz
    """
    kelimeler = metin.split()
    ters_kelimeler = [kelime[::-1] for kelime in kelimeler]
    return ' '.join(ters_kelimeler)


# Test
test_metin = "Python Programlama Dili"
print(f"Orijinal: '{test_metin}'")
print(f"Karakterler ters: '{karakterleri_ters_cevir_cozum(test_metin)}'")
print(f"Beklenen: 'iliD amalmargorP nohtyP'")
print(f"\nKelimeler ters: '{kelimeleri_ters_cevir_cozum(test_metin)}'")
print(f"Beklenen: 'Dili Programlama Python'")
print(f"\nHer kelime ters: '{her_kelimeyi_ters_cevir_cozum(test_metin)}'")
print(f"Beklenen: 'nohtyP amalmargorP iliD'\n")


# ============================================================================
# Alıştırma 4: Kelime Sayacı
# Bir metindeki toplam kelime sayısını, benzersiz kelime sayısını ve
# her kelimenin kaç kez geçtiğini bulan fonksiyon yazın.
print("=" * 70)
print("Alıştırma 4: Kelime Sayacı")
print("=" * 70)

# TODO: kelime_istatistikleri fonksiyonunu tamamlayın

def kelime_istatistikleri(metin):
    """
    Metin içindeki kelime istatistiklerini hesaplar.

    Args:
        metin (str): Analiz edilecek metin

    Returns:
        dict: İstatistikleri içeren dictionary
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def kelime_istatistikleri_cozum(metin):
    """
    Metin içindeki kelime istatistiklerini hesaplar.

    Mantık:
    1. Metni küçük harfe çevirip, kelimelere ayırıyoruz
    2. Toplam kelime sayısını len() ile buluyoruz
    3. set() ile benzersiz kelimeleri buluyoruz
    4. Dictionary comprehension ile her kelimenin sayısını buluyoruz
    """
    # Metni küçük harfe çevir ve kelimelere ayır
    kelimeler = metin.lower().split()

    # Toplam kelime sayısı
    toplam = len(kelimeler)

    # Benzersiz kelime sayısı
    benzersiz = len(set(kelimeler))

    # Her kelimenin sayısı
    kelime_sayilari = {}
    for kelime in kelimeler:
        kelime_sayilari[kelime] = kelime_sayilari.get(kelime, 0) + 1

    return {
        'toplam_kelime': toplam,
        'benzersiz_kelime': benzersiz,
        'kelime_frekanslari': kelime_sayilari
    }


# Test
test_metin = "Python dili harika bir dili Python öğrenmek kolay"
sonuc = kelime_istatistikleri_cozum(test_metin)
print(f"Metin: '{test_metin}'")
print(f"Toplam kelime: {sonuc['toplam_kelime']}")
print(f"Benzersiz kelime: {sonuc['benzersiz_kelime']}")
print(f"Kelime frekansları: {sonuc['kelime_frekanslari']}\n")


# ============================================================================
# Alıştırma 5: Baş Harfleri Alma
# Verilen metindeki her kelimenin baş harfini alarak kısaltma oluşturan
# fonksiyon yazın. Örnek: "Türkiye Cumhuriyeti" -> "TC"
print("=" * 70)
print("Alıştırma 5: Baş Harfleri Alma (Kısaltma)")
print("=" * 70)

# TODO: bas_harfleri_al fonksiyonunu tamamlayın

def bas_harfleri_al(metin, buyuk_harf=True):
    """
    Metindeki her kelimenin baş harfini alır.

    Args:
        metin (str): İşlenecek metin
        buyuk_harf (bool): Büyük harf olarak mı döndürülsün

    Returns:
        str: Baş harflerden oluşan kısaltma
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def bas_harfleri_al_cozum(metin, buyuk_harf=True):
    """
    Metindeki her kelimenin baş harfini alır.

    Mantık:
    1. Metni kelimelere ayırıyoruz
    2. Her kelimenin ilk karakterini (kelime[0]) alıyoruz
    3. List comprehension kullanarak tüm baş harfleri topluyoruz
    4. join() ile birleştiriyoruz
    5. buyuk_harf parametresine göre upper() veya lower() uyguluyoruz
    """
    kelimeler = metin.split()
    bas_harfler = [kelime[0] for kelime in kelimeler if kelime]
    kisaltma = ''.join(bas_harfler)

    return kisaltma.upper() if buyuk_harf else kisaltma.lower()


# Test
test1 = "Türkiye Cumhuriyeti"
test2 = "Application Programming Interface"
test3 = "Dünya Sağlık Örgütü"

print(f"'{test1}' -> '{bas_harfleri_al_cozum(test1)}'")
print(f"'{test2}' -> '{bas_harfleri_al_cozum(test2)}'")
print(f"'{test3}' -> '{bas_harfleri_al_cozum(test3)}'")
print(f"'{test2}' (küçük) -> '{bas_harfleri_al_cozum(test2, False)}'\n")


# ============================================================================
# ORTA SEVİYE (MEDIUM LEVEL)
# ============================================================================

# Alıştırma 6: Palindrome Kontrolü
# Bir string'in palindrome (tersten okunuşu aynı) olup olmadığını kontrol eden
# fonksiyon yazın. Boşlukları ve noktalama işaretlerini yok sayın.
print("=" * 70)
print("Alıştırma 6: Palindrome Kontrolü")
print("=" * 70)

# TODO: palindrome_mu fonksiyonunu tamamlayın

def palindrome_mu(metin):
    """
    String'in palindrome olup olmadığını kontrol eder.

    Args:
        metin (str): Kontrol edilecek metin

    Returns:
        bool: Palindrome ise True, değilse False
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def palindrome_mu_cozum(metin):
    """
    String'in palindrome olup olmadığını kontrol eder.

    Mantık:
    1. Metni küçük harfe çeviriyoruz (case-insensitive)
    2. Sadece harf ve rakamları tutuyoruz (boşluk ve noktalama temizleniyor)
    3. String'i kendisinin tersi ile karşılaştırıyoruz

    Alternatif yöntem: re.sub() veya filter() kullanılabilir
    """
    # Sadece harf ve rakamları tut, küçük harfe çevir
    temiz_metin = ''.join(karakter.lower() for karakter in metin
                          if karakter.isalnum())

    # String kendisinin tersi mi?
    return temiz_metin == temiz_metin[::-1]


# Test
test_metinler = [
    "A man a plan a canal Panama",
    "race a car",
    "Ey edip Adana'da pide ye",
    "Python",
    "12321",
    "Was it a car or a cat I saw?"
]

for test in test_metinler:
    sonuc = palindrome_mu_cozum(test)
    print(f"'{test}' -> {sonuc}")
print()


# ============================================================================
# Alıştırma 7: E-posta Validasyonu
# Basit bir e-posta validasyon fonksiyonu yazın.
# Kurallar:
# - @ işareti olmalı ve sadece bir tane olmalı
# - @ işaretinden önce en az bir karakter olmalı
# - @ işaretinden sonra nokta olmalı
# - Nokta en sonda olmamalı
print("=" * 70)
print("Alıştırma 7: E-posta Validasyonu")
print("=" * 70)

# TODO: email_gecerli_mi fonksiyonunu tamamlayın

def email_gecerli_mi(email):
    """
    E-posta adresinin geçerli olup olmadığını kontrol eder.

    Args:
        email (str): Kontrol edilecek e-posta adresi

    Returns:
        bool: Geçerli ise True, değilse False
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def email_gecerli_mi_cozum(email):
    """
    E-posta adresinin geçerli olup olmadığını kontrol eder.

    Mantık:
    1. @ işareti sayısını kontrol ediyoruz (tam 1 olmalı)
    2. @ işaretinden önce ve sonra içerik olmalı
    3. @ işaretinden sonra nokta olmalı
    4. Nokta en sonda olmamalı

    Not: Bu basit bir validasyon. Gerçek projede regex veya
    email-validator kütüphanesi kullanılmalı.
    """
    # @ işareti kontrolü
    if email.count('@') != 1:
        return False

    # @ işaretine göre böl
    kullanici_adi, domain = email.split('@')

    # Kullanıcı adı boş olmamalı
    if not kullanici_adi:
        return False

    # Domain'de nokta olmalı
    if '.' not in domain:
        return False

    # Nokta en sonda olmamalı
    if domain.endswith('.'):
        return False

    # Domain en az 2 karakter olmalı
    if len(domain) < 3:  # en az "a.b" formatında
        return False

    return True


# Test
test_emailler = [
    ("test@example.com", True),
    ("invalid.email", False),
    ("user@domain", False),
    ("@example.com", False),
    ("user@.com", False),
    ("user@domain.", False),
    ("user@@domain.com", False),
    ("ahmet.yilmaz@firma.com.tr", True)
]

for email, beklenen in test_emailler:
    sonuc = email_gecerli_mi_cozum(email)
    durum = "✓" if sonuc == beklenen else "✗"
    print(f"{durum} '{email}' -> {sonuc} (beklenen: {beklenen})")
print()


# ============================================================================
# Alıştırma 8: String Sıkıştırma
# Ardışık tekrarlanan karakterleri sıkıştıran fonksiyon yazın.
# Örnek: "aaabbbccc" -> "a3b3c3"
# Eğer sıkıştırılmış hali daha uzunsa, orijinali döndürün.
print("=" * 70)
print("Alıştırma 8: String Sıkıştırma")
print("=" * 70)

# TODO: string_sikistir fonksiyonunu tamamlayın

def string_sikistir(metin):
    """
    Ardışık tekrarlanan karakterleri sıkıştırır.

    Args:
        metin (str): Sıkıştırılacak metin

    Returns:
        str: Sıkıştırılmış metin (veya daha kısaysa orijinal)
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def string_sikistir_cozum(metin):
    """
    Ardışık tekrarlanan karakterleri sıkıştırır.

    Mantık:
    1. Boş string kontrolü yapıyoruz
    2. Her karakteri bir öncekiyle karşılaştırıyoruz
    3. Aynı karakterler devam ettiği sürece sayacı artırıyoruz
    4. Farklı karakter geldiğinde, karakter + sayı ekliyoruz
    5. Sonuç orijinalden kısa değilse, orijinali döndürüyoruz
    """
    if not metin:
        return metin

    sikistirilmis = []
    mevcut_karakter = metin[0]
    sayac = 1

    # Metni karakter karakter gez
    for i in range(1, len(metin)):
        if metin[i] == mevcut_karakter:
            # Aynı karakter devam ediyor
            sayac += 1
        else:
            # Farklı karakter geldi
            sikistirilmis.append(mevcut_karakter + str(sayac))
            mevcut_karakter = metin[i]
            sayac = 1

    # Son karakteri ekle
    sikistirilmis.append(mevcut_karakter + str(sayac))

    sonuc = ''.join(sikistirilmis)

    # Sıkıştırılmış hali daha uzunsa orijinali döndür
    return sonuc if len(sonuc) < len(metin) else metin


# Test
test_metinler = [
    "aaabbbccc",
    "abcdef",
    "aabbcc",
    "aaaaaaaaaa",
    "a",
    ""
]

for test in test_metinler:
    sonuc = string_sikistir_cozum(test)
    print(f"'{test}' -> '{sonuc}' (Uzunluk: {len(test)} -> {len(sonuc)})")
print()


# ============================================================================
# Alıştırma 9: Slug Oluşturucu
# URL-friendly slug oluşturan fonksiyon yazın.
# Türkçe karakterleri İngilizce karşılıklarına çevirin,
# özel karakterleri ve boşlukları tire ile değiştirin.
print("=" * 70)
print("Alıştırma 9: Slug Oluşturucu (URL-Friendly)")
print("=" * 70)

# TODO: slug_olustur fonksiyonunu tamamlayın

def slug_olustur(metin, ayrac='-'):
    """
    Metinden URL-friendly slug oluşturur.

    Args:
        metin (str): Slug'a çevrilecek metin
        ayrac (str): Kelimeler arasında kullanılacak ayırıcı

    Returns:
        str: URL-friendly slug
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def slug_olustur_cozum(metin, ayrac='-'):
    """
    Metinden URL-friendly slug oluşturur.

    Mantık:
    1. Türkçe karakterleri İngilizce karşılıklarına çeviriyoruz
    2. Küçük harfe çeviriyoruz
    3. Harf ve rakam olmayan karakterleri ayırıcı ile değiştiriyoruz
    4. Ardışık ayırıcıları tek ayırıcıya indirgiyoruz
    5. Başta ve sondaki ayırıcıları temizliyoruz
    """
    # Türkçe karakter dönüşüm tablosu
    turkce_karakterler = 'çğıöşüÇĞİÖŞÜ'
    ingilizce_karakterler = 'cgiosuCGIOSU'
    ceviri_tablosu = str.maketrans(turkce_karakterler, ingilizce_karakterler)

    # Türkçe karakterleri çevir
    metin = metin.translate(ceviri_tablosu)

    # Küçük harfe çevir
    metin = metin.lower()

    # Harf ve rakam olmayan karakterleri ayırıcı ile değiştir
    slug = ''
    for karakter in metin:
        if karakter.isalnum():
            slug += karakter
        else:
            slug += ayrac

    # Ardışık ayırıcıları tek ayırıcıya indirgiyoruz
    while ayrac + ayrac in slug:
        slug = slug.replace(ayrac + ayrac, ayrac)

    # Başta ve sondaki ayırıcıları temizle
    slug = slug.strip(ayrac)

    return slug


# Test
test_metinler = [
    "Python Programlama Dili Öğreniyorum!",
    "İstanbul'dan Ankara'ya Seyahat",
    "Web Geliştirme 101: Başlangıç",
    "C++ vs Python: Hangisi Daha İyi?"
]

for test in test_metinler:
    sonuc = slug_olustur_cozum(test)
    print(f"'{test}'")
    print(f"  -> '{sonuc}'\n")


# ============================================================================
# Alıştırma 10: CSV Parser
# Basit bir CSV satırı parser'ı yazın.
# Virgülle ayrılmış değerleri ayırın ve temizleyin.
# Tırnak içindeki virgülleri yok sayın.
print("=" * 70)
print("Alıştırma 10: CSV Satırı Parser")
print("=" * 70)

# TODO: csv_parse fonksiyonunu tamamlayın

def csv_parse(satir, ayrac=','):
    """
    CSV satırını parse eder.

    Args:
        satir (str): CSV satırı
        ayrac (str): Değer ayırıcı karakter

    Returns:
        list: Parse edilmiş değerler listesi
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def csv_parse_cozum(satir, ayrac=','):
    """
    CSV satırını parse eder.

    Mantık:
    1. Satırı ayırıcıya göre böleriz
    2. Her değerin başındaki ve sonundaki boşlukları temizleriz
    3. Tırnak içindeki değerleri özel olarak işleriz
    4. Tırnakları kaldırırız

    Not: Bu basit bir implementasyon. Gerçek projede
    csv modülü kullanılmalı.
    """
    # Basit yaklaşım: split ve strip
    degerler = satir.split(ayrac)
    temiz_degerler = []

    for deger in degerler:
        # Başta ve sondaki boşlukları temizle
        deger = deger.strip()

        # Tırnak içindeyse tırnakları kaldır
        if deger.startswith('"') and deger.endswith('"'):
            deger = deger[1:-1]
        elif deger.startswith("'") and deger.endswith("'"):
            deger = deger[1:-1]

        temiz_degerler.append(deger)

    return temiz_degerler


# Test
test_satirlar = [
    "Ahmet,Yılmaz,30,İstanbul",
    "Ayşe, Demir, 25, Ankara",
    '"Mehmet Ali",Çelik,35,"İzmir, Karşıyaka"',
    "Python,Java,C++,JavaScript"
]

for satir in test_satirlar:
    sonuc = csv_parse_cozum(satir)
    print(f"CSV: {satir}")
    print(f"Parse: {sonuc}\n")


# ============================================================================
# ZOR SEVİYE (CHALLENGE LEVEL)
# ============================================================================

# Alıştırma 11: Anagram Kontrolü
# İki string'in anagram (aynı harflerden oluşmuş) olup olmadığını
# kontrol eden fonksiyon yazın. Boşlukları ve büyük/küçük harfi yok sayın.
print("=" * 70)
print("Alıştırma 11: Anagram Kontrolü")
print("=" * 70)

# TODO: anagram_mu fonksiyonunu tamamlayın

def anagram_mu(metin1, metin2):
    """
    İki string'in anagram olup olmadığını kontrol eder.

    Args:
        metin1 (str): İlk metin
        metin2 (str): İkinci metin

    Returns:
        bool: Anagram ise True, değilse False
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def anagram_mu_cozum(metin1, metin2):
    """
    İki string'in anagram olup olmadığını kontrol eder.

    Mantık:
    1. Her iki metni de küçük harfe çeviriyoruz
    2. Boşlukları ve alfanumerik olmayan karakterleri kaldırıyoruz
    3. Her iki metni de sıralıyoruz
    4. Sıralanmış halleri karşılaştırıyoruz

    Alternatif: Counter kullanarak karakter frekanslarını karşılaştırabiliriz
    """
    from collections import Counter

    # Metinleri temizle: küçük harf + sadece harfler
    def temizle(metin):
        return ''.join(karakter.lower() for karakter in metin
                      if karakter.isalpha())

    temiz1 = temizle(metin1)
    temiz2 = temizle(metin2)

    # Yöntem 1: Sıralama
    # return sorted(temiz1) == sorted(temiz2)

    # Yöntem 2: Counter (daha verimli)
    return Counter(temiz1) == Counter(temiz2)


# Test
test_ciftleri = [
    ("listen", "silent", True),
    ("Astronomer", "Moon starer", True),
    ("The Eyes", "They See", True),
    ("Python", "Java", False),
    ("Conversation", "Voices rant on", True)
]

for metin1, metin2, beklenen in test_ciftleri:
    sonuc = anagram_mu_cozum(metin1, metin2)
    durum = "✓" if sonuc == beklenen else "✗"
    print(f"{durum} '{metin1}' & '{metin2}' -> {sonuc}")
print()


# ============================================================================
# Alıştırma 12: Regex ile Telefon Numarası Formatı
# Farklı formatlardaki telefon numaralarını standart bir formata
# dönüştüren fonksiyon yazın.
# Çıktı formatı: (0555) 123-4567
print("=" * 70)
print("Alıştırma 12: Telefon Numarası Formatlama")
print("=" * 70)

# TODO: telefon_formatla fonksiyonunu tamamlayın

def telefon_formatla(telefon):
    """
    Telefon numarasını standart formata çevirir.

    Args:
        telefon (str): Ham telefon numarası

    Returns:
        str: Formatlanmış telefon numarası veya hata mesajı
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def telefon_formatla_cozum(telefon):
    """
    Telefon numarasını standart formata çevirir.

    Mantık:
    1. regex ile rakam olmayan karakterleri temizliyoruz
    2. Rakam sayısını kontrol ediyoruz (10 olmalı)
    3. Rakamları gruplandırarak format uyguluyoruz: (0XXX) XXX-XXXX

    Format: (0555) 123-4567
    """
    import re

    # Sadece rakamları al
    rakamlar = re.sub(r'\D', '', telefon)

    # Başta 0 yoksa ekle (Türkiye için)
    if len(rakamlar) == 10 and rakamlar[0] != '0':
        rakamlar = '0' + rakamlar[1:]

    # Uzunluk kontrolü (11 olmalı: 0 + 10 rakam)
    if len(rakamlar) == 11 and rakamlar[0] == '0':
        # Format: (0XXX) XXX-XXXX
        return f"({rakamlar[:4]}) {rakamlar[4:7]}-{rakamlar[7:]}"
    elif len(rakamlar) == 10:
        # Format: (0XXX) XXX-XXXX
        return f"({rakamlar[:4]}) {rakamlar[4:7]}-{rakamlar[7:]}"
    else:
        return "Geçersiz telefon numarası"


# Test
test_telefonlar = [
    "05551234567",
    "0555 123 45 67",
    "0555-123-45-67",
    "(0555) 123 45 67",
    "+90 555 123 45 67",
    "555 123 45 67",
    "12345"  # Geçersiz
]

for telefon in test_telefonlar:
    sonuc = telefon_formatla_cozum(telefon)
    print(f"'{telefon}' -> '{sonuc}'")
print()


# ============================================================================
# Alıştırma 13: Metin Şifreleme (Caesar Cipher)
# Caesar cipher algoritması ile metin şifreleme ve çözme fonksiyonları yazın.
# Her harf alfabede belirli sayıda ilerletilir veya geriletilir.
print("=" * 70)
print("Alıştırma 13: Caesar Cipher Şifreleme")
print("=" * 70)

# TODO: caesar_sifrele ve caesar_coz fonksiyonlarını tamamlayın

def caesar_sifrele(metin, kaydirma=3):
    """
    Metni Caesar cipher ile şifreler.

    Args:
        metin (str): Şifrelenecek metin
        kaydirma (int): Kaydırma miktarı

    Returns:
        str: Şifrelenmiş metin
    """
    # Kodunuzu buraya yazın
    pass


def caesar_coz(sifre, kaydirma=3):
    """
    Caesar cipher ile şifrelenmiş metni çözer.

    Args:
        sifre (str): Şifrelenmiş metin
        kaydirma (int): Kaydırma miktarı

    Returns:
        str: Çözülmüş metin
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def caesar_sifrele_cozum(metin, kaydirma=3):
    """
    Metni Caesar cipher ile şifreler.

    Mantık:
    1. Her karakteri kontrol ediyoruz
    2. Harf ise alfabedeki konumunu buluyoruz
    3. Kaydırma miktarı kadar ilerletiyoruz
    4. Alfabenin sonuna gelirse başa dönüyoruz (modulo)
    5. Harf değilse olduğu gibi bırakıyoruz
    """
    sonuc = []

    for karakter in metin:
        if karakter.isalpha():
            # Büyük harf mi küçük harf mi?
            ascii_baslangic = ord('A') if karakter.isupper() else ord('a')

            # Karakterin alfabedeki pozisyonu (0-25)
            pozisyon = ord(karakter) - ascii_baslangic

            # Kaydırma uygula ve alfabeye geri çevir
            yeni_pozisyon = (pozisyon + kaydirma) % 26

            # Yeni karakteri oluştur
            yeni_karakter = chr(ascii_baslangic + yeni_pozisyon)
            sonuc.append(yeni_karakter)
        else:
            # Harf değilse olduğu gibi ekle
            sonuc.append(karakter)

    return ''.join(sonuc)


def caesar_coz_cozum(sifre, kaydirma=3):
    """
    Caesar cipher ile şifrelenmiş metni çözer.

    Mantık:
    Şifreleme fonksiyonunu negatif kaydırma ile çağırıyoruz.
    """
    return caesar_sifrele_cozum(sifre, -kaydirma)


# Test
orijinal = "Python Programlama Dili"
kaydirma = 5

sifreli = caesar_sifrele_cozum(orijinal, kaydirma)
cozulmus = caesar_coz_cozum(sifreli, kaydirma)

print(f"Orijinal: '{orijinal}'")
print(f"Şifreli (kaydırma={kaydirma}): '{sifreli}'")
print(f"Çözülmüş: '{cozulmus}'")
print(f"Doğrulama: {orijinal == cozulmus}\n")

# Farklı kaydırma değerleri
for k in [1, 3, 7, 13]:
    sifre = caesar_sifrele_cozum("HELLO WORLD", k)
    print(f"Kaydırma {k}: 'HELLO WORLD' -> '{sifre}'")
print()


# ============================================================================
# Alıştırma 14: Metin Analiz Aracı
# Bir metin için detaylı istatistikler sağlayan kapsamlı bir
# analiz fonksiyonu yazın.
print("=" * 70)
print("Alıştırma 14: Kapsamlı Metin Analiz Aracı")
print("=" * 70)

# TODO: metin_analiz_et fonksiyonunu tamamlayın

def metin_analiz_et(metin):
    """
    Metin hakkında detaylı istatistikler üretir.

    Args:
        metin (str): Analiz edilecek metin

    Returns:
        dict: Çeşitli istatistikler içeren dictionary
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def metin_analiz_et_cozum(metin):
    """
    Metin hakkında detaylı istatistikler üretir.

    Mantık:
    1. Karakter, kelime, cümle sayılarını hesaplıyoruz
    2. Ortalama kelime uzunluğunu buluyoruz
    3. En uzun ve en kısa kelimeleri buluyoruz
    4. Benzersiz kelime sayısını hesaplıyoruz
    5. En sık kullanılan kelimeleri buluyoruz
    6. Büyük harf, küçük harf, rakam, boşluk sayılarını sayıyoruz
    """
    from collections import Counter
    import re

    # Temel sayımlar
    karakter_sayisi = len(metin)
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)

    # Cümle sayısı (basit: . ! ? ile biten)
    cumle_sayisi = len(re.findall(r'[.!?]+', metin))
    cumle_sayisi = max(1, cumle_sayisi)  # En az 1 cümle var

    # Paragraf sayısı (çift satır sonu)
    paragraf_sayisi = len(metin.split('\n\n'))

    # Kelime uzunlukları
    kelime_uzunluklari = [len(kelime) for kelime in kelimeler]
    ortalama_kelime_uzunlugu = sum(kelime_uzunluklari) / kelime_sayisi if kelime_sayisi > 0 else 0

    # En uzun ve en kısa kelimeler
    # Noktalama işaretlerini temizle
    temiz_kelimeler = [re.sub(r'[^\w]', '', kelime) for kelime in kelimeler]
    temiz_kelimeler = [k for k in temiz_kelimeler if k]  # Boş olanları kaldır

    en_uzun_kelime = max(temiz_kelimeler, key=len) if temiz_kelimeler else ""
    en_kisa_kelime = min(temiz_kelimeler, key=len) if temiz_kelimeler else ""

    # Benzersiz kelimeler
    kucuk_kelimeler = [kelime.lower() for kelime in temiz_kelimeler]
    benzersiz_kelime_sayisi = len(set(kucuk_kelimeler))

    # En sık kullanılan kelimeler (top 5)
    kelime_frekanslari = Counter(kucuk_kelimeler)
    en_sik_kelimeler = kelime_frekanslari.most_common(5)

    # Karakter analizleri
    buyuk_harf_sayisi = sum(1 for k in metin if k.isupper())
    kucuk_harf_sayisi = sum(1 for k in metin if k.islower())
    rakam_sayisi = sum(1 for k in metin if k.isdigit())
    bosluk_sayisi = sum(1 for k in metin if k.isspace())
    ozel_karakter_sayisi = karakter_sayisi - buyuk_harf_sayisi - kucuk_harf_sayisi - rakam_sayisi - bosluk_sayisi

    return {
        'genel': {
            'toplam_karakter': karakter_sayisi,
            'toplam_kelime': kelime_sayisi,
            'toplam_cumle': cumle_sayisi,
            'toplam_paragraf': paragraf_sayisi,
            'benzersiz_kelime': benzersiz_kelime_sayisi
        },
        'ortalamalar': {
            'kelime_uzunlugu': round(ortalama_kelime_uzunlugu, 2),
            'cumle_basina_kelime': round(kelime_sayisi / cumle_sayisi, 2),
            'paragraf_basina_cumle': round(cumle_sayisi / paragraf_sayisi, 2)
        },
        'kelimeler': {
            'en_uzun': en_uzun_kelime,
            'en_kisa': en_kisa_kelime,
            'en_sik_kullanilanlar': en_sik_kelimeler
        },
        'karakter_dagilimi': {
            'buyuk_harf': buyuk_harf_sayisi,
            'kucuk_harf': kucuk_harf_sayisi,
            'rakam': rakam_sayisi,
            'bosluk': bosluk_sayisi,
            'ozel_karakter': ozel_karakter_sayisi
        }
    }


# Test
test_metin = """
Python, yüksek seviyeli bir programlama dilidir.
Guido van Rossum tarafından geliştirilmiştir.
Python öğrenmek kolaydır ve çok güçlüdür!

Python ile web geliştirme, veri analizi, yapay zeka ve
daha birçok alanda çalışabilirsiniz.
"""

sonuc = metin_analiz_et_cozum(test_metin)

print("GENEL İSTATİSTİKLER:")
for anahtar, deger in sonuc['genel'].items():
    print(f"  {anahtar}: {deger}")

print("\nORTALAMALAR:")
for anahtar, deger in sonuc['ortalamalar'].items():
    print(f"  {anahtar}: {deger}")

print("\nKELİME ANALİZİ:")
for anahtar, deger in sonuc['kelimeler'].items():
    print(f"  {anahtar}: {deger}")

print("\nKARAKTER DAĞILIMI:")
for anahtar, deger in sonuc['karakter_dagilimi'].items():
    print(f"  {anahtar}: {deger}")
print()


# ============================================================================
# Alıştırma 15: Gelişmiş Regex - Log Parser
# Log dosyasından bilgi çıkaran gelişmiş bir parser yazın.
# Log formatı: "YYYY-MM-DD HH:MM:SS LEVEL Message"
print("=" * 70)
print("Alıştırma 15: Gelişmiş Log Parser")
print("=" * 70)

# TODO: log_parse ve log_filtrele fonksiyonlarını tamamlayın

def log_parse(log_satiri):
    """
    Tek bir log satırını parse eder.

    Args:
        log_satiri (str): Parse edilecek log satırı

    Returns:
        dict: Parse edilmiş log bilgileri veya None
    """
    # Kodunuzu buraya yazın
    pass


def log_filtrele(log_satirlari, seviye=None, tarih=None, arama=None):
    """
    Log satırlarını filtreleyerek analiz eder.

    Args:
        log_satirlari (list): Log satırları listesi
        seviye (str): Filtrelenecek log seviyesi (INFO, WARNING, ERROR)
        tarih (str): Filtrelenecek tarih (YYYY-MM-DD)
        arama (str): Mesajda aranacak kelime

    Returns:
        list: Filtrelenmiş log kayıtları
    """
    # Kodunuzu buraya yazın
    pass


# ÇÖZÜM:
def log_parse_cozum(log_satiri):
    """
    Tek bir log satırını parse eder.

    Mantık:
    1. Regex pattern ile log formatını tanımlıyoruz
    2. Named groups kullanarak bilgileri çıkarıyoruz
    3. Match başarılıysa dictionary döndürüyoruz
    """
    import re

    # Log pattern: YYYY-MM-DD HH:MM:SS LEVEL Message
    pattern = r'^(?P<tarih>\d{4}-\d{2}-\d{2}) ' \
              r'(?P<saat>\d{2}:\d{2}:\d{2}) ' \
              r'(?P<seviye>\w+) ' \
              r'(?P<mesaj>.+)$'

    match = re.match(pattern, log_satiri.strip())

    if match:
        return {
            'tarih': match.group('tarih'),
            'saat': match.group('saat'),
            'seviye': match.group('seviye'),
            'mesaj': match.group('mesaj'),
            'tam_zaman': f"{match.group('tarih')} {match.group('saat')}"
        }
    return None


def log_filtrele_cozum(log_satirlari, seviye=None, tarih=None, arama=None):
    """
    Log satırlarını filtreleyerek analiz eder.

    Mantık:
    1. Her log satırını parse ediyoruz
    2. Filtreleme kriterlerine göre kontrol ediyoruz
    3. Kriterlere uyan logları topluyoruz
    4. İstatistikler oluşturuyoruz
    """
    from collections import Counter

    parse_edilmis_loglar = []
    basarisiz_satirlar = []

    for i, satir in enumerate(log_satirlari, 1):
        parsed = log_parse_cozum(satir)
        if parsed:
            # Filtreleme
            uygun = True

            if seviye and parsed['seviye'] != seviye:
                uygun = False

            if tarih and parsed['tarih'] != tarih:
                uygun = False

            if arama and arama.lower() not in parsed['mesaj'].lower():
                uygun = False

            if uygun:
                parse_edilmis_loglar.append(parsed)
        else:
            basarisiz_satirlar.append((i, satir))

    # İstatistikler
    seviye_dagilimi = Counter(log['seviye'] for log in parse_edilmis_loglar)

    return {
        'loglar': parse_edilmis_loglar,
        'toplam': len(parse_edilmis_loglar),
        'seviye_dagilimi': dict(seviye_dagilimi),
        'basarisiz_parse': basarisiz_satirlar
    }


# Test
test_log_satirlari = [
    "2024-10-15 10:30:45 INFO Application started successfully",
    "2024-10-15 10:31:12 ERROR Database connection failed",
    "2024-10-15 10:31:45 INFO User logged in: ahmet@example.com",
    "2024-10-15 10:32:30 WARNING Low disk space: 5% remaining",
    "2024-10-15 10:33:15 INFO User logged out: ahmet@example.com",
    "2024-10-15 10:34:00 ERROR Failed to send email notification",
    "2024-10-16 09:15:22 INFO System backup completed",
    "Bu geçersiz bir log satırıdır"  # Geçersiz
]

# Tüm logları parse et
print("TÜM LOGLAR:")
sonuc = log_filtrele_cozum(test_log_satirlari)
print(f"Toplam geçerli log: {sonuc['toplam']}")
print(f"Seviye dağılımı: {sonuc['seviye_dagilimi']}")
print()

# Sadece ERROR loglarını filtrele
print("SADECE ERROR LOGLARI:")
error_loglar = log_filtrele_cozum(test_log_satirlari, seviye='ERROR')
for log in error_loglar['loglar']:
    print(f"  [{log['tam_zaman']}] {log['mesaj']}")
print()

# Belirli bir tarihteki loglar
print("2024-10-15 TARİHİNDEKİ LOGLAR:")
tarih_filtre = log_filtrele_cozum(test_log_satirlari, tarih='2024-10-15')
print(f"Toplam: {tarih_filtre['toplam']}")
print()

# Mesajda "user" geçen loglar
print("'USER' KELİMESİ GEÇEN LOGLAR:")
arama_sonuc = log_filtrele_cozum(test_log_satirlari, arama='user')
for log in arama_sonuc['loglar']:
    print(f"  [{log['seviye']}] {log['mesaj']}")
print()

# Başarısız parse
if sonuc['basarisiz_parse']:
    print("BAŞARISIZ PARSE EDİLEN SATIRLAR:")
    for satir_no, satir in sonuc['basarisiz_parse']:
        print(f"  Satır {satir_no}: {satir}")


print("\n" + "=" * 70)
print("TÜM ALIŞTIRMALAR TAMAMLANDI!")
print("=" * 70)
print("""
Bu alıştırmalarla Python string işlemlerinde şunları öğrendiniz:

✓ Temel string metodları (upper, lower, strip, split, join)
✓ String formatlama (f-strings, format())
✓ String slicing ve indexing
✓ Karakter kontrolü ve validasyon
✓ Regular expressions (regex) temelleri
✓ Metin analizi ve işleme
✓ String algoritmaları (palindrome, anagram, cipher)
✓ Gerçek dünya uygulamaları (email, telefon, log parsing)

Pratik yapmaya devam edin ve kendi projelerinizde kullanın!
""")
