from character import *
from player import *
from functions import *
from battleLogic import *

def Creature(Character):
    def __init__(self):
        super().__init__()
        
        
player1 = Player()
# creates player1 object
player1.getAtk()

enemy = Character()
# creates enemy object

while player1.getHP() > 0 or enemy.getHP() > 0:
    turnChoices(player1, enemy)
    enemyChoice(enemy, player1)

if enemy.getHP() <= 0:
    print("Congradulations, you defeated the enemy!")
    
if player1.getHP() <= 0:
    print("You have been slain.")