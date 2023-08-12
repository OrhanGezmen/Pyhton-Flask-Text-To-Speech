# Pyhton-Flask-Text-To-Speech

Bu basit Flask uygulaması, girilen metni ses dosyasına dönüştürerek kullanıcılara dinleme veya indirme seçeneği sunar.

## Başlangıç

Aşağıdaki adımları takip ederek uygulamayı yerelde çalıştırabilirsiniz.

1. Gerekli Kütüphaneleri Kurma

   Uygulamanın düzgün çalışması için gerekli kütüphaneleri kurun.

   ```bash
   pip install Flask gTTS os
   Uygulamayı Çalıştırma

Terminalde proje dizininde aşağıdaki komutu çalıştırarak Flask uygulamanızı başlatın:

  **python app.py**
  Uygulama şimdi yerelde http://localhost:5000 adresinde çalışıyor olmalı.

Kullanım
Tarayıcıda http://localhost:5000 adresine gidin.

Metin kutusuna dönüştürmek istediğiniz metni girin.

"Dönüştür" düğmesine tıklayın.

"Play" bağlantısına tıklayarak dönüştürülen sesi dinleyebilirsiniz.

"Download" bağlantısına tıklayarak ses dosyasını indirebilirsiniz.

## Notlar
Bu uygulama gTTS (Google Text-to-Speech) kütüphanesini kullanarak çalışır.
Geliştirme veya özelleştirme yapmak isterseniz, kodu inceleyebilir ve uygulamayı özelleştirebilirsiniz.
Güvenlik ve kullanıcı deneyimini artırmak için ek önlemler almayı unutmayin
