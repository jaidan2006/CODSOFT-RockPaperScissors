import random

def get_user_choice():
    print("\nChoose one: Rock, Paper, or Scissors")
    return input("Your choice: ").strip().lower()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    if winner == "tie":
        print("Result: It's a tie!")
    elif winner == "user":
        print("Result: You win!")
    else:
        print("Result: Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input! Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScoreboard -> You: {user_score} | Computer: {computer_score}")

        again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\nThanks for playing! Final Score -> You: {} | Computer: {}".format(user_score, computer_score))
            break

play_game()