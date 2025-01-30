from character import *
from functions import diceRoll
import math


class Player(Character):
    def __init__(self):
        super().__init__()
        # calls back the parent constructor cause *python*
        self.__pots:int = 3
        self.__xp:int = 0
        self.__gold:int = 0
        self.__level:int = 1
    # creates player class, adding onto the character class giving it pots, xp, and gold

    
    def getPots(self):
        return self.__pots
    # allows to see the number of potions left in the inventory
    
    def getLvl(self):
        return self.__level
    # getter for player's level

    def getGold(self):
        return self.__gold
    # getter for player's gold

    def changeGold(self, ammount:int, add:bool):
        if add == True:
            self.__gold += ammount
        elif add == False:
            self.__gold -= ammount
        else:
            print("how the fuck...")
        print(f"You now have {self.__gold} gold (beaucoup de bidous ca mon homme)")    
    # changes the gold of the player, depending on if needed to add or
    
    def potionDrinking(self):
        if self.__pots <= 0:
            print("You don't have any remaining potions, you can buy some more next time you visit a shop")
            return
        self.__pots -= 1
        self.heal(diceRoll(1, 6, 2))
    # function to make drinking potions, heals by 1d4 + 2 and removes 1 potion from player inventory
    
    def killRewards(self):
        self.__xp += diceRoll(4, 10, 5) 
        self.changeGold(diceRoll(2, 10, 5), True)
        self.lvlup()
    # gives the player gold and xp per enemy kill and checks if the player can lvl up
    
    def xpToLvlUp(self):
        return round(math.log(self.__lvl, 1.5)*100, None)
    # function to calculate the the xp needed to lvl up

    def lvlUp(self):
        if self.__xp >= self.xpToLvlUp():
            self.__level += 1
            self.__xp -= self.xpToLvlUp()
            self.__atk += 2
            self.__hp += 10
            self.__defense += 1
            print(f"Congrats! You are now level {self.getLvl()} and have increased your stats! ")
        else:
            return
        
    # function to calculate lvl up and gives stats, resets xp back to xp - xp needed to lvl up
    