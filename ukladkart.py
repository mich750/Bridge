import tkinter as tk
import Karta
import funkcje_aplikacji as f
import zmienne as z
import tworzenie_kart

def podnies(event, kto, co):
    widget=event.widget
    if kto=='S' and warunek('S') and widget.winfo_y()==240:
        if z.wzial=='S':
            widget.place(y=widget.winfo_y() - 20)
        elif z.stol[z.wzial].kolor==co.kolor or not [x for x in z.karty[1]['S'].reka if x.kolor==z.stol[z.wzial].kolor]:
            widget.place(y=widget.winfo_y()-20)

    elif widget.winfo_y() == 20: widget.place(y=widget.winfo_y() - 20)

def obniz(event, kto, co):
    widget=event.widget
    if widget.winfo_y()==220:
        widget.place(y=widget.winfo_y()+20)
    if kto=='N' and warunek('N') and widget.winfo_y()==0:
        if z.wzial=='N':
            widget.place(y=widget.winfo_y() + 20)
        elif z.stol[z.wzial].kolor==co.kolor or not [x for x in z.karty[1]['N'].reka if x.kolor==z.stol[z.wzial].kolor]:
            widget.place(y=widget.winfo_y()+20)
    elif widget.winfo_y()==220: widget.place(y=widget.winfo_y() + 20)

def dorzuc(event, kto, co, root):
    pusta = Karta.Karta('X', 1)
    widget=event.widget
    if kto=='S' and warunek('S'):
        if z.wzial=='S':
            if z.rozgrywa=='EW' and len(z.karty[1]['W'].reka)==13:
                tworzenie_kart.karty_dziadka(root)
            widget.place(x=200, y=0)
            z.stol['S'] = co
            z.karty[1]['S'].reka[z.karty[1]['S'].reka.index(co)] = pusta
            if z.rozgrywa=='NS':
                f.doloz(z.stol[z.wzial], 'W')
            else:
                for i in ['W', 'N', 'E']:
                    f.doloz(z.stol['S'], i)
            z.stol_app.append(widget)
        elif z.stol[z.wzial].kolor == co.kolor or not [x for x in z.karty[1]['S'].reka if x.kolor == z.stol[z.wzial].kolor]:
            widget.place(x=200, y=0)
            z.stol['S']=co
            z.karty[1]['S'].reka[z.karty[1]['S'].reka.index(co)] = pusta
            if z.rozgrywa=='NS' and len(z.stol)<4:
                f.doloz(z.stol[z.wzial], 'W')
            elif len(z.stol)<4:
                for i in ['W', 'N', 'E']:
                    f.doloz(z.stol[z.wzial], i)
                    if len(z.stol)>3: break
            z.stol_app.append(widget)
    elif kto=='N' and warunek('N') and z.rozgrywa=='NS':
        if z.wzial=='N':
            widget.place(x=200, y=210)
            z.stol['N'] = co
            z.karty[1]['N'].reka[z.karty[1]['N'].reka.index(co)] = pusta
            if len(z.stol)<4: f.doloz(z.stol[z.wzial], 'E')
            z.stol_app.append(widget)
        elif z.stol[z.wzial].kolor==co.kolor or not [x for x in z.karty[1]['N'].reka if x.kolor==z.stol[z.wzial].kolor]:
            widget.place(x=200, y=210)
            z.stol['N']=co
            z.karty[1]['N'].reka[z.karty[1]['N'].reka.index(co)]=pusta
            if len(z.stol)<4: f.doloz(z.stol[z.wzial], 'E')
            z.stol_app.append(widget)

def warunek(kto):
    kolejnosc = ["N", "E", "S", "W", "N", "E", "S"]
    if kto=="S":
        return True in [(z.wzial==kolejnosc[6-i] and len(z.stol)==i) for i in range(4)]
    else:
        return True in [(z.wzial == kolejnosc[4 - i] and len(z.stol) == i) for i in range(4)]