import tkinter as tk
import Karta
import funkcje_aplikacji as f
import zmienne as z
import tworzenie_kart
import ruszanie

def podnies(event, kto, co, obrazek):
    canva=event.widget
    if kto=='S' and warunek('S') and canva.coords(obrazek)[1]==675 and event.y<810:
        if z.wzial=='S':
            canva.move(obrazek, 0, -20)
        elif z.stol[z.wzial].kolor==co.kolor or not [x for x in z.karty[1]['S'].reka if x.kolor==z.stol[z.wzial].kolor]:
            canva.move(obrazek, 0, -20)
    elif canva.coords(obrazek)[1] == 35: canva.move(obrazek, 0, -20)

def obniz(event, kto, co, obrazek):
    canva=event.widget
    y=canva.coords(obrazek)[1]
    if y==655:
        canva.move(obrazek, 0, 20)
    if kto=='N' and warunek('N') and y==15 and event.y>35:
        if z.wzial=='N':
            canva.move(obrazek, 0, 20)
        elif z.stol[z.wzial].kolor==co.kolor or not [x for x in z.karty[1]['N'].reka if x.kolor==z.stol[z.wzial].kolor]:
            canva.move(obrazek, 0, 20)

def dorzuc(event, kto, co, root, obrazek):
    pusta = Karta.Karta('X', 1)
    canva=event.widget
    if kto=='S' and warunek('S'):
        if z.wzial=='S':
            if z.rozgrywa=='EW' and len(z.karty[1]['W'].reka)==13:
                tworzenie_kart.karty_dziadka(root)
            ruszanie.ustaw(obrazek, -1)
            z.stol['S'] = co
            z.karty[1]['S'].reka[z.karty[1]['S'].reka.index(co)] = pusta
            if z.rozgrywa=='NS':
                root.after(75, lambda: f.doloz(z.stol[z.wzial], 'W'))
            else:
                for j, i in enumerate(['W', 'N', 'E'], start=1):
                    root.after(75*j, lambda x=i: f.doloz(z.stol['S'], x))
            z.stol_app.append(obrazek)
        elif z.stol[z.wzial].kolor == co.kolor or not [x for x in z.karty[1]['S'].reka if x.kolor == z.stol[z.wzial].kolor]:
            ruszanie.ustaw(obrazek, -1)
            z.stol['S']=co
            z.karty[1]['S'].reka[z.karty[1]['S'].reka.index(co)] = pusta
            z.stol_app.append(obrazek)
            if len(z.stol)==4:
                z.czekaj=True
            if z.rozgrywa=='NS' and len(z.stol)<4:
                root.after(75, lambda: f.doloz(z.stol[z.wzial], 'W'))
            elif len(z.stol)<4:
                l= len(z.stol)
                for j, i in enumerate(['W', 'N', 'E'], start=1):
                    root.after(75*j, lambda x=i: f.doloz(z.stol[z.wzial], x))
                    l+=1
                    if l>3: break
    elif kto=='N' and warunek('N') and z.rozgrywa=='NS':
        if z.wzial=='N':
            ruszanie.ustaw(obrazek, 1)
            z.stol['N'] = co
            z.karty[1]['N'].reka[z.karty[1]['N'].reka.index(co)] = pusta
            if len(z.stol)<4: f.doloz(z.stol[z.wzial], 'E')
            z.stol_app.append(obrazek)
        elif z.stol[z.wzial].kolor==co.kolor or not [x for x in z.karty[1]['N'].reka if x.kolor==z.stol[z.wzial].kolor]:
            ruszanie.ustaw(obrazek, 1)
            z.stol['N']=co
            z.karty[1]['N'].reka[z.karty[1]['N'].reka.index(co)]=pusta
            if len(z.stol)==4:
                z.czekaj=True
            else:
                root.after(75, lambda: f.doloz(z.stol[z.wzial], 'E'))
            z.stol_app.append(obrazek)

def warunek(kto):
    kolejnosc = ["N", "E", "S", "W", "N", "E", "S"]
    if kto=="S":
        return True in [(z.wzial==kolejnosc[6-i] and len(z.stol)==i) for i in range(4)]
    else:
        return True in [(z.wzial == kolejnosc[4 - i] and len(z.stol) == i) for i in range(4)]