import random

print("Welcome to the second part of my first project in python, the Dice Duel")

def roll():     ##Define a function that generates and return a random number between 1-6.
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:     ##Creates a loop that makes sure there are 2-4 players playing the game.
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)] ##List comprehension. Puts a 0 inside of the list for every single player in a loop.

while max(player_scores) < max_score:   ##Creates a loop to keep the players playing until they reach the maximum score.

    for players_idx in range(players):     ##Creates a for loop announcing the player's current score.
        print("\nPlayer number", players_idx + 1, "turn just started!")
        print("Your total score is:", player_scores[players_idx], "\n")
        current_score = 0

        while True: ##Creates a loop where the player keeps rolling the dice until he decides to stop or pulls 1.
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower()  != "y":
              break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[players_idx] += current_score
        print("Your total score is:", player_scores[players_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
