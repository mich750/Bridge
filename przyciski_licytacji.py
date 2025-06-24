import licytacja
import zmienne as z

def klik_licytuj(widget, licytowanie, przyciski):
    starszenstwo = ['C', 'D', 'H', 'S', 'NT']
    odzywki=[f'{i}{j}' for i in range(1, 8) for j in starszenstwo]
    if z.koniec==True:
        return 0
    if widget in przyciski[:7] and licytowanie.cget('text')[-1]=='\n':
        if len(z.lic)==0:
            licytowanie.config(text=licytowanie.cget('text') + str(widget.cget('text')))
        elif int(widget.cget('text'))>max([int(x[0]) for x in z.lic if x not in ['pass', 'x', 'xx']]) or (widget.cget('text')==max([int(x[0]) for x in z.lic if x not in ['pass', 'x', 'xx']]) and [x for x in z.lic if x not in ['pass', 'x', 'xx']][-1][1:]!='NT'):
            licytowanie.config(text=licytowanie.cget('text') + str(widget.cget('text')))
    elif widget in przyciski:
        try:
            if len(z.lic)!=0 and widget.cget('text') not in ['pass', 'x', 'xx']:
                if starszenstwo.index(widget.cget('text'))<=starszenstwo.index([x for x in z.lic if x!='pass'][-1][1:]) and int(licytowanie.cget('text')[-1])==int([x for x in z.lic if x!='pass'][-1][0]):
                    return 0
            if widget.cget('text') in ['pass', 'x', 'xx'] and licytowanie.cget('text')[-1]!='\n':
                return 0
            elif widget.cget('text')=='x':
                if len(z.lic)==0: return 0
                elif z.lic[-1] in odzywki or (z.lic[-3] in odzywki and z.lic[-2]=='pass'):
                    z.lic.append('x')
                    licytowanie.config(text=licytowanie.cget('text')+ '  x   ')
                else: return 0
            elif widget.cget('text')=='xx':
                if len(z.lic)==0: return 0
                elif z.lic[-1]=='x' or (z.lic[-3]=='x' and z.lic[-2]=='pass' and z.lic[-1]=='pass'):
                    z.lic.append('xx')
                    licytowanie.config(text=licytowanie.cget('text')+'  xx  ')
                else: return 0
            elif widget==przyciski[-1] and licytowanie.cget('text')[-1]=='\n':
                z.lic.append('pass')
                licytowanie.config(text=licytowanie.cget('text') + widget.cget('text'))
            else:
                int(licytowanie.cget('text')[-1])
                z.lic.append(f'{licytowanie.cget("text")[-1]}{widget.cget("text")}')
                x=f"{licytowanie.cget('text')[-1]}{widget.cget('text')}"
                licytowanie.config(text=licytowanie.cget('text')[:-1] + x.ljust(5))
            for i in ['W', 'N', 'E']:
                try:
                    if z.lic[-1] == 'pass' and z.lic[-2] == 'pass' and z.lic[-3] == 'pass' and len(z.lic) > 3:
                        zakoncz()
                        return 0
                except:
                    pass
                z.lic.append(licytacja.licytuj(i, z.karty[1][i], z.lic))
                if z.lic[-1]=='pass':
                    licytowanie.config(text=licytowanie.cget('text')+' '+z.lic[-1])
                elif z.lic[-1][1:]=='NT':
                    licytowanie.config(text=licytowanie.cget('text') + ' ' + z.lic[-1] + '  ')
                else:
                    licytowanie.config(text=licytowanie.cget('text') + '  ' + z.lic[-1]+'   ')
            if z.lic[-1] == 'pass' and z.lic[-2] == 'pass' and z.lic[-3] == 'pass' and len(z.lic) > 3:
                zakoncz()
                return 0
            licytowanie.config(text=licytowanie.cget('text') + '\n')
        except:
            pass

def zakoncz():
    z.koniec = True
    if z.lic[-4] == 'x':
        if z.lic[-5] == 'pass':
            z.lic[-4] = f'{z.lic[-7]}x'
        else:
            z.lic[-4] = f'{z.lic[-5]}x'
        if len(z.lic) % 2 == 1:
            z.rozgrywa = "NS"
        else:
            z.rozgrywa = 'EW'
    elif z.lic[-4] == 'xx':
        z.lic[-4] = f"{[x for x in z.lic if x not in ['pass', 'x', 'xx']][-1]}xx"
        if len(z.lic) % 2 == 0:
            z.rozgrywa = "NS"
        else:
            z.rozgrywa = 'EW'
    else:
        if len(z.lic) % 2 == 0:
            z.rozgrywa = 'NS'
        else:
            z.rozgrywa = 'EW'
    z.ramka_wynik.config(text=z.ramka_wynik.cget('text') + z.lic[-4])
    try:
        z.wzial = ['W', 'N', 'E', 'S'][z.lic.index([x for x in z.lic if x not in ['pass', 'x', 'xx']][-1]) % 4]
        z.dziadek=['W', 'N', 'E', 'S', 'W'][['W', 'N', 'E', 'S'].index(z.wzial)+1]
    except:
        pass
    for i in z.karty[1].values():
        for j in i.reka:
            if j.kolor == z.lic[-4][1:].replace('x', ''): j.atu = True