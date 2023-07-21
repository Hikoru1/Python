print("""***************************

Sayi tahmini.... 1-50 arasi

*******************************""")

import random

sayi = random.randint(1,50)
tahmin_hakkı= 7
while True:
    sayı =int(input("Bir sayi girin:"))

    if sayı>sayi:
        print("Daha düşük bir sayi girin")
        tahmin_hakkı-=1

    elif sayı<sayi:
        print("Daha yüksek bir sayi girin")
        tahmin_hakkı-=1

    else:
        print("Tebrikler sayimiz:",sayi)
        break

    if tahmin_hakkı==0:
        print("Tahmin hakkınız bitmiştir...")
        break




