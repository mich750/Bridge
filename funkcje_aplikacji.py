import random
import Karta
import tkinter as tk
import zmienne as z
import ruszanie

def doloz(wist, kto):
    if not [x for x in z.karty[1][kto].reka if x.kolor==wist.kolor]:
        if [x for x in z.karty[1][kto].reka if x.atu]:
            doklada=min((x for x in z.karty[1][kto].reka if x.atu), key=lambda x: x.wartosc)
        else:
            doklada = min((x for x in z.karty[1][kto].reka if x.kolor!='X'), key=lambda x: x.wartosc)
    else:
        a= max((x for x in z.karty[1][kto].reka if x.kolor==wist.kolor), key=lambda x: x.wartosc)
        b = min((x for x in z.karty[1][kto].reka if x.kolor==wist.kolor), key=lambda x: x.wartosc)
        warunek=a.wartosc > max(x.wartosc for x in z.stol.values() if x.kolor==wist.kolor)
        if warunek:
            c=min((x for x in z.karty[1][kto].reka if x.kolor==wist.kolor and x.wartosc>max(y.wartosc for y in z.stol.values() if y.kolor==wist.kolor)), key=lambda x: x.wartosc)
        if not warunek:
            doklada=b
        elif len(z.stol)<2:
            doklada=a
        elif kto=='W':
            if len(z.stol)==3:
                if z.stol['E'].kolor==wist.kolor and z.stol['E'].wartosc==max(x.wartosc for x in z.stol.values()):
                    doklada=b
                else:
                    doklada=c
            elif a.wartosc==z.stol['E'].wartosc+1: doklada=b
            else: doklada=a
        elif kto=='E':
            if len(z.stol)==3:
                if z.stol['W'].kolor==wist.kolor and z.stol['W'].wartosc==max(x.wartosc for x in z.stol.values()):
                    doklada=b
                else:
                    doklada=c
            if a.wartosc==z.stol['W'].wartosc+1: doklada=b
            else: doklada=a
        elif len(z.stol)==3:
            doklada=c
        else:
            doklada=a
    if kto=='W':
        x = 220
        y = 345
        k=2
    elif kto=='E':
        x=1150
        y=345
        k=-2
    else:
        x=680
        y=60
        k=1
    label = z.ramki.create_image(x, y, image=z.karty[0][kto][z.karty[1][kto].reka.index(doklada)], anchor='nw')
    ruszanie.przesun(label, k)
    z.stol_app.append(label)
    if kto==z.dziadek:
        z.ramki.delete(z.obrazki[kto][z.karty[1][kto].reka.index(doklada)])
        z.obrazki[kto].pop(z.karty[1][kto].reka.index(doklada))
    z.kosz.append(z.karty[0][kto][z.karty[1][kto].reka.index(doklada)])
    z.karty[0][kto].pop(z.karty[1][kto].reka.index(doklada))
    z.karty[1][kto].reka.remove(doklada)
    z.stol[kto] = doklada

def wistuj(kto):
    if True in [True in [x.atu for x in z.karty[1][y].reka] for y in ['N', 'E', 'S', 'W']]:
        wist = random.choice(z.karty[1][kto].reka)
    else:
        wist=max((x for x in z.karty[1][kto].reka if x.kolor==z.karty[1][kto].najdluzszy()), key=lambda x: x.wartosc)
    if kto == 'W':
        x=220
        y=345
        k=2
    elif kto=='E':
        x=1150
        y=345
        k=-2
    else:
        x=680
        y=60
        k=1
    label = z.ramki.create_image(x, y, image=z.karty[0][kto][z.karty[1][kto].reka.index(wist)], anchor='nw')
    ruszanie.przesun(label, k)
    z.stol_app.append(label)
    if kto==z.dziadek:
        z.ramki.delete(z.obrazki[kto][z.karty[1][kto].reka.index(wist)])
        z.obrazki[kto].pop(z.karty[1][kto].reka.index(wist))
    z.stol[kto] = wist
    z.kosz.append(z.karty[0][kto][z.karty[1][kto].reka.index(wist)])
    z.karty[0][kto].pop(z.karty[1][kto].reka.index(wist))
    z.karty[1][kto].reka.remove(wist)
    z.stol[kto]=wist

def dodaj_punkty(kontrakt, lewy, kto):
    if kto=='NS':
        x=lewy-6
    else: x=7-lewy
    bonus=0
    n=int(kontrakt[0])
    kontra=1
    while kontrakt[-1]=='x':
        kontrakt=kontrakt[:-1]
        kontra=kontra*2
    if z.punkty['NSpod2']>=100 or z.punkty['EWpod2']>=100:
        gdzie=f'{kto}pod3'
        po = 2
    elif z.punkty['NSpod1']>=100 or z.punkty['EWpod1']>=100:
        gdzie=f'{kto}pod2'
        if z.punkty[f'{kto}pod1']>=100:
            po=2
        else:
            po = 1
    else:
        gdzie=f'{kto}pod1'
        po=1
    if n==6: bonus=250*(po+1)
    if n==7: bonus=500*(po+1)
    if kontra>1 and x>=n: bonus+=25*kontra
    if x<n:
        if kontra==1:
            if kto=='NS':
                z.punkty['EWnad']+=50*(n-x)*po
            else:
                z.punkty['NSnad']+=50*(n-x)*po
        elif po==1:
            if kto=='NS':
                z.punkty['EWnad']+=(100*(n-x)+max(0, n-x-3)*50-50)*kontra
            else:
                z.punkty['NSnad']+=(100*(n-x)+max(0, n-x-3)*50-50)*kontra
        else:
            if kto=='NS':
                z.punkty['EWnad']+=(150*(n-x)-50)*kontra
            else:
                z.punkty['NSnad']+=(150*(n-x)-50)*kontra
    elif kontrakt[1] in ['C', 'D']:
        z.punkty[gdzie]+=20*n*kontra
        if kontra==1:
            z.punkty[f'{kto}nad']+=20*(x-n)+bonus
        else:
            z.punkty[f'{kto}nad']+=50*(x-n)*kontra*po + bonus
    elif kontrakt[1] in ['H', 'S']:
        z.punkty[gdzie] += 30 * n * kontra
        if kontra==1:
            z.punkty[f'{kto}nad'] += 30 * (x - n) + bonus
        else:
            z.punkty[f'{kto}nad'] += 50 * (x - n) * kontra * po + bonus
    else:
        z.punkty[gdzie] += (10+30 * n)* kontra
        if kontra == 1:
            z.punkty[f'{kto}nad'] += 30 * (x - n) + bonus
        else:
            z.punkty[f'{kto}nad'] += 50 * (x - n) * kontra * po + bonus
    z.doliczono=True
