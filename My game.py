import random

class Character:
    def __init__ (self):
        self.__hp:int = 20
        self.__atk:int = 2
        self.__defense:int = 0
# base class/object for all things living with base values

    def getHP(self):
        return self.__hp
    def getDmg(self):
        return self.__atk
    def getDefense(self):
        return self.__defense
    #creates functions to return values to child
    
    def heal(self, healAmmount:int):
        self.__hp += healAmmount
    def hurt(self, dmgDealt:int):
        if dmgDealt < self.__defense:
            return
        else:
            self.__hp = self.__hp - dmgDealt + self.__defense 
    # functions to calculate healing and damage dealt to characters
    
        
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
        self.__pots -= 1
        self.heal(diceRoll(1, 4, 2))
    # function to make drinking potions, heals by 1d4 + 2 and removes 1 potion from player inventory
    
    def killRewards(self):
        self.__xp += diceRoll(4, 10, 5) 
        self.__gold += diceRoll(2, 10, 2)
        self.lvlup()
    # gives the player gold and xp per enemy kill and checks if the player can lvl up
    
    def lvlUp(self):
        if self.__xp // 100:
            self.__level += 1
            self.__xp -= 100
            self.__atk += 2
            self.__hp += 10
            self.__defense += 1
    # function to calculate lvl up (100 xp per lvl) and gives stats, resets xp back to xp - 100

def Creature(Character):
    def __init__(self):
        super().__init__()
        
        
player1 = Player()
# creates player1 object

# print(player1.getHP(), player1.getDmg(), player1.getDefense())
# used to figure out wtf is wrong with my objects

def diceRoll(numberOfDices:int , diceSize:int, modifier:int):
    roll:int = 0 
    for i in range(0,numberOfDices + 1):
        roll += random.randint(1, diceSize)
    roll += modifier
# creates a dice roll function, which calculates the total of the dice roll depending on the number and max value of the dice

