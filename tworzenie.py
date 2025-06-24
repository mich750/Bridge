import tkinter as tk
from tkinter import *
import przyciski_licytacji as p
import zmienne as z
import tworzenie_kart

def zamien(root):
    z.ramka_wynik.destroy()
    z.fr_przyciski.destroy()
    z.wygrany=tk.Label()
    z.wygrany.destroy()
    for i in z.ramki.values(): i.destroy()

    z.koniec=False
    z.lic=[]
    z.stol={}
    z.stol_app=[]
    z.wzial='W'
    z.lewyNS=0
    z.koniecgry=False

    z.karty = tworzenie_kart.karty()
    z.ramki = tworzenie_kart.uklad_kart(root)
    z.ramka_wynik = tk.Label(root, text="Lewy NS: 0 \nKontrakt: ", font=('Arial', 50), bg='ForestGreen', justify='left')
    z.ramka_wynik.place(x=30, y=10)
    z.fr_przyciski = tk.Frame(root, bg='ForestGreen')
    z.fr_przyciski.place(x=500, y=200)
    do_licytacji()

def menu(root):
    menu = Menu(root)
    root.config(menu=menu)
    menumenu = Menu(menu)
    menu.add_cascade(label='Menu', menu=menumenu)
    menumenu.add_command(label='Rozdaj ponownie (R)', command=lambda: zamien(root))
    menumenu.add_separator()
    menumenu.add_command(label='Wyłącz (Esc)', command=root.quit)

def do_licytacji():

    przyciski =[]
    licytowanie = tk.Label(z.fr_przyciski, text='  S      W     N      E  \n', font=('Arial', 25), pady=15, justify='left', bg='ForestGreen')
    for i in range(7):
        przycisk = tk.Button(z.fr_przyciski, text=i + 1, font=('Arial', 15))
        przycisk.config(command=lambda x=przycisk: p.klik_licytuj(x, licytowanie, przyciski), width=5, height=2)
        przyciski.append(przycisk)
    for j in ['C', 'D', 'H', 'S', 'NT', 'x', 'xx']:
        przycisk = tk.Button(z.fr_przyciski, text=j, font=('Arial', 15))
        przycisk.config(command=lambda x=przycisk: p.klik_licytuj(x, licytowanie, przyciski), width=5, height=2)
        przyciski.append(przycisk)
    przycisk=tk.Button(z.fr_przyciski, text='pass', font=('Arial', 15))
    przycisk.config(command=lambda x=przycisk: p.klik_licytuj(x, licytowanie, przyciski), width=11, height=2)
    przyciski.append(przycisk)
    licytowanie.grid(row=0, column=0, columnspan=8)
    for i in range(7):
        przyciski[i].grid(row=1, column=i)
    for i in range(5):
        przyciski[i + 7].grid(row=2, column=i)
    przyciski[-1].grid(row=2, column=5, columnspan=2)
    for i in [2, 3]:
        przyciski[-i].grid(row=2-i%2, column=7)