class Karta:
    atu = False
    def __init__(self, kolor, wartosc):
        self.kolor = kolor
        self.wartosc = wartosc
    def __str__(self):
        if self.wartosc<=10:
            return f"{self.wartosc}{self.kolor}"
        elif self.wartosc==11:
            return f"J{self.kolor}"
        elif self.wartosc==12:
            return f"Q{self.kolor}"
        elif self.wartosc==13:
            return f"K{self.kolor}"
        else:
            return f"A{self.kolor}"
    def __repr__(self):
        return str(self)
