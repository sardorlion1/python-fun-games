import random 

final = 100

player1 = input("Ismingizni kiriting(o'yinchi1): ")
player2 = input("Ismingizni kiriting(o'yinchi2): ")

def roll_dice():
    return random.randint(1, 6)

def update_position(current_position, dice_result):
    
    new_position = current_position + dice_result
    
    if new_position > final:
        return current_position
    
    # define snakes and ladders 
    
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
    if new_position in snakes:
        new_position = snakes[new_position]
    
    elif new_position in ladders:
        new_position = ladders[new_position]
    return new_position

def run():  
    position1, position2, positions1, positions2 = new_func()
    
    running = True
    
    while running:
        input("O'yinchi1 'Enter' tugmasini bosing zarlarni tashlash uchun: ")
        dice1 = roll_dice()
        print(player1 + " ga " + str(dice1)+" tushdi!")
        position1 = update_position(position1, dice1)
        print(player1+" " + str(position1) + " pasitsiyada")
        positions1.append(position1)
        
        # check if the player1 wins
        if position1 == final:
            running = False
            print(player1 + " G'o'lib!")
            play_again()
            break
     
        input("O'yinchi2 'Enter' tugmasini bosing zarlarni tashlash uchun: ")
        dice2 = roll_dice()
        print(player2 + " ga " + str(dice2)+" tushdi!")
        position2 = update_position(position2, dice2)
        print(player2+" " + str(position2) + " pasitsiyada")
        positions2.append(position2)
        
        # check if the player2 wins
        if position2 == final:
            running = False
            print(player2 + " G'o'lib!")
            play_again()
            break
     
     
def new_func():
    position1 = 0
    position2 = 0
    
    positions1 = [position1]
    positions2 = [position2]
    return position1,position2,positions1,positions2
def play_again():
    again = input("Yana o'ynashni xohlaysizmi? (ha/yo'q): ")
    if again.lower() == 'ha' or again.lower() == 'xa':
        run()
    else:
        print("Xayir!")
        
def ready():
    game = input("O'yinni boshlashga tayyormisiz?(ha/yo'q): ")
    if game.lower() == 'ha' or game.lower() == 'xa':
        run()
    else:
        print("Xayir!")
ready()


