def steigungsverhalten(a,b,c,d,x0):
    """
    Analysiert das Verhalten eines Polynoms der Form ax3 + bx2 + cx + d an der Stelle x0.

    @param: int a Koeffizient des kubischen Glieds
    @param: int b Koeffizient des quadratischen Glieds
    @param: int c Koeffizient des linearen Glieds
    @param: int d Koeffizient des konstanten Glieds
    @param: int x0 Ganzzahlige Stelle
    @return: str Das Verhalten am Punkt x0
    """
    fprime = 3*a*x0**2 + 2*b*x0 + c # Erste Ableitung
    fsec = 6*a*x0 + 2*b # Zweite Ableitung

    if fprime > 0:
        print('An der Stelle {} steigt die Funktion.'.format(x0))
    elif fprime < 0:
        print('An der Stelle {} fällt die Funktion.'.format(x0))
    elif fsec > 0:
        print('An der Stelle {} hat die Funktion ein lokales Minimum.'.format(x0))
    elif fsec < 0:
        print('An der Stelle {} hat die Funktion ein lokales Maximum.'.format(x0))
    else:
        print('An der Stelle {} hat die Funktion einen kritischen Punkt unbekannten Typs.'.format(x0))
    

def test():
    steigungsverhalten(1,-1,1,-1,1)
    steigungsverhalten(1,3,3,1,-1)