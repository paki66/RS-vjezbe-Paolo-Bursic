def count_vowels_consonants(tekst):
    output = {"vowels": 0, "consonants": 0}
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    for i in tekst:
        if i in vowels:
            output["vowels"] += 1
        if i in consonants:
            output["consonants"] += 1

    return output


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(count_vowels_consonants(tekst))
