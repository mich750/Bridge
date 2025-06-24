class Reka:
    def __init__(self, reka):
        self.reka=reka
    def sila(self):
        return sum([max(x.wartosc-10, 0) for x in self.reka])
    def sklad(self):
        uklad={}
        for i in ['H', 'S', 'C', 'D']:
            uklad[i]=len([x for x in self.reka if x.kolor==i])
        uklad['NT']=0
        return uklad
    def najdluzszy(self):
        return max(self.sklad(), key=self.sklad().get)
