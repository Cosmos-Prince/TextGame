import random    
from player import *
from functions import *

def Creature(Character):
    def __init__(self):
        super().__init__()
        
        
player1 = Player()
# creates player1 object

# print(player1.getHP(), player1.getDmg(), player1.getDefense())
# used to figure out wtf is wrong with my objects

print(diceRoll(1, 10, 0))