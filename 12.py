file=open("bus_vytazenost.txt","r")
pocitadlo=-1
zastavky=[]
zastavka=""
cislo=""
kapacita=0
nastup=0
vystup=0
max_prestup=0
max_zastavka=""
for riadok in file:
    riadok=riadok.strip()

    if pocitadlo==-1:
        kapacita=int(riadok)
        kapacita2=0
    else:
        nastup,vystup,zastavka=riadok.split(maxsplit=2)

        kapacita2=kapacita2+int(nastup)-int(vystup)
        if kapacita2>kapacita:
            print("na zastavke",zastavka,"prekrocil autobus kapacitu")
            if max_prestup<kapacita2-kapacita:
                max_prestup=kapacita2-kapacita
                max_zastavka=zastavka
        zastavky.append(zastavka)
        zastavka=""
        nastup=""
        vystup=""
    pocitadlo+=1

print("najviac autobus prekrocil kapacitu na zastavke",max_zastavka,"o pocet",max_prestup,"ludi")
print(" ,".join(zastavky))
print("pocet zastavok:",pocitadlo)