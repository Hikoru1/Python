

class hayvan_sınıfı():
    def __init__(self, eşeyli_üreme, çok_hücreli, hareket_kabiliyeti, gelişmiş_sinir_sistemi):
        self.eşeyli_üreme = eşeyli_üreme
        self.çok_hücreli = çok_hücreli
        self.hareket_kabiliyeti = hareket_kabiliyeti
        self.gelişmiş_sinir_sistemi = gelişmiş_sinir_sistemi
    def bilgileri_göster(self):
        print("Hayvanların Genel Özellikleri:\n{}\n{}\n{}\n{}".format(self.eşeyli_üreme,self.çok_hücreli,self.hareket_kabiliyeti,self.gelişmiş_sinir_sistemi))




class Köpekler(hayvan_sınıfı):
    def __init__(self,eşeyli_üreme,çok_hücreli,hareket_kabiliyeti,gelişmiş_sinir_sistemi, köpek_türü,köpeğin_ömrü,boyut):
        super().__init__(eşeyli_üreme,çok_hücreli,hareket_kabiliyeti,gelişmiş_sinir_sistemi)
        self.köpek_türü = köpek_türü
        self.köpeğin_ömrü = köpeğin_ömrü
        self.boyut = boyut
        print("Köpek türünün spesifik özellikleri:\n{}\n{}\n{}".format(self.köpek_türü,self.köpeğin_ömrü,self.boyut))

class Kuşlar(hayvan_sınıfı):
    def __init__(self,eşeyli_üreme,çok_hücreli,hareket_kabiliyeti,gelişmiş_sinir_sistemi,tüy_uzunluğu,kanat_genişliği,beslenme_türü):
        super().__init__(eşeyli_üreme,çok_hücreli,hareket_kabiliyeti,gelişmiş_sinir_sistemi)
        self.tüy_uzunluğu = tüy_uzunluğu
        self.kanat_genişliği = kanat_genişliği
        self.beslenme_türü = beslenme_türü
        print("Kuş türünün spesifik özellikler:\n{}\n{}\n{}".format(self.tüy_uzunluğu,self.kanat_genişliği,self.beslenme_türü))
    def __str__(self):
        return "Kuşlar uçabilen hayvanlardır...."



print("------------------------\nHayvanların Özellikleri\n-------------------------")






while True:

    işlem = input("Lütfen bir işlem seçiniz:")
    print("Çıkmak için 'q' ya basın...")

    if işlem == "1":
        tür = input("Köpek türü:")
        boyut = input("Köpek boyutu:")
        ortalama_ömür = input("Ortalama ömrü:")
        köpek = Köpekler("Eşeyli Üreme", "Çok hücreli", "Hareket kabiliyeti", "Gelişmiş sinir sistemi", tür,ortalama_ömür, boyut)

        köpek.bilgileri_göster()
    elif işlem == "2":
        tüy_uzunluğu = input("Tüy uzunluğu:")
        kanat_genişliği = input("Kanat genişliği:")
        beslenme_türü = input("Beslenme türü:")
        kuş = Kuşlar("Eşeyli Üreme", "Çok hücreli", "Hareket kabiliyeti", "Gelişmiş sinir sistemi",tüy_uzunluğu,kanat_genişliği,beslenme_türü)

        kuş.bilgileri_göster()
        print(kuş)





















