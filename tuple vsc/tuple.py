hetnapjai =("hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap")



print(hetnapjai)
print(hetnapjai[1])
for nap in hetnapjai:
    print(nap)
print(len(hetnapjai))
print(hetnapjai[len(hetnapjai)-1])
print(hetnapjai[-1])

for i in range(len(hetnapjai)):
    print(hetnapjai[i])


#Lista
#Dinamikus
#Deklaráció
tanulok=[]
tanarok=["Madarasz","Prohászka"]
print(tanarok)

#Feltöltés
tanulok.append("Köteles")
print(tanulok)
tanulok.append("Szecsko")
print(tanulok)
tanarok.insert(1,"Krasznahorkai")
print(tanarok)
for tanar in tanarok:
    print(tanar)
tanulok.append(73245612434)
tanulok.append(True)
print(tanulok)
tanulok.remove(True)
print(tanulok)
tanulok.clear()
print(tanulok)
print(tanarok.index("Madarasz"))
#Kérjünk be a felhazsnálótól 20 számot
#100 és 320 között
#(Figyeljen a heles érték megadására)
#Az értékeket tárolja el egy sorozatba
lista=[]
szam=int(input("Kérek egy számot 100 és 320 között"))
for i in range(4):
    while szam < 100 or szam > 320:
        print("Hibás érték", end='')
        szam=int(input("Kérek egy számot 100 és 320 között"))
    lista.append(szam)
    szam=int(input(f"Kérem a {i+2}-dik számot 100 és 320 között"))
lista.append(szam)
print(lista)

#Vegye ki a sorozatból a legnagyobb elemet
legnagyobb = max(lista)
lista.remove(legnagyobb)
print(lista)
lista.remove(min(lista))
print(lista)



