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
