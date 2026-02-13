#Generáljon egy -100 és 100 közötti számot és határozza meg, hogy pozitív vagy negatív vagy 0-a e?
#Valamint határozza meg a 10-es helyiérték számjegyét!
import random
szam=random.randint(-100,100)
print(szam)
if szam > 0:
    print("A szám Pozitív")
elif  szam == 0:
    print("A szám 0")
else:
    print("A szám negatív")





#1. Készítsen programot, amely Celsius értéket vált át Fahrenheité ÉS fordítva

fvagyc = input("mértékegység :(C/F)").upper()
while fvagyc!="C" and fvagyc!="F":
    print("Nem megfelelő a mértékegység")
    fvagyc = input("mértékegység :(C/F)").upper()
fok=int(input("Mennyi a kiinduló egység: "))


if fvagyc == "C":
    f = (fok*1.8)+32
    print(f"{fok}°C átváltva {f} Farenheit lesz")
elif fvagyc =="F":
    c = (fok-32)/1.8
    print(f"{fok} Farenheit átváltva {c} °C lesz")
else:
    print("Nem megfelelő mértékegység!")



