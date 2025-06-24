import zmienne as z


def licytuj(kto, reka, licytacja):
    if kto=="E" or kto=='W':
        if not [i for i in licytacja if i in kolejnosc]:
            if 6<reka.sila()<12 and max(reka.sklad().values())>5: return f'2{reka.najdluzszy()}'
            elif reka.sila()<12: return 'pass'
            elif 14<reka.sila()<18 and max(reka.sklad().values())<5 and min(reka.sklad().values())>1: return '1NT'
            elif max(reka.sklad().values())>4: return f'1{reka.najdluzszy()}'
            else: return '1C'
        elif len(licytacja)<2:
            if 6<reka.sila()<11 and max(reka.sklad().values())>4: return spr(f'1{reka.najdluzszy()}')
            elif reka.sila()>10 and max(reka.sklad().values())>4: return spr(f'2{reka.najdluzszy()}')
            elif reka.sila()>11 and max(reka.sklad().values())<5 and min(reka.sklad().values())>1: return spr('1NT')
            else: return 'pass'
        else:
            if licytacja[-2]=='pass':
                if reka.sila()<12: return 'pass'
                elif max(reka.sklad().values())>4:
                    if spr(f'1{reka.najdluzszy()}')=='pass': return spr(f'2{reka.najdluzszy()}')
                    else: return spr(f'1{reka.najdluzszy()}')
                else: return spr('1NT')
            elif licytacja[-2]=='1C':
                if reka.sila()<7: return 'pass'
                elif reka.sklad()['H']>3: return spr('1H')
                elif reka.sklad()['S']>3: return spr('1S')
                else: return spr('1NT')
            elif reka.sklad()[licytacja[-2][1:]]>2:
                if 6<reka.sila()<10: return spr(f'2{licytacja[-2][1:]}')
                elif 11 < reka.sila() and licytacja[-2][1:] in starsze: return spr(f'4{licytacja[-2][1:]}')
                elif 9 < reka.sila(): return spr(f'3{licytacja[-2][1:]}')
                else: return 'pass'
            elif reka.sila()>11: return spr('3NT')
            elif reka.sila()>9: return spr('2NT')
            else: return 'pass'
    elif licytacja[0]=='pass':
        if reka.sila()<12: return 'pass'
        elif 14<reka.sila()<18 and max(reka.sklad().values())<5 and min(reka.sklad().values())>1:
            if len(licytacja)<3: return spr('1NT')
            elif licytacja[-2]=='2C':
                if reka.sklad()['H']==4: return spr('2H')
                elif reka.sklad()['S']==4: return spr('2S')
                else: return spr('2D')
            elif licytacja[-2]=='3NT': return 'pass'
            elif licytacja[-2]=='2NT':
                if reka.sila()>15: return spr('3NT')
                else: return 'pass'
            elif licytacja[-2]=='2S': return spr('3C')
            else: return spr(kolejnosc[kolejnosc.index(licytacja[-2])+1])
        elif max(reka.sklad().values())>4:
            if len(licytacja)<4: return spr(f'1{reka.najdluzszy()}')
            elif licytacja[-2]=='1NT' and reka.sklad()[reka.najdluzszy()]>5: return spr(f'2{reka.najdluzszy()}')
            elif licytacja[-2]=='1NT' and reka.sila()>15: return spr('2NT')
            elif licytacja[-2][1:]=='NT': return 'pass'
            elif licytacja[-2] in ['pass', 'x', 'xx']: return 'pass'
            elif reka.sklad()[licytacja[-2][1:]]>3 and licytacja[-2][0]=='3' and reka.sila()>13: return spr(f'4{licytacja[-2][1:]}')
            elif reka.sklad()[licytacja[-2][1:]]>3 and licytacja[-2][0]=='2' and reka.sila()>15: return spr(f'4{licytacja[-2][1:]}')
            else: return 'pass'
        elif len(licytacja)<4:
            if spr('1C')=='1C': return '1C'
            else: return 'x'
        elif licytacja[-2]=='1D' and reka.najdluzszy() in starsze: return spr(f'1{reka.najdluzszy()}')
        elif licytacja[-2]=='1D' and reka.najdluzszy()=='C': return spr('2C')
        else: return 'pass'
    elif licytacja[0]!=['pass']:
        if licytacja[0]=='1NT':
            if len(licytacja)<4:
                if reka.najdluzszy() in starsze and max(reka.sklad().values())>4:
                    return spr(kolejnosc[kolejnosc.index(f'2{reka.najdluzszy()}')-1])
                elif reka.najdluzszy()=='C' and max(reka.sklad().values())>5:
                    return spr('2S')
                elif reka.najdluzszy()=='D' and max(reka.sklad().values())>5:
                    return spr('3C')
                elif reka.sila()<8: return 'pass'
                elif reka.sklad()['H']>3 or reka.sklad()['S']>3: return spr('2C')
                elif 7<reka.sila()<10: return spr('2NT')
                else: return spr('3NT')
            elif len(licytacja)<8:
                if licytacja[-2]=='2NT':
                    if reka.sila()>8: return spr('3NT')
                    else: return 'pass'
                elif licytacja[-2]=='2H' and reka.sklad()['H']<4: return spr('2S')
                elif licytacja[-2] in ['2H', '2S']:
                    if reka.sila()>8 and reka.sklad()[licytacja[-2][1:]]>3: return spr(f'4{licytacja[-2][1:]}')
                    elif licytacja[-2]=="2S" and reka.sklad()['S']<4: return spr('2NT')
                    else: return 'pass'
                elif licytacja[-2] == '2D' and reka.sila() < 10: return spr('2NT')
                elif licytacja[-2]=='2D': return spr('3NT')
                else: return 'pass'
            elif len(licytacja)<12:
                if licytacja[-2]=='2NT':
                    if reka.sila()>8: return spr('3NT')
                    else: return 'pass'
                elif licytacja[-2]=='3S':
                    if reka.sila()>8: return spr('4S')
                    else: return 'pass'
                else: return 'pass'
            else: return 'pass'
        elif reka.sila()<7:
            if licytacja[0]=='1C' and len(licytacja)<4: return spr('1D')
            else: return 'pass'
        elif licytacja[0] in ['1C', '1D'] and reka.najdluzszy() in starsze:
            if len(licytacja)<4:
                if spr(f'1{reka.najdluzszy()}')=='pass' and reka.sila()>8: return spr(f'2{reka.najdluzszy()}')
                else: return spr(f'1{reka.najdluzszy()}')
            elif licytacja[-2]=='1S' and reka.sklad()['S']<4: return spr('1NT')
            elif licytacja[-2]=='1NT':
                if reka.sila()>12: return spr('3NT')
                elif reka.sila()>10: return spr('2NT')
                else: return 'pass'
            elif licytacja[-2]=='2NT':return spr('3NT')
            elif licytacja[-2][1:]=='NT': return 'pass'
            elif licytacja[-2][-1]=='x': return 'pass'
            elif reka.sklad()[licytacja[-2][1:]]<4 and reka.sila()>9:
                return spr('2NT')
            elif reka.sklad()[licytacja[-2][1:]]>3:
                if reka.sila()>11 and int(licytacja[-2][0])<4: return spr(f'4{licytacja[-2][1:]}')
                elif reka.sila()>9 and int(licytacja[-2][0])<3: return spr(f'3{licytacja[-2][1:]}')
                elif licytacja[-2]=='1S':return spr('2S')
                else: return 'pass'
            else: return 'pass'
        elif reka.sklad()[licytacja[0][1:]]>2 and licytacja[0][0]=='1':
            if len(licytacja)>4: return 'pass'
            elif 6<reka.sila()<10: return spr(f'2{licytacja[0][1:]}')
            elif licytacja[0] in ['H', 'S'] and reka.sila()>11: return spr(f'4{licytacja[0][1:]}')
            elif 9 < reka.sila(): return spr(f'3{licytacja[0][1:]}')
        elif licytacja[-2]=='1H' and reka.sklad()['S']>3: return spr('1S')
        else:
            return spr('1NT')
    else: return 'pass'


def spr(x):
    if not [i for i in z.lic if i in kolejnosc]:
        return x
    elif kolejnosc.index(x)>max(kolejnosc.index(i) for i in z.lic if i in kolejnosc):
        return x
    else:
        return 'pass'


kolejnosc=[f'{x}{y}' for x in range(1, 8) for y in ['C', 'D', 'H', 'S', 'NT']]
mlodsze=['C', 'D']
starsze=['H', 'S']