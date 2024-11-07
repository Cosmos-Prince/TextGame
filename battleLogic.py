from functions import *
from character import *

def turnChoices(player, opponent):
    choice:int = askInput([" Heal yourself using a potion", " Attack the enemy", " Prepare to block the enemy's next attack"])
    # shows the option the player has
    player.turnStart()
    match choice:
        case 1:
            player.potionDrinking()
            print(f"You now have {player.getHP} and are left with {player.getPots} potions")
            # if user selects to heal, calls the drinking potion functions and displays the stats
        case 2:
            opponent.hurt(diceRoll(1, 20, player.__atk))
        case 3:
            d:int = player.defend()
            print(f"You managed to increase your defense by {d}")
            
            