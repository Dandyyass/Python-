# Rock Paper Scissors Game
# Player vs Computer. First to win 3 rounds wins the match.

import random

# --- Part 1: Basic version (no class) ---

choices = ["rock", "paper", "scissors"]

player = input("Enter rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if player == computer:
    result = "Draw!"
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    result = "You win!"
else:
    result = "Computer wins!"

print(result)
print(choices.__class__, "\n", player.__class__)

"""
Instance Variable: Each player has their own win count and name.
Class Variable: All players share the same choices list (rock, paper, scissors).
* Instance variable is unique per player, class variable is shared by all.
"""



class RPSGame:
    choices = ["rock", "paper", "scissors"]  
    wins_needed = 3                           

    def __init__(self, player):
        self.player = player      
        self.player_wins = 0      
        self.computer_wins = 0    

    def _get_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "draw"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            return "player"
        else:
            return "computer"

    def play(self):
        print("\n--- {} vs Computer ---".format(self.player))
        print("First to {} wins!\n".format(self.wins_needed))

        while self.player_wins < self.wins_needed and self.computer_wins < self.wins_needed:
            player_choice = input("Enter rock, paper, or scissors: ").lower()
            if player_choice not in self.choices:
                print("Invalid choice! Try again.")
                continue

            computer_choice = random.choice(self.choices)
            print("Computer chose:", computer_choice)

            result = self._get_result(player_choice, computer_choice)
            if result == "player":
                self.player_wins += 1
                print("You win this round!")
            elif result == "computer":
                self.computer_wins += 1
                print("Computer wins this round!")
            else:
                print("Draw!")

            print("Score -> {}: {} | Computer: {}\n".format(
                self.player, self.player_wins, self.computer_wins))

        if self.player_wins == self.wins_needed:
            print(" {} wins the match!".format(self.player))
        else:
            print(" Computer wins the match!")
        again = input("Do you want to play again? (y/n): ").lower()
        if again == "y":
            self.player_wins = 0
            self.computer_wins = 0
            self.play()
        else:
            print("Thanks for playing!")

    def info(self):
        print("Player        :", self.player)
        print("Player Wins   :", self.player_wins)
        print("Computer Wins :", self.computer_wins)
        print("-------------------")


# --- Create 2 players ---
game_1 = RPSGame("James")
game_2 = RPSGame("Charlie")

print(game_1.__dict__, "\n", game_2.__dict__)

game_1.play()
game_1.info()

game_2.play()
game_2.info()