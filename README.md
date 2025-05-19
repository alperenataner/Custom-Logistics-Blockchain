# Gümrük ve Lojistik Blockchain Takip Sistemi

Bu proje, gümrük ve lojistik süreçlerini blockchain teknolojisi kullanarak güvenli ve şeffaf bir şekilde takip etmeyi sağlayan modern bir uygulamadır.

## 🚀 Özellikler

- **Blockchain Tabanlı Takip**: Tüm gönderiler blockchain üzerinde güvenli bir şekilde saklanır
- **Modern Kullanıcı Arayüzü**: CustomTkinter ile tasarlanmış şık ve kullanıcı dostu arayüz
- **Gerçek Zamanlı Durum Güncellemeleri**: Gönderilerin durumunu anlık olarak takip edebilme
- **Güvenlik Kontrolü**: Blockchain bütünlüğünü kontrol etme özelliği
- **Detaylı Gönderi Bilgileri**: Her gönderi için kapsamlı bilgi takibi

## 📋 Gönderi Takip Süreci

1. **Gönderi Oluşturma**
   - Otomatik takip numarası oluşturma
   - Gönderici ve alıcı bilgileri
   - Gönderi açıklaması ve değeri
   - Başlangıç durumu atama

2. **Durum Güncellemeleri**
   - Gümrük İşlemlerinde
   - Gümrük İşlemi Tamamlandı
   - Yolda
   - Teslim Edildi

3. **Blockchain Güvenliği**
   - Her işlem blockchain'e kaydedilir
   - Hash değerleri ile veri bütünlüğü korunur
   - Zincir bütünlüğü kontrol edilebilir

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler

- Python 3.x
- CustomTkinter (Modern GUI Framework)
- SHA-256 Hash Algoritması
- JSON Veri Formatı

### Gereksinimler

```bash
pip install customtkinter
```

## 💻 Kurulum ve Çalıştırma

1. Projeyi klonlayın:
```bash
git clone [repo-url]
```

2. Gerekli kütüphaneyi yükleyin:
```bash
pip install customtkinter
```

3. Uygulamayı çalıştırın:
```bash
python customs_gui.py
```

## 📱 Kullanım

1. **Yeni Gönderi Oluşturma**
   - "Yeni Gönderi Oluştur" butonuna tıklayın
   - Gerekli bilgileri doldurun
   - "Gönderi Oluştur" butonuna tıklayın

2. **Gönderi Sorgulama**
   - "Gönderi Sorgula" butonuna tıklayın
   - Takip numarasını girin
   - "Sorgula" butonuna tıklayın

3. **Durum Güncelleme**
   - "Gönderi Güncelle" butonuna tıklayın
   - Takip numarasını girin
   - Yeni durumu seçin
   - "Durumu Güncelle" butonuna tıklayın

4. **Blockchain Görüntüleme**
   - "Blockchain Görüntüle" butonuna tıklayın
   - Tüm blokları ve işlemleri görüntüleyin

## 🔒 Güvenlik

- Her blok, önceki bloğun hash değerini içerir
- Veri değişiklikleri hash değerlerini etkiler
- Blockchain bütünlüğü otomatik kontrol edilebilir

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Açıklama'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👥 İletişim

Proje Sahibi - [GitHub Profilim](https://github.com/alperenataner)

Proje Linki: [https://github.com/alperenataner/Customs-Logistics-Blockchain](https://github.com/alperenataner/Custom-Logistics-Blockchain) 
