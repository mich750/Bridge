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
    for i in karty:
        wynik[i]=[]
        for j in karty[i].reka:
            x=Image.open(f'Grafika/{j}.png')
            x=x.resize((110, 156))
            x=ImageTk.PhotoImage(x)
            wynik[i].append(x)
    return [wynik, karty]

def uklad_kart(root):
    rewers=Image.open('Grafika/Rewers.png')
    rewers=rewers.resize((110, 156))
    rewers=rewers.rotate(90, expand=True)
    rewers=ImageTk.PhotoImage(rewers)
    fr_karty = {}
    for i in ['W', 'E']:
        fr_karty[i] = tk.Frame(root, height=532, width=500, bg='ForestGreen')
        fr_karty[i].pack_propagate(False)
        if i == 'W':
            fr_karty[i].place(x=20, y=170)
            a = 0
        else:
            fr_karty[i].place(x=1050, y=170)
            a = 300
        y_pos = 0
        for j in range(13):
            label = tk.Label(fr_karty[i], image=rewers, bg='ForestGreen')
            label.image = rewers
            label.place(x=a, y=y_pos)
            y_pos += 35
    fr_karty['S'] = tk.Frame(root, height=400, width=532, bg='ForestGreen')
    fr_karty['S'].pack_propagate(False)
    fr_karty['S'].place(x=470, y=435)
    x_pos = 0
    for i in range(13):
        label = tk.Label(fr_karty['S'], image=z.karty[0]['S'][i], bg='ForestGreen')
        label.image = z.karty[0]['S'][i]
        label.place(x=x_pos, y=240)
        label.bind('<Enter>', lambda x=label, y=i: u.podnies(x, 'S', z.karty[1]['S'].reka[y]))
        label.bind('<Leave>', lambda x=label, y=i: u.obniz(x, 'S', z.karty[1]['S'].reka[y]))
        label.bind('<Button-1>', lambda x=label, y=i: u.dorzuc(x, 'S', z.karty[1]['S'].reka[y], root))
        x_pos += 35
    if z.koniec:
        fr_karty['N'] = tk.Frame(root, height=400, width=532, bg="ForestGreen")
        fr_karty['N'].pack_propagate(False)
        fr_karty['N'].place(x=470, y=15)
        x_pos = 0
        for i in range(13):
            label = tk.Label(fr_karty['N'], image=z.karty[0]['N'][i], bg='ForestGreen')
            label.image = z.karty[0]['N'][i]
            label.place(x=x_pos, y=0)
            label.bind('<Enter>', lambda x=label, y=i: u.obniz(x, 'N', z.karty[1]['N'].reka[y]))
            label.bind('<Leave>', lambda x=label, y=i: u.podnies(x, 'N', z.karty[1]['N'].reka[y]))
            label.bind('<Button-1>', lambda x=label, y=i: u.dorzuc(x, 'N', z.karty[1]['N'].reka[y], root))
            x_pos += 35
    return fr_karty

def brakujace(root):
    z.ramki['N'] = tk.Frame(root, height=400, width=532, bg="ForestGreen")
    z.ramki['N'].pack_propagate(False)
    z.ramki['N'].place(x=470, y=15)
    x_pos = 0
    for i in range(13):
        label = tk.Label(z.ramki['N'], image=z.karty[0]['N'][i], bg='ForestGreen')
        label.image = z.karty[0]['N'][i]
        label.place(x=x_pos, y=0)
        label.bind('<Enter>', lambda x=label, y=i: u.obniz(x, 'N', z.karty[1]['N'].reka[y]))
        label.bind('<Leave>', lambda x=label, y=i: u.podnies(x, 'N', z.karty[1]['N'].reka[y]))
        label.bind('<Button-1>', lambda x=label, y=i: u.dorzuc(x, 'N', z.karty[1]['N'].reka[y], root))
        x_pos += 35

def zakryte_N(root):
    z.ramki['N'] = tk.Frame(root, height=400, width=532, bg="ForestGreen")
    z.ramki['N'].pack_propagate(False)
    z.ramki['N'].place(x=470, y=15)
    x_pos = 0
    rewers = Image.open('Grafika/Rewers.png')
    rewers = rewers.resize((110, 156))
    rewers = ImageTk.PhotoImage(rewers)
    for j in range(13):
        label = tk.Label(z.ramki['N'], image=rewers, bg='ForestGreen')
        label.image = rewers
        label.place(x=x_pos, y=0)
        x_pos += 35
def karty_dziadka(root):
    y_pos=0
    z.ramki[z.dziadek].destroy()
    z.ramki[z.dziadek] = tk.Frame(root, height=532, width=500, bg='ForestGreen')
    z.ramki[z.dziadek].pack_propagate(False)
    z.ramki[z.dziadek].lower()
    if z.dziadek == 'W':
        z.ramki[z.dziadek].place(x=20, y=170)
        a = 0
    else:
        z.ramki[z.dziadek].place(x=1050, y=170)
        a = 300
    for i in range(13):
        obrazek = Image.open(f'Grafika/{z.karty[1][z.dziadek].reka[i]}.png')
        obrazek = obrazek.resize((110, 156))
        obrazek = obrazek.rotate(90, expand=True)
        obrazek = ImageTk.PhotoImage(obrazek)
        label = tk.Label(z.ramki[z.dziadek], image=obrazek, bg='ForestGreen')
        label.image = obrazek
        label.place(x=a, y=y_pos)
        z.obrazki.append(label)
        y_pos += 35