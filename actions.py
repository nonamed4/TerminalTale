from os import system
from typing import List
from classes import player
import random
import time
def list_input(stop : int) -> List[int]:
    """Takes input from user stop times and appends them to list."""
    list = []
    i = 0
    while i < stop:
        try :
            list.append(int(input(f"Enter the #{i+1} number:").strip()))
            i += 1
        except Exception:
            print("Enter numbers only!")
            continue
    return list

def nsame(list1 : List[int], list2 : List[int]) -> int:
    """Returns how many elements of list1 and list2 are same."""
    sum = 0
    for i in range(0, len(list1)):
        if list1[i] == list2[i]:
            sum += 1
    return sum


def attack(attacker : player, target : player) -> None:
    """Attack mechanism of TerminalTale.
    rtype: None"""
    print("Sort and enter these numbers in 5 seconds: (Seperated with enters. Example :1 [Enter] 2 [Enter]3 [Enter] 5 [Enter])")
    time.sleep(3)
    list = []
    for i in range(0, 5):
        list.append(random.randrange(1, 11))
    print(list)
    list.sort()
    start = time.time()
    userInput = list[:]
    stop = time.time()
    damageDealt = int(attacker.damage + (2 * nsame(list, userInput) - 1) * 2/3) + len(list) - 2 * int(stop - start - 1)
    system("clear")        
    print(f"You dealt {damageDealt} damage to the enemy! (max: {int(attacker.damage + (2 * len(list) - 1) * 2/3) + len(list)})")
    target.hp -= damageDealt

def fight(main : player, enemies : List[player]) -> bool:
    while True:
        print(f"{main.name} HP:{main.hp}/{main.maxhp}")
        for i in enemies:
            print(f"{i.name} HP:{i.hp}/{i.maxhp}")
        while True:
            userChoice = input("What to do now? (1: Attack, 2:Act, 3:Item, 4:Mercy)")
            if userChoice not in ["1", "2", "3", "4"]:
                continue
            break
        if userChoice == "1":
            print("Enemies:")
            for i, e in enumerate(enemies):
                print(f"{i+1} for {e.name}")
            while True: 
                enemyToAttack = input("Select an enemy:")
                if enemyToAttack not in [str(i) for i in range(1, len(enemies)+1)]:
                    continue
                break
            attack(main, enemies[int(enemyToAttack)-1])
        for i, e in enumerate(enemies):
            if e.hp <= 0:
                enemies.pop(i)
        if enemies == []:
            print("You Won!")
            return True
    #Enemies turn.
"""
    for i, e in enumerate(enemies):

        if main.hp <= 0:
            print("You lost")
            return False
"""




        




        

