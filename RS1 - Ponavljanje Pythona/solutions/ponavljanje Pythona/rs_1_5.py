faktorijela = int(input("faktorijela: "))

rezultat = 1

for i in range(1, faktorijela + 1):
    rezultat *= i

print(rezultat)
rezultat = 1
j = 1

while j <= faktorijela:
    rezultat *= j
    j += 1

print(rezultat)
