"""
DOSYA İŞLEMLERİ EGZERSİZLERİ
Python Fundamentals - File Operations

Her egzersiz için:
1. Önce problemi okuyun
2. TODO bölümünde kendi çözümünüzü yazın
3. Sonra çözüm bölümünü inceleyin
"""

# ============================================================================
# SORU 1: TEMEL DOSYA YAZMA (KOLAY)
# ============================================================================
"""
Bir "merhaba.txt" dosyası oluşturun ve içine aşağıdaki metni yazın:
"Merhaba Dünya!
Python dosya işlemlerini öğreniyorum.
Bu çok eğlenceli!"

Dosyayı kapatmayı unutmayın.
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 1:
def soru1_cozum():
    """
    Temel dosya yazma işlemi.
    with statement kullanarak dosyayı otomatik kapatıyoruz.
    """
    # Dosyayı yazma modunda aç (w modu)
    with open("merhaba.txt", "w", encoding="utf-8") as dosya:
        # write() metodu ile satır satır yazma
        dosya.write("Merhaba Dünya!\n")
        dosya.write("Python dosya işlemlerini öğreniyorum.\n")
        dosya.write("Bu çok eğlenceli!")

    print("✓ 'merhaba.txt' dosyası başarıyla oluşturuldu!")

# Test
# soru1_cozum()


# ============================================================================
# SORU 2: DOSYA OKUMA VE SATIR SAYMA (KOLAY)
# ============================================================================
"""
Bir önceki soruda oluşturduğunuz "merhaba.txt" dosyasını okuyun ve:
1. Dosyanın tüm içeriğini ekrana yazdırın
2. Dosyadaki toplam satır sayısını bulun ve yazdırın
3. Dosyadaki toplam karakter sayısını bulun ve yazdırın
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 2:
def soru2_cozum():
    """
    Dosya okuma ve içerik analizi.
    Farklı okuma metodlarını kullanıyoruz.
    """
    # Dosyayı okuma modunda aç
    with open("merhaba.txt", "r", encoding="utf-8") as dosya:
        # Tüm içeriği oku
        icerik = dosya.read()

    # İçeriği yazdır
    print("Dosya İçeriği:")
    print("-" * 40)
    print(icerik)
    print("-" * 40)

    # Satır sayısını bul (newline karakterine göre)
    satirlar = icerik.split('\n')
    satir_sayisi = len([s for s in satirlar if s])  # Boş satırları hariç tut

    # Karakter sayısı
    karakter_sayisi = len(icerik)

    print(f"\nToplam satır sayısı: {satir_sayisi}")
    print(f"Toplam karakter sayısı: {karakter_sayisi}")

# Test
# soru2_cozum()


# ============================================================================
# SORU 3: KULLANICI BİLGİLERİNİ KAYDETME (KOLAY-ORTA)
# ============================================================================
"""
Kullanıcıdan ad, soyad, yaş ve şehir bilgilerini alın.
Bu bilgileri "kullanici_bilgisi.txt" dosyasına düzenli bir formatta kaydedin.

Örnek çıktı formatı:
Ad: Ahmet
Soyad: Yılmaz
Yaş: 25
Şehir: İstanbul
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 3:
def soru3_cozum():
    """
    Kullanıcı bilgilerini dosyaya kaydetme.
    Format kullanarak düzenli çıktı oluşturuyoruz.
    """
    # Kullanıcıdan bilgileri al
    print("Kullanıcı Bilgilerini Girin:")
    print("-" * 40)
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    yas = input("Yaş: ")
    sehir = input("Şehir: ")

    # Bilgileri dosyaya yaz
    with open("kullanici_bilgisi.txt", "w", encoding="utf-8") as dosya:
        dosya.write(f"Ad: {ad}\n")
        dosya.write(f"Soyad: {soyad}\n")
        dosya.write(f"Yaş: {yas}\n")
        dosya.write(f"Şehir: {sehir}\n")

    print("\n✓ Bilgiler 'kullanici_bilgisi.txt' dosyasına kaydedildi!")

    # Dosyayı oku ve kontrol et
    print("\nKaydedilen bilgiler:")
    with open("kullanici_bilgisi.txt", "r", encoding="utf-8") as dosya:
        print(dosya.read())

# Test
# soru3_cozum()


# ============================================================================
# SORU 4: SAYILARI FILTRELEME (ORTA)
# ============================================================================
"""
"sayilar.txt" adında bir dosya oluşturun ve içine 1'den 50'ye kadar sayıları yazın.
(Her satırda bir sayı olacak)

Sonra bu dosyayı okuyun ve:
1. Sadece çift sayıları "cift_sayilar.txt" dosyasına yazın
2. Sadece tek sayıları "tek_sayilar.txt" dosyasına yazın
3. Her iki dosyadaki toplam sayıları ekrana yazdırın
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 4:
def soru4_cozum():
    """
    Dosyadan veri okuma, filtreleme ve yeni dosyalara yazma.
    Liste comprehension ve dosya işlemlerini birlikte kullanıyoruz.
    """
    # 1-50 arası sayıları dosyaya yaz
    with open("sayilar.txt", "w", encoding="utf-8") as dosya:
        for sayi in range(1, 51):
            dosya.write(f"{sayi}\n")
    print("✓ 'sayilar.txt' oluşturuldu")

    # Dosyayı oku ve sayıları listele
    with open("sayilar.txt", "r", encoding="utf-8") as dosya:
        sayilar = [int(satir.strip()) for satir in dosya.readlines()]

    # Çift sayıları filtrele ve kaydet
    cift_sayilar = [sayi for sayi in sayilar if sayi % 2 == 0]
    with open("cift_sayilar.txt", "w", encoding="utf-8") as dosya:
        for sayi in cift_sayilar:
            dosya.write(f"{sayi}\n")

    # Tek sayıları filtrele ve kaydet
    tek_sayilar = [sayi for sayi in sayilar if sayi % 2 != 0]
    with open("tek_sayilar.txt", "w", encoding="utf-8") as dosya:
        for sayi in tek_sayilar:
            dosya.write(f"{sayi}\n")

    # Sonuçları yazdır
    print(f"\n✓ Çift sayılar 'cift_sayilar.txt' dosyasına yazıldı")
    print(f"  Toplam çift sayı: {len(cift_sayilar)}")
    print(f"  Toplamları: {sum(cift_sayilar)}")

    print(f"\n✓ Tek sayılar 'tek_sayilar.txt' dosyasına yazıldı")
    print(f"  Toplam tek sayı: {len(tek_sayilar)}")
    print(f"  Toplamları: {sum(tek_sayilar)}")

# Test
# soru4_cozum()


# ============================================================================
# SORU 5: KELIME SAYACI (ORTA)
# ============================================================================
"""
"metin.txt" adında bir metin dosyası oluşturun ve içine birkaç cümle yazın.
Sonra bu dosyayı analiz eden bir program yazın:

1. Toplam kelime sayısı
2. Toplam karakter sayısı (boşluklar dahil)
3. Toplam satır sayısı
4. En uzun kelime
5. En kısa kelime

Sonuçları hem ekrana yazdırın hem de "metin_analiz.txt" dosyasına kaydedin.
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 5:
def soru5_cozum():
    """
    Metin dosyası analizi.
    String metodları ve dosya işlemlerini kullanarak detaylı analiz yapıyoruz.
    """
    # Örnek metin dosyası oluştur
    ornek_metin = """Python programlama dili öğrenmek çok eğlenceli.
Dosya işlemleri ile verilerimizi kalıcı olarak saklayabiliriz.
Bu alıştırma sayesinde dosya okuma ve yazma konusunda ustalaşıyoruz.
Python'un gücünü keşfetmek harika bir deneyim."""

    with open("metin.txt", "w", encoding="utf-8") as dosya:
        dosya.write(ornek_metin)
    print("✓ 'metin.txt' oluşturuldu\n")

    # Dosyayı oku ve analiz et
    with open("metin.txt", "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
        satirlar = dosya.readlines()

    # Analizler
    satirlar = icerik.split('\n')
    satir_sayisi = len([s for s in satirlar if s])  # Boş satırları hariç tut

    # Tüm kelimeleri al
    kelimeler = icerik.split()
    kelime_sayisi = len(kelimeler)
    karakter_sayisi = len(icerik)

    # Sadece alfabetik karakterlerden oluşan kelimeleri al
    temiz_kelimeler = [k.strip('.,!?;:') for k in kelimeler]
    temiz_kelimeler = [k for k in temiz_kelimeler if k]

    en_uzun = max(temiz_kelimeler, key=len)
    en_kisa = min(temiz_kelimeler, key=len)

    # Sonuçları hazırla
    sonuc = f"""METIN ANALİZ RAPORU
{'=' * 50}

Toplam Satır Sayısı    : {satir_sayisi}
Toplam Kelime Sayısı   : {kelime_sayisi}
Toplam Karakter Sayısı : {karakter_sayisi}
En Uzun Kelime         : {en_uzun} ({len(en_uzun)} karakter)
En Kısa Kelime         : {en_kisa} ({len(en_kisa)} karakter)
Ortalama Kelime Uzunluğu: {sum(len(k) for k in temiz_kelimeler) / len(temiz_kelimeler):.2f}

{'=' * 50}
"""

    # Ekrana yazdır
    print(sonuc)

    # Dosyaya kaydet
    with open("metin_analiz.txt", "w", encoding="utf-8") as dosya:
        dosya.write(sonuc)

    print("✓ Analiz sonuçları 'metin_analiz.txt' dosyasına kaydedildi!")

# Test
# soru5_cozum()


# ============================================================================
# SORU 6: ÖĞRENCİ NOT SİSTEMİ - CSV (ORTA-ZOR)
# ============================================================================
"""
Bir öğrenci not sistemi oluşturun. CSV formatında "ogrenci_notlari.csv" dosyası:

1. Dosyaya en az 5 öğrenci ekleyin (Ad, Soyad, Matematik, Fizik, Kimya notları)
2. Dosyayı okuyup her öğrencinin ortalamasını hesaplayın
3. Sınıf ortalamasını bulun
4. En yüksek ve en düşük ortalamaya sahip öğrenciyi bulun
5. Sonuçları "not_raporu.txt" dosyasına yazdırın
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 6:
def soru6_cozum():
    """
    CSV ile öğrenci not sistemi.
    CSV modülü kullanarak yapılandırılmış veri işleme.
    """
    import csv

    # Öğrenci verilerini hazırla
    ogrenciler = [
        ['Ad', 'Soyad', 'Matematik', 'Fizik', 'Kimya'],
        ['Ahmet', 'Yılmaz', 85, 90, 88],
        ['Ayşe', 'Demir', 92, 87, 95],
        ['Mehmet', 'Kaya', 78, 82, 80],
        ['Zeynep', 'Öz', 95, 93, 97],
        ['Can', 'Arslan', 88, 85, 90]
    ]

    # CSV dosyasına yaz
    with open('ogrenci_notlari.csv', 'w', newline='', encoding='utf-8') as dosya:
        csv_yazici = csv.writer(dosya)
        csv_yazici.writerows(ogrenciler)

    print("✓ 'ogrenci_notlari.csv' oluşturuldu\n")

    # CSV dosyasını oku ve analiz et
    with open('ogrenci_notlari.csv', 'r', encoding='utf-8') as dosya:
        csv_okuyucu = csv.DictReader(dosya)

        ogrenci_listesi = []
        tum_ortalamalar = []

        for satir in csv_okuyucu:
            ad = satir['Ad']
            soyad = satir['Soyad']
            mat = int(satir['Matematik'])
            fiz = int(satir['Fizik'])
            kim = int(satir['Kimya'])

            # Ortalama hesapla
            ortalama = (mat + fiz + kim) / 3

            ogrenci_listesi.append({
                'ad_soyad': f"{ad} {soyad}",
                'notlar': {'Matematik': mat, 'Fizik': fiz, 'Kimya': kim},
                'ortalama': ortalama
            })

            tum_ortalamalar.append(ortalama)

    # En yüksek ve en düşük ortalamayı bul
    en_yuksek = max(ogrenci_listesi, key=lambda x: x['ortalama'])
    en_dusuk = min(ogrenci_listesi, key=lambda x: x['ortalama'])
    sinif_ortalamasi = sum(tum_ortalamalar) / len(tum_ortalamalar)

    # Raporu oluştur
    rapor = f"""ÖĞRENCİ NOT RAPORU
{'=' * 70}

ÖĞRENČ NOT LİSTESİ:
{'-' * 70}
{'Ad Soyad':<20} {'Matematik':<12} {'Fizik':<12} {'Kimya':<12} {'Ortalama':<12}
{'-' * 70}
"""

    for ogr in ogrenci_listesi:
        rapor += f"{ogr['ad_soyad']:<20} "
        rapor += f"{ogr['notlar']['Matematik']:<12} "
        rapor += f"{ogr['notlar']['Fizik']:<12} "
        rapor += f"{ogr['notlar']['Kimya']:<12} "
        rapor += f"{ogr['ortalama']:<12.2f}\n"

    rapor += f"\n{'-' * 70}\n"
    rapor += f"SINIF ORTALAMASI: {sinif_ortalamasi:.2f}\n\n"
    rapor += f"EN YÜKSEK ORTALAMA: {en_yuksek['ad_soyad']} - {en_yuksek['ortalama']:.2f}\n"
    rapor += f"EN DÜŞÜK ORTALAMA : {en_dusuk['ad_soyad']} - {en_dusuk['ortalama']:.2f}\n"
    rapor += f"{'=' * 70}\n"

    # Ekrana yazdır
    print(rapor)

    # Dosyaya kaydet
    with open('not_raporu.txt', 'w', encoding='utf-8') as dosya:
        dosya.write(rapor)

    print("✓ Rapor 'not_raporu.txt' dosyasına kaydedildi!")

# Test
# soru6_cozum()


# ============================================================================
# SORU 7: JSON VERİ YÖNETİMİ (ORTA-ZOR)
# ============================================================================
"""
Bir kişisel kütüphane yönetim sistemi oluşturun:

1. "kutuphane.json" dosyası oluşturun
2. En az 5 kitap ekleyin (başlık, yazar, yıl, sayfa sayısı, okundu mu?)
3. Kitap ekleme fonksiyonu yazın
4. Okunmuş kitapları listeleyen fonksiyon yazın
5. Yazara göre kitap arama fonksiyonu yazın
6. Tüm kitapların toplam sayfa sayısını hesaplayan fonksiyon yazın
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 7:
def soru7_cozum():
    """
    JSON ile kütüphane yönetim sistemi.
    JSON modülü kullanarak yapılandırılmış veri saklama ve sorgulama.
    """
    import json

    # İlk kütüphane verisini oluştur
    kutuphane = {
        "kitaplar": [
            {
                "id": 1,
                "baslik": "Suç ve Ceza",
                "yazar": "Fyodor Dostoyevski",
                "yil": 1866,
                "sayfa": 671,
                "okundu": True
            },
            {
                "id": 2,
                "baslik": "1984",
                "yazar": "George Orwell",
                "yil": 1949,
                "sayfa": 328,
                "okundu": True
            },
            {
                "id": 3,
                "baslik": "Simyacı",
                "yazar": "Paulo Coelho",
                "yil": 1988,
                "sayfa": 208,
                "okundu": False
            },
            {
                "id": 4,
                "baslik": "Sefiller",
                "yazar": "Victor Hugo",
                "yil": 1862,
                "sayfa": 1463,
                "okundu": True
            },
            {
                "id": 5,
                "baslik": "Tutunamayanlar",
                "yazar": "Oğuz Atay",
                "yil": 1971,
                "sayfa": 724,
                "okundu": False
            }
        ]
    }

    # JSON dosyasına kaydet
    def kutuphane_kaydet(veri):
        """Kütüphane verisini JSON dosyasına kaydet"""
        with open('kutuphane.json', 'w', encoding='utf-8') as dosya:
            json.dump(veri, dosya, ensure_ascii=False, indent=4)

    # JSON dosyasından oku
    def kutuphane_yukle():
        """Kütüphane verisini JSON dosyasından yükle"""
        try:
            with open('kutuphane.json', 'r', encoding='utf-8') as dosya:
                return json.load(dosya)
        except FileNotFoundError:
            return {"kitaplar": []}

    # Kitap ekle
    def kitap_ekle(baslik, yazar, yil, sayfa, okundu=False):
        """Kütüphaneye yeni kitap ekle"""
        veri = kutuphane_yukle()

        # Yeni ID oluştur
        if veri["kitaplar"]:
            yeni_id = max(k["id"] for k in veri["kitaplar"]) + 1
        else:
            yeni_id = 1

        yeni_kitap = {
            "id": yeni_id,
            "baslik": baslik,
            "yazar": yazar,
            "yil": yil,
            "sayfa": sayfa,
            "okundu": okundu
        }

        veri["kitaplar"].append(yeni_kitap)
        kutuphane_kaydet(veri)
        print(f"✓ '{baslik}' kütüphaneye eklendi!")

    # Okunmuş kitapları listele
    def okunmus_kitaplar():
        """Okunmuş kitapları listele"""
        veri = kutuphane_yukle()
        okunmus = [k for k in veri["kitaplar"] if k["okundu"]]

        print("\nOKUNMUŞ KİTAPLAR:")
        print("-" * 60)
        for kitap in okunmus:
            print(f"📖 {kitap['baslik']} - {kitap['yazar']} ({kitap['yil']})")
        print(f"\nToplam: {len(okunmus)} kitap")

    # Yazara göre ara
    def yazara_gore_ara(yazar_adi):
        """Belirli bir yazarın kitaplarını bul"""
        veri = kutuphane_yukle()
        bulunan = [k for k in veri["kitaplar"]
                   if yazar_adi.lower() in k["yazar"].lower()]

        print(f"\n'{yazar_adi}' YAZARINA AİT KİTAPLAR:")
        print("-" * 60)
        if bulunan:
            for kitap in bulunan:
                durum = "✓ Okundu" if kitap["okundu"] else "○ Okunmadı"
                print(f"{durum} | {kitap['baslik']} ({kitap['yil']}) - {kitap['sayfa']} sayfa")
        else:
            print("Bu yazara ait kitap bulunamadı.")

    # Toplam sayfa sayısı
    def toplam_sayfa_sayisi():
        """Kütüphanedeki tüm kitapların toplam sayfa sayısı"""
        veri = kutuphane_yukle()
        toplam = sum(k["sayfa"] for k in veri["kitaplar"])
        okunmus_toplam = sum(k["sayfa"] for k in veri["kitaplar"] if k["okundu"])

        print(f"\nKÜTÜPHANE İSTATİSTİKLERİ:")
        print("-" * 60)
        print(f"Toplam kitap sayısı    : {len(veri['kitaplar'])}")
        print(f"Okunmuş kitap sayısı   : {sum(1 for k in veri['kitaplar'] if k['okundu'])}")
        print(f"Toplam sayfa sayısı    : {toplam:,}")
        print(f"Okunan sayfa sayısı    : {okunmus_toplam:,}")
        print(f"Okunmayan sayfa sayısı : {toplam - okunmus_toplam:,}")

    # İlk veriyi kaydet
    kutuphane_kaydet(kutuphane)
    print("✓ 'kutuphane.json' oluşturuldu\n")

    # Fonksiyonları test et
    okunmus_kitaplar()
    yazara_gore_ara("Orwell")
    toplam_sayfa_sayisi()

    # Yeni kitap ekle
    print("\n" + "=" * 60)
    kitap_ekle("İnce Memed", "Yaşar Kemal", 1955, 420, False)

# Test
# soru7_cozum()


# ============================================================================
# SORU 8: LOG DOSYASI YÖNETİMİ (ZOR)
# ============================================================================
"""
Bir log dosyası yönetim sistemi oluşturun:

1. "sistem.log" dosyasına farklı seviyelerde (INFO, WARNING, ERROR) loglar yazın
2. Her log kaydı tarih-saat damgası içersin
3. Log seviyesine göre filtreleme yapan fonksiyon yazın
4. Belirli bir tarih aralığındaki logları filtreleyen fonksiyon yazın
5. En çok tekrarlanan hata mesajını bulan fonksiyon yazın
6. Log istatistiklerini gösteren rapor oluşturun
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 8:
def soru8_cozum():
    """
    Log dosyası yönetim sistemi.
    Tarih-saat işlemleri, dosya okuma-yazma ve veri analizi.
    """
    from datetime import datetime, timedelta
    import random

    # Log yazma fonksiyonu
    def log_yaz(seviye, mesaj):
        """Belirtilen seviyede log kaydı oluştur"""
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_satiri = f"[{zaman}] [{seviye}] {mesaj}\n"

        with open("sistem.log", "a", encoding="utf-8") as dosya:
            dosya.write(log_satiri)

    # Örnek log kayıtları oluştur
    def ornek_loglar_olustur():
        """Test için örnek log kayıtları oluştur"""
        # Dosyayı temizle
        with open("sistem.log", "w", encoding="utf-8") as dosya:
            dosya.write("")

        mesajlar = {
            "INFO": [
                "Sistem başlatıldı",
                "Kullanıcı girişi yapıldı",
                "Veritabanı bağlantısı kuruldu",
                "Dosya yükleme tamamlandı",
                "Rapor oluşturuldu"
            ],
            "WARNING": [
                "Disk alanı azalıyor",
                "Bellek kullanımı yüksek",
                "Yavaş internet bağlantısı",
                "Eski sürüm kullanılıyor",
                "Geçici dosya sayısı fazla"
            ],
            "ERROR": [
                "Veritabanı bağlantı hatası",
                "Dosya bulunamadı",
                "Yetki hatası",
                "Ağ bağlantısı koptu",
                "Bellek yetersiz"
            ]
        }

        # 50 adet rastgele log kaydı oluştur
        for _ in range(50):
            seviye = random.choice(["INFO", "INFO", "INFO", "WARNING", "WARNING", "ERROR"])
            mesaj = random.choice(mesajlar[seviye])
            log_yaz(seviye, mesaj)

        print("✓ Örnek log kayıtları oluşturuldu\n")

    # Seviyeye göre filtrele
    def seviyeye_gore_filtrele(seviye):
        """Belirli seviyedeki logları filtrele"""
        with open("sistem.log", "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        filtrelenmis = [s for s in satirlar if f"[{seviye}]" in s]

        print(f"\n{seviye} SEVİYESİNDEKİ LOGLAR ({len(filtrelenmis)} adet):")
        print("-" * 80)
        for log in filtrelenmis[:10]:  # İlk 10 tanesini göster
            print(log.strip())
        if len(filtrelenmis) > 10:
            print(f"... ve {len(filtrelenmis) - 10} kayıt daha")

    # En çok tekrarlanan hata
    def en_cok_tekrarlanan_hata():
        """En çok tekrarlanan ERROR mesajını bul"""
        with open("sistem.log", "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        # Sadece ERROR loglarını al
        hatalar = [s for s in satirlar if "[ERROR]" in s]

        # Hata mesajlarını say
        hata_sayaci = {}
        for hata in hatalar:
            # Mesajı ayıkla
            mesaj = hata.split("[ERROR]")[1].strip()
            hata_sayaci[mesaj] = hata_sayaci.get(mesaj, 0) + 1

        if hata_sayaci:
            en_cok = max(hata_sayaci.items(), key=lambda x: x[1])
            print(f"\nEN ÇOK TEKRARLANAN HATA:")
            print("-" * 80)
            print(f"Hata: {en_cok[0]}")
            print(f"Tekrar Sayısı: {en_cok[1]}")

    # Log istatistikleri
    def log_istatistikleri():
        """Detaylı log istatistikleri oluştur"""
        with open("sistem.log", "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        toplam = len(satirlar)
        info_sayisi = len([s for s in satirlar if "[INFO]" in s])
        warning_sayisi = len([s for s in satirlar if "[WARNING]" in s])
        error_sayisi = len([s for s in satirlar if "[ERROR]" in s])

        rapor = f"""
LOG İSTATİSTİKLERİ RAPORU
{'=' * 80}

Toplam Log Kaydı  : {toplam}

Seviye Dağılımı:
  INFO    : {info_sayisi} ({info_sayisi/toplam*100:.1f}%)
  WARNING : {warning_sayisi} ({warning_sayisi/toplam*100:.1f}%)
  ERROR   : {error_sayisi} ({error_sayisi/toplam*100:.1f}%)

Sistem Sağlığı:
  {'✓ İyi' if error_sayisi < toplam * 0.1 else '⚠ Dikkat' if error_sayisi < toplam * 0.2 else '✗ Kritik'}

{'=' * 80}
"""
        print(rapor)

        # Raporu dosyaya kaydet
        with open("log_raporu.txt", "w", encoding="utf-8") as dosya:
            dosya.write(rapor)

        print("✓ Rapor 'log_raporu.txt' dosyasına kaydedildi!")

    # Tüm fonksiyonları çalıştır
    ornek_loglar_olustur()
    seviyeye_gore_filtrele("ERROR")
    en_cok_tekrarlanan_hata()
    log_istatistikleri()

# Test
# soru8_cozum()


# ============================================================================
# SORU 9: DOSYA YEDEKLEME SİSTEMİ (ZOR)
# ============================================================================
"""
Basit bir dosya yedekleme sistemi oluşturun:

1. Kullanıcının belirlediği bir dosyayı yedekleyin
2. Yedekleme sırasında tarih damgası ekleyin (dosya_2024_01_15_14_30.txt)
3. Aynı dosyanın birden fazla yedeğini tutun
4. Eski yedekleri listeleyen fonksiyon yazın
5. Bir dosyanın belirli bir yedeğini geri yükleyen fonksiyon yazın
6. Yedek sayısını sınırlayan (örn. son 5 yedek) fonksiyon yazın
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 9:
def soru9_cozum():
    """
    Dosya yedekleme ve geri yükleme sistemi.
    Dosya kopyalama, tarih işlemleri ve dosya yönetimi.
    """
    import os
    import shutil
    from datetime import datetime
    from pathlib import Path

    # Yedekleme dizinini oluştur
    YEDEK_DIZINI = "yedekler"
    Path(YEDEK_DIZINI).mkdir(exist_ok=True)

    def dosya_yedeyi(dosya_yolu):
        """Dosyayı tarih damgası ile yedekle"""
        if not os.path.exists(dosya_yolu):
            print(f"✗ Hata: '{dosya_yolu}' dosyası bulunamadı!")
            return None

        # Dosya adını ve uzantısını ayır
        dosya_adi = os.path.basename(dosya_yolu)
        ad, uzanti = os.path.splitext(dosya_adi)

        # Tarih damgası oluştur
        zaman_damgasi = datetime.now().strftime("%Y%m%d_%H%M%S")
        yedek_adi = f"{ad}_{zaman_damgasi}{uzanti}"
        yedek_yolu = os.path.join(YEDEK_DIZINI, yedek_adi)

        # Dosyayı kopyala
        shutil.copy2(dosya_yolu, yedek_yolu)
        print(f"✓ Yedekleme başarılı: {yedek_adi}")

        return yedek_yolu

    def yedekleri_listele(dosya_adi=None):
        """Mevcut yedekleri listele"""
        yedekler = os.listdir(YEDEK_DIZINI)

        if dosya_adi:
            # Belirli bir dosyanın yedeklerini filtrele
            ad, _ = os.path.splitext(dosya_adi)
            yedekler = [y for y in yedekler if y.startswith(ad + "_")]

        if not yedekler:
            print("Yedek dosya bulunamadı.")
            return []

        print(f"\nMEVCUT YEDEKLER ({len(yedekler)} adet):")
        print("-" * 80)
        print(f"{'No':<5} {'Dosya Adı':<40} {'Boyut':<15} {'Tarih':<20}")
        print("-" * 80)

        # Tarihe göre sırala (en yeni önce)
        yedekler.sort(reverse=True)

        for i, yedek in enumerate(yedekler, 1):
            yedek_yolu = os.path.join(YEDEK_DIZINI, yedek)
            boyut = os.path.getsize(yedek_yolu)

            # Dosya adından tarih bilgisini çıkar
            try:
                tarih_str = yedek.split('_')[-2] + '_' + yedek.split('_')[-1].split('.')[0]
                tarih = datetime.strptime(tarih_str, "%Y%m%d_%H%M%S")
                tarih_okunabilir = tarih.strftime("%Y-%m-%d %H:%M:%S")
            except:
                tarih_okunabilir = "Bilinmiyor"

            print(f"{i:<5} {yedek:<40} {boyut:>10} byte   {tarih_okunabilir}")

        return yedekler

    def yedek_geri_yukle(yedek_adi, hedef_yol=None):
        """Belirtilen yedeği geri yükle"""
        yedek_yolu = os.path.join(YEDEK_DIZINI, yedek_adi)

        if not os.path.exists(yedek_yolu):
            print(f"✗ Hata: '{yedek_adi}' yedeği bulunamadı!")
            return False

        # Hedef yol belirtilmemişse orijinal dosya adını kullan
        if hedef_yol is None:
            # Tarih damgasını kaldır
            ad_parcalari = yedek_adi.split('_')
            if len(ad_parcalari) >= 3:
                # Son iki parçayı (tarih damgası) kaldır
                orijinal_ad = '_'.join(ad_parcalari[:-2])
                # Uzantıyı ekle
                uzanti = os.path.splitext(yedek_adi)[1]
                hedef_yol = orijinal_ad + uzanti
            else:
                hedef_yol = yedek_adi

        # Geri yükle
        shutil.copy2(yedek_yolu, hedef_yol)
        print(f"✓ '{yedek_adi}' yedeği '{hedef_yol}' olarak geri yüklendi!")

        return True

    def eski_yedekleri_temizle(dosya_adi, max_yedek=5):
        """Belirlenen sayıdan fazla yedeği sil"""
        ad, _ = os.path.splitext(dosya_adi)
        tum_yedekler = os.listdir(YEDEK_DIZINI)

        # Belirli dosyanın yedeklerini filtrele
        dosya_yedekleri = [y for y in tum_yedekler if y.startswith(ad + "_")]

        if len(dosya_yedekleri) <= max_yedek:
            print(f"✓ Yedek sayısı limit dahilinde ({len(dosya_yedekleri)}/{max_yedek})")
            return

        # Tarihe göre sırala (en yeni önce)
        dosya_yedekleri.sort(reverse=True)

        # Fazla yedekleri sil
        silinecekler = dosya_yedekleri[max_yedek:]

        print(f"\n{len(silinecekler)} eski yedek siliniyor...")
        for yedek in silinecekler:
            yedek_yolu = os.path.join(YEDEK_DIZINI, yedek)
            os.remove(yedek_yolu)
            print(f"  ✗ Silindi: {yedek}")

        print(f"✓ Temizleme tamamlandı. Kalan yedek: {max_yedek}")

    # Sistem testi
    print("DOSYA YEDEKLEME SİSTEMİ")
    print("=" * 80)

    # Test dosyası oluştur
    test_dosya = "test_veri.txt"
    with open(test_dosya, "w", encoding="utf-8") as f:
        f.write(f"Test verisi - Oluşturulma zamanı: {datetime.now()}\n")
        f.write("Bu dosya yedekleme sistemi için oluşturulmuştur.\n")

    print(f"\n✓ Test dosyası oluşturuldu: {test_dosya}\n")

    # 3 farklı zamanda yedekleme yap
    print("Yedekleme işlemleri:")
    print("-" * 80)
    for i in range(3):
        # Dosyayı güncelle
        with open(test_dosya, "a", encoding="utf-8") as f:
            f.write(f"Güncelleme {i+1} - {datetime.now()}\n")

        dosya_yedeyi(test_dosya)
        import time
        time.sleep(1)  # Farklı zaman damgaları için bekle

    # Yedekleri listele
    yedek_listesi = yedekleri_listele(test_dosya)

    # Eski yedekleri temizle (son 2 yedeği tut)
    print("\n" + "=" * 80)
    eski_yedekleri_temizle(test_dosya, max_yedek=2)

    # Güncel listeyi göster
    print("\n" + "=" * 80)
    yedek_listesi = yedekleri_listele(test_dosya)

    # En eski yedeği geri yükle
    if yedek_listesi:
        print("\n" + "=" * 80)
        print("Geri yükleme işlemi:")
        print("-" * 80)
        en_eski = yedek_listesi[-1]
        yedek_geri_yukle(en_eski, "geri_yuklenen.txt")

# Test
# soru9_cozum()


# ============================================================================
# SORU 10: KİŞİSEL FİNANS TAKİP SİSTEMİ (ZOR)
# ============================================================================
"""
Kişisel finans takip sistemi oluşturun (CSV + JSON):

1. "gelir_gider.csv" dosyasında işlemleri saklayın (tarih, tip, kategori, tutar, açıklama)
2. Gelir ve gider ekleme fonksiyonları yazın
3. Aylık özet raporu oluşturun
4. Kategoriye göre harcama analizi yapın
5. Bütçe belirleme ve takip sistemi oluşturun (JSON)
6. Grafik verileri için çıktı hazırlayın
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 10:
def soru10_cozum():
    """
    Kişisel finans takip sistemi.
    CSV ve JSON kullanarak karmaşık veri yönetimi ve analizi.
    """
    import csv
    import json
    from datetime import datetime
    from collections import defaultdict

    # Dosya isimleri
    CSV_DOSYA = "gelir_gider.csv"
    JSON_DOSYA = "butce.json"

    # CSV başlangıç verileri
    def baslangic_verisi_olustur():
        """Test için başlangıç verileri oluştur"""
        islemler = [
            ['2024-01-05', 'Gelir', 'Maaş', 15000, 'Aylık maaş'],
            ['2024-01-07', 'Gider', 'Market', 850, 'Haftalık alışveriş'],
            ['2024-01-10', 'Gider', 'Ulaşım', 500, 'Aylık kart'],
            ['2024-01-12', 'Gider', 'Faturalar', 1200, 'Elektrik, su, internet'],
            ['2024-01-15', 'Gelir', 'Freelance', 3000, 'Web tasarım projesi'],
            ['2024-01-18', 'Gider', 'Yemek', 650, 'Restoran'],
            ['2024-01-20', 'Gider', 'Kıyafet', 1500, 'Kışlık mont'],
            ['2024-01-22', 'Gider', 'Eğlence', 400, 'Sinema ve kahve'],
            ['2024-01-25', 'Gider', 'Market', 920, 'Haftalık alışveriş'],
            ['2024-01-28', 'Gider', 'Sağlık', 350, 'Doktor muayenesi']
        ]

        with open(CSV_DOSYA, 'w', newline='', encoding='utf-8') as f:
            yazici = csv.writer(f)
            yazici.writerow(['Tarih', 'Tip', 'Kategori', 'Tutar', 'Açıklama'])
            yazici.writerows(islemler)

        # Bütçe verileri
        butce = {
            "aylik_butceler": {
                "Market": 2000,
                "Ulaşım": 500,
                "Faturalar": 1500,
                "Yemek": 1000,
                "Eğlence": 800,
                "Kıyafet": 1000,
                "Sağlık": 500
            },
            "tasarruf_hedefi": 5000
        }

        with open(JSON_DOSYA, 'w', encoding='utf-8') as f:
            json.dump(butce, f, ensure_ascii=False, indent=4)

        print("✓ Başlangıç verileri oluşturuldu\n")

    def islem_ekle(tarih, tip, kategori, tutar, aciklama):
        """Yeni gelir/gider işlemi ekle"""
        with open(CSV_DOSYA, 'a', newline='', encoding='utf-8') as f:
            yazici = csv.writer(f)
            yazici.writerow([tarih, tip, kategori, tutar, aciklama])

        print(f"✓ {tip} eklendi: {kategori} - {tutar} TL")

    def islemleri_oku():
        """Tüm işlemleri oku ve dict listesi olarak döndür"""
        with open(CSV_DOSYA, 'r', encoding='utf-8') as f:
            okuyucu = csv.DictReader(f)
            return list(okuyucu)

    def aylik_ozet():
        """Aylık gelir-gider özeti"""
        islemler = islemleri_oku()

        toplam_gelir = sum(float(i['Tutar']) for i in islemler if i['Tip'] == 'Gelir')
        toplam_gider = sum(float(i['Tutar']) for i in islemler if i['Tip'] == 'Gider')
        net_durum = toplam_gelir - toplam_gider

        rapor = f"""
AYLIK FİNANS ÖZETİ
{'=' * 70}

Toplam Gelir       : {toplam_gelir:>12,.2f} TL
Toplam Gider       : {toplam_gider:>12,.2f} TL
{'-' * 70}
Net Durum          : {net_durum:>12,.2f} TL

Durum: {'✓ Pozitif' if net_durum > 0 else '✗ Negatif' if net_durum < 0 else '○ Dengede'}
Tasarruf Oranı     : {(net_durum/toplam_gelir*100) if toplam_gelir > 0 else 0:>11,.1f}%

{'=' * 70}
"""
        print(rapor)
        return {'gelir': toplam_gelir, 'gider': toplam_gider, 'net': net_durum}

    def kategori_analizi():
        """Kategoriye göre harcama analizi"""
        islemler = islemleri_oku()

        # Kategoriye göre grupla
        kategori_toplam = defaultdict(float)
        for islem in islemler:
            if islem['Tip'] == 'Gider':
                kategori_toplam[islem['Kategori']] += float(islem['Tutar'])

        # Bütçe bilgilerini oku
        with open(JSON_DOSYA, 'r', encoding='utf-8') as f:
            butce_veri = json.load(f)

        print("\nKATEGORİ BAZLI HARCAMA ANALİZİ")
        print("=" * 90)
        print(f"{'Kategori':<15} {'Harcama':<15} {'Bütçe':<15} {'Kalan':<15} {'Durum':<15}")
        print("-" * 90)

        toplam_gider = sum(kategori_toplam.values())

        for kategori, harcama in sorted(kategori_toplam.items(), key=lambda x: x[1], reverse=True):
            butce = butce_veri['aylik_butceler'].get(kategori, 0)
            kalan = butce - harcama
            oran = (harcama / butce * 100) if butce > 0 else 0

            if oran > 100:
                durum = "⚠ Aşım"
            elif oran > 80:
                durum = "⚡ Dikkat"
            else:
                durum = "✓ İyi"

            print(f"{kategori:<15} {harcama:>12,.2f} TL {butce:>12,.2f} TL "
                  f"{kalan:>12,.2f} TL {durum:<15}")

        print("-" * 90)
        print(f"{'TOPLAM':<15} {toplam_gider:>12,.2f} TL")
        print("=" * 90)

    def butce_takip():
        """Bütçe hedefi takibi"""
        islemler = islemleri_oku()

        toplam_gelir = sum(float(i['Tutar']) for i in islemler if i['Tip'] == 'Gelir')
        toplam_gider = sum(float(i['Tutar']) for i in islemler if i['Tip'] == 'Gider')
        tasarruf = toplam_gelir - toplam_gider

        with open(JSON_DOSYA, 'r', encoding='utf-8') as f:
            butce_veri = json.load(f)

        hedef = butce_veri['tasarruf_hedefi']
        hedefe_ulasilma = (tasarruf / hedef * 100) if hedef > 0 else 0

        print("\nTASARRUF HEDEFİ TAKİBİ")
        print("=" * 70)
        print(f"Tasarruf Hedefi   : {hedef:>12,.2f} TL")
        print(f"Mevcut Tasarruf   : {tasarruf:>12,.2f} TL")
        print(f"Hedefe Ulaşma     : {hedefe_ulasilma:>11,.1f}%")
        print(f"Kalan             : {hedef - tasarruf:>12,.2f} TL")

        # Progress bar
        bar_uzunluk = 50
        dolu = int(bar_uzunluk * min(hedefe_ulasilma, 100) / 100)
        bar = "█" * dolu + "░" * (bar_uzunluk - dolu)
        print(f"\n[{bar}] {min(hedefe_ulasilma, 100):.1f}%")

        if tasarruf >= hedef:
            print("\n✓ Tebrikler! Tasarruf hedefinize ulaştınız!")
        elif hedefe_ulasilma >= 80:
            print("\n⚡ Hedefinize yaklaşıyorsunuz! Devam edin!")
        elif hedefe_ulasilma >= 50:
            print("\n○ İyi gidiyorsunuz. Biraz daha dikkatli olun.")
        else:
            print("\n⚠ Harcamalarınızı gözden geçirmeniz gerekebilir.")

        print("=" * 70)

    def grafik_verisi_hazirla():
        """Grafik çizimi için veri hazırla (dict formatında)"""
        islemler = islemleri_oku()

        # Kategoriye göre giderler
        kategori_gider = defaultdict(float)
        for islem in islemler:
            if islem['Tip'] == 'Gider':
                kategori_gider[islem['Kategori']] += float(islem['Tutar'])

        # Günlük bakiye değişimi
        gunluk_bakiye = []
        bakiye = 0

        for islem in islemler:
            tutar = float(islem['Tutar'])
            if islem['Tip'] == 'Gelir':
                bakiye += tutar
            else:
                bakiye -= tutar

            gunluk_bakiye.append({
                'tarih': islem['Tarih'],
                'bakiye': bakiye
            })

        grafik_veri = {
            'kategori_giderler': dict(kategori_gider),
            'gunluk_bakiye': gunluk_bakiye,
            'ozet': {
                'toplam_gelir': sum(float(i['Tutar']) for i in islemler if i['Tip'] == 'Gelir'),
                'toplam_gider': sum(float(i['Tutar']) for i in islemler if i['Tip'] == 'Gider')
            }
        }

        # JSON dosyasına kaydet
        with open('grafik_verisi.json', 'w', encoding='utf-8') as f:
            json.dump(grafik_veri, f, ensure_ascii=False, indent=4)

        print("\n✓ Grafik verisi 'grafik_verisi.json' dosyasına kaydedildi")
        print("\nKategori Gider Dağılımı:")
        for kategori, tutar in sorted(kategori_gider.items(), key=lambda x: x[1], reverse=True):
            yuzde = (tutar / sum(kategori_gider.values())) * 100
            bar = "█" * int(yuzde / 2)
            print(f"{kategori:<15} {bar} {yuzde:.1f}%")

    # Ana program
    print("KİŞİSEL FİNANS TAKİP SİSTEMİ")
    print("=" * 70)

    baslangic_verisi_olustur()
    aylik_ozet()
    kategori_analizi()
    butce_takip()
    grafik_verisi_hazirla()

    # Yeni işlem ekleme örneği
    print("\n" + "=" * 70)
    print("Yeni işlem ekleme örneği:")
    print("-" * 70)
    islem_ekle('2024-01-30', 'Gider', 'Market', 750, 'Aylık temel gıda')

# Test
# soru10_cozum()


# ============================================================================
# BONUS SORU 11: MARKDOWN NOTLAR VE TODO LİSTESİ (ORTA-ZOR)
# ============================================================================
"""
Markdown formatında not tutma ve todo sistemi:

1. Not ekleme (başlık, içerik, etiketler)
2. Todo ekleme (görev, öncelik, durum)
3. Notları markdown dosyasına kaydetme
4. Todo'ları tamamlama/güncelleme
5. Etiketlere göre notları filtreleme
6. Önceliğe göre todo sıralaması
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 11:
def soru11_cozum():
    """
    Markdown not ve todo sistemi.
    Markdown formatında veri saklama ve yönetme.
    """
    import json
    from datetime import datetime

    NOTLAR_DOSYA = "notlarim.md"
    TODO_DOSYA = "todo_listesi.json"

    def not_ekle(baslik, icerik, etiketler=None):
        """Markdown formatında not ekle"""
        if etiketler is None:
            etiketler = []

        tarih = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Markdown formatında not
        markdown_not = f"""
## {baslik}

**Tarih:** {tarih}
**Etiketler:** {', '.join(['`' + e + '`' for e in etiketler])}

{icerik}

---

"""

        # Dosyaya ekle
        with open(NOTLAR_DOSYA, 'a', encoding='utf-8') as f:
            f.write(markdown_not)

        print(f"✓ Not eklendi: '{baslik}'")

    def todo_ekle(gorev, oncelik='orta', kategori='genel'):
        """Todo listesine görev ekle"""
        # Mevcut todoları oku
        try:
            with open(TODO_DOSYA, 'r', encoding='utf-8') as f:
                todos = json.load(f)
        except FileNotFoundError:
            todos = {"gorevler": []}

        yeni_todo = {
            "id": len(todos["gorevler"]) + 1,
            "gorev": gorev,
            "oncelik": oncelik,
            "kategori": kategori,
            "durum": "bekliyor",
            "olusturulma": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        todos["gorevler"].append(yeni_todo)

        # Kaydet
        with open(TODO_DOSYA, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=4)

        print(f"✓ Todo eklendi: '{gorev}' (Öncelik: {oncelik})")

    def todo_tamamla(todo_id):
        """Todo'yu tamamlandı olarak işaretle"""
        with open(TODO_DOSYA, 'r', encoding='utf-8') as f:
            todos = json.load(f)

        for todo in todos["gorevler"]:
            if todo["id"] == todo_id:
                todo["durum"] = "tamamlandi"
                todo["tamamlanma"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                break

        with open(TODO_DOSYA, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=4)

        print(f"✓ Todo #{todo_id} tamamlandı!")

    def todo_listele():
        """Tüm todo'ları listele"""
        try:
            with open(TODO_DOSYA, 'r', encoding='utf-8') as f:
                todos = json.load(f)
        except FileNotFoundError:
            print("Henüz todo bulunmuyor.")
            return

        # Öncelik sırası
        oncelik_sirasi = {"yuksek": 1, "orta": 2, "dusuk": 3}

        # Sırala: Önce durum (bekliyor önce), sonra öncelik
        gorevler = sorted(todos["gorevler"],
                         key=lambda x: (x["durum"] == "tamamlandi",
                                      oncelik_sirasi.get(x["oncelik"], 2)))

        print("\nTODO LİSTESİ")
        print("=" * 80)

        bekleyen = [g for g in gorevler if g["durum"] == "bekliyor"]
        tamamlanan = [g for g in gorevler if g["durum"] == "tamamlandi"]

        if bekleyen:
            print("\n🔴 BEKLEYEN GÖREVLER:")
            print("-" * 80)
            for todo in bekleyen:
                oncelik_icon = "🔥" if todo["oncelik"] == "yuksek" else "⚡" if todo["oncelik"] == "orta" else "○"
                print(f"{oncelik_icon} #{todo['id']}: {todo['gorev']}")
                print(f"   Kategori: {todo['kategori']} | Öncelik: {todo['oncelik']} | {todo['olusturulma']}")

        if tamamlanan:
            print("\n✓ TAMAMLANAN GÖREVLER:")
            print("-" * 80)
            for todo in tamamlanan:
                print(f"✓ #{todo['id']}: {todo['gorev']}")
                print(f"   {todo.get('tamamlanma', 'Bilinmiyor')}")

        print("\n" + "=" * 80)
        print(f"Toplam: {len(gorevler)} görev ({len(bekleyen)} bekliyor, {len(tamamlanan)} tamamlandı)")

    # Sistem demo
    print("MARKDOWN NOTLAR VE TODO SİSTEMİ")
    print("=" * 80)

    # Notlar dosyasını başlat
    with open(NOTLAR_DOSYA, 'w', encoding='utf-8') as f:
        f.write("# Notlarım\n\n")
        f.write("Bu dosya otomatik olarak oluşturulmuştur.\n\n")
        f.write("---\n")

    print("\nNot ekleme örnekleri:")
    print("-" * 80)
    not_ekle("Python Dosya İşlemleri",
             "Bugün Python'da dosya okuma ve yazma işlemlerini öğrendim. "
             "CSV ve JSON formatları çok kullanışlı.",
             ["python", "egitim", "dosya"])

    not_ekle("Proje Fikirleri",
             "1. Kişisel blog sistemi\n2. Todo uygulaması\n3. Not defteri",
             ["projeler", "fikirler"])

    print("\nTodo ekleme örnekleri:")
    print("-" * 80)
    todo_ekle("Python egzersizlerini tamamla", "yuksek", "egitim")
    todo_ekle("Proje dokümantasyonu yaz", "orta", "proje")
    todo_ekle("Kod review yap", "yuksek", "is")
    todo_ekle("Blog yazısı hazırla", "dusuk", "kisisel")
    todo_ekle("Veritabanı optimizasyonu", "orta", "teknik")

    # Listeyi göster
    todo_listele()

    # Bir todo'yu tamamla
    print("\n" + "=" * 80)
    print("Todo tamamlama:")
    print("-" * 80)
    todo_tamamla(1)
    todo_tamamla(3)

    # Güncellenmiş listeyi göster
    todo_listele()

    print(f"\n✓ Notlar '{NOTLAR_DOSYA}' dosyasına kaydedildi")
    print(f"✓ Todo'lar '{TODO_DOSYA}' dosyasına kaydedildi")

# Test
# soru11_cozum()


# ============================================================================
# BONUS SORU 12: DOSYA ŞİFRELEME VE GÜVENLİK (CHALLENGE)
# ============================================================================
"""
Basit dosya şifreleme sistemi:

1. Metin dosyasını şifreleyen fonksiyon (Caesar cipher veya Base64)
2. Şifrelenmiş dosyayı çözen fonksiyon
3. Şifre korumalı arşiv oluşturma
4. Dosya bütünlüğü kontrolü (checksum)
5. Güvenli dosya silme (üzerine yazarak)
"""

# TODO: Çözümünüzü buraya yazın


# ÇÖZÜM 12:
def soru12_cozum():
    """
    Dosya şifreleme ve güvenlik sistemi.
    Temel şifreleme teknikleri ve dosya güvenliği.
    """
    import base64
    import hashlib
    import os

    def sifrele_base64(girdi_dosya, cikti_dosya):
        """Base64 ile dosya şifreleme"""
        with open(girdi_dosya, 'rb') as f:
            veri = f.read()

        # Base64 şifreleme
        sifreli = base64.b64encode(veri)

        with open(cikti_dosya, 'wb') as f:
            f.write(sifreli)

        print(f"✓ '{girdi_dosya}' şifrelendi -> '{cikti_dosya}'")

    def sifrele_caesar(girdi_dosya, cikti_dosya, kaydirma=3):
        """Caesar cipher ile şifreleme"""
        with open(girdi_dosya, 'r', encoding='utf-8') as f:
            metin = f.read()

        sifreli_metin = ""
        for karakter in metin:
            if karakter.isalpha():
                # ASCII değerini al
                ascii_deger = ord(karakter)

                # Büyük/küçük harf kontrolü
                if karakter.isupper():
                    sifreli = chr((ascii_deger - 65 + kaydirma) % 26 + 65)
                else:
                    sifreli = chr((ascii_deger - 97 + kaydirma) % 26 + 97)

                sifreli_metin += sifreli
            else:
                sifreli_metin += karakter

        with open(cikti_dosya, 'w', encoding='utf-8') as f:
            f.write(sifreli_metin)

        print(f"✓ '{girdi_dosya}' Caesar cipher ile şifrelendi (Kaydırma: {kaydirma})")

    def coz_base64(girdi_dosya, cikti_dosya):
        """Base64 şifresini çöz"""
        with open(girdi_dosya, 'rb') as f:
            sifreli = f.read()

        # Base64 çözme
        cozulmus = base64.b64decode(sifreli)

        with open(cikti_dosya, 'wb') as f:
            f.write(cozulmus)

        print(f"✓ '{girdi_dosya}' şifresi çözüldü -> '{cikti_dosya}'")

    def coz_caesar(girdi_dosya, cikti_dosya, kaydirma=3):
        """Caesar cipher şifresini çöz"""
        # Ters kaydırma yaparak çöz
        sifrele_caesar(girdi_dosya, cikti_dosya, -kaydirma)
        print(f"✓ Caesar cipher çözüldü")

    def dosya_hash_hesapla(dosya_yolu):
        """Dosyanın SHA256 hash'ini hesapla"""
        sha256 = hashlib.sha256()

        with open(dosya_yolu, 'rb') as f:
            # Büyük dosyalar için parça parça oku
            for blok in iter(lambda: f.read(4096), b''):
                sha256.update(blok)

        return sha256.hexdigest()

    def dosya_butunluk_kontrol(dosya_yolu, beklenen_hash):
        """Dosya bütünlüğünü kontrol et"""
        mevcut_hash = dosya_hash_hesapla(dosya_yolu)

        if mevcut_hash == beklenen_hash:
            print(f"✓ Dosya bütünlüğü doğrulandı")
            return True
        else:
            print(f"✗ Dosya bütünlüğü bozulmuş!")
            print(f"  Beklenen: {beklenen_hash}")
            print(f"  Mevcut  : {mevcut_hash}")
            return False

    def guvenli_sil(dosya_yolu, gecis=3):
        """Dosyayı güvenli şekilde sil (üzerine yazarak)"""
        if not os.path.exists(dosya_yolu):
            print(f"✗ Dosya bulunamadı: {dosya_yolu}")
            return

        dosya_boyutu = os.path.getsize(dosya_yolu)

        # Birden fazla geçişle üzerine yaz
        with open(dosya_yolu, 'wb') as f:
            for i in range(gecis):
                f.seek(0)
                # Rastgele veri yaz
                f.write(os.urandom(dosya_boyutu))
                f.flush()
                os.fsync(f.fileno())

        # Dosyayı sil
        os.remove(dosya_yolu)
        print(f"✓ '{dosya_yolu}' güvenli şekilde silindi ({gecis} geçiş)")

    # Demo
    print("DOSYA ŞİFRELEME VE GÜVENLİK SİSTEMİ")
    print("=" * 80)

    # Test dosyası oluştur
    test_dosya = "gizli_bilgi.txt"
    gizli_icerik = """Bu dosya gizli bilgiler içermektedir.

Kullanıcı Adı: admin
Şifre: Super_Gizli_123
API Key: abc123def456ghi789

Bu bilgiler şifrelenmeli!
"""

    with open(test_dosya, 'w', encoding='utf-8') as f:
        f.write(gizli_icerik)

    print(f"\n✓ Test dosyası oluşturuldu: '{test_dosya}'")

    # Hash hesapla
    print("\n" + "-" * 80)
    print("Dosya bütünlüğü kontrolü:")
    orijinal_hash = dosya_hash_hesapla(test_dosya)
    print(f"SHA256 Hash: {orijinal_hash}")

    # Base64 şifreleme
    print("\n" + "-" * 80)
    print("Base64 şifreleme:")
    sifrele_base64(test_dosya, "gizli_base64.enc")

    # Caesar cipher şifreleme
    print("\n" + "-" * 80)
    print("Caesar Cipher şifreleme:")
    sifrele_caesar(test_dosya, "gizli_caesar.enc", kaydirma=7)

    # Şifreleri çöz
    print("\n" + "-" * 80)
    print("Şifreleri çözme:")
    coz_base64("gizli_base64.enc", "cozulmus_base64.txt")
    coz_caesar("gizli_caesar.enc", "cozulmus_caesar.txt", kaydirma=7)

    # Bütünlük kontrolü
    print("\n" + "-" * 80)
    print("Çözülen dosya bütünlüğü kontrolü:")
    dosya_butunluk_kontrol("cozulmus_base64.txt", orijinal_hash)

    # Güvenli silme
    print("\n" + "-" * 80)
    print("Güvenli dosya silme:")
    guvenli_sil("gizli_base64.enc")
    guvenli_sil("gizli_caesar.enc")

    print("\n" + "=" * 80)
    print("✓ Tüm güvenlik işlemleri tamamlandı!")

# Test
# soru12_cozum()


# ============================================================================
# TÜM ÇÖZÜMLERİ ÇALIŞTIRMAK İÇİN
# ============================================================================

def tum_cozumleri_calistir():
    """Tüm egzersiz çözümlerini sırayla çalıştır"""
    import time

    cozumler = [
        ("SORU 1: Temel Dosya Yazma", soru1_cozum),
        ("SORU 2: Dosya Okuma ve Satır Sayma", soru2_cozum),
        ("SORU 3: Kullanıcı Bilgilerini Kaydetme", soru3_cozum),
        ("SORU 4: Sayıları Filtreleme", soru4_cozum),
        ("SORU 5: Kelime Sayacı", soru5_cozum),
        ("SORU 6: Öğrenci Not Sistemi - CSV", soru6_cozum),
        ("SORU 7: JSON Veri Yönetimi", soru7_cozum),
        ("SORU 8: Log Dosyası Yönetimi", soru8_cozum),
        ("SORU 9: Dosya Yedekleme Sistemi", soru9_cozum),
        ("SORU 10: Kişisel Finans Takip", soru10_cozum),
        ("BONUS 11: Markdown Notlar ve TODO", soru11_cozum),
        ("BONUS 12: Dosya Şifreleme", soru12_cozum),
    ]

    print("=" * 80)
    print("TÜM DOSYA İŞLEMLERİ EGZERSİZLERİ")
    print("=" * 80)

    for i, (baslik, fonksiyon) in enumerate(cozumler, 1):
        print(f"\n\n{'#' * 80}")
        print(f"# {i}. {baslik}")
        print(f"{'#' * 80}\n")

        try:
            fonksiyon()
        except Exception as e:
            print(f"\n✗ Hata oluştu: {e}")

        if i < len(cozumler):
            time.sleep(1)  # Sonraki egzersize geçmeden önce kısa bekleme

    print("\n\n" + "=" * 80)
    print("TÜM EGZERSİZLER TAMAMLANDI!")
    print("=" * 80)


if __name__ == "__main__":
    print(__doc__)
    print("\nHer bir soruyu test etmek için fonksiyon çağrılarının")
    print("başındaki '#' işaretini kaldırın.")
    print("\nÖrnek: soru1_cozum()")
    print("\nTüm çözümleri çalıştırmak için:")
    print("tum_cozumleri_calistir()")
