def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


print(is_prime(7))  # True
print(is_prime(10))  # False


def primes_in_range(start, end):
    output = []

    for i in range(start, end + 1):
        if is_prime(i):
            output.append(i)

    return output


print(primes_in_range(1, 10))
