"""
Definirajte varijablu min_duljina koja će pohranjivati minimalnu duljinu riječi int. Koristeći odgovarajuću funkciju
višeg reda i lambda izraz, pohranite u varijablu duge_rijeci sve riječi iz liste rijeci koje su dulje od min_duljina:
"""

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

min_duljina = input("Unesite minimalnu duljinu riječi: ")

# min_duljina = 7
duge_rijeci = list(filter(lambda rijec : len(rijec) > int(min_duljina), rijeci))

print(duge_rijeci) # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']
