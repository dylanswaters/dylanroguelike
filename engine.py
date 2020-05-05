from core.maps.mapoftiles import *
from core.actors.actor import *
from core.items.meleeWeapon import *
from core.items.rangedWeapon import *
import random
from tkinter import *

inputBuffer = " "

# returns damage dealt (-1 on a miss)
def attackActor(attacker,target):
    damage = -1
    if(attacker.weaponSlot == None):
        hitChance = (random.randint(90,100) + int(attacker.getAttribute("unarmed").getModifiedScore() * 0.75)) - target.getAttribute("dodge").getModifiedScore()
    else:
        hitChance = (random.randint(90,100) + int(attacker.getAttribute(attacker.weaponSlot.getWeaponSkill()).getModifiedScore() * 0.75)) - target.getAttribute("dodge").getModifiedScore()
        print(attacker.weaponSlot.getName() + " " + str(hitChance))
    if(hitChance >= 100):
        if(attacker.weaponSlot == None):
            print("no wep damage calc")
            damage = (attacker.getAttribute("strength").getModifiedScore() * int(attacker.getAttribute("unarmed").getModifiedScore() / 10))
        elif(attacker.weaponSlot.getWeaponType() == "melee"):
            print("melee damage calc")
            damage = (random.randint(attacker.weaponSlot.getDamageMin(), attacker.weaponSlot.getDamageMax()) * int(attacker.getAttribute(attacker.weaponSlot.getWeaponSkill()).getModifiedScore() / 10)) + int(attacker.getAttribute("strength").getModifiedScore())
        elif(attacker.weaponSlot.getWeaponType() == "ranged"):
            print("gun dmg calc")
            damage = (random.randint(attacker.weaponSlot.getDamageMin(), attacker.weaponSlot.getDamageMax()) * int(attacker.getAttribute(attacker.weaponSlot.getWeaponSkill()).getModifiedScore() / 10)) + int(attacker.getAttribute("agility").getModifiedScore())
        target.getAttribute("hp").decrementModifiedScore(damage)
        print("actor " + str(attacker.getID()) + " rolled " + str(hitChance) + " to hit " +str(target.getID()) + " dealing " + str(damage) + " damage")
    return damage

def key(event):
    global inputBuffer
    print("pressed" + str(repr(event.char)))
    inputBuffer = str(repr(event.char))

def printMap(mtp):
    mapLine = "\n"
    for i in range(0, mtp.getHeight()):
        for j in range(0, mtp.getWidth()):
            if(mtp.getTile(j,i).getActor() != None):
                mapLine += mtp.getTile(j,i).getActor().getToken()
            else:
                mapLine += mtp.getTile(j,i).getToken()
                # if(mtp.getTile(j,i).getToken() == "x"):
                #     if(mtp.getTile(j,i).getBlocked() == True):
                #         mtp.getTile(j,i).setToken("#")
                #     else:
                #         mtp.getTile(j,i).setToken("-")
        mapLine += "\n"
        # mapLine += str(i)
    return mapLine

def actorCreator(actor):
    pass

def main():
    global inputBuffer
    gameLength = 30
    gameHeight = 15
    gameRooms = 1
    gameMap = MapOfTiles(gameLength, gameHeight)
    gameMap.makeRooms(gameRooms)
    gameMap.blockEdges()
    actorList = []

    weaponList = []
    itemListFile = open("text/meleeWeapons.txt",'r')
    for line in itemListFile:
        if(line.startswith("#")):
            pass
        else:
            newItem = []
            line = line.replace("\n","")
            line = line.split(",")
            newItem.append(str(line[0]))
            newItem.append(int(line[1]))
            newItem.append(int(line[2]))
            newItem.append(int(line[3]))
            newItem.append(str(line[4]))
            weaponList.append(newItem)
    itemListFile.close()

    itemListFile = open("text/rangedWeapons.txt",'r')
    for line in itemListFile:
        if(line.startswith("#")):
            pass
        else:
            newItem = []
            line = line.replace("\n","")
            line = line.split(",")
            newItem.append(str(line[0]))
            newItem.append(int(line[1]))
            newItem.append(int(line[2]))
            newItem.append(int(line[3]))
            newItem.append(str(line[4]))
            newItem.append(str(line[5]))
            newItem.append(int(line[6]))
            newItem.append(int(line[7]))
            newItem.append(str(line[8]))
            newItem.append(int(line[9]))
            weaponList.append(newItem)
    itemListFile.close()

    femaleNameList = []
    femaleNameFile = open("text/femaleNames.txt",'r')
    for line in femaleNameFile:
        line = line.replace("\n","")
        femaleNameList.append(line)
    femaleNameFile.close()

    maleNameList = []
    maleNameFile = open("text/maleNames.txt",'r')
    for line in maleNameFile:
        line = line.replace("\n","")
        maleNameList.append(line)
    maleNameFile.close()

    for i in range(0,10):
        randomSex = ""
        randomNamesList = []
        if(random.randint(0,1) == 0):
          randomSex = "female"
          randomNamesList = femaleNameList
        else:
          randomSex = "male"
          randomNamesList = maleNameList
        randName = randomNamesList[random.randint(0,len(randomNamesList)-1)]
        newActor = Actor(randName,randomSex,randName[0],"text/statNames.txt")
        # randomize stats
        newActor.makeAllStatsRandom()
        print(str(newActor.getID()))
        newActor.printStats()

        newActor.setToken(str(newActor.getID()))
        weaponToEquip = None
        randWepIndex = random.randint(0,len(weaponList)-1)
        wepLine = weaponList[randWepIndex]
        if(len(wepLine) == 5):
            weaponToEquip = MeleeWeapon(wepLine[0],wepLine[1],wepLine[2],wepLine[3],wepLine[4],"melee")
        elif(len(wepLine) == 10):
            weaponToEquip = RangedWeapon(wepLine[0],wepLine[1],wepLine[2],wepLine[3],wepLine[4],wepLine[5],wepLine[6],wepLine[7],wepLine[8],wepLine[9])
        newActor.equipWeaponByWeapon(weaponToEquip)
        randX = 0
        randY = 0
        while(gameMap.insertActor(randX, randY, newActor) == 0):
            randX = random.randint(1,gameMap.getWidth()-1)
            randY = random.randint(1,gameMap.getHeight()-1)
        actorList.append(newActor)
        # gameMap.insertActor(randY, randX, Actor())

    master = Tk()
    # frame = Frame(master, height=1000, width=1000)
    # frame.bind("<Key>", key)
    mapStr = StringVar()
    messagesOut = StringVar()
    messagesOut.set(" ")
    Label(master, font=("Courier",12), textvariable=mapStr, height=gameHeight, width=gameLength, wraplength=0, justify=CENTER).pack(side="left")
    Label(master, font=("Courier",12), height=gameHeight, justify=LEFT, width=50, wraplength=500, textvariable=messagesOut).pack(side="left")

    mapStr.set(gameMap.printMap())
    turnNum = 0
    # while(1):
    while(inputBuffer != "q"):
        # print(len(messagesOut.get()))
        # print(messagesOut.get())
        # messagesOut.set(messagesOut.get() + "\nturn " + str(turnNum))
        messagesOut.set("\nturn " + str(turnNum))
        print("\nturn " + str(turnNum) + "\n")
        turnNum += 1
        for currActor in actorList:
            # print(str(currActor) + " takes their turn")
            visibleActors = gameMap.getVisibleActors(currActor, 30)
            # print(len(visibleActors))
            print(str(currActor.getID()) + " can see ")
            for printActor in visibleActors:
                print("    " + str(printActor.getID()))
            if(len(visibleActors) > 0):
                attackChoice = gameMap.getClosestActor(currActor, visibleActors)
                print(" and chooses " + str(attackChoice.getID()) + " as their target")
                if(currActor.getWeapon() == None):
                    if(gameMap.isActorInRangeOfActor(currActor,attackChoice,1) == True):
                        messagesOut.set(messagesOut.get() + "\n" + str(currActor.getID()) + ":" + str(currActor.getName()) + " attempts to punch " + str(attackChoice.getID()) + ":" + str(attackChoice.getName()))
                        attackResult = attackActor(currActor, attackChoice)
                        if(attackResult == -1):
                            messagesOut.set(messagesOut.get() + " but misses!")
                        else:
                            messagesOut.set(messagesOut.get() + " dealing " + str(attackResult) + " damage")
                            if(attackChoice.getAttribute("hp").getModifiedScore() == attackChoice.getAttribute("hp").getMin()):
                                gameMap.removeActor(attackChoice)
                                actorList.remove(attackChoice)
                                messagesOut.set(messagesOut.get() + "\n" + str(attackChoice) + " has been beaten down by " + str(currActor))
                    else:
                        # print("actor " + str(currActor) + " attempts to move towards " + str(attackChoice) + " in direction " + str(gameMap.getDirectionToActor(currActor, attackChoice)))
                        gameMap.moveActor(currActor,gameMap.getDirectionToActor(currActor, attackChoice))
                elif(currActor.getWeapon().getWeaponType() == "ranged"):
                    if(gameMap.isActorInRangeOfActor(currActor,attackChoice,currActor.getWeapon().getRange()) == True):
                        messagesOut.set(messagesOut.get() + "\n" + str(currActor.getID()) + ":" + str(currActor.getName()) + " fires at " + str(attackChoice.getID()) + ":" + str(attackChoice.getName()) + " with their " + str(currActor.getWeapon().getName()))
                        attackResult = attackActor(currActor, attackChoice)
                        if(attackResult == -1):
                            messagesOut.set(messagesOut.get() + " but misses!")
                        else:
                            messagesOut.set(messagesOut.get() + " dealing " + str(attackResult) + " damage")
                            if(attackChoice.getAttribute("hp").getModifiedScore() == attackChoice.getAttribute("hp").getMin()):
                                gameMap.removeActor(attackChoice)
                                actorList.remove(attackChoice)
                                messagesOut.set(messagesOut.get() + "\n" + str(attackChoice) + " has been shot to pieces by " + str(currActor))
                    else:
                        # print("actor " + str(currActor) + " attempts to move towards " + str(attackChoice) + " in direction " + str(gameMap.getDirectionToActor(currActor, attackChoice)))
                        gameMap.moveActor(currActor,gameMap.getDirectionToActor(currActor, attackChoice))
                elif(currActor.getWeapon().getWeaponType() == "melee"):
                    if(gameMap.isActorInRangeOfActor(currActor,attackChoice,1) == True):
                        messagesOut.set(messagesOut.get() + "\n" + str(currActor.getID()) + ":" + str(currActor.getName()) + " attempts to strike " + str(attackChoice.getID()) + ":" + str(attackChoice.getName()) + " with their " + str(currActor.getWeapon().getName()))
                        attackResult = attackActor(currActor, attackChoice)
                        if(attackResult == -1):
                            messagesOut.set(messagesOut.get() + " but misses!")
                        else:
                            messagesOut.set(messagesOut.get() + " dealing " + str(attackResult) + " damage")
                            if(attackChoice.getAttribute("hp").getModifiedScore() == attackChoice.getAttribute("hp").getMin()):
                                gameMap.removeActor(attackChoice)
                                actorList.remove(attackChoice)
                                messagesOut.set(messagesOut.get() + "\n" + str(attackChoice) + " has been slain by " + str(currActor))
                    else:
                        # print("actor " + str(currActor.getID()) + " moves to " + str(attackChoice) + " in direction " + str(gameMap.getDirectionToActor(currActor, attackChoice)))
                        gameMap.moveActor(currActor,gameMap.getDirectionToActor(currActor, attackChoice))
            else:
                randDir = random.randint(1,9)
                # print("actor " + str(currActor) + " wanders in direction " + str(randDir))
                gameMap.moveActor(currActor,randDir)
        mapStr.set(gameMap.printMap())
        master.update_idletasks()
        master.update()
        inputBuffer = input()


if __name__ == '__main__':
    main()
