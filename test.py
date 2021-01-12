from core.maps.mapoftiles import *
from core.actors.actor import *
import random
from tkinter import *

# actor insert and remove function test
def test1():
    gameMap = MapOfTiles(10, 10)
    # print(gameMap.printMap())
    newActor = Actor("test","male","@","text/empty.txt")
    if(gameMap.insertActor(5, 5, newActor) == 0):
        return "test 1 failed: couldn't insert actor"
    newActor2 = Actor("test","male","@","text/empty.txt")
    if(gameMap.insertActor(5, 5, newActor2) == 1):
        return "test 1 failed: allowed insert on tile where another actor already is"
    if(gameMap.getTile(5,5).actorInTile == newActor2):
        return "test 1 failed: incorrect actor in tile"
    gameMap.removeActor(newActor)
    if(gameMap.getTile(5,5).actorInTile == newActor):
        return "test 1 failed: incorrect actor in tile"
    gameMap.removeAllActors()
    del gameMap
    return "test 1 complete"


# visible actor test
def test2():
    gameMap = MapOfTiles(10, 10)
    newActor = Actor("test","male","@","text/empty.txt")
    gameMap.insertActor(5, 5, newActor)
    gameMap.insertActor(5, 8, Actor("test","male","@","text/empty.txt"))
    gameMap.insertActor(5, 2, Actor("test","male","@","text/empty.txt"))
    gameMap.insertActor(8, 5, Actor("test","male","@","text/empty.txt"))
    gameMap.insertActor(2, 5, Actor("test","male","@","text/empty.txt"))
    gameMap.insertActor(8, 2, Actor("test","male","@","text/empty.txt"))
    gameMap.insertActor(2, 8, Actor("test","male","@","text/empty.txt"))
    gameMap.insertActor(2, 2, Actor("test","male","@","text/empty.txt"))
    gameMap.insertActor(8, 8, Actor("test","male","@","text/empty.txt"))
    # print(gameMap.printMap())
    # v = gameMap.getVisibleActors(gameMap.getTile(2,2).actorInTile,10)
    # for i in v:
    #     print(gameMap.getActorLocation(i))
    # print(len(gameMap.getVisibleActors(gameMap.getTile(2,2).actorInTile,5)))
    # print(len(gameMap.getVisibleActors(gameMap.getTile(2,5).actorInTile,5)))
    # print(len(gameMap.getVisibleActors(gameMap.getTile(2,8).actorInTile,5)))
    # print(len(gameMap.getVisibleActors(gameMap.getTile(5,2).actorInTile,5)))
    # print(len(gameMap.getVisibleActors(gameMap.getTile(5,8).actorInTile,5)))
    # print(len(gameMap.getVisibleActors(gameMap.getTile(8,2).actorInTile,5)))
    # print(len(gameMap.getVisibleActors(gameMap.getTile(8,5).actorInTile,5)))
    # print(len(gameMap.getVisibleActors(gameMap.getTile(8,8).actorInTile,5)))
    if(len(gameMap.getVisibleActors(newActor,10)) != 8):
        return "test 2 failed: saw " + str(len(gameMap.getVisibleActors(newActor,10))) + " instead of 8"
    gameMap.removeAllActors()
    del gameMap
    return "test 2 complete"

# actor move test
def test3():
    gameMap = MapOfTiles(5, 5)
    newActor = Actor("test","male","@","text/empty.txt")
    gameMap.insertActor(2, 2, newActor)
    gameMap.moveActor(newActor, 1)
    if(gameMap.getActorLocation(newActor) != [1,3]):
        return "test 3 failed: actor did not move SW correctly"
    gameMap.moveActor(newActor, 9)
    if(gameMap.getActorLocation(newActor) != [2,2]):
        return "test 3 failed: actor did not move NE correctly"
    gameMap.moveActor(newActor, 2)
    if(gameMap.getActorLocation(newActor) != [2,3]):
        return "test 3 failed: actor did not move S correctly"
    gameMap.moveActor(newActor, 8)
    if(gameMap.getActorLocation(newActor) != [2,2]):
        return "test 3 failed: actor did not move N correctly"
    gameMap.moveActor(newActor, 3)
    if(gameMap.getActorLocation(newActor) != [3,3]):
        return "test 3 failed: actor did not move SE correctly"
    gameMap.moveActor(newActor, 7)
    if(gameMap.getActorLocation(newActor) != [2,2]):
        return "test 3 failed: actor did not move NW correctly"
    gameMap.moveActor(newActor, 4)
    if(gameMap.getActorLocation(newActor) != [1,2]):
        return "test 3 failed: actor did not move W correctly"
    gameMap.moveActor(newActor, 6)
    if(gameMap.getActorLocation(newActor) != [2,2]):
        return "test 3 failed: actor did not move E correctly"
    gameMap.removeAllActors()
    del gameMap
    return "test 3 complete"

def test4():
    gameMap = MapOfTiles(5, 5)
    newActor = Actor("test","male","@","text/empty.txt")
    gameMap.insertActor(2, 2, newActor)
    newActor2 = Actor("test","male","@","text/empty.txt")
    gameMap.insertActor(2, 4, newActor2)
    gameMap.getVisibleActors(newActor, 5)


def main():
    print(test1())
    print(test2())
    print(test3())
    # print(test4())

if __name__ == '__main__':
    main()
