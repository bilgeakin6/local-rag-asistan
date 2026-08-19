# Local RAG AI Assistant - Sistem Analizi Projesi

Bu proje, Microsoft AI Summer Program kapsamında geliştirilmiş, internet bağlantısı gerektirmeyen (tamamen çevrimdışı) bir Yerel RAG (Retrieval-Augmented Generation) Soru-Cevap asistanıdır.

## Projenin Amacı
Konya Teknik Üniversitesi yemekhanesi tedarik zinciri sürecindeki problemleri ve çözüm önerilerini içeren sistem analizi raporu veritabanı olarak kullanılmıştır. Asistan, büyük metin yığınları arasında anlamsal arama yaparak kullanıcının sorularına rapor içerisinden doğru ve net cevaplar bulmayı hedefler.

## Kullanılan Teknolojiler
* **Microsoft Foundry Local SDK:** Yerel yapay zeka modelinin çevrimdışı çalıştırılması.
* **SQLite:** Belgelerin ve metin parçalarının (chunk) saklandığı yerel veritabanı.
* **Python:** Veri işleme ve Komut Satırı Arayüzü (CLI) geliştirme.

## Nasıl Çalıştırılır?
1. Gerekli kütüphaneyi kurun: `pip install foundry-local-sdk`
2. Veritabanını oluşturmak ve metinleri kaydetmek için: `python main.py`
3. Asistan arayüzünü başlatmak ve soru sormak için: `python asistan.py`
