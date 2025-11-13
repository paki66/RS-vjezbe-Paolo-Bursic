def obrni_rjecnik(rjecnik):
    return dict(zip(rjecnik.values(), rjecnik.keys()))


rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

print(obrni_rjecnik(rjecnik))
