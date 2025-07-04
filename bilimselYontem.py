import pandas as pd
import time

# Global veri saklama yapilari
veritoplama_data = {}
tutarlilik_data = {}
data = {}

data_file = "data.csv"
veritoplama_file = "veritoplama.csv"
tutarlilik1_file = "tutarlilik1.csv"

#arayüz ve fonksiyon algoritmaları
class Arayuz:
    def arayuz(self):
        print(" -- BİLİMSEL YÖNTEM PROG --")
        print("başlatmak için (1) veya çıkmak için (q)")

        while True:
            sec = input("---: ")
            if sec == "1":
                print("başlatılıyor...")
                bilim = BilimMain()
                bilim.problem()
                bilim.veritoplama()
                bilim.yapilantahmin()
                bilim.tutarlilik()
                bilim.hipotez()
                bilim.sonuc()

            elif sec == "q":
                print("çıkıldı")
                break

            else:
                print("Geçersiz giriş. Lütfen (1) veya (q) girin.")

#ana class
class BilimMain:
    def problem(self):
        while True:
            problemsor = input("Problem tespit edildi mi (e/h): ").lower()

            if problemsor == "e":
                sor1 = input("Tespit edilen problemi yazınız: ")
                print(f"Tespit edilen problem: {sor1}")
                break

            elif problemsor == "h":
                print("Problemi tespit etmeden gelmeyin.")
                break

            else:
                print("Lütfen sadece 'e' veya 'h' girin.")

    def veritoplama(self):
        global veritoplama_data

        print("Problemin verilerini giriniz")
        input("Açıklama: ")  # sor kullanilmiyor

        gozlem = input("Yapılan gözlem bilgisi: ")
        deney = int(input("Yapılan deney numarası (başarı puanı 0-10):"))
        
        agrup = float(input("A grubunun deneyinde gerçekleşen doğruluk payı(0-100) =")) #yapılan deneyin başarı raporu
        bgrup = float(input("B grubunun deneyinde gerçekleşen doğruluk payı(0-100) ="))
        sonuchesapla = (agrup + bgrup)/2
        
        """ bunun yapılmasının sebebi iki grubun da deneyin nasıl gerçekleştiğini,doğrulanabilirlik durumunu sınamaktır,
        ki bu da aslına bakılırsa oldukça verim alınabilir."""
        

        try:
            deney = float(deney)
            hesap = deney / 2
            veritoplama_data = {
                "Gözlem Bilgisi": [gozlem],
                "Başarı Puanı": [deney],
                "Hesaplanan Puan": [hesap],
                "A grubu deney başarısı" : [agrup],
                "B grubu deney başarısı" : [bgrup],
                "2 Grubun deney doğruluğu(hesaplanmış)" : [sonuchesapla]
            }

            df = pd.DataFrame(veritoplama_data)
            print("Toplanan veri:")
            print(df)

        except ValueError:
            print("Deney değeri sayı olmalı.")

    def yapilantahmin(self):
        tahmin = input("Yapılan tahminleri giriniz: ")
        print(f"Yapılan tahmin: {tahmin}")

    def tutarlilik(self):
        global tutarlilik_data

        try:
            print("Yapılan tahminler, deneyler, gözlemler tutarlılık (0-100)")
            gozlem = float(input("Gözlem puanı: "))
            tahminle = float(input("Tahmin doğruluk oranı: "))
            veri = float(input("Verinin güvenilirliği: "))
            verikaynak = input("Verinin kaynakları (varsa): ")

            tutarlilik_data = {
                "Gözlem Puanı": [gozlem],
                "Tahmin Doğruluk Oranı": [tahminle],
                "Verinin Doğruluğu": [veri],
                "Veri Kaynakları": [verikaynak]
            }
            enyuksekdeger1 = max(gozlem,tahminle,veri) #en yüksek değeri vericek
            enkucukdeger2 = min(gozlem,tahminle,veri) # en kucuk değeri vericek
            print(f"en büyük değerler = {enyuksekdeger1}")
            print(f"en küçük değerler = {enkucukdeger2}")
            

            df = pd.DataFrame(tutarlilik_data)
            print(" -- Tutarlılık Tablosu --")
            print(df)

        except ValueError:
            print("Lütfen sayısal alanlara geçerli bir sayı girin.")

    def hipotez(self):
        global data

        print(" -- Hipotez Kurma --")
        print("""Lütfen her şeyi kesin kurama ulaştıracak şekilde yazınız.her işlemde ve her alanda gerçek sonuçlarla rapor,veri
              ve benzeri kullanılabilir.ayrıca sayısal veri girmeyiniz tamamen alfabetik olucak şekilde yapınız,
              ve idda,yorum,tahmin gibi alanlarda rastgele 
              işlemler yapmayınız herşey mantık alanında olmasına dikkat edin!
              
                 bilimsel tespit = -yanlışlanabilir olması
                                 -tekrarlanabilir olması
                                 -somut olmalıdır
                aksi takdirde bilimdışı veya sözdebilim sınıfına girer.""")

        yapan = input("Araştırmayı yapan kişi: ")
        ana_dusunce = input("Hipotezin ana düşüncesi: ")
        savunma = input("Savunması: ")
        arastirma = input("Araştırması (kaynak): ")
        gozlem = input("Gözlemler: ")
        tahmin = input("Tahminler: ")
        idda = input("Yapılan iddialar: ")
        yorum = input("yorumlar:")
        notiste = input("eklenecek not: ")

        data = {
            "Araştırmayı Yürüten": [yapan],
            "Ana Düşünce": [ana_dusunce],
            "Savunma": [savunma],
            "Araştırma (Kaynak ile)": [arastirma],
            "Gözlemler": [gozlem],
            "Tahminler": [tahmin],
            "Ortaya Atılan İddialar": [idda],
            "yorumlar" : [yorum],
            "Notlar" : [notiste]
            
        }

        print("Yapılandırılıyor...")
        time.sleep(2.5)
        df = pd.DataFrame(data)
        print(" -- İnşa Edilen Hipotez Verileri --\n")
        print(df)

    def sonuc(self):
        print(" -- Veri Sonucu --")
        
        #enyuksekdeger = max(tutarlilik_data) ---#çalışabilecek kodlar (opsiyonel)
        #enkucukdeger = min(tutarlilik_data)
        #print(enyuksekdeger, enkucukdeger)

        df = pd.DataFrame(veritoplama_data)
        df1 = pd.DataFrame(tutarlilik_data)
        df2 = pd.DataFrame(data)

        print(df)
        print(df1)
        print(df2)

        try:
            df2.to_csv(data_file, index=False)
            print("data.csv dosyasına kaydedildi")

            df.to_csv(veritoplama_file, index=False)
            print("veritoplama.csv dosyasına kaydedildi")

            df1.to_csv(tutarlilik1_file, index=False)
            print("tutarlılık1.csv dosyasına kaydedildi")

        except Exception as e:
            print(f"Dosya kaydetme hatası: {e}")

        print("Program sona erdirildi...")


if __name__ == "__main__":
    arayuz = Arayuz()
    arayuz.arayuz()