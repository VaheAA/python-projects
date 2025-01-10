import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type a number larger than 0 next time.")
        quit()


random_number = random.randrange(top_of_range)
attempts = 0

while True:
    attempts += 1
    user_guess = input("Name your number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number larger than 0 next time.")
        continue

    if random_number == user_guess:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    else:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number")

    continue
