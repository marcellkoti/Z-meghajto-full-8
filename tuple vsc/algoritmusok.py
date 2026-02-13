#1.feladat
#ELJÁRÁS:
#Definíció
def Koszones():
    #pass
    print("Hello, szia, szeva!")

#Függvény definíció
def Osszead(a,b):
    osszeg=a+b
    #print
    #return osszeg
    return a+b





#Hívás
print("Itt köszönök:")
Koszones()
#Hívás 2
ossz=Osszead(3,5)
print(ossz)
print(Osszead(4,7),Osszead(6,9),Osszead(12,65)/2)
Koszones()
Koszones()
#100 elemű lista amelybe 1000 és 5000 közötti számokat teszünk
import random
lista = []
for i in range(100):
   lista.append (random.randint(999,5001))
print(lista)

#Számítsuk ki a sorozat elemeinek az átlagát
#1.tétel: Összegzés(sorozatszámítás) tétele
#Tétele:

def Osszegzes(A):
    N=len(A)
    szum = 0
    for i in range(1,N,1):
        szum += A[i]
    return szum
print(f"A lista elemeinek átlaga {Osszegzes(lista)/len(lista)}")

#2. Tétel Maximum kiválasztás
#Hívás

def Maxkivalasztas (A):
    N=len(A)
    maxi=0
    for i in range(0,N,1):
        if A[maxi]<A[i]:
            maxi = 1
    return maxi


maxindex = Maxkivalasztas(lista)
print(f"A sororzat legnagyobb eleme: {lista[maxindex]}, amely a {maxindex+1}. helyen van.")
















