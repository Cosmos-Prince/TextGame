from character import *
from player import *
from functions import *
from battleLogic import *
from shop import *

def Creature(Character):
    def __init__(self):
        super().__init__()
        # start of a creature object, to create variation in ennemies
        
player1 = Player()
# creates player1 object

enemy = Character()
# creates enemy object
turnNumber:int = 1
# initialises turnNumber
'''
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
  
'''
player1.changeGold(10000,True)
shopEntrance(player1)