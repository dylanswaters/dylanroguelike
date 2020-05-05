from core.maps.map import *
from core.maps.room import *
from core.maps.tile import *
import random

class MapOfTiles(Map):
    tiles = []

    def __init__(self, w, h):
        Map.__init__(self,w,h)
        for x in range(0, self.maxWidth):
            newTileList = []
            for y in range(0, self.maxHeight):
                newTile = Tile()
                newTileList.append(newTile)
            self.tiles.append(newTileList)


    def printMap(self):
        mapLine = "\n"
        for y in range(0, self.getHeight()):
            for x in range(0, self.getWidth()):
                if(self.getTile(x,y).getActor() != None):
                    mapLine += self.getTile(x,y).getActor().getToken()
                else:
                    mapLine += self.getTile(x,y).getToken()
            mapLine += "\n"
        return mapLine

    def blockEdges(self):
        for i in range(0, self.maxHeight):
            # print(self.maxWidth-2)
            # print(i)
            print(self.maxWidth-1)
            print(i)
            self.getTile(self.maxWidth-1,i).setToken("#")
            self.getTile(self.maxWidth-1,i).setBlocked(True)
            self.getTile(0,i).setToken("#")
            self.getTile(0,i).setBlocked(True)
        for i in range(0, self.maxWidth):
            self.getTile(i,self.maxHeight-1).setToken("#")
            self.getTile(i,self.maxHeight-1).setBlocked(True)
            self.getTile(i,0).setToken("#")
            self.getTile(i,0).setBlocked(True)


    def makeRooms(self,nr):
        if(nr == 0):
            return
        roomList = []
        # master room
        roomList.append(Room(0,self.maxWidth,0,self.maxHeight,1.0))
        # this splits the room zones up
        for i in range(1, nr):
            largestRoomSize = 0
            largestRoomNum = 0
            for roomNum in range(0, len(roomList)):
                if roomList[roomNum].getSize() > largestRoomSize:
                    largestRoomSize = roomList[roomNum].getSize()
                    largestRoomNum = roomNum
            # split vertically
            # print(roomList[largestRoomNum])
            if((roomList[largestRoomNum].getXMax() - roomList[largestRoomNum].getXMin()) >= (roomList[largestRoomNum].getYMax() - roomList[largestRoomNum].getYMin())):
                # print("dividing X axis")
                roomList[largestRoomNum].setPrevXMax(roomList[largestRoomNum].getXMax())
                roomList[largestRoomNum].setXMax(int((roomList[largestRoomNum].getXMax() - roomList[largestRoomNum].getXMin())/2) + roomList[largestRoomNum].getXMin())
                roomList[largestRoomNum].setSize(roomList[largestRoomNum].getSize() / 2)
                roomList.append(Room(roomList[largestRoomNum].getXMax()+1, roomList[largestRoomNum].getPrevXMax(), roomList[largestRoomNum].getYMin(), roomList[largestRoomNum].getYMax(), roomList[largestRoomNum].getSize()))
            # split horizontally
            else:
                # print("dividing Y axis")
                roomList[largestRoomNum].setPrevYMax(roomList[largestRoomNum].getYMax())
                roomList[largestRoomNum].setYMax(int((roomList[largestRoomNum].getYMax() - roomList[largestRoomNum].getYMin())/2) + roomList[largestRoomNum].getYMin())
                roomList[largestRoomNum].setSize(roomList[largestRoomNum].getSize() / 2)
                roomList.append(Room(roomList[largestRoomNum].getXMin(), roomList[largestRoomNum].getXMax(), roomList[largestRoomNum].getYMax() + 1, roomList[largestRoomNum].getPrevYMax(), roomList[largestRoomNum].getSize()))
        # picks random room sizes and draws walls
        for room in roomList:
            # print(room)
            # print("center of room X:" + str(room.getCenterX()) + "Y:" + str(room.getCenterY()))
            yMinBound = random.randint(room.getYMin(),room.getCenterY())-1
            yMaxBound = random.randint(room.getCenterY()+2,room.getYMax())
            # print("Y room size:" + str(yMinBound) + "-" + str(yMaxBound))
            xMinBound = random.randint(room.getXMin(), room.getCenterX())-1
            xMaxBound = random.randint(room.getCenterX()+2,room.getXMax())
            # print("X room size:" + str(xMinBound) + "-" + str(xMaxBound))
            for i in range(yMinBound, yMaxBound):
                self.tiles[xMaxBound-1][i].setToken("#")
                self.tiles[xMaxBound-1][i].setBlocked(True)
                self.tiles[xMinBound][i].setToken("#")
                self.tiles[xMinBound][i].setBlocked(True)
            for j in range(xMinBound, xMaxBound):
                self.tiles[j][yMaxBound-1].setToken("#")
                self.tiles[j][yMaxBound-1].setBlocked(True)
                self.tiles[j][yMinBound].setToken("#")
                self.tiles[j][yMinBound].setBlocked(True)


    def getTile(self,x,y):
        # for i in range(0, self.getHeight()):
        #     for j in range(0, self.getWidth()):
        #         print(self.tiles[i][j])
        # print(x)
        # print(y)
        return self.tiles[x][y]

    # return 1 if successful insert, 0 otherwise
    def insertActor(self, x, y, newActor):
        if(self.getTile(x,y).getBlocked() == True):
            return 0
        else:
            # print(str(y) + ":" + str(x))
            self.getTile(x,y).setActor(newActor)
            self.getTile(x,y).setBlocked(True)
            return 1

    def removeActor(self, actorToRemove):
        xy = self.getActorLocation(actorToRemove)
        self.getTile(xy[0],xy[1]).setActor(None)
        self.getTile(xy[0],xy[1]).setBlocked(False)

    def getDirectionToActor(self, baseActor, targetActor):
        xyb = self.getActorLocation(baseActor)
        xyt = self.getActorLocation(targetActor)
        # print("base actor " + str(xyb))
        # print("target actor " + str(xyt))
        if(xyb[0] < xyt[0] and xyb[1] > xyt[1]):
            return 1
        if(xyb[0] < xyt[0] and xyb[1] == xyt[1]):
            return 2
        if(xyb[0] < xyt[0] and xyb[1] < xyt[1]):
            return 3
        if(xyb[0] == xyt[0] and xyb[1] > xyt[1]):
            return 4
        if(xyb[0] == xyt[0] and xyb[1] < xyt[1]):
            return 6
        if(xyb[0] > xyt[0] and xyb[1] > xyt[1]):
            return 7
        if(xyb[0] > xyt[0] and xyb[1] == xyt[1]):
            return 8
        if(xyb[0] > xyt[0] and xyb[1] < xyt[1]):
            return 9

    def isActorAdjacentToTile(self, py, px, target):
        retVal = False
        for y in range(py - 1, py + 1):
            for x in range(px-1, px + 1):
                if(x < 0 or x > self.maxWidth - 1 or y < 0 or y > self.maxHeight - 1):
                    pass
                elif(self.getTile(x,y).getActor() != None):
                    if(self.getTile(x,y).getActor().getID() == target.getID()):
                        retVal = True
                        break
        return retVal

    def isActorInRangeOfActor(self, baseActor, targetActor, rangeModifier):
        xyb = self.getActorLocation(baseActor)
        xyt = self.getActorLocation(targetActor)
        yInRange = False
        xInRange = False
        if((xyb[0] >= xyt[0]-rangeModifier) and (xyb[0] <= xyt[0]+rangeModifier)):
            yInRange = True
        if((xyb[1] >= xyt[1]-rangeModifier) and (xyb[1] <= xyt[1]+rangeModifier)):
            xInRange = True
        if(xInRange == True and yInRange == True):
            return True
        else:
            return False

    def isActorAdjacentToActor(self, baseActor, targetActor):
        xyb = self.getActorLocation(baseActor)
        xyt = self.getActorLocation(targetActor)
        yInRange = False
        xInRange = False
        if((xyb[0] >= xyt[0]-1) and (xyb[0] <= xyt[0]+1)):
            yInRange = True
        if((xyb[1] >= xyt[1]-1) and (xyb[1] <= xyt[1]+1)):
            xInRange = True
        if(xInRange == True and yInRange == True):
            return True
        else:
            return False

    # creates xypair with absolute value between two actors
    def getDistanceTo(self, initActor, toActor):
        xy1 = self.getActorLocation(initActor)
        xy2 = self.getActorLocation(toActor)
        yDist = abs(xy2[0] - xy1[0])
        xDist = abs(xy2[1] - xy1[1])
        return [yDist, xDist]

    # needs a rewrite
    def getVisibleActors(self, actorLooking, sightDistance):
        listOfActorsFound = []
        xypair = self.getActorLocation(actorLooking)
        actorx = xypair[0]
        actory = xypair[1]
        for x in range(actorx - sightDistance, actorx + sightDistance):
            for y in range(actory - sightDistance, actory + sightDistance):
                # out of bounds check
                # print(str(x) + "," + str(y))
                if(x < 0 or x > self.maxWidth - 1 or y < 0 or y > self.maxHeight - 1):
                    continue
                # we found a actor in range
                elif(self.getTile(x,y).getActor() != None):
                    foundActor = self.getTile(x,y).getActor()
                    # print(foundActor)
                    # check to make sure it isn't the player
                    if(actorLooking == foundActor):
                        continue
                    # find distance between two actors
                    distPair = self.getDistanceTo(actorLooking, foundActor)

                    # print(distPair)
                    xStepAmount = 0
                    yStepAmount = 0
                    xStepAt = 0
                    yStepAt = 0
                    xStepCounter = 0
                    yStepCounter = 0
                    if(distPair[0] != 0 and distPair[1] != 0):
                        if(distPair[0] > distPair[1]):
                            xStepAt = int(round(distPair[0]/distPair[1] + 0.01))
                        elif(distPair[0] < distPair[1]):
                            yStepAt = int(round(distPair[1]/distPair[0] + 0.01))
                    # print("xStepAt: " + str(xStepAt))
                    # print("yStepAt: " + str(yStepAt))

                    # figure out the stepAmount
                    if(actory < y and actorx < x):
                            yStepAmount += 1
                            xStepAmount += 1
                    elif(actory < y and actorx > x):
                            yStepAmount += 1
                            xStepAmount -= 1
                    elif(actory > y and actorx > x):
                            yStepAmount -= 1
                            xStepAmount -= 1
                    elif(actory > y and actorx < x):
                            yStepAmount -= 1
                            xStepAmount += 1
                    elif(actory == y and actorx > x):
                        xStepAmount -= 1
                    elif(actory == y and actorx < x):
                        xStepAmount += 1
                    elif(actory < y and actorx == x):
                        yStepAmount += 1
                    elif(actory > y and actorx == x):
                        yStepAmount -= 1

                    checky = actory
                    checkx = actorx
                    canSee = True
                    while(1):
                        if(checkx == x and checky == y):
                            break
                        # "close enough" check
                        if((checkx == x+1 and checky == y) or (checkx == x-1 and checky == y) or (checky == y+1 and checkx == x) or (checky == y-1 and checkx == x)):
                            break
                        if(xStepCounter == 0):
                            checkx += xStepAmount
                            xStepCounter = 0
                        if(yStepCounter == 0):
                            checky += yStepAmount
                            yStepCounter = 0
                        xStepCounter += 1
                        yStepCounter += 1
                        if(xStepCounter >= xStepAt):
                            xStepCounter = 0
                        if(yStepCounter >= yStepAt):
                            yStepCounter = 0
                        # self.getTile(checky, checkx).setToken(actorLooking.getToken())
                        if(self.getTile(checkx, checky).getBlocked() == True):
                            if(self.getTile(checkx, checky).getActor() != foundActor):
                                # print(str(checky) + "," + str(checkx) + " is blocked")
                                canSee = False
                                break
                    if(canSee == True):
                        listOfActorsFound.append(self.getTile(x,y).getActor())
        return listOfActorsFound

    def getActorLocation(self, actorToFind):
        for x in range(0, self.maxWidth):
            for y in range(0, self.maxHeight):
                if(self.getTile(x,y).getActor() == actorToFind):
                    return [x,y]
        return -1

    # returns the closest actor in a list compared to a base
    def getClosestActor(self, baseActor, listOfActors):
        closestActor = None
        closestDist = 0
        for checkActor in listOfActors:
            xy = self.getDistanceTo(baseActor, checkActor)
            dist = (((xy[0]**2) + (xy[1]**2))**(1/2))
            if(closestActor == None):
                closestActor = checkActor
                closestDist = dist
            elif(dist < closestDist):
                closestActor = checkActor
                closestDist = dist
        return closestActor

    # return 1 on successful move, 0 on a fail
    def moveActor(self, movingActor, direction):
        # print("moving " + str(movingActor) + " in direction " + str(direction))
        xy = self.getActorLocation(movingActor)
        # print(xy)
        tileOfMovingActor = self.getTile(xy[0],xy[1])
        newX = 0
        newY = 0
        # like keypad (5 is actor loc)
        # 7 8 9
        # 4 5 6
        # 1 2 3
        # down and left
        if(direction == 1):
            newX = xy[0]-1
            newY = xy[1]+1
        # down
        if(direction == 2):
            newX = xy[0]
            newY = xy[1]+1
        # down and right
        if(direction == 3):
            newX = xy[0]+1
            newY = xy[1]+1
        # left
        if(direction == 4):
            newX = xy[0]-1
            newY = xy[1]
        # not moving always results in a sucessful move, and no more work needs to be done
        if(direction == 5):
            return 1
        # right
        if(direction == 6):
            newX = xy[0]+1
            newY = xy[1]
        # up and left
        if(direction == 7):
            newX = xy[0]-1
            newY = xy[1]-1
        # up
        if(direction == 8):
            newX = xy[0]
            newY = xy[1]-1
        # up and right
        if(direction == 9):
            newX = xy[0]+1
            newY = xy[1]-1
        if((newY < self.getHeight() and newY > 0) and (newX < self.getWidth() and newX > 0)):
            # print(str(newX) + "," + str(newY))
            newTile = self.getTile(newX, newY)
            # print(newTile.getBlocked())
            if(newTile.getBlocked() == False):
                newTile.setActor(tileOfMovingActor.getActor())
                newTile.setBlocked(True)
                tileOfMovingActor.setActor(None)
                tileOfMovingActor.setBlocked(False)
                return 1
            else:
                return 0
        else:
            return 0

    def removeAllActors(self):
        for x in range(0, self.maxWidth):
            for y in range(0, self.maxHeight):
                if(self.getTile(x,y).getActor() != None):
                    self.removeActor( self.getTile(x,y).getActor() )
