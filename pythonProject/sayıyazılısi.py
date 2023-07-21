

def pisagor():
    liste=[]
    for i in range(1,101):
        for j in range(i,101):
            for c in range(j,101):
                if i **2 + j**2 == c**2:
                    liste.append(i,j,c)
    return liste

pisagor()
