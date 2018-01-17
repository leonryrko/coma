def quicksort(n, cmp, swp):
    """
    QUICKSORT sortiert eine Liste nach gegebener Vergleichsmethode
    
    @param: n Länge der Liste
    @param: cmp Vergleichsmethode
    @param: swp Vertauschmethode
    @return: 1 nach erfolgreichem Sortieren
    """
    
    #Kleine Laenge
    if n == 0:
        return 1

    if n == 1:
        return 1

    """
    #Totale Ordnung
    for l in range(n):
        for k in range(n):
            if l!=k and cmp(l,k) == cmp(k,l):
                raise Exception("Vergleichsmethode und Liste inkompatibel")
    """
    
    #Spezialfall: Laenge zwei
    if n == 2:
        #print(True)
        if not(cmp(0,1)):
            swp(0,1)
        return 1
    
    #Allgemeiner Fall
    if not(cmp(0,1)):
        swp(0,1)
    if not(cmp(1,2)):
        swp(1,2)
    if not(cmp(0,1)):
        swp(0,1)

    quickrange(0,n,cmp,swp)

    return 1

def quickrange(i,j,cmp,swp):
    """
    QUICKRANGE sortiert eine Teilliste nach gegebener Vergleichsmethode zwischen den Positionen i und j (exklusive)
    
    @param: i Startposition der Teilliste
    @param: j Endposition der Teilliste (ausgeschlossen)
    @param: cmp Vergleichsmethode
    @param: swp Vertauschmethode
    """
    #Kleine Laenge
    if j-i == 0:
        return

    if j-i == 1:
        return
    

    #Spezialfall: Laenge zwei
    if j-i == 2:
        #print(True)
        if not(cmp(i,i+1)):
            swp(i,i+1)
        return 
    
    if not(cmp(i,i+1)):
        swp(i,i+1)
    if not(cmp(i+1,i+2)):
        swp(i+1,i+2)
    if not(cmp(i,i+1)):
        swp(i,i+1)
    
    piv = i+1
    k = i+2
    while k < j:
        if piv < j-1 and cmp(k,piv):
            swp(piv,piv+1)
            swp(k,piv)
            piv += 1
        k += 1
    
    if i+1<piv:
        quickrange(i,piv,cmp,swp)
    if piv+1 < j: 
        quickrange(piv+1,j,cmp,swp)
        

#Beispielfunktionen    
def cmp_din5007a(i,j):
    #print(i,j)
    a = L[i].casefold().replace('ä','a').replace('ö','o').replace('ü','u')
    b = L[j].casefold().replace('ä','a').replace('ö','o').replace('ü','u')
    return a<=b

def cmp_din5007b(i,j):
    #print(i,j)
    a = L[i].casefold().replace('ä','ae').replace('ö','oe').replace('ü','ue')
    b = L[j].casefold().replace('ä','ae').replace('ö','oe').replace('ü','ue')
    return a<=b

def swp(i,j):
    global L
    #print(L)
    L[i], L[j] = L[j], L[i]
    
#Beispielaufruf
def test():
    L = ['Gode', 'Göbel', 'Goethe', 'Götz', 'Goldmann']
    quicksort(5,cmp_din5007a,swp)
        #['Göbel', 'Gode', 'Goethe', 'Goldmann', 'Götz']
    quicksort(5,cmp_din5007b,swp)
        #['Gode', 'Göbel', 'Goethe', 'Götz', 'Goldmann']
