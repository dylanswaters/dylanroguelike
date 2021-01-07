from core.actors.inventory import *
from core.actors.attribute import *
import random
import csv

actorID = 0

class Actor:
    id = 0
    name =  ""
    token = ""
    inventory = Inventory()

    # incorporate this into stats
    sex = ""

    stats = []
    # hp = None

    weaponSlot = None
    armorSlot = None

    def __init__(self, name, sex, token, statsFile):
        global actorID
        self.weaponSlot = None
        self.armorSlot = None
        self.inventory = Inventory()
        self.sex = sex
        # self.hp = Attribute("hp",1,1,1)
        self.id = actorID
        self.token = token
        self.name = name
        self.stats = []
        actorID += 1

        statsDicts = csv.DictReader(open(statsFile))

        for s in statsDicts:
            # print(Attribute(s))
            self.stats.append(Attribute(s))

    def __str__(self):
        retStr = "actor has id:" + str(self.id) + ", who is named " + str(self.name) + " and is a " + str(self.sex)
        return retStr

    def printStats(self):
        for stat in self.stats:
            print(stat)
            # print(stat.getName() + str(stat.getValue()))

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def makeAllStatsRandom(self):
        # print(self.name + "(" + str(self.getID()) + ")")
        for stat in self.stats:
            stat.setsm(random.randint(int(stat.min()), int(stat.max())))
            # print(stat)

    def setName(self,newName):
        self.name = newName

    def setToken(self,newToken):
        self.token = newToken

    def getToken(self):
        return self.token

    def getWeapon(self):
        return self.weaponSlot

    def equipWeaponByInvIndex(self,index):
        weaponToEquip = inventory.popItemByIndex(index)
        if(self.weaponSlot == None):
            self.weaponSlot = weaponToEquip
        else:
            self.inventory.addItem(self.weaponSlot)
            self.weaponSlot = weaponToEquip

    def equipWeaponByWeapon(self,weaponToEquip):
        if(self.weaponSlot == None):
            self.weaponSlot = weaponToEquip
        else:
            self.inventory.unequipWeapon()
            self.weaponSlot = weaponToEquip

    def unequipWeapon(self):
        if(self.weaponSlot == None):
            return 0
        else:
            self.inventory.addItem(self.weaponSlot)
            self.weaponSlot = None
            return 1

    def getarmor(self):
        return self.armorSlot

    def equipArmorByInvIndex(self,index):
        armorToEquip = inventory.popItemByIndex(index)
        if(self.armorSlot == None):
            self.armorSlot = armorToEquip
        else:
            self.inventory.addItem(self.weaponSlot)
            self.weaponSlot = weaponToEquip

    def equipArmorByArmor(self,armorToEquip):
        if(self.armorSlot == None):
            self.armorSlot = armorToEquip
        else:
            self.inventory.addItem(self.armorSlot)
            self.armorSlot = armorToEquip

    def unequipArmor(self):
        if(self.armorSlot == None):
            return 0
        else:
            self.inventory.addItem(self.armorSlot)
            return 1

    def getAttribute(self,attrName):
        # print("looking for " + attrName)
        # print(type(attrName))
        # print(len(self.stats))
        for stat in self.stats:
            # print(stat)
            if(stat.getName() == attrName):
                return stat
        else:
            return None

    def setAttribute(self, attrName, value):
        # self.stats[attrName].setStat(value)
        for stat in self.stats:
            # print(stat)
            if(stat.getName() == attrName):
                stat.setStat(value)
                return 1
        return 0
