from functions import diceRoll

class Character:
    def __init__ (self):
        self.__hp:int = 40
        self.__atk:int = 2
        self.__defense:int = 0
        self.__defenseUP:int = 0
    # base class/object for all things living with base values

    def getHP(self):
        return self.__hp
    def getAtk(self):
        return self.__atk
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
        trueDmg:int = self.__defense + self.__defenseUP - dmgDealt
        if trueDmg >=0:
            if trueDmg > 0:
                print(" h o w ")
                # should never exist on god's green earth since dmg = abs() but hey you never know
            else:
                print("No damage was dealt.")
                return 0
                # if the dmg is 0, prints this
        else:
            self.__hp += trueDmg
            return abs(trueDmg)
            # shows the dmg dealt using hurt function and calculates the new hp value
    
    # functions to calculate healing and damage dealt to characters
    
    
