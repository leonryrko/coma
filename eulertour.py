def eulertour(A):
    """
    EULERTOUR gibt aus, ob auf einem Aen eine Eulertour moeglich ist, und im positiven Fall eine moegliche Eulertour heraus

    @param:  list A Adjazenzliste des zu betrachtenden Graphen
    @return: boolean falls negativ, ansonsten
             list moegliche Eulertour 
    """
    #Zusammenhaengend
    C = [list(r) for r in A]
    if not zusammenhaengend(C):
        return False
    
    #Zaehle die Anzahl der Knoten ungeraden Grads
    ungerade = [ x for x in range(len(A)) if len(A[x])%2==1 ]
    
    for n in range(len(A)):
        if len(A[n])>0:
            for elem in A[n]:
                if elem < len(A):
                    ungerade.append(n)
            break
    
    if len(ungerade)>1:
        return False

    kanten = [ungerade[0]]
    tour = []
    
    while len(kanten)>0:
        v = kanten[-1]
        if len(A[v])>0:
            w = A[v][0]
            kanten.append(w)
            A[w].remove(v)
            A[v].remove(w)
        else:
            tour.append(kanten.pop())
    
    return tour




def zusammenhaengend(C):
    """
    ZUSAMMENHAENGEND gibt an, ob ein Graph gegeben durch seine Adjazenzliste A zusammenhaengend ist, oder nicht
    
    @param: A Adjazenzliste des Graphen
    @return: boolean True falls zusammenhaengend, False sonst
    """

    
    R = []
    Q = []
    for r in C:
        if len(r)>0:
            for w in r:
                if w < len(C):
                    R.append(w)
                    Q.append(w)
            break
    
    
    while len(Q)>0:
        v = Q[-1]
        if len(C[v])>0:
            w = C[v][0]
            if w not in R:
                R.append(w)
                Q.append(w)
            C[v].remove(w)    
        else:
            Q.remove(v)

    for n in range(len(C)):
        if n not in R:
            if len(C[n])>0:
                return False

    return True