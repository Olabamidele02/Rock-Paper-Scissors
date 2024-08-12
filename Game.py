import random

player_wins = 0
computer_wins = 0
choices = ["rock","paper","scissors"]

while True:
    user_input = input("Type either rock,paper or scissors or Q to quit the game: ")
    if user_input == "q":
        break

    if user_input not in choices:
        print("Invalid option")
        continue

    random_number = random.randint(0, 2)

    computer_choice = choices[random_number]
    print("Computer chose", computer_choice)

    if user_input == "rock" and computer_choice == "scissors":
        print("You win")
        player_wins += 1
    elif user_input == "paper" and computer_choice == "rock":
        print("You win")
        player_wins += 1
    elif user_input == "scissors" and computer_choice == "paper":
        print("You win")
        player_wins += 1
    elif user_input == computer_choice:
        print("You picked same options play again")
    else:
        print("You lose")
        computer_wins += 1

print("You won", player_wins, "times")
print("The computer won", computer_wins, "times")
print("Good job")