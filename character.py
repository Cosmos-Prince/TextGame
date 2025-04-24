from functions import diceRoll

class Character:
    def __init__ (self):
        self._hp:int = 40
        self._atk:int = 2
        self._defense:int = 0
        self._defenseUP:int = 0
        self._baseHP:int = 0
    # base class/object for all things living with base values

    def getHP(self): return self._hp
    def getAtk(self): return self._atk
    def getDmg(self): return self._atk
    def getDefense(self): return self._defense
    def getDefenseUP(self): return self._defenseUP
    #creates functions to return values to child
    
    def setStats(self, HP:int, atk:int, defense:int ,defenseUP:int):
        self._hp = HP
        self._atk = atk
        self._defense = defense
        self._defenseUP = defenseUP
        self._baseHP = HP

    def defend(self):
        defense:int = diceRoll(1, 4, 1)
        self._defenseUP = defense
        return defense
    # function to set defense when actively blocking during a turn
        
    def turnStart(self):
        self._defenseUP = 0
    # function to dictate stuff that needs to happen on turn start
    # for now only defense is reset to 0 but might add more later
    
    def heal(self, healAmmount:int):
        self._hp += healAmmount
        
    def hurt(self, dmgDealt:int):
        trueDmg:int = self._defense + self._defenseUP - dmgDealt
        if trueDmg >=0:
            if trueDmg > 0:
                print(" h o w ")
                # should never exist on god's green earth since dmg = abs() but hey you never know
            else:
                print("No damage was dealt.")
                return 0
                # if the dmg is 0, prints this
        else:
            self._hp += trueDmg
            return abs(trueDmg)
            # shows the dmg dealt using hurt function and calculates the new hp value
    
    # functions to calculate healing and damage dealt to characters
    
    
class Creature(Character):
    def __init__(self, atkChance:int, defChance:int, name:str):
        super().__init__()
        self.__defChance:int = defChance
        self.__atkChance:int = atkChance
        self.__name:str = name
        # start of a creature object, to create variation in ennemies

    def getAtkChance(self): return self.__atkChance
    def getDefChance(self): return self.__defChance
    def getName(self): return self.__name
    def resetHP(self): self._hp = self._baseHP
    
noobCreature:Creature = Creature(1, 2, "your average Joe")
noobCreature.setStats(20, 2, 0, 0)

tankCreature:Creature = Creature(1, 99, "fucking Rammus")
tankCreature.setStats(50, 1, 1, 1)

oneShotCreature:Creature = Creature(1, 1, "kid with a glock")
oneShotCreature.setStats(1, 10, 0, 0)

betterCreature:Creature = Creature(1, 2, "a trained mercenary")
betterCreature.setStats(40, 3, 1, 2)
