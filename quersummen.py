def quersummen(n):
    """
    Berechnet die Quersumme von n in allen Darstellungen von Basis 2 bis n

    @param: int n Zahl und Grenze der Anzahl der zu beachtenden Basen
    @return: int Durch Leerzeichen getrennte Reihe der Quersummen in aufsteigenden Basen
    """
    
    X = []
    rounds = n
    temp = n
    for b in range(2,rounds+1):
        n = temp
        Koeff = []
        while n >= 1:
            i = 0
            while n/(b**i)>=b:
                i = i + 1
                
            k = 0
            if b**i > n:
                n = n
            else:
                while (k+1)*b**i <= n and k + 1 < b:
                    k = k + 1
                Koeff.append(k)
                n = n%(k*b**i)

            
        x = 0
        for k in range(0,len(Koeff)):
            x = x + Koeff[k]
        X.append(str(x))

    
    zahl = str(' '.join(X))

    print(zahl)