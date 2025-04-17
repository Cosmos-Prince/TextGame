from functions import *
from character import *
from player import *
import random

def turnChoices(player, opponent):
    choice:int = askInput(["Heal yourself using a potion", "Attack the enemy", "Prepare to block the enemy's next attack"])
    # shows the option the player has
    player.turnStart()
    match choice:
        case 1:
            if player.getPots() == 0:
                print("\n" * 3)
                player.potionDrinking()
                print("\n" * 3)
                turnChoices(player, opponent)
            else:    
                player.potionDrinking()
                print(f"You now have {player.getHP()} hp and are left with {player.getPots()} potions")
                # if user selects to heal, calls the drinking potion functions and displays the stats
        case 2:
            dmg:int = opponent.hurt(diceRoll(1, 8, player.getAtk()))
            if dmg == 0:
                return
            else:
                print(f"\nYou dealt {dmg} damage to the enemy!")
            # shows the dmg dealt using hurt function
        case 3:
            d:int = player.defend()
            print(f"\nYou managed to increase your defense by {d}")
            # puts the result of the diceroll to add defence for the turn in d, prints the result
   
            
def enemyChoice(opponent:Creature, player:Player):
    choiceChanceTotal:int = opponent.getAtkChance() + opponent.getDefChance()
    threshold:float = 1/choiceChanceTotal
    enemyChoice:int = random.uniform(0, 1)
    if enemyChoice < threshold:
            dmg:int = player.hurt(diceRoll(1, 8, opponent.getAtk()))
            if dmg == 0:
                return
            else:
                print(f"\nThe enemy did {dmg} dmg to you!")
                
    else:
       d:int = opponent.defend()
       print(f"\nThe opponent increased it's defense by {d}.")
