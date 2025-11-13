"""
Koristeći dictionary comprehension, izgradite rječnik iteriranjem kroz listu brojeva od 50 do 500 s korakom 50, gdje su
ključevi brojevi, a vrijednosti su korijeni tih brojeva zaokruženi na 2 decimale:
"""

from math import sqrt

korjenuj = lambda x : round(sqrt(x), 2)

korijeni = {broj: korjenuj(broj) for broj in range(50, 501, 50)}

print(korijeni) # {50: 7.07, 100: 10.0, 150: 12.25, 200: 14.14, 250: 15.81, 300: 17.32, \
                #  350: 18.71, 400: 20.0, 450: 21.21, 500: 22.36}
