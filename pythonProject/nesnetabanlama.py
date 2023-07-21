class çalışan():
    def __init__(self,isim, maaş,departman):
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgileri_göster(self):
        print("Bilgiler gösteriliyor")
        print("İsim: {}\nMaaş: {}\nDepartman: {}".format(self.isim,self.maaş,self.departman))

    def bilgi_ekle(self,bilgi):

        self.departman = bilgi
        print("Bilgi değişti")


class yönetici(çalışan):
    pass


yönetici=çalışan("Abdullah","4000","İnsan Kaynakarı")

yönetici.bilgileri_göster()
