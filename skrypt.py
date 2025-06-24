import random
import funkcje as f
import Karta
import Reka
import licytacja as l

kolory=['C', 'D', 'H', 'S']
talia=[]
for i in kolory:
    for j in range(2, 15):
        talia.append(Karta.Karta(i, j))
random.shuffle(talia)
karty={"N": Reka.Reka(talia[0:13]), "E": Reka.Reka(talia[13:26]), "S": Reka.Reka(talia[26:39]), "W": Reka.Reka(talia[39:52])}
karty["N"].reka.sort(key=lambda x: (x.kolor, x.wartosc))
karty["S"].reka.sort(key=lambda x: (x.kolor, x.wartosc))

lewyNS=0
wzial="W"
kolejnosc=["N", "E", "S", "W", "N", "E", "S"]
lic=[]
koniec= False
print(f'Twoja ręka: {karty["S"].reka}')

while not koniec:
    lic.append(l.licytuj(kolejnosc[len(lic)%4+2], karty[kolejnosc[len(lic)%4+2]], lic))
    print(f'{kolejnosc[len(lic)%4+1]}: {lic[-1]}')
    try:
        if lic[-1]=='pass' and lic[-2]=='pass' and lic[-3]=='pass' and len(lic)>3: koniec=True
    except: pass

atut=lic[-4][1:]
if lic[-4]=='pass': exit()
print(f'Kontrakt: {lic[-4]}')

for i in karty.values():
    for j in i.reka:
        if j.kolor==atut: j.atu=True

for j in range(13):
    wist=f.wistuj(karty[wzial], wzial)
    for i in range(3):
        f.doloz(karty[kolejnosc[kolejnosc.index(wzial)+i+1]], wist, kolejnosc[kolejnosc.index(wzial)+i+1])

    if True in [x.atu for x in f.stol.values()]:
        wzial = max(filter(lambda x: f.stol[x].kolor == atut, f.stol), key=lambda x: f.stol.get(x).wartosc)
    else:
        wzial=max(filter(lambda x: f.stol[x].kolor==wist.kolor, f.stol), key=lambda x: f.stol.get(x).wartosc)
    print(f"{wzial} zdobył lewę!")
    if wzial=='N' or wzial=='S': lewyNS+=1
    f.stol={}
print(f'Wynik: {f.punkty(lic[-4], lewyNS)}')

