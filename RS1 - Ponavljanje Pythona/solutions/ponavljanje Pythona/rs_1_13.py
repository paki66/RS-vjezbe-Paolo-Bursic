def prvi_i_zadnji(lista):
    return lista[0], lista[-1]


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(prvi_i_zadnji(lista))


def maks_i_min(lista):
    maks = min = lista[0]

    for i in lista:
        if i < min:
            min = i

        if i > maks:
            maks = i

    return maks, min


lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

print(maks_i_min(lista))


def presjek(skup_1, skup_2):
    rezultat = set()

    for i in skup_1:
        if i in skup_2:
            rezultat.add(i)

    return rezultat


skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

print(presjek(skup_1, skup_2))
