"""
Koristeći funkciju map, kvadrirajte duljine svih nizova u listi:
"""

nizovi = ["jabuka", "kruška", "banana", "naranča"]

kvadrirane_duljine = list(map(lambda x : len(x) ** 2, nizovi))

print(kvadrirane_duljine) # [36, 36, 36, 49]
