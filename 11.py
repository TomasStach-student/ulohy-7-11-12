file=open("sutaz_vbehu.txt","r")
meno=""
cas=""
max_cas=0
max_meno=""
pocitadlo=0
for riadok in file:
    riadok = riadok.strip()
    for char in riadok:
        if char.isdigit():
            cas+=str(char)
        if char!=" " and not char.isdigit():
            meno+=char

    if pocitadlo==0:
        max_cas=int(cas)
        max_meno=meno
    elif int(cas)<max_cas:
        max_cas=int(cas)
        max_meno=meno

    print("Súťažiaci",meno,"dobehol do cieľa za",cas, "sekund")
    meno=""
    cas=""
    pocitadlo+=1

minuty=int(max_cas)//60
sekundy=int(max_cas)%60

print("Počet zúčastnených športovcov:", pocitadlo)
print("Najrychlejsi bol ", max_meno," s casom : ", minuty," minut a ",sekundy," sekund")