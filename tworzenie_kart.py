import tkinter as tk
import Karta
import Reka
import random
from PIL import Image, ImageTk
import zmienne as z
import ukladkart as u

def karty():
    kolory = ['C', 'D', 'H', 'S']
    talia = []
    for i in kolory:
        for j in range(2, 15):
            talia.append(Karta.Karta(i, j))
    random.shuffle(talia)
    karty = {"N": Reka.Reka(talia[0:13]), "E": Reka.Reka(talia[13:26]), "S": Reka.Reka(talia[26:39]),
             "W": Reka.Reka(talia[39:52])}
    for i in karty:
        karty[i].reka.sort(key=lambda x: (x.kolor, x.wartosc))
    wynik={}
    obrocone={}
    for i in karty:
        wynik[i]=[]
        obrocone[i]=[]
        for j in karty[i].reka:
            x=Image.open(f'Grafika/{j}.png')
            x=x.resize((110, 156))
            y=x.rotate(90, expand=True)
            obrocone[i].append(ImageTk.PhotoImage(y))
            x=ImageTk.PhotoImage(x)
            wynik[i].append(x)
    rewers = Image.open('Grafika/Rewers.png')
    rewers = rewers.resize((110, 156))
    obrocone['R']= ImageTk.PhotoImage(rewers.rotate(90, expand=True))
    rewers = ImageTk.PhotoImage(rewers)
    wynik['R']=rewers
    return [wynik, karty, obrocone]

def uklad_kart(root):
    fr_karty = tk.Canvas(root, bg='ForestGreen')
    fr_karty.pack(fill='both', expand=True)
    fr_karty.pack_propagate(False)
    y_pos = 170
    for j in range(13):
        karta = fr_karty.create_image(20, y_pos, image=z.karty[2]['R'], anchor="nw")
        z.obrazki['W'].append(karta)
        y_pos += 35
    y_pos = 170
    for j in range(13):
        karta = fr_karty.create_image(1350, y_pos, image=z.karty[2]['R'], anchor="nw")
        z.obrazki['E'].append(karta)
        y_pos += 35
    x_pos = 470
    for i in range(13):
        karta = fr_karty.create_image(x_pos, 675, image=z.karty[0]['S'][i], anchor='nw')
        fr_karty.tag_bind(karta, '<Enter>', lambda e, y=i, k=karta: u.podnies(e, 'S', z.karty[1]['S'].reka[y], k))
        fr_karty.tag_bind(karta, '<Leave>', lambda e, y=i, k=karta: u.obniz(e, 'S', z.karty[1]['S'].reka[y], k))
        fr_karty.tag_bind(karta, '<Button-1>', lambda e, y=i, k=karta: u.dorzuc(e, 'S', z.karty[1]['S'].reka[y], root, k))
        x_pos += 35
    x_pos = 470
    for i in range(13):
        karta = fr_karty.create_image(x_pos, 15, image=z.karty[0]['R'], anchor="nw")
        z.obrazki['N'].append(karta)
        x_pos += 35
    # if z.koniec:
    #     x_pos = 470
    #     for i in range(13):
    #         karta = fr_karty.create_image(x_pos, 15, image=z.karty[0]['N'][i], anchor = 'nw')
    #         fr_karty.tag_bind(karta, '<Enter>', lambda e, y=i, k=karta: u.obniz(e, 'N', z.karty[1]['N'].reka[y], k))
    #         fr_karty.tag_bind(karta, '<Leave>', lambda e, y=i, k=karta: u.podnies(e, 'N', z.karty[1]['N'].reka[y], k))
    #         fr_karty.tag_bind(karta, '<Button-1>', lambda e, y=i, k=karta: u.dorzuc(e, 'N', z.karty[1]['N'].reka[y], root, k))
    #         x_pos += 35
    return fr_karty

def brakujace(root):
    x_pos = 470
    for i in range(13):
        karta = z.ramki.create_image(x_pos, 15, image=z.karty[0]['N'][i], anchor='nw')
        z.ramki.tag_bind(karta, '<Enter>', lambda e, y=i, k=karta: u.obniz(e, 'N', z.karty[1]['N'].reka[y], k))
        z.ramki.tag_bind(karta, '<Leave>', lambda e, y=i, k=karta: u.podnies(e, 'N', z.karty[1]['N'].reka[y], k))
        z.ramki.tag_bind(karta, '<Button-1>', lambda e, y=i, k=karta: u.dorzuc(e, 'N', z.karty[1]['N'].reka[y], root, k))
        x_pos += 35

def zakryte_N():
    x_pos = 470
    for j in range(13):
        z.ramki.create_image(x_pos, 15, image=z.karty[0]['R'], anchor='nw')
        x_pos += 35
def karty_dziadka(root):
    y_pos=170
    x_pos = 470
    for i in z.obrazki[z.dziadek]:
        z.ramki.delete(i)
    z.obrazki[z.dziadek]=[]
    if z.dziadek == 'W':
        a = 20
    elif z.dziadek =='E':
        a = 1350
    if z.dziadek!='N':
        for i in range(13):
            karta = z.ramki.create_image(a, y_pos, image=z.karty[2][z.dziadek][i], anchor='nw')
            y_pos += 35
            z.obrazki[z.dziadek].append(karta)
    else:
        for i in range(13):
            karta = z.ramki.create_image(x_pos, 15, image=z.karty[0][z.dziadek][i], anchor='nw')
            z.ramki.tag_bind(karta, '<Enter>', lambda e, y=i, k=karta: u.obniz(e, 'N', z.karty[1]['N'].reka[y], k))
            z.ramki.tag_bind(karta, '<Leave>', lambda e, y=i, k=karta: u.podnies(e, 'N', z.karty[1]['N'].reka[y], k))
            z.ramki.tag_bind(karta, '<Button-1>',lambda e, y=i, k=karta: u.dorzuc(e, 'N', z.karty[1]['N'].reka[y], root, k))
            z.obrazki['N'].append(karta)
            x_pos += 35