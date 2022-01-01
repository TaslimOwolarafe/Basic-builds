import random

Play_on = True

while Play_on:
    print("Rock smashes Scissors.\nScissors cuts Paper.\nPaper wraps Rock.")
    Inputs = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    user_hand = input("Pick one hehe: (R for rock, P for paper, S for scissors): ")
    print(f"You picked {Inputs[user_hand.upper()]}.")
    computer_hand = random.choice(list(Inputs.values()))

    if Inputs[user_hand.upper()] == computer_hand:
        print(f"It's a tie. You both picked {str(computer_hand)}.")
    elif Inputs[user_hand.upper()] == "Rock":
        if computer_hand == 'Paper':
            print("You lose, computer wins: Paper wraps Rock.")
        else:
            print("You win! Rock smashes scissors.")
    elif Inputs[user_hand.upper()] == "Scissors":
        if computer_hand == "Rock":
            print("You lose, computer wins: Rock smashes Scissors.")
        else:
            print("You win! Scissors cuts Paper.")
    elif Inputs[user_hand.upper()] == "Paper":
        if computer_hand == "Scissors":
            print("You lose, computer wins: Scissors cuts Paper.")
        else:
            print("You win! Paper wraps Rock.")

    Option = input("Do you want to play again? (Yes/No): ")
    if Option[0].upper() != 'Y':
        break
