from functions import diceRoll

class Character:
    def __init__ (self):
        self.__hp:int = 20
        self.__atk:int = 2
        self.__defense:int = 0
        self.__defenseUP:int = 0
    # base class/object for all things living with base values

    def getHP(self):
        return self.__hp
    def getDmg(self):
        return self.__atk
    def getDefense(self):
        return self.__defense
    def getDefenseUP(self):
        return self.__defenseUP
    #creates functions to return values to child
    
    def defend(self):
        defence:int = diceRoll(1, 4, 1)
        self.__defenseUP = defence
        return defence
    # function to set defense when actively blocking during a turn
        
    def turnStart(self):
        self.__defenseUP = 0
    # function to dictate stuff that needs to happen on turn start
    # for now only defense is reset to 0 but might add more later
    
    def heal(self, healAmmount:int):
        self.__hp += healAmmount
    def hurt(self, dmgDealt:int):
        if dmgDealt < self.__defense:
            return
        else:
            self.__hp = self.__hp - dmgDealt + self.__defense + self.__defenseUP
    # functions to calculate healing and damage dealt to characters
