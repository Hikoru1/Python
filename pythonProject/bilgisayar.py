# bir listede olan sadece sayı olanları ekrana bastırın bunu yaparken try except kullan
# 0-100 arası rastgele 3 sayı belirlesin ve bu sayıları listeye atasın


import random
sayılar_listesi = []
while True:
        sayı = random.randint(0,100)
        sayılar_listesi.append(sayı)
        if len(sayılar_listesi) == 10 :
                break

kelimeler =["ibrahim","Mahmut","fdsdgfsdg","fdshgffg"]

i = 0
i = int (i)
for i in range(len(kelimeler)):

        yeni = kelimeler[i]
        sayılar_listesi.append(yeni)
        i+=1
print(sayılar_listesi)

for i in sayılar_listesi:
        try:
                i = int(i)
                print(i)

        except:
                pass














