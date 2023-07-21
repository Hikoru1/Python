"""

bir fonksiyon yazılır:
    toplam adında bir değiken tanımlanır
    bu toplam değişkeni range fonksiyonunda gezinen bir i sayisi ile eğer i sayisi tam bölerse
    toplam değişenine atanır ve yeni toplam değişkeni oluşur
    toplam değişkeni sayiya eşitse return fonksiyonu ile alınır

    for döngüsü ile i sayisinin range(1,1001) arasında dolaşarak def fonksiyonundaki sayi değişkeni belirlenir.
    mükemmel(sayi) fonksiyonu kullanılarak sonuca ulaşılır.
"""


def mükemmel(sayi):

    toplam = 0

    for i in range(1,sayi):
        if sayi % i == 0:
            toplam += i

    return toplam == sayi

for i in range (1,1001):

    if mükemmel(i):
        print("Mükemmel sayi:",i)