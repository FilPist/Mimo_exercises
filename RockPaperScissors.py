# Rock, Paper, Scissors Game
# This is a simple game where the player plays against the computer.
# The player needs to win 2 rounds to win the game.

import random

player_wins = 0
computer_wins = 0

print ("Let's play rock, paper, or scissors")


while player_wins < 2 and computer_wins < 2:

  choices = ["rock", "paper", "scissors"]
  player_choice = input("\n Choose rock, paper, or scissors: ").lower()
  computer_choice = random.choice(choices)
  print (f"Computer choses: {computer_choice}")

  if player_choice not in choices:
    print("Please,choose one of these: rock, paper, or scissors.")
    continue

  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
  elif player_choice == computer_choice:
    winner = "Tie"
  else:
    winner = "Computer"

  if winner == "Player":
    player_wins += 1
    print("You won")
  elif winner == "Computer":
    computer_wins += 1
    print("Computer won")
  else:
    print("It's a tie")

  print (f"Current Score - Player: {player_wins}, Computer {computer_wins}.")

if player_wins > computer_wins:
  print ("Congratulations! You won.")
else:
  print ("Computer won!")