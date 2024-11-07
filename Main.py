from character import *
from player import *
from functions import *

def Creature(Character):
    def __init__(self):
        super().__init__()
        
        
player1 = Player()
# creates player1 object


enemy = Character()
# creates enemy object

askInput([" Heal yourself using a potion", " Attack the enemy", " Prepare to block the enemy's next attack"])