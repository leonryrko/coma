def goldener_schnitt(praezision):
    """
    Gibt den Index L an, damit f_{2L+1}/f_{2L} den Goldenen Schnitt zu gegebener PRAEZISION nah ist. 
    Dabei ist f_i die i-te Fibonnacci-Zahl
    
    @param: int praezision
    @return: list Gibt eine Zahl L aus, die fuer die 2L-te Fibonnacci-Zahl steht.
            Zudem werden in zwei Tupeln die Fibonnacci Zahlen (f_2L, f_2L-1) und (f_2L+1, f_2L) ausgegeben.
    """

    f1 = f2 = 1
    f3 = f1 + f2
    f4 = f2 + f3

    l = 2
    while praezision * (f3**2 - f2*f4) >= f4*f3: #praezision * ((f4+f3)*f3 - f4**2) > f4*f3:
        temp = f4
        f3 = f4 + f3 #f5
        f4 = f3 + f4 #f5 + f4 = f6
        f2 = temp #f4
        l += 1


    return [l, (f4, f3), (f4+f3, f4)]
