import random
def doloz(karty,  wist, kto):
    if kto=="W" or kto=="E":
        if not [x for x in karty.reka if x.kolor==wist.kolor]:
            if [x for x in karty.reka if x.atu]:
                doklada=min((x for x in karty.reka if x.atu), key=lambda x: x.wartosc)
            else:
                doklada = min((x for x in karty.reka), key=lambda x: x.wartosc)
        else:
            a= max((x for x in karty.reka if x.kolor==wist.kolor), key=lambda x: x.wartosc)
            b = min((x for x in karty.reka if x.kolor==wist.kolor), key=lambda x: x.wartosc)
            if a.wartosc > wist.wartosc: doklada=a
            else: doklada = b
        print(f'{kto} dołożył {doklada}')
        karty.reka.remove(doklada)
        stol[kto]=doklada
    else:
        print(f"Karty {kto}: {karty.reka}")
        stol[kto]=None
        while stol[kto] is None:
            x=input('Dołóż: ')
            for i in range(len(karty.reka)):
                if x == repr(karty.reka[i]): stol[kto] = karty.reka[i]
            if stol[kto] is None: print("Zła karta!")
        if [x for x in karty.reka if x.kolor==wist.kolor]:
            while stol[kto].kolor!=wist.kolor:
                x= input("Nieprawidłowa karta! Dołóż jeszcze raz: ")
                for i in range(len(karty.reka)):
                    if x == repr(karty.reka[i]): stol[kto] = karty.reka[i]
        karty.reka.remove(stol[kto])

def wistuj(karty, kto):
    if kto=="W" or kto=="E":
        wist=random.choice(karty.reka)
        print(f'{kto} zawistował w {wist}')
    else:
        print(f'{kto} wistuje. Karty do wistu: {karty.reka}')
        wist=None
        while wist is None:
            x = input('Wistuj: ')
            for i in range(len(karty.reka)):
                if x == repr(karty.reka[i]): wist = karty.reka[i]
            if wist is None: print("Zła karta!")
    stol[kto]=wist
    karty.reka.remove(wist)
    return wist

def punkty(kontrakt, lewy):
    x=lewy-6
    bonus=0
    if kontrakt[0]=='6': bonus=500
    if kontrakt[0]=='7': bonus=1000
    if x-int(kontrakt[0])<0: return 50*(x-int(kontrakt[0]))
    elif kontrakt[1] in ['C', 'D']: return 20*x+bonus
    elif kontrakt[1] in ['H', 'S']: return 30*x+bonus
    else: return 30*x+10+bonus

global stol
stol={}

