from core.maps.mapoftiles import *
from core.actors.actor import *
from core.items.meleeWeapon import *
from core.items.rangedWeapon import *
import random
from tkinter import *

# move actor test
def test1():
    gameMap = MapOfTiles(10, 10, 0)
    newActor = Actor("test","male","@","text/statNames.txt")
    if(gameMap.insertActor(5, 5, newActor) == 0):
        return "test 1 failed: couldn't insert actor"
    print(newActor.getActorLocation)
    gameMap.moveActor(newActor, 1)



def main():
    results = []
    results.append(test1())

if __name__ == '__main__':
    main()
