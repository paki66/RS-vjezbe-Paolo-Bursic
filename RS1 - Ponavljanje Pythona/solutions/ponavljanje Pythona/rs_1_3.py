import random

target = random.randint(1, 100)
current_guess = guess_count = 0
print(target)

while target != current_guess:
    current_guess = input("Guess a number between 1 and 100: ")
    current_guess = int(current_guess)
    guess_count += 1

print(f"You have guessed {guess_count} times.")
