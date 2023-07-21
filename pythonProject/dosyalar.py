def not_hesapla(satır):
    satır = satır[:-1]
    öğrencinin_not_listesi = satır.split(",")

    ortalama_not = (int(öğrencinin_not_listesi[1]) + int(öğrencinin_not_listesi[2]) + int(öğrencinin_not_listesi[3])) / 3
    if ortalama_not>=90:
        print("{}: AA".format(öğrencinin_not_listesi[0]))

    elif ortalama_not<=90 and ortalama_not>80:
        print("{}: AB".format(öğrencinin_not_listesi[0]))

    elif ortalama_not<=80 and ortalama_not>70:
        print("{}: BB".format(öğrencinin_not_listesi[0]))

    elif ortalama_not<=70 and ortalama_not>60:
        print("{}: BC".format(öğrencinin_not_listesi[0]))

    elif ortalama_not<=60 and ortalama_not>50:
        print("{}: CC".format(öğrencinin_not_listesi[0]))

    elif ortalama_not<=50 and ortalama_not>40:
        print("{}: CD".format(öğrencinin_not_listesi[0]))
    else :
        print("{}: FF".format(öğrencinin_not_listesi[0]))
    if ortalama_not<40 :
        dersten_kalanlar.append(öğrencinin_not_listesi[0])
    elif ortalama_not>=40:
        dersten_gecenler.append(öğrencinin_not_listesi[0])

with open("bilgiler.txt","r",encoding="utf-8") as file:
    dersten_gecenler=[]
    dersten_kalanlar =[]
    for i in file:
        not_hesapla(i)


with open("derstengecenler.txt","w",encoding="utf-8") as file:
    for j in dersten_gecenler:
        file.write("Dersten geçti:{}\n".format(j))

with open("derstenkalanlar.txt","w",encoding="utf-8") as file:
    for k in dersten_kalanlar:
        file.write("Dersten kaldı:{}\n".format(k))



