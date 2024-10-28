import random
from player import *
from Main import player1
from Main import enemy

def diceRoll(numberOfDices:int , diceSize:int, modifier:int) -> int:
    roll:int = 0 
    for i in range(0,numberOfDices):
        roll += random.randint(1, diceSize)
    roll += modifier
    return roll
# creates a dice roll function, which calculates the total of the dice roll depending on the number and max value of the dice


def askInput(choice):
    choice:int = 0
    print("Please choose your next action...")
    print("1- Heal yourself using a potion")
    print("2- Attack the enemy")
    print("3- Prepare to block the enemy's next attack")
    choice = input()
    # shows the option the player has
    if choice < 1 and choice > 3:
        print("Please choose a number associated to the action you wish to take.")
    
    match choice:
        case 1:
            player1.potionDrinking()
            print(f"You now have {player1.getHP} and are left with {player1.getPots} potions")
            # if user selects to heal, calls the drinking potion functions and displays the stats
        case 2:
            enemy.hurt(diceRoll(1, 20, player1.__atk))
        case 3:
            player1.getDefense  
            
            