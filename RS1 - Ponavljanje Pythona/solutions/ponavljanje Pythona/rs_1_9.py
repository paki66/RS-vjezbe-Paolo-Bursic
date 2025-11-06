def ukloni_duplikate(lista):
    sets = set(lista)
    return list(sets)


print(ukloni_duplikate([1, 2, 3, 1, 2, 3]))
