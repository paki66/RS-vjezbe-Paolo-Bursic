from phone_number_book import phone_number_book

possible_starts = ('385', '+385', '00385', '(385)')  # ću pustit 2. i 4. iako mislim da ne rabi

suffix_len = {
    'fiksna mreža': range(6, 8),
    'mobilna mreža': range(6, 8),
    'posebne usluge': 6
}

invalid_response = {
    "pozivni_broj": '0',
    "broj_ostatak": '0',
    "vrsta": None,
    "mjesto": None,
    "operater": None,
    "validan": False
}


def find_matching_prefix(text, prefixes):
    for prefix in prefixes:
        if text.startswith(prefix):
            return prefix
    return None


def validate_phone_number(phone_number: str):
    phone_number_digits = ''

    for char in phone_number:
        if char.isdigit():
            phone_number_digits += char

    invalid_start = find_matching_prefix(phone_number_digits, possible_starts)

    if invalid_start:
        invalid_start_len = len(invalid_start)
        phone_number = phone_number_digits[invalid_start_len:]
        phone_number = '0' + phone_number

    book_key = find_matching_prefix(phone_number, phone_number_book.keys())
    pozivni_broj = phone_number_book.book_key

    if not book_key:
        return invalid_response

    pozivni_len = len(book_key)
    broj_ostatak = phone_number_digits[pozivni_len:]

    return {
        "pozivni_broj": book_key,
        "broj_ostatak": broj_ostatak,
        "vrsta": pozivni_broj["vrsta"],
        "mjesto": pozivni_broj["mjesto"],
        "operater": pozivni_broj["operater"],
        "validan": True
    }
