
#DheyeaHussein#
import random

# define the game rules
rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

# define the game function
def play_game(rounds):
    # initialize scores
    player1_score = 0
    player2_score = 0
    
    # loop through the rounds
    for i in range(rounds):
        print(f"Round {i+1}:")
        
        # player 1 input
        player1_choice = input("Player 1, choose rock, paper, or scissors: ").lower()
        
        # validate player 1 input
        while player1_choice not in rules.keys():
            player1_choice = input("Invalid input. Player 1, choose rock, paper, or scissors: ").lower()
        
        # player 2 input
        player2_choice = random.choice(list(rules.keys()))
        
        print(f"Player 2 chose {player2_choice}.")
        
        # determine winner
        if player1_choice == player2_choice:
            print("It's a tie!")
        elif rules[player1_choice] == player2_choice:
            print("Player 1 wins!")
            player1_score += 1
        else:
            print("Player 2 wins!")
            player2_score += 1
    
    # print final scores and winner
    print(f"\nFinal scores:\nPlayer 1: {player1_score}\nPlayer 2: {player2_score}")
    if player1_score > player2_score:
        print("Player 1 wins the game!")
    elif player2_score > player1_score:
        print("Player 2 wins the game!")
    else:
        print("It's a tie game!")

        
# start the game
rounds = int(input("How many rounds do you want to play? "))
play_game(rounds)