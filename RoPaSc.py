import random

Play_on = True

while Play_on:
    Wins = "Rock smashes Scissors.\nScissors cuts Paper.\nPaper wraps Rock."
    print(Wins)
    Inputs = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    user_hand = input("Pick one hehe: (R for rock, P for paper, S for scissors): ")
    print(f"You picked {Inputs[user_hand.upper()]}.")
    computer_hand = random.choice(list(Inputs.values()))
    Hey = Wins.split('.')
    if Inputs[user_hand.upper()] == computer_hand:
        print(f"It's a tie. You both picked {str(computer_hand)}.")
    elif Inputs[user_hand.upper()] == "Rock":
        if computer_hand == 'Paper':
            print(f"You lose, computer wins: {Hey[2]}.")
        else:
            print(f"You win! {Hey[0]}.")
    elif Inputs[user_hand.upper()] == "Scissors":
        if computer_hand == "Rock":
            print(f"You lose, computer wins: {Hey[0]}.")
        else:
            print(f"You win! {Hey[1]}.")
    elif Inputs[user_hand.upper()] == "Paper":
        if computer_hand == "Scissors":
            print(f"You lose, computer wins: {Hey[1]}.")
        else:
            print(f"You win! {Hey[2]}.")

    Option = input("Do you want to play again? (Yes/No): ")
    if Option[0].upper() != 'Y':
        break
