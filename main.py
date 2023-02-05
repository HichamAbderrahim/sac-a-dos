class Objet:
    def __init__(self, valeur, poid):
        self.valeur = valeur
        self.poid = poid

    def __str__(self):
        return str.format("Objet(valeur = {}, poid = {})", self.valeur, self.poid)


def maximum(x, y):
    """ Cette fonction est utilisée dans la fonction exhaustive pour calculer le maximum entre deux valeurs """

    if x > y:
        return x
    return y


def exhaustive(P, tableau, N):
    """ Cette fonction calcule la valeur maximale que l'on peut atteindre en mettant des objets dans un sac à dos en
    essayant toutes les possibilités possibles, la complexité est O(2^n) """

    if N == 0 or P == 0:
        return 0
    if tableau[N - 1].poid > P:
        return exhaustive(P, tableau, N - 1)
    return maximum(tableau[N - 1].valeur + exhaustive(P - tableau[N - 1].poid, tableau, N - 1),
                   exhaustive(P, tableau, N - 1))


def fusion(tableau, g, m, d, comparer):
    """ Cette fonction est utilisée dans la fonction tri_fusion pour fusionner"""

    G = [None] * (m - g + 1)
    D = [None] * (d - m)

    for i in range(G.__len__()):
        G[i] = tableau[g + i]

    for i in range(D.__len__()):
        D[i] = tableau[m + 1 + i]

    i = j = 0
    k = g

    while i < G.__len__() and j < D.__len__():
        if comparer(G[i], D[j]):
            tableau[k] = G[i]
            i = i + 1
        else:
            tableau[k] = D[j]
            j = j + 1
        k = k + 1

    while i < G.__len__():
        tableau[k] = G[i]
        i = i + 1
        k = k + 1

    while j < D.__len__():
        tableau[k] = D[j]
        j = j + 1
        k = k + 1


def tri_fusion(tableau, g, d, comparer):
    """ Cette fonction trier un tableau avec une comparer donnée, la complexité est O(n log n) """

    if g < d:
        m = int(g + (d - g) / 2)
        tri_fusion(tableau, g, m, comparer)
        tri_fusion(tableau, m + 1, d, comparer)
        fusion(tableau, g, m, d, comparer)


def glouton(W, tableau, N):
    """ Cette fonction calcule la valeur maximale que l'on peut atteindre en mettant des objets dans un sac à dos en
        utilisant la méthode glouton, la complexité est O(n log n) """

    tri_fusion(tableau, 0, N - 1, lambda o1, o2: (o1.valeur / o1.poid) > (o2.valeur / o2.poid))
    total = 0.0
    for item in tableau:
        if item.poid <= W:
            W -= item.poid
            total += item.valeur
    return total


try:
    taille_de_sac = int(input("Entrez la taille de sac à dos:"))
    nombre_de_objets = int(input("Entrez le nombre d'objets:"))
    objets = [Objet] * nombre_de_objets

    for pos in range(nombre_de_objets):
        print("---------------")
        print("Objet " + str(pos+1))
        objets[pos] = Objet(float(input("Entrez la valeur : ")), float(input("Entrez le poid : ")))

    print("---------------")
    for pos in range(nombre_de_objets):
        print(objets[pos])
    print("---> Exhaustive: " + str(exhaustive(taille_de_sac, objets, nombre_de_objets)))
    print("---> Glouton: " + str(glouton(taille_de_sac, objets, nombre_de_objets)))

except ValueError:
    print("La taille du sac à dos et le nombre d'objets doivent être un nombre entier")
