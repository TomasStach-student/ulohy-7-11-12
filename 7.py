import random

ziaci=int(input("zadaj pocet ziakov:"))
otazky=int(input("zadaj pocet otazok:"))

z=[]
o=[]
while len(z)!=ziaci:
    x=random.randint(1,ziaci)
    if not z:
        z.append(x)
    else:
        if x not in z:
            z.append(x)
        else:
            pass
while len(o)!=ziaci:
    y = random.randint(1, otazky)
    if not o:
        o.append(y)
    else:
        if y not in o:
            o.append(y)
        else:
            pass

o1=[]
poc=0
while len(o1)!=ziaci:
    q=random.randint(1, otazky)
    if not o1:
        o1.append(o[0])
        o.remove(o[0])
    else:
        if q%2==0 and o1[poc]%2==1 and q not in o1:
            o1.append(q)
            poc+=1
        if q%2==1 and o1[poc]%2==0 and q not in o1:
            o1.append(q)
            poc+=1
o=o1

print(z)
print(o)
