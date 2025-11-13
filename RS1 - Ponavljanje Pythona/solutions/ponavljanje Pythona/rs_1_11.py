def grupiraj_po_paritetu(lista):
    grupirani_brojevi = {"parni": [], "neparni": []}

    for i in lista:
        if i % 2:
            grupirani_brojevi["neparni"].append(i)
        else:
            grupirani_brojevi["parni"].append(i)

    return grupirani_brojevi


print(grupiraj_po_paritetu([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
