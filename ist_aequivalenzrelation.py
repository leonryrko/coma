def ist_aequivalenzrelation(n,R):
    """
    IST_AEQUIVALENZRELATION ueberprueft, ob zu gegebener Zahl n die Relation R eine Aequivalenzrelation auf {1,...,n} ist.
    
    @param: int n Maximum der Menge {1,...,n}
    @param: list R Liste aller Relationen auf der Menge {1,...,n} 
    @return: boolean TRUE wenn die Relation eine Aequivalenz auf der Menge {1,...,n} ist, FALSE sonst
    """
    #if n==0 and R==[]: return True

    Equiv = []
    for i in range(1,n+1):
        equiv = []
        for r in R:
            if r[0] == i and 0 < r[1] <= n: #and r[1] not in equiv:
                equiv.append(r[1])
            if r[0]>n or r[1]>n:
                return False
        Equiv.append(equiv)

    for e in Equiv:
        if Equiv.index(e) + 1 not in e: return False #Reflexiv
        for j in e:
            if len(e) != len(Equiv[j-1]): return False #Symmetrisch & Transitiv

    return True

