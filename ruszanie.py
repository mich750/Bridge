import tkinter as tk
import zmienne as z

def przesun(karta, kierunek):
    x, y = z.ramki.coords(karta)
    if kierunek in [-2, 2] and abs(x-685)>165:
        z.ramki.move(karta, 10*kierunek, 0)
        z.ramki.after(5, lambda: przesun(karta, kierunek))
    elif kierunek==1 and y<210:
        z.ramki.move(karta, 0, 10*kierunek)
        z.ramki.after(5, lambda: przesun(karta, kierunek))

def ustaw(karta, kierunek):
    x, y = z.ramki.coords(karta)
    bok = 10*(680-x)/abs(326-y-115*kierunek)
    if abs(y-330)>130:
        z.ramki.move(karta, bok, 10*kierunek)
        z.ramki.after(5, lambda: ustaw(karta, kierunek))
    else:
        z.ramki.coords(karta, 680, y)