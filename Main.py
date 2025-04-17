from character import *
from player import *
from functions import *
from battleLogic import *
from shop import *
        

def battleRound(player:Player, enemy:Creature):
    turnNumber:int = 1
    # initialises turnNumber
    print(f"\n\n------You are now fighting {enemy.getName()}------\n")
    while player1.getHP() > 0 or enemy.getHP() > 0:
        print("\n \n")    
        print("-" * 20, f"Turn {turnNumber}", "-" * 20)
        # header for each turn

        print(f"Your hp: {player1.getHP()} | Enemy's hp: {enemy.getHP()}") 
        # prints both hp bars
        print("\n")

        turnNumber += 1
        # counter to print out which turn we are at


        #----- turn order -----

        turnChoices(player1, enemy)

        # runs player turn
        if enemy.getHP() <= 0:
            print("Congradulations, you defeated the enemy!")
            player1.killRewards()
            break
            #checks if the player's hit killed


        enemyChoice(enemy, player1)
        #runs enemy turn

        if player1.getHP() <= 0:
            print("You have been slain.")
            break
            # checks if the player died after enemy's turn

def randomEvent(player:Player):   
    event:int = random.randint(1, 5)
    match event:
        case 1: shopEntrance(player)
        case 2: battleRound(player, noobCreature)
        case 3: battleRound(player, tankCreature)
        case 4: battleRound(player, oneShotCreature)
        case 5: battleRound(player, betterCreature)
# generates a random event, either going to the shop or fighting one of the 4 ennemy types

player1 = Player()
# creates player1 object


battleRound(player1, noobCreature)
shopEntrance(player1)
battleRound(player1, noobCreature)
battleRound(player1, noobCreature)
shopEntrance(player1)
battleRound(player1, noobCreature)
# early game logic, always ensures same start to be fair and give players a chance 
# to get up and get going
while player1.getHP() > 0:
    randomEvent(player1)
# while player is alive, gives a random event based on previous function
