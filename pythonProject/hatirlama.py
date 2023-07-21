
onlar=["","on","yirmi" "otuz" "kırk" "elli" "altmış" "yetmiş" "seksen" "doksan"]
birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]

def yazılıs(sayi):
    birlerbasamagi= sayi%10
    onlarbasamagi=sayi//10


    return onlar[onlarbasamagi] + " " + birler[birlerbasamagi]


sayı = int(input("Bir sayi girin:"))

print(yazılıs(sayı))