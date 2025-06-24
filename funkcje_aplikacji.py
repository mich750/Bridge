import random
import tkinter as tk
import zmienne as z

def doloz(wist, kto):
    if not [x for x in z.karty[1][kto].reka if x.kolor==wist.kolor]:
        if [x for x in z.karty[1][kto].reka if x.atu]:
            doklada=min((x for x in z.karty[1][kto].reka if x.atu), key=lambda x: x.wartosc)
        else:
            doklada = min((x for x in z.karty[1][kto].reka), key=lambda x: x.wartosc)
    else:
        a= max((x for x in z.karty[1][kto].reka if x.kolor==wist.kolor), key=lambda x: x.wartosc)
        b = min((x for x in z.karty[1][kto].reka if x.kolor==wist.kolor), key=lambda x: x.wartosc)
        warunek=a.wartosc > max(x.wartosc for x in z.stol.values() if x.kolor==wist.kolor)
        if not warunek:
            doklada=b
        elif len(z.stol)<2:
            doklada=a
        elif kto=='W':
            if a.wartosc==z.stol['E'].wartosc+1: doklada=b
            else: doklada=a
        elif kto=='E' and a.wartosc==z.stol['W'].wartosc+1:
            doklada=b
        else:
            doklada=a
    label=tk.Label(z.ramki[kto], image=z.karty[0][kto][z.karty[1][kto].reka.index(doklada)], bg='ForestGreen')
    label.image=z.karty[0][kto][z.karty[1][kto].reka.index(doklada)]
    if kto=='W':
        label.place(x=300, y=170)
    elif kto=='E':
        label.place(x=0, y=170)
    else:
        label.place(x=200, y=210)
    if kto==z.dziadek:
        z.obrazki[z.karty[1][kto].reka.index(doklada)].destroy()
        z.obrazki.pop(z.karty[1][kto].reka.index(doklada))
    z.stol_app.append(label)
    z.karty[0][kto].pop(z.karty[1][kto].reka.index(doklada))
    z.karty[1][kto].reka.remove(doklada)
    z.stol[kto] = doklada

def wistuj(kto):
    wist = random.choice(z.karty[1][kto].reka)
    label = tk.Label(z.ramki[kto], image=z.karty[0][kto][z.karty[1][kto].reka.index(wist)], bg='ForestGreen')
    label.image = z.karty[0][kto][z.karty[1][kto].reka.index(wist)]
    if kto == 'W':
        label.place(x=300, y=170)
    elif kto=='E':
        label.place(x=0, y=170)
    else:
        label.place(x=200, y=210)
    if kto==z.dziadek:
        z.obrazki[z.karty[1][kto].reka.index(wist)].destroy()
        z.obrazki.pop(z.karty[1][kto].reka.index(wist))
    z.stol_app.append(label)
    z.stol[kto] = wist
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
