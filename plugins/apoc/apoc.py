from core.items.item import *
from core.actors.actor import *
import random

# functions to support apocalypse version

# returns damage dealt (-1 on a miss)
def attackActor(attacker,target):
    damage = -1
    if(attacker.weaponSlot == None):
        hitChance = (random.randint(90,100) + int(attacker.getAttribute("unarmed").getValue() * 0.75)) - target.getAttribute("dodge").getValue()
    else:
        hitChance = (random.randint(90,100) + int(attacker.getAttribute(attacker.weaponSlot.getStat("skill")).getValue() * 0.75)) - target.getAttribute("dodge").getValue()
        # print(attacker.weaponSlot.getStat("name") + " " + str(hitChance))
    if(hitChance >= 100):
        if(attacker.weaponSlot == None):
            # print("no wep damage calc")
            damage = (int(attacker.getAttribute("strength").getValue()) * int(attacker.getAttribute("unarmed").getValue() / 10))
        elif(attacker.weaponSlot.getStat("itemType") == "meleeWeapon"):
            # print("melee damage calc")
            damage = (int(random.randint(int(attacker.weaponSlot.getStat("damageMin")), int(attacker.weaponSlot.getStat("damageMax"))))) * int(attacker.getAttribute(attacker.weaponSlot.getStat("skill")).getValue() / 10) + int(attacker.getAttribute("strength").getValue())
        elif(attacker.weaponSlot.getStat("itemType") == "rangedWeapon"):
            # print("gun dmg calc")
            damage = (random.randint(int(attacker.weaponSlot.getStat("damageMin")), int(attacker.weaponSlot.getStat("damageMax"))) * int(attacker.getAttribute(attacker.weaponSlot.getStat("skill")).getValue() / 10)) + int(attacker.getAttribute("agility").getValue())
        # target.getAttribute("hp").decrementModifiedScore(damage)
        target.setAttribute("hp", int(target.getAttribute("hp").getValue()) - damage)
        # print("actor " + str(attacker.getID()) + " rolled " + str(hitChance) + " to hit " +str(target.getID()) + " dealing " + str(damage) + " damage")
    return damage

# returns number of bullets fired or 0 if out of ammo
def fire(wep):
    # if the gun is out of ammo return
    if(wep.getStat("ammoCapacity") == 0):
        return 0
    else:
        # if the gun usually fires more than one shot, and there is less ammo remaining
        if(wep.getStat("ammoConsumption") > wep.getStat("currentAmmo")):
            retVal = wep.getStat("currentAmmo")
            wep.setStat("currentAmmo", 0)
            return retVal
        # reduce current ammo by ammo consumption
        else:
            wep.setStat("currentAmmo", wep.getStat("currentAmmo") - wep.getStat("ammoConsumption"))
            return wep.getStat("ammoConsumption")

# returns number of bullets placed in gun
# use this like:
# numAmmo = player.inv.getCountOfItem(player.getWeapon().getStat("ammoType"))
# for i in range(reload(player.getWeapon(), numAmmo)):
#   player.inv.popItemByName(player.getWeapon().getStat("ammoType"))
def reload(self,wep,numAmmo):
    missingAmmo = wep.getStat("ammoCapacity") - wep.getStat("currentAmmo")
    # wep is already full
    if(missingAmmo == 0):
        return 0
    # more ammo missing than passed in
    if(missingAmmo > numAmmo):
        wep.setStat("currentAmmo", wep.getStat("currentAmmo") + numAmmo)
        return numAmmo
    # more ammo passed in than wep has capacity
    else:
        wep.setStat("currentAmmo", wep.getStat("ammoCapacity"))
        return numAmmo - missingAmmo
