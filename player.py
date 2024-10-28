from character import *
from functions import diceRoll

class Player(Character):
    def __init__(self):
        super().__init__()
        # calls back the parent constructor cause *python*
        self.__pots:int = 3
        self.__xp:int = 0
        self.__gold:int = 0
        self.__level:int = 1
# creates player class, adding onto the character class giving it pots, xp, and gold
  
    def potionDrinking(self):
        if self.__pots <= 0:
            print("You don't have any remaining potions, you can buy some more next time you visit a shop")
            return
        self.__pots -= 1
        self.heal(diceRoll(1, 4, 2))
    # function to make drinking potions, heals by 1d4 + 2 and removes 1 potion from player inventory
    
    def killRewards(self):
        self.__xp += diceRoll(4, 10, 5) 
        self.__gold += diceRoll(2, 10, 2)
        self.lvlup()
    # gives the player gold and xp per enemy kill and checks if the player can lvl up
    
    def lvlUp(self):
        if self.__xp >= 100:
            self.__level += 1
            self.__xp -= 100
            self.__atk += 2
            self.__hp += 10
            self.__defense += 1
    # function to calculate lvl up (100 xp per lvl) and gives stats, resets xp back to xp - 100