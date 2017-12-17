def repraesentant(a,m,k):
    """
    Gibt den Repraesentant modulo m in {k, k+1, ..., k+m-1} des Eingabewertes a an.
    
    @param: int a Ganze Zahl, dessen Repraesentant modulo m bestimmt werden soll
    @param: int m 
    @param: int k
    @return:
    """
    
    for q in range(k,k+m):
        if (a-q)%m == 0:
            return q

def f(z, l):
    """
    Gibt das binaere Komplement von z bei l Stellen in Basis 10 wieder
    
    @param: int z mit -2**(l-1) <= z <= 2**(l-1)-1
    @param: int l strikt positiv
    @return:
    """

        

    if z >= 0:
        return z
    else:
        return repraesentant(z,2**l,0)


def umkehrfunktion_von_f(r, l):
    """
    Gibt das Urbildelement von r unter der Funktion f bezueglich der Basis 2
    und der Darstellungslaenge l zurueck
    
    @param:
    @param:
    @return:
    """

    if r <= 2**(l-1)-1:
        return r
    else:
        return -repraesentant(2**l-r,2**l,0)



