import random

def get_user_choice():
    # TODO: Ask the user for their choice (rock, paper, or scissors) and return it
    choice=input("enter your choice")
    choice=choice.lower()
    if choice=="rock" or choice=="paper" or choice=="scissors":
        return choice.lower()
    else:
        print("Please enter valid your choice")
        return
   

def get_computer_choice():
    # TODO: Select a random choice for the computer (rock, paper, or scissors) and return it
   return random.choice(['rock', 'paper', 'scissors'])
 


def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return 'draw'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return 'user'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'user'
    else:
        return 'computer'


def update_score(winner, scores):
    if winner == 'user':
        scores['user'] += 1
    elif winner == 'computer':
        scores['computer'] += 1
    elif winner == 'draw':
        scores['draw'] += 1
    return scores


def display_score(scores):
    print("------- Score -------")
    print(f"User: {scores['user']} | Computer: {scores['computer']} | Draws: {scores['draw']}")
    print("---------------------")

def play_again():
    # TODO: Ask the user if they want to play again
    # Return True if they want to play again, otherwise return False
    pass

def main():
    scores = {'user': 0, 'computer': 0, 'draw': 0}

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    winner = determine_winner(user_choice, computer_choice)
    print(f"User choice: {user_choice}, Computer choice: {computer_choice}, Winner: {winner}")

    print("Thank you for playing Rock, Paper, Scissors!")

def main():
    scores = {'user': 0, 'computer': 0, 'draw': 0}

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        winner = determine_winner(user_choice, computer_choice)
        print(f"User choice: {user_choice}, Computer choice: {computer_choice}, Winner: {winner}")

        scores = update_score(winner, scores)
        display_score(scores)

        play_again_input = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again_input != 'yes':
            break

    print("Thank you for playing Rock, Paper, Scissors!")

if __name__ == "__main__":
    main()
