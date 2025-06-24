import tkinter as tk
import Karta
import Reka
import zmienne as z
import funkcje_aplikacji as f
import tworzenie_kart

def klik(root):
    if z.koniec:
        if z.lic[-4]=='pass': return 0
        z.fr_przyciski.destroy()
        if len(z.ramki)==3 and z.rozgrywa=='NS':
            tworzenie_kart.brakujace(root)
        elif len(z.ramki)==3 and z.wzial=='N':
            tworzenie_kart.zakryte_N(root)
            tworzenie_kart.karty_dziadka(root)
        elif len(z.ramki)==3:
            tworzenie_kart.zakryte_N(root)
        if len(z.stol)==5:
            if True in [x.atu for x in z.stol.values()]:
                z.wzial = max(filter(lambda x: z.stol[x].kolor == z.lic[-4][1:].replace('x', ''), z.stol), key=lambda x: z.stol.get(x).wartosc)
            else:
                z.wzial = max(filter(lambda x: z.stol[x].kolor == z.stol[z.wzial].kolor, z.stol), key=lambda x: z.stol.get(x).wartosc)
            z.stol={}
            for i in range(len(z.stol_app)):
                z.stol_app[i].destroy()
            z.stol_app = []
            if z.wzial in ['N', 'S']: z.lewyNS+=1
            z.ramka_wynik.config(text=f"{z.ramka_wynik.cget('text')[:9]}{z.lewyNS} \nKontrakt: {z.lic[-4]}")
        elif len(z.stol)==4:
            z.stol['X']=Karta.Karta('X', 1)
        if len(z.stol)==0 and z.wzial in ['E', 'N', 'W'] and z.karty[1][z.wzial].reka:
            if z.rozgrywa=='EW' and z.wzial=='N':
                f.wistuj('N')
                f.doloz(z.stol['N'], 'E')
            elif z.rozgrywa=='EW' and z.wzial=='W':
                f.wistuj(z.wzial)
                f.doloz(z.stol['W'], 'N')
                f.doloz(z.stol['W'], 'E')
            elif z.rozgrywa=='EW':
                f.wistuj(z.wzial)
            elif z.wzial!='N':
                f.wistuj(z.wzial)
        if len(z.stol)==0 and not z.karty[1]['E'].reka and not z.karty[1]['W'].reka:
            z.koniecgry=True
    if z.koniecgry:
        f.dodaj_punkty(z.lic[-4], z.lewyNS, z.rozgrywa)
        z.fr_przyciski=tk.Frame(root, bg='ForestGreen')
        z.fr_przyciski.place(x=575, y=250)
        z.koniec=False
        labelki=[]
        for i in ['NSnad', 'NSpod1', 'NSpod2', 'EWnad', 'EWpod1', 'EWpod2', 'NSpod3', 'EWpod3']:
            label=tk.Label(z.fr_przyciski, text=z.punkty[i], padx=50, font=('Arial', 45), bg='ForestGreen')
            labelki.append(label)
        labelNS=tk.Label(z.fr_przyciski, text='NS', font=('Arial', 45), bg='ForestGreen')
        labelEW = tk.Label(z.fr_przyciski, text='EW', font=('Arial', 45), bg='ForestGreen')
        linia=tk.Label(z.fr_przyciski, text='--------------------------------', font=('Arial', 20), bg='ForestGreen')
        labelNS.grid(row=0, column=0)
        labelEW.grid(row=0, column=1)
        linia.grid(row=2, column=0, columnspan=2)
        for i in range(6):
            labelki[i].grid(row=2*(i%3)-(i%3)//2+1, column=i//3)
        if z.punkty['NSpod3']>0 or z.punkty['EWpod3']>0:
            labelki[6].grid(row=5, column=0)
            labelki[7].grid(row=5, column=1)
        if (z.punkty['NSpod2']>=100 and z.punkty['NSpod1']>=100) or (z.punkty['EWpod2']>=100 and z.punkty['EWpod1']>=100) or z.punkty['NSpod3']>=100 or z.punkty['EWpod3']>=100:
            if z.punkty['NSnad']+z.punkty['NSpod1']+z.punkty['NSpod2']+z.punkty['NSpod3']>z.punkty['EWnad']+z.punkty['EWpod1']+z.punkty['EWpod2']+z.punkty['EWpod3']:
                tekst='WYGRAŁEŚ'
            else: tekst='PRZEGRAŁEŚ'
            z.wygrany=tk.Label(root, text=tekst, font=('Arial', 70), bg='Forestgreen', fg='red')
            z.wygrany.place(x=525, y=30)
            for i in z.punkty: z.punkty[i]=0
        z.koniecgry=False