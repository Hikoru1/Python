import math

print("""
hesap makinesi

1-Mutlak değer alma
2- Faktöriyel döndürme
3- Birinci değerin ikinci değer bölümünden kalan
4- Verilen değerlerin hepsinin toplamı
5-İki değerin EBOB'u
6- Euler sabiti ile dört işlem
""")


while True:
    sondeğer = int(sondeğer)
    işlem = int(input("Bir işlem seçiniz:"))

    if işlem == 1:
        değer = int(input("Bir değer giriniz:"))
        print(math.fabs(değer))
        sondeğer = math.fabs(değer)
    elif işlem ==2:
        değer = int(input("Bir değer giriniz:"))
        print(math.factorial(değer))

    elif işlem ==3:
        birincideğer = int(input("Birinci değer:"))
        ikincideğer = int(input("İkinci değer:"))
        print(math.fmod(birincideğer,ikincideğer))

    elif işlem==4:
        print("Sayilari girin ve toplamak istediğinizde '00' basın")
        liste=[]
        while True:
            değer = int(input("Toplanacak sayi:"))
            liste.append(değer)
            if değer == 00:
                print(math.fsum(liste))
                break
    elif işlem ==5 :
        değer1= int(input("Lütfen birinci değeri girin:"))
        değer2= int(input("Lütfen ikinci değeri girin:"))
        print(math.gcd(değer1,değer2))
    elif işlem == 6 :
        euler = math.e
        print("Euler sayısı:",euler)


