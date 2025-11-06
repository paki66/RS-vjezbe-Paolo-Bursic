def filtriraj_parne(lista):
    output_lista = []

    for i in lista:
        if i % 2 == 0:
            output_lista.append(i)

    return output_lista


print(filtriraj_parne([1, 2, 3, 4, 5]))
