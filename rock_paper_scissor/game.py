import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: 1 for Rock, 2 for Paper, 3 for Scissors")

    choices = ['Rock', 'Paper', 'Scissors']
    player_choice = int(input("Your turn: "))
    computer_choice = random.randint(1, 3)

    print("You chose:", choices[player_choice - 1])
    print("Computer chose:", choices[computer_choice - 1])

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
        print("Congratulations! You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Thank you for playing!")

play_game()






