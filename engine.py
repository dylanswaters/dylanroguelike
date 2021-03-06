from core.maps.mapoftiles import *
from core.actors.actor import *
from plugins.apoc.apoc import *
import random
from tkinter import *

inputBuffer = " "

def key(event):
    global inputBuffer
    print("pressed" + str(repr(event.char)))
    inputBuffer = str(repr(event.char))

def main():
    global inputBuffer
    gameLength = 30
    gameHeight = 15
    gameRooms = 1
    gameMap = MapOfTiles(gameLength, gameHeight)
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
        newActor = Actor(randName,randomSex,randName[0],"plugins/apoc/statNames.csv")
        # randomize stats
        newActor.makeAllStatsRandom()
        print(str(newActor.id))
        newActor.printStats()

        newActor.token = str(newActor.id)
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
            randX = random.randint(1,gameMap.maxWidth-1)
            randY = random.randint(1,gameMap.maxHeight-1)
        actorList.append(newActor)
        # gameMap.insertActor(randY, randX, Actor())

    master = Tk()
    # frame = Frame(master, height=1000, width=1000)
    # frame.bind("<Key>", key)
    mapStr = StringVar()
    messagesOut = StringVar()
    messagesOut.set(" ")
    Label(master, font=("Courier",12), textvariable=mapStr, height=gameHeight, width=gameLength, wraplength=0, justify=CENTER).pack(side="left")
    Label(master, font=("Courier",12), height=gameHeight+2, justify=LEFT, width=50, wraplength=gameLength*30, textvariable=messagesOut).pack(expand=True)

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
            print(str(currActor.id) + " can see ")
            for printActor in visibleActors:
                print("    " + str(printActor.id))
            if(len(visibleActors) > 0):
                attackChoice = gameMap.getClosestActor(currActor, visibleActors)
                print(" and chooses " + str(attackChoice.id) + " as their target")

                wepRange = 1
                attackMessage = str(currActor.id) + ":" + str(currActor.name)
                if(currActor.weaponSlot != None):
                    if(currActor.weaponSlot.getStat("itemType") == "meleeWeapon"):
                        attackMessage += " attempts to strike "
                    if(currActor.weaponSlot.getStat("itemType") == "rangedWeapon"):
                        wepRange = int(currActor.weaponSlot.getStat("range"))
                        attackMessage += " fires at "
                else:
                    attackMessage += " attempts to punch "
                attackMessage += str(attackChoice.id) + ":" + str(attackChoice.name)

                if(gameMap.isActorInRangeOfActor(currActor,attackChoice,wepRange) == True):
                    # messagesOut.set(messagesOut.get() + "\n" + str(currActor.id) + ":" + str(currActor.name) + " attempts to punch " + str(attackChoice.id) + ":" + str(attackChoice.name))
                    attackResult = attackActor(currActor, attackChoice)
                    if(attackResult == -1):
                        # messagesOut.set(messagesOut.get() + " but misses!")
                        attackMessage += ", but misses!"
                        messagesOut.set(messagesOut.get() + "\n" + attackMessage)
                    else:
                        attackMessage += ", dealing " + str(attackResult) + " damage"
                        messagesOut.set(messagesOut.get() + "\n" + attackMessage)
                        # messagesOut.set(messagesOut.get() + " dealing " + str(attackResult) + " damage")
                        if(attackChoice.getAttribute("hp") == attackChoice.getAttribute("hp").min()):
                            gameMap.removeActor(attackChoice)
                            actorList.remove(attackChoice)
                            messagesOut.set(messagesOut.get() + "\n" + str(attackChoice) + " has been killed by " + str(currActor))
                else:
                    print(str(currActor.id) + ":" + str(currActor.name) + " attempts to move towards " + str(attackChoice.id) + ":" + str(attackChoice.name) + " in direction " + str(gameMap.getDirectionToActor(currActor, attackChoice)))
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
