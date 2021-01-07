from core.maps.mapoftiles import *
from core.actors.actor import *
from plugins.apoc.apoc import *
import random
import time
from tkinter import *

inputBuffer = " "

def key(event):
    global inputBuffer
    print("pressed" + str(repr(event.char)))
    inputBuffer = str(repr(event.char))

def main():
    global inputBuffer
    gameLength = 50
    gameHeight = 25
    gameRooms = 1
    gameMap = MapOfTiles(gameLength, gameHeight)
    print("made map")
    # gameMap.makeRooms(gameRooms)
    gameMap.blockEdges()
    actorList = []

    itemDicts = []
    f = csv.DictReader(open("plugins/apoc/meleeWeapons.csv"))
    for i in f:
        i["itemType"] = "meleeWeapon"
        itemDicts.append(i)
    f = csv.DictReader(open("plugins/apoc/rangedWeapons.csv"))
    for i in f:
        i["itemType"] = "rangedWeapon"
        itemDicts.append(i)
    # for i in itemDicts:
    #     print(i)

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

    for i in range(0,100):
        randomSex = ""
        randomNamesList = []
        if(random.randint(0,1) == 0):
          randomSex = "female"
          randomNamesList = femaleNameList
        else:
          randomSex = "male"
          randomNamesList = maleNameList
        randName = randomNamesList[random.randint(0,len(randomNamesList)-1)]
        newActor = Actor(randName,randomSex,randName[0],"plugins/apoc/statNames.csv")
        # randomize stats
        newActor.makeAllStatsRandom()
        newActor.getAttribute("hp").setsm(5)
        newActor.getAttribute("dodge").setsm(0)
        # print(str(newActor.getID()))
        # newActor.printStats()

        # newActor.setToken(str(newActor.getID()))
        weaponToEquip = Item(itemDicts[random.randint(0,len(itemDicts)-1)])
        # randWepIndex = random.randint(0,len(weaponList)-1)
        # wepLine = weaponList[randWepIndex]
        # if(len(wepLine) == 5):
        #     weaponToEquip = MeleeWeapon(wepLine[0],wepLine[1],wepLine[2],wepLine[3],wepLine[4],"melee")
        # elif(len(wepLine) == 10):
        #     weaponToEquip = RangedWeapon(wepLine[0],wepLine[1],wepLine[2],wepLine[3],wepLine[4],wepLine[5],wepLine[6],wepLine[7],wepLine[8],wepLine[9])
        newActor.equipWeaponByWeapon(weaponToEquip)
        randX = 0
        randY = 0
        while(gameMap.insertActor(randX, randY, newActor) == 0):
            randX = random.randint(1,gameMap.getWidth()-1)
            randY = random.randint(1,gameMap.getHeight()-1)
        actorList.append(newActor)
        # gameMap.insertActor(randY, randX, Actor())

    print("made actors")

    # mapStr.set(gameMap.printMap())
    turnNum = 0
    # while(1):
    while(inputBuffer != "q"):
        # print(len(messagesOut.get()))
        # print(messagesOut.get())
        # messagesOut.set(messagesOut.get() + "\nturn " + str(turnNum))
        # messagesOut.set("\nturn " + str(turnNum))
        # print("\nturn " + str(turnNum) + "\n")
        startTime = time.time()
        print(gameMap.printMap())
        turnNum += 1
        loopCount = 0
        for currActor in actorList:
            loopCount += 1
            # print("\t" + str((loopCount/len(actorList))*100) + "%")
            # print("\t" + str((loopCount/len(actorList))*100) + "% complete (" + str(loopCount) + "/" + str(len(actorList)) + ")")
            # print(str(currActor) + " takes their turn")
            visibleActors = gameMap.getVisibleActors(currActor, 30)
            # print(len(visibleActors))
            # print(str(currActor.getID()) + " can see ")
            # for printActor in visibleActors:
                # print("    " + str(printActor.getID()))
            if(len(visibleActors) > 0):
                attackChoice = gameMap.getClosestActor(currActor, visibleActors)
                # print(" and chooses " + str(attackChoice.getID()) + " as their target")

                wepRange = 1
                # attackMessage = str(currActor.getID()) + ":" + str(currActor.getName())
                if(currActor.getWeapon() != None):
                    # if(currActor.getWeapon().getStat("itemType") == "meleeWeapon"):
                        # attackMessage += " attempts to strike "
                    if(currActor.getWeapon().getStat("itemType") == "rangedWeapon"):
                        wepRange = int(currActor.getWeapon().getStat("range"))
                        # attackMessage += " fires at "
                # else:
                    # attackMessage += " attempts to punch "
                # attackMessage += str(attackChoice.getID()) + ":" + str(attackChoice.getName())

                if(gameMap.isActorInRangeOfActor(currActor,attackChoice,wepRange) == True):
                    # messagesOut.set(messagesOut.get() + "\n" + str(currActor.getID()) + ":" + str(currActor.getName()) + " attempts to punch " + str(attackChoice.getID()) + ":" + str(attackChoice.getName()))
                    attackResult = attackActor(currActor, attackChoice)
                    if(attackResult == -1):
                        pass
                        # messagesOut.set(messagesOut.get() + " but misses!")
                        # attackMessage += ", but misses!"
                        # messagesOut.set(messagesOut.get() + "\n" + attackMessage)
                        # print(currActor.getName() + "(" + str(currActor.getID()) + ") misses " + attackChoice.getName() + "(" + str(attackChoice.getID()) + ")(" + str(attackChoice.getAttribute("hp").getValue()) + "/" + str(attackChoice.getAttribute("hp").softmax()) + ")")
                    else:
                        # print(currActor.getName() + "(" + str(currActor.getID()) + ") hits " + attackChoice.getName() + "(" + str(attackChoice.getID()) + ")")
                        # print("   " + attackChoice.getName() + "(" + str(attackChoice.getID()) + ") took " + str(attackResult) + " damage! (" + str(attackChoice.getAttribute("hp").getValue()) + "/" + str(attackChoice.getAttribute("hp").softmax()) + ")")
                        # attackMessage += ", dealing " + str(attackResult) + " damage"
                        # messagesOut.set(messagesOut.get() + "\n" + attackMessage)
                        # messagesOut.set(messagesOut.get() + " dealing " + str(attackResult) + " damage")
                        # print(attackChoice.getAttribute("hp").getValue())
                        # print(attackChoice.getAttribute("hp").min())
                        if(attackChoice.getAttribute("hp").getValue() == attackChoice.getAttribute("hp").min()):
                            gameMap.removeActor(attackChoice)
                            print(attackChoice.getName() + "(" + str(attackChoice.getID()) + ")" + " has died!")
                            actorList.remove(attackChoice)
                            # messagesOut.set(messagesOut.get() + "\n" + str(attackChoice) + " has been killed by " + str(currActor))
                else:
                    # print(str(currActor.getID()) + ":" + str(currActor.getName()) + " attempts to move towards " + str(attackChoice.getID()) + ":" + str(attackChoice.getName()) + " in direction " + str(gameMap.getDirectionToActor(currActor, attackChoice)))
                    gameMap.moveActor(currActor,gameMap.getDirectionToActor(currActor, attackChoice))
            else:
                randDir = random.randint(1,9)
                # print("actor " + str(currActor) + " wanders in direction " + str(randDir))
                gameMap.moveActor(currActor,randDir)
        # mapStr.set(gameMap.printMap())
        # master.update_idletasks()
        # master.update()
        endTime = time.time()
        print("Took " + str(endTime - startTime) + " seconds to process turn " + str(turnNum))
        # for a in actorList:
        #     print( a.getToken() + " HP: " + str(a.getAttribute("hp")))
        inputBuffer = input()


if __name__ == '__main__':
    main()
