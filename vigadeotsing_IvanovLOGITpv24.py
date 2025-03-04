from math import *
print("Ruudu karakteristikud")
try:
    a=int(input("Sisesta ruudu külje pikkus => "))
    if a<=0:
        print(("0 and negatiivsed arvud ei saa sisestada!"))
    else:
        S=a**2
        print("Ruudu pindala", S)
        P=4*a
        print("Ruudu ümbermõõt", P)
        di=a*sqrt(2)
        print("Ruudu diagonaal", round(di,2))
        print("Ristküliku karakteristikud")
except:
        print("Külje suurus on vaja int formaadis sisestada")
try:
    b=int(input("Sisesta ristküliku 1. külje pikkus => "))
    c=int(input("Sisesta ristküliku 2. külje pikkus => "))
    if b<=0 and c<=0:
        print(("0 and negatiivsed arvud ei saa sisestada!"))
    else:
        S=b*c
        print("Ristküliku pindala", (S))
        P=2*(b+c)
        print("Ristküliku ümbermõõt", (P))
        di=sqrt(b*2+c*2)
        print("Ristküliku diagonaal", round(di))
        print("Ringi karakteristikud")
except:
    print("Ristküljeku suurus on vaja int formaadis sisestada")

try:
    r=float(input("Sisesta ringi raadiusi pikkus => "))
    if r<=0:
        print(("0 and negatiivsed arvud ei saa sisestada!"))
    else:
        d=2*r
        print("Ringi läbimõõt", (d))
        S=pi*r*2
        print("Ringi pindala", round(S))
        C=2*pi*r
        print("Ringjoone pikkus", round(C))
except: 
    print("Ringi suurus on vaja int formaadis sisestada")