file=open("sutaz_vbehu.txt","r")
pocitadlo=0
min_cas=0
min_meno=0
for line in file:
    line=line.strip()
    meno,cas=line.split()
    if pocitadlo==0:
        min_cas=int(cas)
    if int(cas)<min_cas:
        min_cas=int(cas)
        min_meno=meno

    print("Súťažiaci", meno,"dobehol do cieľa za",cas,"sekund")

    pocitadlo+=1

print("Pocet zucastnenych sportovcov:",pocitadlo)
minuty=min_cas//60
sekundy=min_cas%60
print("Najrychlejsi bol", min_meno,"dobehol do ciela za",minuty,"minut a",sekundy,"sekund")