def recherche_dichotomique(element, liste_triee):
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b :
        if liste_triee[m] == element:
            return m
        elif liste_triee[m] > element:
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a

li = [0, 4, 5, 19, 100, 200, 450, 999]
print(recherche_dichotomique(5, li))