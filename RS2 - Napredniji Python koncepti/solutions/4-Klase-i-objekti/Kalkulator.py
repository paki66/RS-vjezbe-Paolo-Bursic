"""
Definirajte klasu Kalkulator s atributima a i b. Dodajte metode zbroj, oduzimanje, mnozenje, dijeljenje, potenciranje
    i korijen koje će izvršavati odgovarajuće operacije nad atributima a i b.
"""

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self, a, b):
        return a + b

    def oduzimanje(self, a, b):
        return a - b

    def mnozenje(self, a, b):
        return a * b

    def dijeljenje(self, a, b):
        return a / b

    def potenciranje(self, a, b):
        return a ** b

    def korijen(self, a, b):
        return a ** (1 / b)

