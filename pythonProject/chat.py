
class hayvan_sınıfı():


    def __init__(self,eşeyli_üreme ="Eşeyli Üreme",çok_hücreli = "Çok hücreli",hareket_kabiliyeti = "Kas ve iskelet sistemi",gelişmiş_sinir_sistemi = "Gelişmiş sinir sisteni "):
        self.eşeyli_üreme = eşeyli_üreme
        self.çok_hücreli = çok_hücreli
        self.hareket_kabiliyeti = hareket_kabiliyeti
        self.gelişmiş_sinir_sistemi = gelişmiş_sinir_sistemi


class köpekler(hayvan_sınıfı):

    def __init__(self,boyut,ömür,tür):
        self.boyut = boyut
        self.ömür = ömür
        self.tür= tür

        if self.tür == "Golden" :
            self.boyut= "1 Metre"
            self.ömür ="10 Yıl"
            print("Üreme tipi: {}\nHücre tipi: {}\nHareket kabiliyeti: {}\nKas ve iskelet sistemi: {}\nKöpeğin boyutu: {}\nKöpeğin Ortalama ömrü: {}\nKöpeğin cinsi: {}".format(self.eşeyli_üreme,self.çok_hücreli,self.hareket_kabiliyeti,self.gelişmiş_sinir_sistemi,self.boyut, self.ömür,self.tür))
        elif self.tür == "Rodvaydır" :
            self.boyut= "1.10 Metre"
            self.ömür ="12 Yıl"
            print("Köpeğin boyutu: {}\nKöpeğin Ortalama ömrü: {}\nKöpeğin cinsi: {}".format(self.boyut, self.ömür,self.tür))



class kuşlar(hayvan_sınıfı):

    def __init__(self,gaga_tipi,kanat_genişliği,max_irtifa):

        self.gaga_tipi = gaga_tipi
        self.kanat_genişliği = kanat_genişliği
        self.max_irtifa = max_irtifa

class atlar(hayvan_sınıfı):

    def __init__(self,hız,boyut,tüy_uzunluğu):
        self.hız = hız
        self.boyut = boyut
        self.tüy_uzunluğu = tüy_uzunluğu


print("-----------------------------------------------"
      
      
      "Hayvan Sınıfları...."
      
      "1. Lütfen köpeğin türünü yazın..."
      "-----------------------------------------------")

while True:


    işlem = int(input("Lütfen işlem tipini seçiniz:"))

    if işlem == 1:
        tür = input("Lütfen köpeğin türünü girin:")
        köpek = köpekler("","","","","","",tür)

        break
















