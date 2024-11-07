from Main import player1
from functions import *


def turnChoices():
    choice:int = askInput([" Heal yourself using a potion", " Attack the enemy", " Prepare to block the enemy's next attack"])
    # shows the option the player has

    askInput()

    if choice < 1 and choice > 3:
        print("Please choose a number associated to the action you wish to take.")
        return
    match choice:
        case 1:
            player1.potionDrinking()
            print(f"You now have {player1.getHP} and are left with {player1.getPots} potions")
            # if user selects to heal, calls the drinking potion functions and displays the stats
        case 2:
            enemy.hurt(diceRoll(1, 20, player1.__atk))
        case 3:
            player1.getDefense  
            
            