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
    answer = int(input("Name your number: "))

    if random_number == answer:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    else:
        print("Incorrect, try again")
    attempts += 1
    continue    