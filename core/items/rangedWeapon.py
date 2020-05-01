from core.items.meleeWeapon import *

class RangedWeapon(MeleeWeapon):
    ammoCapacity = 0
    ammoType = ""
    ammoConsumption = 0

    def __init__(self, name, weight, damageMin, damageMax, skill, type, range, ammoCapacity, ammoType, ammoConsumption):
        MeleeWeapon.__init__(self, name, weight, damageMin, damageMax, skill, type)
        self.range = range
        self.ammoCapacity = ammoCapacity
        self.ammoType = ammoType
        self.ammoConsumption = ammoConsumption

    # returns number of bullets placed in gun
    def reload(self,numBullets):
        if(self.ammoCapacity == 0):
            return numBullets
        elif(self.currentAmmo < self.ammoCapacity):
            maxAmmo = (self.ammoCapacity - self.currentAmmo)
            if(numBullets < maxAmmo):
                self.currentAmmo += numBullets
                return numBullets
            else:
                self.currentAmmo = self.ammoCapacity
                return maxAmmo

    # returns 1 if fires weapon, 0 otherwise
    def fire(self):
        if(self.ammoCapacity == 0 or self.ammoConsumption > self.currentAmmo):
            return 0
        else:
            self.currentAmmo -= self.ammoConsumption

    def getRange(self):
        return self.range

    def setRange(self,range):
        self.range = range

    def getAmmoType(self):
        return self.ammoType

    def setAmmoType(self,ammoType):
        self.ammoType = ammoType

    def getAmmoCapacity(self):
        return self.ammoCapacity()

    def setAmmoCapacity(self,ammoCapacity):
        self.ammoCapacity = ammoCapacity

    def getAmmoConsumption(self):
        return self.ammoConsumption

    def setAmmoConsumption(self,ammoConsumption):
        self.ammoConsumption = ammoConsumption

    def getCurrentAmmo(self):
        return self.currentAmmo

    def setCurrentAmmo(self,currentAmmo):
        self.currentAmmo = currentAmmo
