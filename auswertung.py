def auswertung(wort, interpretation):
    """

    @param: str 
    @param: list[bool] 
    @return:
    """

    #Check type correctedness
    if not type(wort) == str:
        raise Exception('Unzulaessige Eingabe : Das Wort muss ein String sein')
    
    if len(wort) <= 1:
        raise Exception('Unzulaessige Eingabe : Leeres oder zu kurzes Wort')
    
    if not(type(interpretation) == list):
        raise Exception('Unzulaessige Eingabe : Deine Interpretation ist keine Liste')
    
    for boolean in interpretation:
        if not type(boolean)==bool:
            raise Exception('Unzulaessige Eingabe : Falsche Werte in der Interpretation')


    wortalsliste = list(wort)
    
    """
    for el in wortalsliste:
        if not(el in ['!','&','|','(',')','[',']','x'] or el.isdigit()):
            raise Exception('Dein Wort beinhaltet unerlaubte Zeichen')
        elif el.isdigit() and int(el)>len(interpretation):
            raise Exception('Dein Wort beinhaltet einen Satzbuchstabenindex mit größerem Wert als die Länge deiner interpretation-Liste')
    """
    
    for idx in range(len(wortalsliste)):
        el = wort[idx]
        if not(el in ['!','&','|','(',')','[',']','x'] or el.isdigit()):
            raise Exception('Unzulaessige Eingabe : Dein Wort beinhaltet unerlaubte Zeichen')
        if el.isdigit() and idx < len(wort)-1:
            if wort[idx+1].isdigit():
                ctr = idx+1
                while ctr < len(wort) and wort[ctr].isdigit():
                    ctr += 1
                el = wort[idx:ctr]
            if int(el)>len(interpretation):
                raise Exception('Unzulaessige Eingabe : Dein Wort beinhaltet einen Satzbuchstabenindex mit größerem Wert als die Länge deiner interpretation-Liste')
                
                    
    
    d = integritaet(wort)
    
    #Aussagenwert berechnen
    wert = klammer(wortalsliste,interpretation)
    
    return (wert,d)



def integritaet(wort):
    """
    INTEGRITAET testet, ob das Wort eine korrekte Formel ist

    """
    
    zielLog = ['x','[','(','!']
    zielAuf = ['x','[','(','!',']',')']
    zielZu = ['&','|',')',']']
    
    Klammern = []
    Tiefe = [0]
    tiefe = 0
    
    wort = list(wort)
    
    for idx in range(len(wort)):
        bst = wort[idx]
        if idx == 0 and bst not in zielLog:
            raise Exception('Unzulaessige logische Aussage am Anfang ')
        if idx == len(wort)-1 and not(bst.isdigit()) and bst not in [')',']']:
            raise Exception('Unzulaessige logische Aussage am Ende ')
        if bst == 'x' and idx < len(wort)-1 and not(wort[idx+1].isdigit()):
                raise Exception('Unzulaessiger Satzbuchstabenindex : ' + wort[idx+1] + ' gefunden ; Zahl erwartet.')
        elif bst == "[" or bst == "(":
            if idx < len(wort)-1 and wort[idx+1] not in zielAuf:
                raise Exception('Unzulaessige Formel : Klammerpaare duerfen nicht aufeinander folgen.')
            Klammern.append(bst)
            tiefe += 1
        elif bst == "]":
            if Klammern:
                klammer = Klammern.pop()
            else:
                raise Exception('Unzulaessige Formel : Klammerkombinationen falsch oder nicht genügend Klammern je Paar')
            if idx < len(wort)-1 and wort[idx+1] not in zielZu:
                raise Exception('Unzulaessige Formel : Klammerpaare duerfen nicht aufeinander folgen.')
            elif klammer != "[":
                raise Exception('Unzulaessige Formel : Klammern passen nicht zusammen : ' + klammer + ' gefunden ; [ erwartet . ')
            else:
                Tiefe.append(tiefe)
                tiefe -= 1
        elif bst == ")":
            if Klammern:
                klammer = Klammern.pop()
            else:
                raise Exception('Unzulaessige Formel : Klammerkombinationen falsch oder nicht genügend Klammern je Paar')
            if idx < len(wort)-1 and wort[idx+1] not in zielZu:
                raise Exception('Unzulaessige Formel : Klammerpaare duerfen nicht aufeinander folgen.')
            elif klammer != "(":
                raise Exception('Unzulaessige Formel : Klammern passen nicht zusammen : ' + klammer + ' gefunden ; ( erwartet . ')
            else:
                Tiefe.append(tiefe)
                tiefe -= 1
        elif bst.isdigit():
            if idx < len(wort)-1 and wort[idx+1] not in zielZu:
                if wort[idx+1].isdigit():
                    ctr = idx+1
                    while ctr < len(wort) and wort[ctr].isdigit():
                        ctr += 1
                    el = wort[idx:ctr]
                    if ctr < len(wort)-1 and wort[ctr] not in zielZu:
                        raise Exception('Unzulaessiger Satzbuchstabenindex : ' + ''.join(wort[idx:ctr+1]) + ' ist keine Zahl .')
        elif bst == '|' or bst == '&' or bst == '!':
            if idx < len(wort)-1 and wort[idx+1] not in zielLog:
                print(wort[idx:])
                raise Exception('Unzulaessige logische Aussage nach einem logischen Operator')
    
    if Klammern != []:
        raise Exception ( ' Unzulaessige Formel : Oeffnende Klammer ' + Klammern.pop() + ' wird nicht geschlossen . ' )
        
    return max(Tiefe)
    
    
def klammer(wort,interpretation):
    
    if len(wort) == 1:
        return wort[0]
    
    idx = 0
    auf = 0
    while idx < len(wort) and not((wort[idx] == "]" or wort[idx] == ")")):
        if wort[idx] == "[" or wort[idx] == "(":
            auf = idx
        idx +=1
    

    if auf == 0 and not(wort[auf] == '(' or wort[auf] == '['):
        return aussagenwert(wort,interpretation)
    
    aussage = aussagenwert(wort[auf+1:idx],interpretation)
    
    return klammer(wort[:auf] + [aussage] + wort[idx+1:],interpretation)

def aussagenwert(wort,interpretation):
    
    
    for bst in wort:
        if bst == 'x':
            wort.remove(bst)
            
    for zhl in range(len(wort)):
        if type(wort[zhl]) == str and wort[zhl].isdigit():
            wort[zhl] = interpretation[int(wort[zhl])]
            
    
    und = oder = neg = 0
    while "!" in wort:
        if neg < len(wort) and wort[neg] == '!' and wort[neg+1] == "!":
                del wort[neg+1]
                del wort[neg]
                neg = -1
        elif neg < len(wort) and wort[neg] == '!' and type(wort[neg+1]) == bool:
                wort[neg+1] = not(wort[neg+1])
                del wort[neg]
                neg = -1
        neg = neg + 1

    
    while "&" in wort:
        if und < len(wort) and wort[und] == "&": #and wort[und+1] != '!':
                wort[und] = wort[und-1] and wort[und+1]
                del wort[und+1]
                del wort[und-1]
                und = -1
        und = und + 1

                
    while "|" in wort:
        if oder < len(wort) and wort[oder] == "|": # and wort[oder+1] != '!':
                wort[oder] = wort[oder-1] or wort[oder+1]
                del wort[oder+1]
                del wort[oder-1]
                oder = -1
        oder = oder + 1
    
    if type(wort[0]) == str and wort[0].isdigit():
        wort[0] = interpretation[int(wort[0])]

    return wort[0]