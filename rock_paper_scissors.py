import random


moves= ["rock" , "paper", "scissor"]

while True :

    user_input = input("Enter you choice (rock , paper , scissors): ")

    computer_action = random.choice(moves)

    if user_input == computer_action:
        print(f"You both selected {user_input}. It,s a Tie!")

    elif (
            (user_input == "rock" and computer_action == "scissors")
            or (user_input == "rock" and computer_action == "scissors")
            or (user_input == "rock" and computer_action == "scissors")
    ):

        print(f"You Win!. {user_input} beats {computer_action}")

    else:
        print(f"You lose!. {computer_action} beats {user_input}")

    play_again = input("Do you want to play again(yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing")
