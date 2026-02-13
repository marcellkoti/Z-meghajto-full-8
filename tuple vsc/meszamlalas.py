#Feladat: Mennyi 2000 alati 3-mal osztható szám van a sorozatban
import random
lista = []
for i in range(100):
    lista.append(random.randint(999,5001))
print(lista)

#A[i]<2000 and A[i]%3 == 0


def KicsiHarmadDarab(A):
    N = len(A)
    db = 0
    for i in range(0,N,1):
        if A[i]<2000 and A[i]%3 == 0:
            db+=1
    return db

dbszam = KicsiHarmadDarab(lista)
print(f"A listában 2000 alatti 3-mal oszthtó számok összege: {dbszam}")

#4.tétel: Eldöntés tétele
#Van e benne 2000-es szám?
#T tulajdonság: A[i]==2000
#NEM T tulajdonság: A[i]!=2000
def VanE2000(A):
    N = len(A)
    i = 0
    while(i<N and A[i]!=2000):
        i+=1
    if (i<N):
        return True
    else:
        return False
if(lista.__contains__(2000)):
    print("VAN e 2000-es szám a sorozatban")
else:
    print("NINCS e 2000-es szám a sorozatban")

    















