import tkinter as tk
import tworzenie
import ukladkart
import klikanie
import zmienne as z
import tworzenie_kart

root=tk.Tk()
root.title('Brydż')
root.attributes('-fullscreen', True)
root.config(bg='ForestGreen')

z.karty= tworzenie_kart.karty()
z.ramki=tworzenie_kart.uklad_kart(root)

z.ramka_wynik=tk.Label(root, text="Lewy NS: 0 \nKontrakt: ", font=('Arial', 50), bg='ForestGreen', justify='left')
z.ramka_wynik.place(x=10, y=10)

z.fr_przyciski = tk.Frame(root, bg='ForestGreen')
z.fr_przyciski.place(x=500, y=200)
tworzenie.do_licytacji()

tworzenie.menu(root)

root.bind('<Button-1>', lambda x: klikanie.klik(root))
root.bind('<Escape>', lambda x: root.quit())
root.bind('<r>', lambda x: tworzenie.zamien(root))
#root.bind('<Button-3>', lambda x: root.quit())

root.mainloop()
