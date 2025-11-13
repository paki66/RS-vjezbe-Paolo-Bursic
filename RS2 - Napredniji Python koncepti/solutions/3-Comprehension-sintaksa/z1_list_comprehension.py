"""
Koristeći list comprehension, izgradite listu parnih kvadrata brojeva od 20 do 50:
"""

parni_kvadrati = [kvadrat ** 2 for kvadrat in range(20, 51) if kvadrat % 2 == 0]

print(parni_kvadrati) # [400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500]
