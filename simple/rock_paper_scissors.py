import random

options = ["rock", "paper", "scissors"]
user_wins = 0
ai_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        quit()
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    ai_choice = options[random_number]
    print("Ai choice is", ai_choice)

    if user_input == "rock" and ai_choice == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and ai_choice == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and ai_choice == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == ai_choice:
        print("Draw!")
    else:
        print("You lose!")
        ai_wins += 1

print("You won", user_wins, "times")
print("Ai won", ai_wins, "times")
print("Goodbye!")
