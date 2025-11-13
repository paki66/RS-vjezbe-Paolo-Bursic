def brojanje_rijeci(tekst):
    rijeci = tekst.split(" ")
    razlicite_rijeci = set(rijeci)
    brojac_rijeci = dict.fromkeys(razlicite_rijeci, 0)

    for rijec in rijeci:
        brojac_rijeci[rijec] += 1

    return brojac_rijeci


print(brojanje_rijeci("Python je programski jezik koji je jednostavan "
                      "za učenje i korištenje. Python je vrlo popularan."))
