from functions import *
from character import *
import random

def turnChoices(player, opponent):
    choice:int = askInput([" Heal yourself using a potion", " Attack the enemy", " Prepare to block the enemy's next attack"])
    # shows the option the player has
    player.turnStart()
    match choice:
        case 1:
            player.potionDrinking()
            print(f"You now have {player.getHP()} hp and are left with {player.getPots()} potions")
            # if user selects to heal, calls the drinking potion functions and displays the stats
        case 2:
            dmg:int = opponent.hurt(diceRoll(1, 20, player.getAtk()))
            if dmg == 0:
                return
            else:
                print(f"You dealt {dmg} damage to the enemy!")
            # shows the dmg dealt using hurt function
        case 3:
            d:int = player.defend()
            print(f"You managed to increase your defense by {d}")
            # puts the result of the diceroll to add defence for the turn in d, prints the result
   
            
def enemyChoice(opponent, player):
    enemyChoice:int = random.randint(1,2)
    match enemyChoice:
        case 1:
            dmg:int = player.hurt(diceRoll(1, 20, opponent.getAtk()))
            if dmg == 0:
                return
            else:
                print(f"The enemy did {dmg} dmg to you!")
                
        case 2:
            d:int = opponent.defend()
            print(f"The opponent increased it's defense by {d}.")
            