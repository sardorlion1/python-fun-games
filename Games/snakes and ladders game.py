
import random
import matplotlib.pyplot as plt

final = 100

player1 = input("Player 1 enter your name: ")
player2 = input("Player 2 enter your name: ")

# Initialize player positions
position1 = 0
position2 = 0

positions1 = [position1]  # List to store player 1 positions
positions2 = [position2]  # List to store player 2 positions

def roll_dice():
    return random.randint(1, 6)

def update_position(current_position, dice_result):
    new_position = current_position + dice_result

    if new_position > final:
        return current_position

    # Define snakes and ladders positions
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    if new_position in snakes:
        new_position = snakes[new_position]
    elif new_position in ladders:
        new_position = ladders[new_position]

    return new_position

running = True
while running:

    # Roll the dice for player 1
    input("Player 1 - Press Enter to roll the dice")
    dice1 = roll_dice()
    print(player1 + " rolled a " + str(dice1))
    position1 = update_position(position1, dice1)
    print(player1 + " is at position " + str(position1))
    positions1.append(position1)  # Store the updated position

    # Check if player 1 wins
    if position1 == final:
        print(player1 + " wins!")
        break

    # Roll the dice for player 2
    input("Player 2 - Press Enter to roll the dice")
    dice2 = roll_dice()
    print(player2 + " rolled a " + str(dice2))
    position2 = update_position(position2, dice2)
    print(player2 + " is at position " + str(position2))
    positions2.append(position2)  # Store the updated position

    # Check if player 2 wins
    if position2 == final:
        print(player2 + " wins!")
        break

# Plot the positions on a graph
plt.plot(positions1, label=player1)
plt.plot(positions2, label=player2)
plt.xlabel("Number of Moves")
plt.ylabel("Position")
plt.legend()
plt.title("Player Positions")
plt.show()