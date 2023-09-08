# We will write a rock paper scissors game in class - Complete it in this file

import random

player_choice = 'rock'
computer_choice = 'paper'

#Creates a function that gets choices
def get_choices():
    options = ['rock', 'paper', 'scissors']

    player_choice = input("Enter a choice (rock, paper, scissors): ") 
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}

    return choices

# Function to check for a win
def check_win(player, computer):
    print(f"you chose {player}, and computer chose {computer}")

    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors, You Win!"
        else:
            return "Paper covers rock, You Lose :("
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You Win!"
        else:
            return "Paper gets cut by scissors! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You Win!"
        else:
            return "Rock smashes scissors! You Lose"

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)