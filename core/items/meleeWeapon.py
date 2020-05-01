from core.items.item import *

class MeleeWeapon(Item):
    # how much damage the item does
    damageMin = 1
    damageMax = 1
    # which skill the item uses
    weaponSkill = ""
    # melee or ranged
    weaponType = ""
    # melee is 0 range
    range = 0

    def __init__(self, name, weight, damageMin, damageMax, skill, type):
        Item.__init__(self, name, "weapon", weight)
        self.damageMin = damageMin
        self.damageMax = damageMax
        self.weaponSkill = skill
        self.weaponType = type
        self.range = 0

    # def __init__(self, name, weight, damageMin, damageMax, skill):
    #     Item.__init__(self, name, "weapon", weight)
    #     self.damageMin = damageMin
    #     self.damageMax = damageMax
    #     self.weaponSkill = skill
    #     self.weaponType = "melee"

    def getDamageMin(self):
        return self.damageMin

    def setDamageMin(self,damage):
        self.damageMin = damage

    def getDamageMax(self):
        return self.damageMax

    def setDamageMax(self,damage):
        self.damageMax = damage

    def getWeaponSkill(self):
        return self.weaponSkill

    def setWeaponSkill(self,weaponSkill):
        self.weaponSkill = weaponSkill

    def getWeaponType(self):
        return self.weaponType

    def setWeaponType(self, weaponType):
        self.weaponType = weaponType
