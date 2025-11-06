
def provjera_lozinke(lozinka):
    length = len(lozinka)

    if 8 >= length >= 15:
        return "Lozinka mora sadržavati između 8 i 15 znakova."

    if lozinka.islower() and not lozinka.isdigit():
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"

    lozinka_lower = lozinka.lower()

    if "password" in lozinka_lower or "lozinka" in lozinka_lower:
        return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"

    return "Lozinka je jaka!"


password = input("Enter your password: ")
output = provjera_lozinke(password)
print(output)
