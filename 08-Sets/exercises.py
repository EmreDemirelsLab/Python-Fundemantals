"""
PYTHON SETS (KÜMELER) - ALIŞTIRMALAR
=====================================

Bu dosya Python Set (Küme) konusunu pekiştirmek için hazırlanmış
kapsamlı alıştırmaları içerir.

Her alıştırma şu formatı takip eder:
1. Soru açıklaması
2. TODO: Yapılması gereken görev
3. Çözüm: Detaylı açıklamalarla birlikte çözüm

Zorluk Seviyeleri:
- KOLAY: Temel set işlemleri
- ORTA: Set operasyonları ve metodlar
- ZOR: Karmaşık problemler ve gerçek dünya senaryoları
"""

# =============================================================================
# ALIŞTIRMA 1: Set Oluşturma ve Temel İşlemler (KOLAY)
# =============================================================================
"""
SORU 1: Set Oluşturma ve Tekrar Temizleme

Bir öğrenci yoklama listesi var ve bazı öğrenciler listede birden fazla kez
görünüyor. Bu listeyi temizleyip benzersiz öğrencileri bulun ve sıralı bir
liste halinde yazdırın.

Verilen liste: ['Ahmet', 'Ayşe', 'Mehmet', 'Ahmet', 'Zeynep', 'Ayşe', 'Can', 'Mehmet']

Beklenen çıktı: Benzersiz öğrencilerin sıralı listesi
"""

# TODO: Öğrenci listesini set'e çevirip, tekrarları kaldırın ve sıralayın
# İpucu: set() kullanın, sonra sorted() ile sıralayın


# ÇÖZÜM 1:
def soru_1_cozum():
    """
    Set Oluşturma ve Tekrar Temizleme Çözümü

    Yaklaşım:
    1. Liste'yi set'e çevirerek otomatik olarak tekrarları kaldır
    2. Set'i tekrar listeye çevir ve sırala
    3. Sonuçları karşılaştır
    """
    print("=" * 70)
    print("SORU 1 ÇÖZÜMÜ: Set Oluşturma ve Tekrar Temizleme")
    print("=" * 70)

    # Orijinal liste (tekrarlı)
    ogrenciler = ['Ahmet', 'Ayşe', 'Mehmet', 'Ahmet', 'Zeynep', 'Ayşe', 'Can', 'Mehmet']

    print(f"Orijinal liste: {ogrenciler}")
    print(f"Toplam kayıt: {len(ogrenciler)}")

    # Set'e çevirme (tekrarlar otomatik kaldırılır)
    benzersiz_ogrenciler = set(ogrenciler)
    print(f"\nBenzersiz öğrenciler (set): {benzersiz_ogrenciler}")
    print(f"Benzersiz öğrenci sayısı: {len(benzersiz_ogrenciler)}")

    # Sıralı liste oluşturma
    sirali_ogrenciler = sorted(benzersiz_ogrenciler)
    print(f"\nSıralı benzersiz öğrenciler: {sirali_ogrenciler}")

    # Alternatif: Tek satırda
    tek_satirda = sorted(set(ogrenciler))
    print(f"Tek satırda: {tek_satirda}")

    # Tekrar eden öğrencileri bulma
    tekrarlar = [ogr for ogr in set(ogrenciler) if ogrenciler.count(ogr) > 1]
    print(f"\nTekrar eden öğrenciler: {sorted(tekrarlar)}")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_1_cozum()


# =============================================================================
# ALIŞTIRMA 2: Set Union (Birleşim) İşlemi (KOLAY)
# =============================================================================
"""
SORU 2: Tüm Katılımcıları Bulma

İki farklı etkinlikte katılan kişilerin listeleri var. Her iki etkinliğe
katılan tüm benzersiz kişileri bulun.

Etkinlik 1: {'Ali', 'Ayşe', 'Mehmet', 'Fatma'}
Etkinlik 2: {'Zeynep', 'Ali', 'Can', 'Ayşe'}

Görevler:
1. Her iki etkinliğe katılan tüm benzersiz kişileri bulun
2. Toplam katılımcı sayısını yazdırın
3. Hem | operatörü hem de union() metodunu kullanın
"""

# TODO: Union işlemini hem | operatörü hem de union() metodu ile yapın


# ÇÖZÜM 2:
def soru_2_cozum():
    """
    Set Union (Birleşim) İşlemi Çözümü

    Yaklaşım:
    1. İki yöntemle birleşim oluştur: | operatörü ve union() metodu
    2. Sonuçları karşılaştır
    3. Özet istatistikler çıkar
    """
    print("=" * 70)
    print("SORU 2 ÇÖZÜMÜ: Set Union (Birleşim) İşlemi")
    print("=" * 70)

    # Etkinlik katılımcıları
    etkinlik_1 = {'Ali', 'Ayşe', 'Mehmet', 'Fatma'}
    etkinlik_2 = {'Zeynep', 'Ali', 'Can', 'Ayşe'}

    print(f"Etkinlik 1 katılımcıları: {etkinlik_1}")
    print(f"Etkinlik 2 katılımcıları: {etkinlik_2}")

    # Yöntem 1: | operatörü ile birleşim
    tum_katilimcilar_1 = etkinlik_1 | etkinlik_2
    print(f"\n| operatörü ile birleşim: {tum_katilimcilar_1}")

    # Yöntem 2: union() metodu ile birleşim
    tum_katilimcilar_2 = etkinlik_1.union(etkinlik_2)
    print(f"union() metodu ile birleşim: {tum_katilimcilar_2}")

    # Her iki yöntem aynı sonucu verir
    print(f"\nSonuçlar eşit mi? {tum_katilimcilar_1 == tum_katilimcilar_2}")

    # İstatistikler
    print(f"\nEtkinlik 1 katılımcı sayısı: {len(etkinlik_1)}")
    print(f"Etkinlik 2 katılımcı sayısı: {len(etkinlik_2)}")
    print(f"Toplam benzersiz katılımcı: {len(tum_katilimcilar_1)}")
    print(f"Her iki etkinliğe de katılan: {len(etkinlik_1 & etkinlik_2)}")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_2_cozum()


# =============================================================================
# ALIŞTIRMA 3: Set Intersection (Kesişim) İşlemi (KOLAY)
# =============================================================================
"""
SORU 3: Ortak Becerileri Bulma

Üç farklı iş ilanında aranan beceriler listelenmiş. Her üç ilanda da aranan
ortak becerileri bulun.

İlan 1: {'Python', 'SQL', 'Git', 'Docker', 'API'}
İlan 2: {'Python', 'JavaScript', 'SQL', 'React', 'Git'}
İlan 3: {'Python', 'SQL', 'AWS', 'Linux', 'Git'}

Görevler:
1. Her üç ilanda da ortak becerileri bulun
2. En az iki ilanda aranan becerileri bulun
3. Sonuçları yorumlayın
"""

# TODO: Intersection işlemini kullanarak ortak becerileri bulun


# ÇÖZÜM 3:
def soru_3_cozum():
    """
    Set Intersection (Kesişim) İşlemi Çözümü

    Yaklaşım:
    1. Üç setin kesişimini bul (ortak beceriler)
    2. İki-ikili kesişimleri hesapla
    3. En az iki ilanda geçen becerileri bul
    """
    print("=" * 70)
    print("SORU 3 ÇÖZÜMÜ: Set Intersection (Kesişim) İşlemi")
    print("=" * 70)

    # İş ilanları ve aranan beceriler
    ilan_1 = {'Python', 'SQL', 'Git', 'Docker', 'API'}
    ilan_2 = {'Python', 'JavaScript', 'SQL', 'React', 'Git'}
    ilan_3 = {'Python', 'SQL', 'AWS', 'Linux', 'Git'}

    print("İş İlanları:")
    print(f"İlan 1: {ilan_1}")
    print(f"İlan 2: {ilan_2}")
    print(f"İlan 3: {ilan_3}")

    # Her üç ilanda da ortak beceriler
    ortak_uc = ilan_1 & ilan_2 & ilan_3
    print(f"\nHer üç ilanda da aranan beceriler: {ortak_uc}")

    # İki-ikili kesişimler
    ortak_1_2 = ilan_1 & ilan_2
    ortak_1_3 = ilan_1 & ilan_3
    ortak_2_3 = ilan_2 & ilan_3

    print(f"\nİlan 1 ve 2'de ortak: {ortak_1_2}")
    print(f"İlan 1 ve 3'te ortak: {ortak_1_3}")
    print(f"İlan 2 ve 3'te ortak: {ortak_2_3}")

    # En az iki ilanda geçen beceriler
    en_az_iki = (ortak_1_2 | ortak_1_3 | ortak_2_3)
    print(f"\nEn az iki ilanda aranan beceriler: {en_az_iki}")

    # Sadece bir ilanda geçen beceriler
    tum_beceriler = ilan_1 | ilan_2 | ilan_3
    sadece_bir = tum_beceriler - en_az_iki
    print(f"Sadece bir ilanda aranan beceriler: {sadece_bir}")

    # Yorum
    print(f"\nYORUM:")
    print(f"- En kritik beceriler (3 ilanda da var): {sorted(ortak_uc)}")
    print(f"- Öğrenilmesi önerilen beceriler: {sorted(en_az_iki)}")
    print(f"- Toplam farklı beceri sayısı: {len(tum_beceriler)}")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_3_cozum()


# =============================================================================
# ALIŞTIRMA 4: Set Difference (Fark) İşlemi (ORTA)
# =============================================================================
"""
SORU 4: Eksik Görevleri Bulma

Bir projede tamamlanması gereken görevler ve şu ana kadar tamamlanan
görevler var. Hangi görevlerin henüz tamamlanmadığını bulun.

Tüm görevler: {'Tasarım', 'Frontend', 'Backend', 'Test', 'Deployment',
               'Dokümantasyon', 'Code Review'}
Tamamlanan: {'Tasarım', 'Frontend', 'Test'}

Görevler:
1. Tamamlanmayan görevleri bulun
2. Tamamlanma yüzdesini hesaplayın
3. Fazladan yapılan görevleri kontrol edin (olmamalı ama kontrol edin)
"""

# TODO: Difference işlemini kullanarak eksik görevleri bulun


# ÇÖZÜM 4:
def soru_4_cozum():
    """
    Set Difference (Fark) İşlemi Çözümü

    Yaklaşım:
    1. Tamamlanmayan görevleri bul (difference)
    2. İlerleme yüzdesini hesapla
    3. Anomalileri kontrol et
    """
    print("=" * 70)
    print("SORU 4 ÇÖZÜMÜ: Set Difference (Fark) İşlemi")
    print("=" * 70)

    # Proje görevleri
    tum_gorevler = {'Tasarım', 'Frontend', 'Backend', 'Test',
                    'Deployment', 'Dokümantasyon', 'Code Review'}
    tamamlanan = {'Tasarım', 'Frontend', 'Test'}

    print("Proje Durumu:")
    print(f"Tüm görevler: {tum_gorevler}")
    print(f"Tamamlanan görevler: {tamamlanan}")

    # Tamamlanmayan görevler (difference)
    tamamlanmayan = tum_gorevler - tamamlanan
    print(f"\nTamamlanmayan görevler: {tamamlanmayan}")
    print(f"Kalan görev sayısı: {len(tamamlanmayan)}")

    # Tamamlanma yüzdesi
    tamamlanma_yuzdesi = (len(tamamlanan) / len(tum_gorevler)) * 100
    print(f"\nİlerleme: {tamamlanma_yuzdesi:.1f}% tamamlandı")
    print(f"Tamamlanan: {len(tamamlanan)}/{len(tum_gorevler)} görev")

    # Fazladan yapılan görevler var mı? (olmamalı)
    fazladan = tamamlanan - tum_gorevler
    if fazladan:
        print(f"\nUYARI: Listede olmayan görevler yapılmış: {fazladan}")
    else:
        print(f"\n✓ Tüm tamamlanan görevler listede var")

    # Öncelikli görevler belirleme (örnek)
    oncelikli = {'Backend', 'Deployment'}
    oncelikli_kalan = oncelikli & tamamlanmayan

    print(f"\nÖncelikli görevlerden kalanlar: {oncelikli_kalan}")

    # Görev sıralaması önerisi
    if tamamlanmayan:
        print(f"\nYapılması gereken görevler (alfabetik):")
        for i, gorev in enumerate(sorted(tamamlanmayan), 1):
            oncelik = "🔴" if gorev in oncelikli else "⚪"
            print(f"  {oncelik} {i}. {gorev}")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_4_cozum()


# =============================================================================
# ALIŞTIRMA 5: Symmetric Difference (Simetrik Fark) İşlemi (ORTA)
# =============================================================================
"""
SORU 5: Farklı Tercihleri Bulma

İki arkadaşın sevdiği filmler var. Sadece birinin sevdiği (ortak olmayanlar)
filmleri bulun.

Ahmet'in sevdikleri: {'Inception', 'Interstellar', 'The Matrix', 'Titanic', 'Avatar'}
Ayşe'nin sevdikleri: {'Titanic', 'Avatar', 'Forrest Gump', 'The Shawshank Redemption'}

Görevler:
1. Sadece birinin sevdiği filmleri bulun (symmetric difference)
2. Her ikisinin de sevdiği filmleri bulun
3. Film önerisi yapın (biri sevip diğeri izlememiş)
"""

# TODO: Symmetric difference işlemini kullanın


# ÇÖZÜM 5:
def soru_5_cozum():
    """
    Symmetric Difference (Simetrik Fark) İşlemi Çözümü

    Yaklaşım:
    1. Simetrik farkı hesapla (sadece birinde olan)
    2. Kesişimi hesapla (her ikisinde de olan)
    3. Film önerileri oluştur
    """
    print("=" * 70)
    print("SORU 5 ÇÖZÜMÜ: Symmetric Difference (Simetrik Fark) İşlemi")
    print("=" * 70)

    # Film tercihleri
    ahmet_filmler = {'Inception', 'Interstellar', 'The Matrix', 'Titanic', 'Avatar'}
    ayse_filmler = {'Titanic', 'Avatar', 'Forrest Gump', 'The Shawshank Redemption'}

    print("Film Tercihleri:")
    print(f"Ahmet'in sevdikleri: {ahmet_filmler}")
    print(f"Ayşe'nin sevdikleri: {ayse_filmler}")

    # Simetrik fark (sadece birinin sevdiği)
    farkli_tercihler = ahmet_filmler ^ ayse_filmler
    print(f"\nSadece birinin sevdiği filmler: {farkli_tercihler}")

    # Ortak tercihler
    ortak_tercihler = ahmet_filmler & ayse_filmler
    print(f"Her ikisinin de sevdiği filmler: {ortak_tercihler}")

    # Ahmet'in sevip Ayşe'nin sevmediği
    sadece_ahmet = ahmet_filmler - ayse_filmler
    print(f"\nSadece Ahmet'in sevdiği: {sadece_ahmet}")

    # Ayşe'nin sevip Ahmet'in sevmediği
    sadece_ayse = ayse_filmler - ahmet_filmler
    print(f"Sadece Ayşe'nin sevdiği: {sadece_ayse}")

    # Film önerileri
    print(f"\nFİLM ÖNERİLERİ:")
    print(f"Ahmet'e öneriler (Ayşe'nin sevdikleri): {sorted(sadece_ayse)}")
    print(f"Ayşe'ye öneriler (Ahmet'in sevdikleri): {sorted(sadece_ahmet)}")

    # İstatistikler
    print(f"\nİSTATİSTİKLER:")
    print(f"Ahmet toplam {len(ahmet_filmler)} film seviyor")
    print(f"Ayşe toplam {len(ayse_filmler)} film seviyor")
    print(f"Ortak beğeni: {len(ortak_tercihler)} film")
    print(f"Farklı beğeni: {len(farkli_tercihler)} film")

    # Benzerlik yüzdesi
    tum_filmler = ahmet_filmler | ayse_filmler
    benzerlik = (len(ortak_tercihler) / len(tum_filmler)) * 100
    print(f"Beğeni benzerliği: {benzerlik:.1f}%")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_5_cozum()


# =============================================================================
# ALIŞTIRMA 6: Set Metodları (add, remove, discard, pop) (ORTA)
# =============================================================================
"""
SORU 6: Alışveriş Sepeti Yönetimi

Bir online alışveriş sitesinde kullanıcının sepetini set ile yönetin.
Kullanıcı ürün ekleyebilir, çıkarabilir ve sepeti temizleyebilir.

Görevler:
1. Boş sepet oluşturun
2. Ürün ekleyin (add)
3. Olmayan ürün çıkarmayı deneyin (remove vs discard farkı)
4. Rastgele ürün çıkarın (pop)
5. Sepeti temizleyin (clear)
"""

# TODO: Set metodlarını kullanarak alışveriş sepeti yönetimi yapın


# ÇÖZÜM 6:
def soru_6_cozum():
    """
    Set Metodları Çözümü

    Yaklaşım:
    1. Her metodu pratik bir senaryoda kullan
    2. Hata durumlarını göster
    3. Metodlar arası farkları açıkla
    """
    print("=" * 70)
    print("SORU 6 ÇÖZÜMÜ: Set Metodları (add, remove, discard, pop)")
    print("=" * 70)

    # Boş sepet oluşturma
    sepet = set()
    print(f"Başlangıç sepeti: {sepet}")

    # add() ile ürün ekleme
    print(f"\n--- ÜRÜN EKLEME (add) ---")
    urunler = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam']

    for urun in urunler:
        sepet.add(urun)
        print(f"{urun} sepete eklendi. Sepet: {sepet}")

    # Aynı ürünü tekrar eklemeye çalışma
    sepet.add('Laptop')
    print(f"\nLaptop tekrar eklendi (değişiklik yok): {sepet}")

    # remove() ile ürün çıkarma (ürün yoksa hata verir)
    print(f"\n--- ÜRÜN ÇIKARMA (remove) ---")
    sepet.remove('Webcam')
    print(f"Webcam çıkarıldı: {sepet}")

    # Olmayan ürünü remove ile çıkarmaya çalışma
    try:
        sepet.remove('Printer')  # Bu ürün sepette yok
    except KeyError as e:
        print(f"HATA: remove() ile olmayan ürün çıkarılamaz - KeyError: {e}")

    # discard() ile ürün çıkarma (ürün yoksa hata vermez)
    print(f"\n--- GÜVENLİ ÇIKARMA (discard) ---")
    sepet.discard('Mouse')
    print(f"Mouse çıkarıldı: {sepet}")

    sepet.discard('Printer')  # Olmayan ürün, hata vermez
    print(f"Printer discard edildi (hata yok): {sepet}")

    # pop() ile rastgele ürün çıkarma
    print(f"\n--- RASTGELE ÇIKARMA (pop) ---")
    print(f"Sepet (pop öncesi): {sepet}")

    if sepet:  # Sepet boş değilse
        cikarilan = sepet.pop()
        print(f"Pop ile çıkarılan: {cikarilan}")
        print(f"Sepet (pop sonrası): {sepet}")

    # Tekrar pop
    if sepet:
        cikarilan = sepet.pop()
        print(f"İkinci pop: {cikarilan}")
        print(f"Sepet: {sepet}")

    # update() ile çoklu ekleme
    print(f"\n--- ÇOKLU EKLEME (update) ---")
    yeni_urunler = ['Headset', 'USB Cable', 'Mouse Pad']
    sepet.update(yeni_urunler)
    print(f"Yeni ürünler eklendi: {sepet}")

    # clear() ile sepeti temizleme
    print(f"\n--- SEPETİ TEMİZLEME (clear) ---")
    print(f"Sepet (clear öncesi): {sepet}")
    sepet.clear()
    print(f"Sepet (clear sonrası): {sepet}")

    # Boş sepette pop yapmaya çalışma
    try:
        sepet.pop()
    except KeyError:
        print(f"\nHATA: Boş sepette pop() çalışmaz - KeyError")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_6_cozum()


# =============================================================================
# ALIŞTIRMA 7: Set Comprehension (ZOR)
# =============================================================================
"""
SORU 7: Veri Analizi ile Set Comprehension

Bir e-ticaret sitesinin kullanıcı verilerini analiz edin.

Veriler:
- Kullanıcı ID'leri (1-100)
- Aktif kullanıcılar: 3'e bölünenler
- Premium kullanıcılar: 5'e bölünenler
- VIP kullanıcılar: Hem 3'e hem 5'e bölünenler (15'e bölünenler)

Görevler (Set comprehension kullanarak):
1. Aktif kullanıcıları bulun
2. Premium kullanıcıları bulun
3. VIP kullanıcıları bulun
4. Sadece aktif (premium olmayan) kullanıcıları bulun
5. Sadece premium (aktif olmayan) kullanıcıları bulun
"""

# TODO: Set comprehension kullanarak kullanıcı segmentasyonu yapın


# ÇÖZÜM 7:
def soru_7_cozum():
    """
    Set Comprehension Çözümü

    Yaklaşım:
    1. Set comprehension ile kullanıcı segmentleri oluştur
    2. Karmaşık koşullarla filtreleme yap
    3. Segment analizleri çıkar
    """
    print("=" * 70)
    print("SORU 7 ÇÖZÜMÜ: Set Comprehension")
    print("=" * 70)

    # Tüm kullanıcılar
    tum_kullanicilar = set(range(1, 101))
    print(f"Toplam kullanıcı sayısı: {len(tum_kullanicilar)}")

    # Set comprehension ile segmentler
    # Aktif kullanıcılar (3'e bölünenler)
    aktif = {user for user in tum_kullanicilar if user % 3 == 0}
    print(f"\nAktif kullanıcılar (3'e bölünen): {len(aktif)} kullanıcı")
    print(f"Örnek: {sorted(list(aktif))[:10]}...")

    # Premium kullanıcılar (5'e bölünenler)
    premium = {user for user in tum_kullanicilar if user % 5 == 0}
    print(f"\nPremium kullanıcılar (5'e bölünen): {len(premium)} kullanıcı")
    print(f"Örnek: {sorted(list(premium))[:10]}...")

    # VIP kullanıcılar (hem 3'e hem 5'e bölünen = 15'e bölünen)
    vip = {user for user in tum_kullanicilar if user % 15 == 0}
    print(f"\nVIP kullanıcılar (15'e bölünen): {len(vip)} kullanıcı")
    print(f"VIP'ler: {sorted(vip)}")

    # Sadece aktif (premium olmayan)
    sadece_aktif = {user for user in aktif if user not in premium}
    print(f"\nSadece aktif kullanıcılar: {len(sadece_aktif)} kullanıcı")
    print(f"Örnek: {sorted(list(sadece_aktif))[:10]}...")

    # Sadece premium (aktif olmayan)
    sadece_premium = {user for user in premium if user not in aktif}
    print(f"\nSadece premium kullanıcılar: {len(sadece_premium)} kullanıcı")
    print(f"Örnek: {sorted(list(sadece_premium))[:10]}...")

    # Pasif kullanıcılar (ne aktif ne premium)
    pasif = {user for user in tum_kullanicilar
             if user not in aktif and user not in premium}
    print(f"\nPasif kullanıcılar: {len(pasif)} kullanıcı")

    # Alternatif: Set operasyonları ile
    pasif_alt = tum_kullanicilar - (aktif | premium)
    print(f"Pasif (alternatif): {len(pasif_alt)} kullanıcı")

    # Gelişmiş: Kategorilere göre dağılım
    print(f"\n--- KULLANICI DAĞILIMI ---")
    print(f"VIP (Aktif + Premium): {len(vip)} ({len(vip)/len(tum_kullanicilar)*100:.1f}%)")
    print(f"Sadece Aktif: {len(sadece_aktif)} ({len(sadece_aktif)/len(tum_kullanicilar)*100:.1f}%)")
    print(f"Sadece Premium: {len(sadece_premium)} ({len(sadece_premium)/len(tum_kullanicilar)*100:.1f}%)")
    print(f"Pasif: {len(pasif)} ({len(pasif)/len(tum_kullanicilar)*100:.1f}%)")
    print(f"Toplam: {len(vip) + len(sadece_aktif) + len(sadece_premium) + len(pasif)}")

    # Karmaşık set comprehension: Asal sayılar
    print(f"\n--- BONUS: ASAL SAYILAR ---")
    asallar = {x for x in range(2, 101)
               if all(x % i != 0 for i in range(2, int(x**0.5) + 1))}
    print(f"1-100 arası asal sayılar: {len(asallar)} adet")
    print(f"Asal sayılar: {sorted(asallar)}")

    # Asal VIP'ler
    asal_vip = asallar & vip
    print(f"\nAsal VIP kullanıcılar: {asal_vip if asal_vip else 'Yok'}")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_7_cozum()


# =============================================================================
# ALIŞTIRMA 8: Frozenset Kullanımı (ORTA)
# =============================================================================
"""
SORU 8: Ders Programı Yönetimi

Bir üniversitede ders kombinasyonlarını yönetin. Her kombinasyon değişmez
olmalı (frozenset) ve bu kombinasyonlar başka bir set içinde saklanmalı.

Görevler:
1. Farklı bölümlerin zorunlu derslerini frozenset olarak oluşturun
2. Bu frozenset'leri bir set içinde toplayın
3. Ortak zorunlu dersleri bulun
4. Frozenset'i dictionary key olarak kullanın
"""

# TODO: Frozenset ile ders kombinasyonları oluşturun


# ÇÖZÜM 8:
def soru_8_cozum():
    """
    Frozenset Kullanımı Çözümü

    Yaklaşım:
    1. Frozenset ile değişmez ders setleri oluştur
    2. Set içinde frozenset kullanımını göster
    3. Dictionary key olarak frozenset kullan
    """
    print("=" * 70)
    print("SORU 8 ÇÖZÜMÜ: Frozenset Kullanımı")
    print("=" * 70)

    # Bölümlerin zorunlu dersleri (frozenset olarak)
    bilgisayar_muhendisligi = frozenset([
        'Programlama', 'Veri Yapıları', 'Algoritmalar',
        'Veritabanı', 'Matematik'
    ])

    yazilim_muhendisligi = frozenset([
        'Programlama', 'Veri Yapıları', 'Yazılım Mühendisliği',
        'Veritabanı', 'Web Teknolojileri'
    ])

    elektrik_muhendisligi = frozenset([
        'Fizik', 'Matematik', 'Devreler', 'Elektronik', 'Sinyal İşleme'
    ])

    endustri_muhendisligi = frozenset([
        'Matematik', 'İstatistik', 'Üretim', 'Kalite', 'Optimizasyon'
    ])

    print("Bölümlerin Zorunlu Dersleri:")
    print(f"Bilgisayar Müh.: {bilgisayar_muhendisligi}")
    print(f"Yazılım Müh.: {yazilim_muhendisligi}")
    print(f"Elektrik Müh.: {elektrik_muhendisligi}")
    print(f"Endüstri Müh.: {endustri_muhendisligi}")

    # Frozenset'leri bir set içinde saklama
    tum_bolumler = {
        bilgisayar_muhendisligi,
        yazilim_muhendisligi,
        elektrik_muhendisligi,
        endustri_muhendisligi
    }

    print(f"\nToplam bölüm sayısı: {len(tum_bolumler)}")

    # Ortak zorunlu dersler (tüm bölümlerde)
    ortak_dersler = bilgisayar_muhendisligi & yazilim_muhendisligi & \
                    elektrik_muhendisligi & endustri_muhendisligi
    print(f"\nTüm bölümlerde ortak dersler: {ortak_dersler}")

    # Bilgisayar ve Yazılım Müh. ortak dersleri
    cs_se_ortak = bilgisayar_muhendisligi & yazilim_muhendisligi
    print(f"\nBilgisayar ve Yazılım Müh. ortak dersleri: {cs_se_ortak}")
    print(f"Ortak ders sayısı: {len(cs_se_ortak)}")

    # Frozenset'i dictionary key olarak kullanma
    print(f"\n--- FROZENSET'İ DICTIONARY KEY OLARAK KULLANMA ---")

    bolum_bilgileri = {
        bilgisayar_muhendisligi: {
            'isim': 'Bilgisayar Mühendisliği',
            'ogrenci_sayisi': 150,
            'akreditasyon': 'MÜDEK'
        },
        yazilim_muhendisligi: {
            'isim': 'Yazılım Mühendisliği',
            'ogrenci_sayisi': 120,
            'akreditasyon': 'MÜDEK'
        },
        elektrik_muhendisligi: {
            'isim': 'Elektrik Mühendisliği',
            'ogrenci_sayisi': 100,
            'akreditasyon': 'MÜDEK'
        }
    }

    print("Bölüm Bilgileri (frozenset key'li dictionary):")
    for dersler, bilgi in bolum_bilgileri.items():
        print(f"\n{bilgi['isim']}:")
        print(f"  Öğrenci: {bilgi['ogrenci_sayisi']}")
        print(f"  Ders sayısı: {len(dersler)}")
        print(f"  Akreditasyon: {bilgi['akreditasyon']}")

    # Frozenset immutable olduğunu gösterme
    print(f"\n--- FROZENSET IMMUTABLE KANITI ---")
    try:
        bilgisayar_muhendisligi.add('Yapay Zeka')
    except AttributeError as e:
        print(f"Frozenset değiştirilemez: {e}")

    # Normal set hashable değil (set elemanı olamaz)
    try:
        normal_set = {1, 2, 3}
        test_set = {normal_set}  # Bu hata verecek
    except TypeError as e:
        print(f"Normal set hashable değil: {e}")

    # Ders istatistikleri
    print(f"\n--- İSTATİSTİKLER ---")
    tum_dersler = bilgisayar_muhendisligi | yazilim_muhendisligi | \
                  elektrik_muhendisligi | endustri_muhendisligi
    print(f"Toplam farklı ders: {len(tum_dersler)}")
    print(f"Tüm dersler: {sorted(tum_dersler)}")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_8_cozum()


# =============================================================================
# ALIŞTIRMA 9: Gerçek Dünya Senaryosu - Sosyal Medya Analizi (ZOR)
# =============================================================================
"""
SORU 9: Sosyal Medya Takipçi Analizi

Bir sosyal medya platformunda 3 influencer'ın takipçilerini analiz edin.

Görevler:
1. Her influencer'ın benzersiz takipçi sayısını bulun
2. Hepsini takip eden kullanıcıları bulun (sadık takipçiler)
3. Sadece birini takip edenleri bulun
4. En az ikisini takip edenleri bulun
5. Cross-promotion fırsatlarını belirleyin
6. Influencer benzerlik skorları hesaplayın
"""

# TODO: Karmaşık set operasyonları ile sosyal medya analizi yapın


# ÇÖZÜM 9:
def soru_9_cozum():
    """
    Gerçek Dünya Senaryosu - Sosyal Medya Analizi Çözümü

    Yaklaşım:
    1. Veri simülasyonu oluştur
    2. Çoklu set operasyonları kullan
    3. Analiz ve öngörü üret
    """
    print("=" * 70)
    print("SORU 9 ÇÖZÜMÜ: Sosyal Medya Takipçi Analizi")
    print("=" * 70)

    # Influencer takipçileri (user_id ile)
    influencer_a_takipciler = {
        f'user_{i}' for i in range(1, 101)  # 100 takipçi
        if i % 2 == 0 or i % 3 == 0
    }

    influencer_b_takipciler = {
        f'user_{i}' for i in range(1, 101)
        if i % 3 == 0 or i % 5 == 0
    }

    influencer_c_takipciler = {
        f'user_{i}' for i in range(1, 101)
        if i % 5 == 0 or i % 7 == 0
    }

    print("Influencer Takipçi Sayıları:")
    print(f"Influencer A: {len(influencer_a_takipciler)} takipçi")
    print(f"Influencer B: {len(influencer_b_takipciler)} takipçi")
    print(f"Influencer C: {len(influencer_c_takipciler)} takipçi")

    # 1. Toplam benzersiz kullanıcı (reach)
    toplam_reach = influencer_a_takipciler | influencer_b_takipciler | influencer_c_takipciler
    print(f"\nToplam erişim (benzersiz kullanıcı): {len(toplam_reach)}")

    # 2. Hepsini takip eden kullanıcılar (sadık takipçiler)
    sadik_takipciler = influencer_a_takipciler & influencer_b_takipciler & influencer_c_takipciler
    print(f"\nSadık takipçiler (3'ünü de takip eden): {len(sadik_takipciler)}")
    print(f"Sadık takipçi oranı: {len(sadik_takipciler)/len(toplam_reach)*100:.1f}%")

    # 3. Sadece birini takip edenler
    sadece_a = influencer_a_takipciler - influencer_b_takipciler - influencer_c_takipciler
    sadece_b = influencer_b_takipciler - influencer_a_takipciler - influencer_c_takipciler
    sadece_c = influencer_c_takipciler - influencer_a_takipciler - influencer_b_takipciler

    print(f"\nSadece birini takip edenler:")
    print(f"  Sadece A: {len(sadece_a)} ({len(sadece_a)/len(influencer_a_takipciler)*100:.1f}%)")
    print(f"  Sadece B: {len(sadece_b)} ({len(sadece_b)/len(influencer_b_takipciler)*100:.1f}%)")
    print(f"  Sadece C: {len(sadece_c)} ({len(sadece_c)/len(influencer_c_takipciler)*100:.1f}%)")

    # 4. En az ikisini takip edenler
    ab_ortak = influencer_a_takipciler & influencer_b_takipciler
    ac_ortak = influencer_a_takipciler & influencer_c_takipciler
    bc_ortak = influencer_b_takipciler & influencer_c_takipciler

    en_az_iki = (ab_ortak | ac_ortak | bc_ortak)
    print(f"\nEn az ikisini takip eden: {len(en_az_iki)}")
    print(f"  A ve B ortak: {len(ab_ortak)}")
    print(f"  A ve C ortak: {len(ac_ortak)}")
    print(f"  B ve C ortak: {len(bc_ortak)}")

    # 5. Cross-promotion fırsatları
    print(f"\n--- CROSS-PROMOTION ÖNERİLERİ ---")

    # A'nın takipçilerine B ve C'yi öner
    a_icin_b_potansiyel = influencer_a_takipciler - influencer_b_takipciler
    a_icin_c_potansiyel = influencer_a_takipciler - influencer_c_takipciler

    print(f"\nInfluencer A'nın takipçilerine:")
    print(f"  B'yi öner: {len(a_icin_b_potansiyel)} potansiyel takipçi")
    print(f"  C'yi öner: {len(a_icin_c_potansiyel)} potansiyel takipçi")

    # B'nin takipçilerine A ve C'yi öner
    b_icin_a_potansiyel = influencer_b_takipciler - influencer_a_takipciler
    b_icin_c_potansiyel = influencer_b_takipciler - influencer_c_takipciler

    print(f"\nInfluencer B'nin takipçilerine:")
    print(f"  A'yı öner: {len(b_icin_a_potansiyel)} potansiyel takipçi")
    print(f"  C'yi öner: {len(b_icin_c_potansiyel)} potansiyel takipçi")

    # C'nin takipçilerine A ve B'yi öner
    c_icin_a_potansiyel = influencer_c_takipciler - influencer_a_takipciler
    c_icin_b_potansiyel = influencer_c_takipciler - influencer_b_takipciler

    print(f"\nInfluencer C'nin takipçilerine:")
    print(f"  A'yı öner: {len(c_icin_a_potansiyel)} potansiyel takipçi")
    print(f"  B'yi öner: {len(c_icin_b_potansiyel)} potansiyel takipçi")

    # 6. Influencer benzerlik skorları (Jaccard Similarity)
    def jaccard_benzerlik(set1, set2):
        """İki setin Jaccard benzerlik skorunu hesaplar"""
        kesisim = len(set1 & set2)
        birlesim = len(set1 | set2)
        return (kesisim / birlesim) * 100 if birlesim > 0 else 0

    print(f"\n--- BENZERLİK SKORLARI (Jaccard) ---")
    ab_benzerlik = jaccard_benzerlik(influencer_a_takipciler, influencer_b_takipciler)
    ac_benzerlik = jaccard_benzerlik(influencer_a_takipciler, influencer_c_takipciler)
    bc_benzerlik = jaccard_benzerlik(influencer_b_takipciler, influencer_c_takipciler)

    print(f"A ve B benzerliği: {ab_benzerlik:.1f}%")
    print(f"A ve C benzerliği: {ac_benzerlik:.1f}%")
    print(f"B ve C benzerliği: {bc_benzerlik:.1f}%")

    # En yüksek benzerlik
    benzerlikler = [
        ('A ve B', ab_benzerlik),
        ('A ve C', ac_benzerlik),
        ('B ve C', bc_benzerlik)
    ]
    en_benzer = max(benzerlikler, key=lambda x: x[1])
    print(f"\nEn benzer çift: {en_benzer[0]} ({en_benzer[1]:.1f}%)")

    # Özet rapor
    print(f"\n--- ÖZET RAPOR ---")
    print(f"Toplam erişim: {len(toplam_reach)} kullanıcı")
    print(f"Sadık takipçi oranı: {len(sadik_takipciler)/len(toplam_reach)*100:.1f}%")
    print(f"En büyük cross-promotion fırsatı: {max([len(a_icin_b_potansiyel), len(a_icin_c_potansiyel), len(b_icin_a_potansiyel), len(b_icin_c_potansiyel), len(c_icin_a_potansiyel), len(c_icin_b_potansiyel)])} kullanıcı")
    print(f"Ortalama takipçi benzerliği: {(ab_benzerlik + ac_benzerlik + bc_benzerlik)/3:.1f}%")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_9_cozum()


# =============================================================================
# ALIŞTIRMA 10: İleri Seviye - Metin Analizi (ZOR)
# =============================================================================
"""
SORU 10: Metin Benzerlik Analizi

İki metin arasındaki benzerliği set operasyonları ile hesaplayın.

Görevler:
1. Her metindeki benzersiz kelimeleri bulun
2. Ortak kelimeleri bulun
3. Her metne özel kelimeleri bulun
4. Jaccard benzerlik skorunu hesaplayın
5. Cosine benzerlik yaklaşımı yapın (basitleştirilmiş)
"""

# TODO: Set operasyonları ile metin analizi yapın


# ÇÖZÜM 10:
def soru_10_cozum():
    """
    İleri Seviye - Metin Analizi Çözümü

    Yaklaşım:
    1. Metinleri işle ve set'e çevir
    2. Çeşitli benzerlik metrikleri hesapla
    3. Sonuçları yorumla
    """
    print("=" * 70)
    print("SORU 10 ÇÖZÜMÜ: Metin Benzerlik Analizi")
    print("=" * 70)

    # Örnek metinler
    metin1 = """
    Python programlama dili öğrenmek çok eğlenceli ve faydalıdır.
    Python ile veri analizi yapabilir, web uygulamaları geliştirebilirsiniz.
    Python öğrenmek için birçok kaynak ve topluluk desteği mevcuttur.
    """

    metin2 = """
    Python öğrenmek yazılım kariyeriniz için harika bir başlangıçtır.
    Python programlama dili veri bilimi ve yapay zeka alanlarında çok popülerdir.
    Python topluluğu çok yardımsever ve destekleyicidir.
    """

    # Metinleri işleme
    def metin_isle(metin):
        """Metni küçük harfe çevir, noktalama işaretlerini temizle, kelimelere ayır"""
        import string
        # Küçük harfe çevir
        metin = metin.lower()
        # Noktalama işaretlerini kaldır
        metin = metin.translate(str.maketrans('', '', string.punctuation))
        # Kelimelere ayır
        kelimeler = metin.split()
        # Set'e çevir (benzersiz kelimeler)
        return set(kelimeler)

    kelimeler1 = metin_isle(metin1)
    kelimeler2 = metin_isle(metin2)

    print("Metin İstatistikleri:")
    print(f"Metin 1 - Benzersiz kelime sayısı: {len(kelimeler1)}")
    print(f"Metin 2 - Benzersiz kelime sayısı: {len(kelimeler2)}")

    # 1. Ortak kelimeler
    ortak = kelimeler1 & kelimeler2
    print(f"\nOrtak kelimeler ({len(ortak)} adet):")
    print(f"{sorted(ortak)}")

    # 2. Her metne özel kelimeler
    sadece_1 = kelimeler1 - kelimeler2
    sadece_2 = kelimeler2 - kelimeler1

    print(f"\nSadece Metin 1'de olan kelimeler ({len(sadece_1)} adet):")
    print(f"{sorted(sadece_1)}")

    print(f"\nSadece Metin 2'de olan kelimeler ({len(sadece_2)} adet):")
    print(f"{sorted(sadece_2)}")

    # 3. Tüm benzersiz kelimeler
    tum_kelimeler = kelimeler1 | kelimeler2
    print(f"\nToplam benzersiz kelime sayısı: {len(tum_kelimeler)}")

    # 4. Jaccard Benzerlik Skoru
    # Jaccard = |A ∩ B| / |A ∪ B|
    jaccard = len(ortak) / len(tum_kelimeler)
    print(f"\n--- BENZERLİK METRİKLERİ ---")
    print(f"Jaccard Benzerlik Skoru: {jaccard:.4f} ({jaccard*100:.2f}%)")

    # 5. Dice Coefficient (Alternatif benzerlik metriği)
    # Dice = 2 * |A ∩ B| / (|A| + |B|)
    dice = (2 * len(ortak)) / (len(kelimeler1) + len(kelimeler2))
    print(f"Dice Coefficient: {dice:.4f} ({dice*100:.2f}%)")

    # 6. Overlap Coefficient
    # Overlap = |A ∩ B| / min(|A|, |B|)
    overlap = len(ortak) / min(len(kelimeler1), len(kelimeler2))
    print(f"Overlap Coefficient: {overlap:.4f} ({overlap*100:.2f}%)")

    # 7. Cosine Benzerlik Yaklaşımı (Basitleştirilmiş)
    # Cosine ≈ |A ∩ B| / sqrt(|A| * |B|)
    cosine_approx = len(ortak) / ((len(kelimeler1) * len(kelimeler2)) ** 0.5)
    print(f"Cosine Benzerlik (yaklaşık): {cosine_approx:.4f} ({cosine_approx*100:.2f}%)")

    # 8. Örtüşme analizi
    ortusme_yuzdesi_1 = len(ortak) / len(kelimeler1) * 100
    ortusme_yuzdesi_2 = len(ortak) / len(kelimeler2) * 100

    print(f"\n--- ÖRTÜŞME ANALİZİ ---")
    print(f"Metin 1'in {ortusme_yuzdesi_1:.1f}% kelimesi Metin 2'de de var")
    print(f"Metin 2'nin {ortusme_yuzdesi_2:.1f}% kelimesi Metin 1'de de var")

    # 9. En çok tekrar eden kelimeler (ortak kelimeler)
    print(f"\n--- ORTAK ANAHTAR KELİMELER ---")
    # Python ve python-related kelimeleri filtrele
    python_related = {word for word in ortak if 'python' in word or 'programlama' in word}
    print(f"Python ile ilgili ortak kelimeler: {python_related}")

    # 10. Sonuç yorumu
    print(f"\n--- SONUÇ YORUMU ---")
    if jaccard > 0.5:
        yorum = "Metinler çok benzer"
    elif jaccard > 0.3:
        yorum = "Metinler orta derecede benzer"
    elif jaccard > 0.1:
        yorum = "Metinler az benzer"
    else:
        yorum = "Metinler çok farklı"

    print(f"Benzerlik değerlendirmesi: {yorum}")
    print(f"Ortak kelime oranı: {len(ortak)/len(tum_kelimeler)*100:.1f}%")
    print(f"Farklı kelime oranı: {(len(sadece_1) + len(sadece_2))/len(tum_kelimeler)*100:.1f}%")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_10_cozum()


# =============================================================================
# ALIŞTIRMA 11: Performans Analizi (ORTA)
# =============================================================================
"""
SORU 11: Set vs List Performans Karşılaştırması

Set ve List'in performans farklarını pratik örneklerle gösterin.

Görevler:
1. Büyük veri setlerinde üyelik kontrolü performansını karşılaştırın
2. Tekrar temizleme performansını karşılaştırın
3. Sonuçları yorumlayın
"""

# TODO: Set ve List performansını karşılaştırın


# ÇÖZÜM 11:
def soru_11_cozum():
    """
    Performans Analizi Çözümü

    Yaklaşım:
    1. time modülü ile ölçüm yap
    2. Farklı işlemler için karşılaştır
    3. Sonuçları görselleştir
    """
    print("=" * 70)
    print("SORU 11 ÇÖZÜMÜ: Set vs List Performans Karşılaştırması")
    print("=" * 70)

    import time

    # Büyük veri setleri oluştur
    buyukluk = 50000
    liste_buyuk = list(range(buyukluk))
    set_buyuk = set(range(buyukluk))

    print(f"Veri seti boyutu: {buyukluk:,} eleman\n")

    # 1. Üyelik Kontrolü Performansı
    print("--- TEST 1: ÜYELİK KONTROLÜ ---")

    # Liste ile
    start = time.time()
    for _ in range(1000):
        _ = (buyukluk - 1) in liste_buyuk  # En sondaki eleman (worst case)
    liste_sure = time.time() - start

    # Set ile
    start = time.time()
    for _ in range(1000):
        _ = (buyukluk - 1) in set_buyuk
    set_sure = time.time() - start

    print(f"Liste arama (1000 arama): {liste_sure:.6f} saniye")
    print(f"Set arama (1000 arama): {set_sure:.6f} saniye")
    print(f"Set {liste_sure/set_sure:.1f}x daha hızlı")

    # 2. Tekrar Temizleme Performansı
    print(f"\n--- TEST 2: TEKRAR TEMİZLEME ---")

    # Tekrarlı liste oluştur
    tekrarli = [i % 1000 for i in range(10000)]

    # Liste yöntemi
    start = time.time()
    benzersiz_liste = []
    for item in tekrarli:
        if item not in benzersiz_liste:
            benzersiz_liste.append(item)
    liste_temizleme = time.time() - start

    # Set yöntemi
    start = time.time()
    benzersiz_set = list(set(tekrarli))
    set_temizleme = time.time() - start

    print(f"Liste yöntemi: {liste_temizleme:.6f} saniye")
    print(f"Set yöntemi: {set_temizleme:.6f} saniye")
    print(f"Set {liste_temizleme/set_temizleme:.1f}x daha hızlı")

    # 3. Birleşim İşlemi Performansı
    print(f"\n--- TEST 3: BİRLEŞİM İŞLEMİ ---")

    list1 = list(range(0, 5000))
    list2 = list(range(2500, 7500))
    set1 = set(range(0, 5000))
    set2 = set(range(2500, 7500))

    # Liste birleşimi
    start = time.time()
    birlesim_liste = list(set(list1 + list2))
    liste_birlesim = time.time() - start

    # Set birleşimi
    start = time.time()
    birlesim_set = set1 | set2
    set_birlesim = time.time() - start

    print(f"Liste birleşim: {liste_birlesim:.6f} saniye")
    print(f"Set birleşim: {set_birlesim:.6f} saniye")
    print(f"Set {liste_birlesim/set_birlesim:.1f}x daha hızlı")

    # 4. Bellek Kullanımı
    print(f"\n--- TEST 4: BELLEK KULLANIMI ---")
    import sys

    sample_size = 10000
    liste_sample = list(range(sample_size))
    set_sample = set(range(sample_size))

    liste_bellek = sys.getsizeof(liste_sample)
    set_bellek = sys.getsizeof(set_sample)

    print(f"Liste bellek ({sample_size} eleman): {liste_bellek:,} byte")
    print(f"Set bellek ({sample_size} eleman): {set_bellek:,} byte")
    print(f"Fark: {abs(liste_bellek - set_bellek):,} byte")

    if liste_bellek < set_bellek:
        print(f"Liste {set_bellek/liste_bellek:.2f}x daha az bellek kullanıyor")
    else:
        print(f"Set {liste_bellek/set_bellek:.2f}x daha az bellek kullanıyor")

    # Özet
    print(f"\n--- ÖZET ---")
    print("Set avantajları:")
    print("  ✓ Üyelik kontrolü çok hızlı (O(1))")
    print("  ✓ Tekrar temizleme çok hızlı")
    print("  ✓ Küme operasyonları optimize edilmiş")
    print("\nList avantajları:")
    print("  ✓ Sıralı veri saklama")
    print("  ✓ İndeksleme desteği")
    print("  ✓ Tekrarlı eleman saklama")
    print("\nKullanım önerisi:")
    print("  • Benzersiz veri + hızlı arama → Set")
    print("  • Sıralı veri + indeksleme → List")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_11_cozum()


# =============================================================================
# ALIŞTIRMA 12: Gerçek Dünya Challenge - E-Ticaret Ürün Öneri Sistemi (ZOR)
# =============================================================================
"""
SORU 12: E-Ticaret Ürün Öneri Sistemi

Kullanıcıların satın aldığı ürünlere göre ürün önerisi yapan bir sistem
geliştirin.

Senaryo:
- Kullanıcıların satın alma geçmişi var
- Benzer kullanıcıları bulun (benzer ürün alan)
- Kullanıcıya yeni ürünler önerin

Görevler:
1. Kullanıcı benzerliğini hesaplayın
2. En benzer kullanıcıları bulun
3. Öneri listesi oluşturun
4. Öneri skorları hesaplayın
"""

# TODO: Set operasyonları ile ürün öneri sistemi geliştirin


# ÇÖZÜM 12:
def soru_12_cozum():
    """
    Gerçek Dünya Challenge - Ürün Öneri Sistemi Çözümü

    Yaklaşım:
    1. Collaborative filtering yaklaşımı (basitleştirilmiş)
    2. Set operasyonları ile kullanıcı benzerliği
    3. Öneri skoru hesaplama
    """
    print("=" * 70)
    print("SORU 12 ÇÖZÜMÜ: E-Ticaret Ürün Öneri Sistemi")
    print("=" * 70)

    # Kullanıcı satın alma geçmişi
    kullanici_urunler = {
        'Ahmet': {'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Hub'},
        'Ayşe': {'Laptop', 'Mouse', 'Webcam', 'Headset', 'Monitor'},
        'Mehmet': {'Phone', 'Charger', 'Case', 'Screen Protector', 'Earbuds'},
        'Fatma': {'Laptop', 'Keyboard', 'USB Hub', 'Mousepad', 'HDMI Cable'},
        'Can': {'Phone', 'Case', 'Earbuds', 'Powerbank', 'Charger'},
        'Zeynep': {'Laptop', 'Mouse', 'Keyboard', 'Webcam', 'Desk Lamp'},
        'Ali': {'Tablet', 'Stylus', 'Tablet Case', 'Screen Protector'},
        'Elif': {'Phone', 'Earbuds', 'Powerbank', 'Bluetooth Speaker'},
    }

    # Hedef kullanıcı
    hedef_kullanici = 'Ahmet'
    hedef_urunler = kullanici_urunler[hedef_kullanici]

    print(f"Hedef Kullanıcı: {hedef_kullanici}")
    print(f"Satın aldığı ürünler: {hedef_urunler}")
    print(f"Ürün sayısı: {len(hedef_urunler)}\n")

    # 1. Kullanıcı benzerlik skorları hesaplama
    print("--- KULLANICI BENZERLİK SKORLARI ---")

    def jaccard_benzerlik(set1, set2):
        """Jaccard benzerlik skoru"""
        if not set1 or not set2:
            return 0
        kesisim = len(set1 & set2)
        birlesim = len(set1 | set2)
        return kesisim / birlesim if birlesim > 0 else 0

    benzerlikler = []
    for kullanici, urunler in kullanici_urunler.items():
        if kullanici != hedef_kullanici:
            skor = jaccard_benzerlik(hedef_urunler, urunler)
            benzerlikler.append((kullanici, skor, urunler))

    # Benzerliğe göre sırala
    benzerlikler.sort(key=lambda x: x[1], reverse=True)

    print("En benzer kullanıcılar:")
    for i, (kullanici, skor, urunler) in enumerate(benzerlikler[:5], 1):
        ortak = hedef_urunler & urunler
        print(f"{i}. {kullanici}: {skor:.3f} benzerlik")
        print(f"   Ortak ürünler: {ortak}")
        print(f"   Farklı ürünleri: {urunler - hedef_urunler}")

    # 2. Ürün önerileri oluşturma
    print(f"\n--- ÜRÜN ÖNERİLERİ ---")

    # Weighted voting: Her kullanıcının önerisi, benzerlik skoru ile ağırlıklandırılır
    oneri_skorlari = {}

    for kullanici, benzerlik, urunler in benzerlikler:
        # Kullanıcının sahip olduğu ama hedef kullanıcının olmadığı ürünler
        yeni_urunler = urunler - hedef_urunler

        for urun in yeni_urunler:
            if urun not in oneri_skorlari:
                oneri_skorlari[urun] = 0
            # Benzerlik skoru kadar puan ekle
            oneri_skorlari[urun] += benzerlik

    # Skorlara göre sırala
    oneriler = sorted(oneri_skorlari.items(), key=lambda x: x[1], reverse=True)

    print(f"\nÖnerilen ürünler (skor sırasına göre):")
    for i, (urun, skor) in enumerate(oneriler[:10], 1):
        # Bu ürünü kaç kullanıcı satın almış
        sahip_sayisi = sum(1 for u in kullanici_urunler.values() if urun in u)
        print(f"{i}. {urun}")
        print(f"   Öneri skoru: {skor:.3f}")
        print(f"   Popülerlik: {sahip_sayisi}/{len(kullanici_urunler)} kullanıcı")

    # 3. Kategori bazlı analiz
    print(f"\n--- KATEGORİ ANALİZİ ---")

    # Basit kategorizasyon (ürün ismine göre)
    def kategorize(urun):
        urun_lower = urun.lower()
        if any(k in urun_lower for k in ['laptop', 'monitor', 'keyboard', 'mouse']):
            return 'Bilgisayar Aksesuarları'
        elif any(k in urun_lower for k in ['phone', 'earbuds', 'charger']):
            return 'Telefon Aksesuarları'
        elif any(k in urun_lower for k in ['tablet', 'stylus']):
            return 'Tablet Aksesuarları'
        else:
            return 'Diğer'

    # Hedef kullanıcının kategorileri
    hedef_kategoriler = {kategorize(urun) for urun in hedef_urunler}
    print(f"{hedef_kullanici}'in ilgi alanları: {hedef_kategoriler}")

    # Öneri kategorileri
    oneri_kategorileri = {}
    for urun, skor in oneriler[:10]:
        kategori = kategorize(urun)
        if kategori not in oneri_kategorileri:
            oneri_kategorileri[kategori] = []
        oneri_kategorileri[kategori].append((urun, skor))

    print(f"\nKategorilere göre öneriler:")
    for kategori, urunler in oneri_kategorileri.items():
        print(f"\n{kategori}:")
        for urun, skor in urunler:
            print(f"  • {urun} (skor: {skor:.3f})")

    # 4. Cross-selling fırsatları
    print(f"\n--- CROSS-SELLING FIRSATLARI ---")

    # Sıklıkla birlikte alınan ürünler
    def birlikte_alinanlar(hedef_urun):
        """Hedef ürün ile sıklıkla birlikte alınan ürünleri bul"""
        birlikte = {}
        for kullanici, urunler in kullanici_urunler.items():
            if hedef_urun in urunler:
                for urun in urunler:
                    if urun != hedef_urun:
                        birlikte[urun] = birlikte.get(urun, 0) + 1
        return sorted(birlikte.items(), key=lambda x: x[1], reverse=True)

    # Laptop ile birlikte alınanlar
    if 'Laptop' in hedef_urunler:
        print("Laptop ile sıklıkla birlikte alınan ürünler:")
        birlikte = birlikte_alinanlar('Laptop')
        for urun, sayi in birlikte[:5]:
            if urun not in hedef_urunler:
                print(f"  • {urun} ({sayi} kullanıcı)")

    # 5. Özet rapor
    print(f"\n--- ÖZET RAPOR ---")
    print(f"Analiz edilen kullanıcı: {hedef_kullanici}")
    print(f"Mevcut ürün sayısı: {len(hedef_urunler)}")
    print(f"En benzer kullanıcı: {benzerlikler[0][0]} ({benzerlikler[0][1]:.3f})")
    print(f"Toplam öneri: {len(oneriler)} ürün")
    print(f"Top 3 öneri:")
    for i, (urun, skor) in enumerate(oneriler[:3], 1):
        print(f"  {i}. {urun} (skor: {skor:.3f})")

    print("\n" + "=" * 70 + "\n")

# Çözümü çalıştır
soru_12_cozum()


# =============================================================================
# TÜM ÇÖZÜMLERI TOPLU ÇALIŞTIR
# =============================================================================
def tum_cozumleri_calistir():
    """Tüm alıştırma çözümlerini sırayla çalıştırır"""
    print("\n")
    print("=" * 70)
    print(" " * 15 + "PYTHON SETS - TÜM ALIŞTIRMALAR")
    print("=" * 70)
    print("\n")

    # Not: Yukarıdaki fonksiyonlar zaten çağrıldı, bu yüzden tekrar çağırmaya gerek yok
    # Ama isterseniz bu fonksiyonu çağırarak tüm çözümleri görebilirsiniz

    print("✓ Tüm alıştırmalar tamamlandı!")
    print("\nÖğrenilenler:")
    print("  1. Set oluşturma ve temel işlemler")
    print("  2. Union (birleşim) operasyonu")
    print("  3. Intersection (kesişim) operasyonu")
    print("  4. Difference (fark) operasyonu")
    print("  5. Symmetric difference (simetrik fark)")
    print("  6. Set metodları (add, remove, discard, pop, clear)")
    print("  7. Set comprehension")
    print("  8. Frozenset kullanımı")
    print("  9. Sosyal medya analizi")
    print(" 10. Metin benzerlik analizi")
    print(" 11. Performans karşılaştırması")
    print(" 12. Ürün öneri sistemi")

# Ana program
if __name__ == "__main__":
    print("\nPython Sets Alıştırmaları - Tüm çözümler yukarıda gösterilmiştir.")
    print("İstediğiniz çözümü tekrar çalıştırmak için ilgili fonksiyonu çağırabilirsiniz.")
    print("Örnek: soru_1_cozum(), soru_2_cozum(), ..., soru_12_cozum()")
