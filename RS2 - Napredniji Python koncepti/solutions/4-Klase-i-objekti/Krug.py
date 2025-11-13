"""
Definirajte klasu Krug s atributom r. Dodajte metode opseg i povrsina koje će računati opseg i površinu kruga.

Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.
"""

from math import pi

class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return round(2 * pi * self.r, 2)

    def povrsina(self):
        return round(pi * (self.r ** 2), 2)


proizvoljni_radijus = 5
proizvoljni_krug = Krug(proizvoljni_radijus)

opseg_kruga = proizvoljni_krug.opseg()
povrsina_kruga = proizvoljni_krug.povrsina()

print(f"Krug: r={proizvoljni_radijus}, o={opseg_kruga}, P={povrsina_kruga}")
