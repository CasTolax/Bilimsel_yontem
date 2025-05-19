import pandas as pd
import time

# Global veri saklama yapilari
veritoplama_data = {}
tutarlilik_data = {}
data = {}

data_file = "data.txt"
veritoplama_file = "veritoplama.txt"
tutarlilik1_file = "tutarlilik1.txt"


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
        deney = input("Yapılan deney numarası (başarı puanı 0-10): ")

        try:
            deney = float(deney)
            hesap = deney / 2
            veritoplama_data = {
                "Gözlem Bilgisi": [gozlem],
                "Başarı Puanı": [deney],
                "Hesaplanan Puan": [hesap]
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

            df = pd.DataFrame(tutarlilik_data)
            print(" -- Tutarlılık Tablosu --")
            print(df)

        except ValueError:
            print("Lütfen sayısal alanlara geçerli bir sayı girin.")

    def hipotez(self):
        global data

        print(" -- Hipotez Kurma --")
        print("Lütfen her şeyi kesin kurama ulaştıracak şekilde yazınız.")

        yapan = input("Araştırmayı yapan kişi: ")
        ana_dusunce = input("Hipotezin ana düşüncesi: ")
        savunma = input("Savunması: ")
        arastirma = input("Araştırması (kaynak): ")
        gozlem = input("Gözlemler: ")
        tahmin = input("Tahminler: ")
        idda = input("Yapılan iddialar: ")

        data = {
            "Araştırmayı Yürüten": [yapan],
            "Ana Düşünce": [ana_dusunce],
            "Savunma": [savunma],
            "Araştırma (Kaynak ile)": [arastirma],
            "Gözlemler": [gozlem],
            "Tahminler": [tahmin],
            "Ortaya Atılan İddialar": [idda]
        }

        print("Yapılandırılıyor...")
        time.sleep(2.5)
        df = pd.DataFrame(data)
        print(" -- İnşa Edilen Hipotez Verileri --\n")
        print(df)

    def sonuc(self):
        print(" -- Veri Sonucu --")

        df = pd.DataFrame(veritoplama_data)
        df1 = pd.DataFrame(tutarlilik_data)
        df2 = pd.DataFrame(data)

        print(df)
        print(df1)
        print(df2)

        try:
            df2.to_csv(data_file, index=False)
            print("data.txt dosyasına kaydedildi")

            df.to_csv(veritoplama_file, index=False)
            print("veritoplama.txt dosyasına kaydedildi")

            df1.to_csv(tutarlilik1_file, index=False)
            print("tutarlılık1.txt dosyasına kaydedildi")

        except Exception as e:
            print(f"Dosya kaydetme hatası: {e}")

        print("Program sona erdirildi...")


if __name__ == "__main__":
    arayuz = Arayuz()
    arayuz.arayuz()