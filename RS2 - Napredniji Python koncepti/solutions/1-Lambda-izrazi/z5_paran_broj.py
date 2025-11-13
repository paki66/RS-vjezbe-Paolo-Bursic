"""
Vrati True ako je broj paran, inače vrati None:

def paran_broj(x):
    if x % 2 == 0:
        return True
    else:
        return None
"""

paran_broj = lambda x : True if x % 2 == 0 else None



ex_1, ex_2, ex_3 = 2, 3, -1

print(f"paran_broj({ex_1}) = {paran_broj(ex_1)}")
print(f"paran_broj({ex_2}) = {paran_broj(ex_2)}")
print(f"paran_broj({ex_3}) = {paran_broj(ex_3)}")