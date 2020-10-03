import sys

inventory = []
case = []
rooms = {
        1: {"name": "West of House",
            "east": 2,
            "south": 21,
            "west": 2,
            "item": "leaflet"},
        2: {"name": "Behind House", #enter house (kitchen)
            "east": 1,
            "west": 24},
        3: {"name": "Kitchen", #climb down to studio
            "south": 6,
            "north": 9,
            "east": 4,
            "item": "sack",
            "item": "bottle"},
        4: {"name": "Living Room", #climb down to cellar
            "east": 3,
            "item": "lantern:",
            "item": "sword"},
        5: {"name": "Cellar",
            "south": 10,
            "north": 7},
        6: {"name": "Attic",
            "north": 3,
            "item": "knife",
            "item": "rope"},
        7: {"name": "East of Chasm",
            "south": 5,
            "west": 8},
        8: {"name": "Gallery",
            "east": 7,
            "south": 9,
            "item": "painting"},
        9: {"name": "Studio",
            "north": 8,
            "south": 3},
        10: {"name": "Troll Room",
             "north": 5
             },
        11: {"name": "East-West Passge",
             "east": 10,
             "west": 12},
        12: {"name": "Round Room",
             "east": 11,
             "north": 13},
        13: {"name": "Engravings Cave",
             "west": 14},
        14: {"name": "Dome Room",
             "east": 13,
             "north": 15},
        15: {"name": "Torch Room",
             "south": 14,
             "north": 16},
        16: {"name": "Temple",
             "west": 17,
             "north": 18},
        17: {"name": "Egyptian Room",
             "east": 16,
             "item": "coffin:"},
        18: {"name": "Altar", #connects to forest(west)
             "south": 16},
        19: {"name": "Forest(west)",
             "south": 20,
             "west": 1},
        20: {"name": "Clearing(west)",
             "north": 19,
             "west": 21},
        21: {"name": "Clearing(north)",
             "east": 20,
             "north": 1,
             "west": 22},
        22: {"name": "Forest(north)",
             "east": 21,
             "west": 23},
        23: {"name": "Forest(east)",
             "east": 22,
             "north": 24},
        24: {"name": "Clearing(east)",
             "south": 23,
             "east": 2,
             "west": 25},
        25: {"name": "Canyon View", #climb down to 26
             "east": 24},
        26: {"name": "Rocky Ledge"}, #climb down to 27 | climb up to 25
        27: {"name": "Canyon Bottom", #
             "west": 28}, #climb down to 28 | climb up to 26
        28: {"name": "End of Rainbow",
             "east": 27,
             "item": "sceptre",
             "item": "gold"}

}

def zork_license():
    print("ZORK I: The Great Underground Empire")
    print("Copyright (c) 1981, 1982, 1983 Infocom, Inc.")
    print("ZORK is a registered trademark of Infocom, Inc.")
    print("Revision 88/ Serial number 840726")
"""
def add_to_inventory():
    inventory.append()
    # add_to_inventory("item")

def remove_from_inventory():
    inventory.remove()
    # remove_from_inventory("item")
"""
def display_inventory():
    print("Items you currently hold:", "\n")
    for items in inventory:
        print(items)

def starting_room():
    global inventory
    currentRoom = 1
    print("West of House", "\n")
    print("You are standing in an open field west of a white house, with a boarded front door.")
    print("There is a small mailbox here.")
    while True:
        #splits "go" and direction or "get" and item
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "take":
            if "item" in rooms[currentRoom] and cmd[1] in rooms[currentRoom]["item"]:
                inventory += [cmd[1]]
                del rooms[currentRoom]["item"]
            else:
                print("Can't get" +cmd[1] + "!")
        if cmd == "open mailbox":
            print("Opening the small mailbox reveals a leaflet.")
            if cmd == "read leaflet":
                print('"WELCOME TO ZORK!"', "\n")
                print("ZORK is a game of adventure, danger, and low cunning.")
                print("In it you will explore some of the most amazing territory ever seen by mortals.")
                print("No computer should be without one!")
                print("Your goal is to bring back a coffin, a sceptre, a painting, and gold to the case in the white house.")
            if cmd == "drop leaflet":
                if "item" in [inventory]:
                    inventory.remove("leaflet")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def behind_room():
    global inventory
    currentRoom = 2
    print("Behind House","\n")
    print("You are behind the white house. A path leads into the forest to the east.")
    print("In one corner of the house there is a small window which is slightly ajar.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd == "open window":
            print("With great effort, you open the window far enough to allow entry.")
            if cmd == "enter house":
                currentRoom = 3
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Kitchen():
    global inventory
    currentRoom = 3
    print("Kitchen","\n")
    print("You are in the kitched of the white house. A table seems to have been used recently for the preparation of food.")
    print("A passage leads to the west and a dark staircase can be seen leading upward.")
    print("A dark chimney leads down and to the east is a small window which is open.")
    print("On the table is an elongated brown sack, smelling of hot peppers.:")
    print("A bottle is sitting on the table.")
    print("The glass bottle contains:")
    print("","A quantity of water")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "take":
            if "item" in rooms[currentRoom] and cmd[1] in rooms[currentRoom]["item"]:
                inventory += [cmd[1]]
                del rooms[currentRoom]["item"]
            else:
                print("Can't get" +cmd[1] + "!")
        if cmd == "take sack":
            inventory.append("sack")
            print("Added to inventory.")
        if cmd == "take bottle":
            inventory.append("bottle")
        if cmd == "drop sack":
            inventory.remove("sack")
            print("Removed from inventory")
        if cmd == "drop bottle":
            inventory.remove("bottle")
            print("Removed from inventory")
        if cmd == "go up":
            currentRoom = 6
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
    else:
        print("I beg your pardon?")

def Living_Room():
    global inventory
    global case
    currentRoom = 4
    print("Living Room","\n")
    print("You are in the living room. There is a door way to the east, a wooden door with strange gothic lettering to the west,")
    print("which appears to be nailed shut, a trophy case, and a large oriental rug in the center of the room.")
    print("Above the trophy case hangs an elvish sword of great antiquity.")
    print("A battery-powered brass lantern is on the trophy case.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "take":
            if "item" in rooms[currentRoom] and cmd[1] in rooms[currentRoom]["item"]:
                inventory += [cmd[1]]
                del rooms[currentRoom]["item"]
            else:
                print("Can't get" +cmd[1] + "!")
        if cmd == "take lantern":
            inventory.append("lantern")
            print("Added to inventory")
        if cmd == "take sword":
            inventory.append("sword")
            print("Added to inventory")
        if cmd == "drop lantern":
            inventory.remove("lantern")
            print("Removed from inventory")
        if cmd == "drop sword":
            inventory.remove("sword")
            print("Removed from inventory")
        if cmd == "open case":
            print("Opened.")
            if cmd[0] == "put":
                if "item" in inventory:
                    del inventory["item"]
                    case += [cmd[1]]
                else:
                    print("Can't put" + cmd[1] + "in case!")
        if cmd == "move rug":
            print("With a great effort, the rug is moved to one side of the room, revealing the dusty cover of a closed trap door.")
            if cmd == "open trap door":
                print("The door reluctantly opens to reveal a rickety staircase descending into darkness.")
                if cmd == "turn on lamp":
                    print("The brass lantern is now on")
                    if cmd == "go down":
                        if "lantern" in inventory:
                            print("The trap door crashes shut, and you hear someone barring it.")
                        currentRoom = 5
                    else:
                        print("It is too dark to see.")
                        currentRoom =4
        if cmd[0] == "put":
            if "item" in inventory:
                del inventory["item"]
                case +=1 [cmd[1]]
                if "coffin" and "gold" and "painting" and "sceptre" in case:
                    print("Thank you for bringing all the items! You've won the game!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Cellar():
    global inventory
    currentRoom = 5
    print("Cellar","\n")
    print("You are in a dark and damp cellar with a narrow passageway leading north, and a crawl way to the south.")
    print("On the west is the bottom of a steep metal ramp which is unclimbable.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd == "climb up":
            currentRoom = 3
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Attic():
    global inventory
    currentRoom = 6
    print("Attic","\n")
    print("This is the attic. The only exit is a stairway leading down.")
    print("A large coil of rope is lying in the corner.")
    print("On a table is a nasty looking knife.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "take":
            if "item" in rooms[currentRoom] and cmd[1] in rooms[currentRoom]["item"]:
                inventory += [cmd[1]]
                del rooms[currentRoom]["item"]
            else:
                print("Can't get" +cmd[1] + "!")
        if cmd == "take knife":
            inventory.append("knife")
            print("Added to inventory.")
        if cmd == "take rope":
            inventory.append("rope")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def East_of_Chasm():
    global inventory
    global case
    currentRoom = 7
    print("East of Chasm","\n")
    print("You are on the east edge of a chasm, the bottom of which cannot be seen.")
    print("A narrow passage goes north, and the path you are on continues to the east.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Gallery():
    global inventory
    global case
    currentRoom = 8
    print("Gallery","\n")
    print("This is an art gallery. Most of the paintings have been stolen by vandals with exceptional taste.")
    print("The vandals left through either the north or west exits.")
    print("Fortunately, there is still one chance for you to be a vandal, for on the far wall is a paiting of unparalleled beauty.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "take":
            if "item" in rooms[currentRoom] and cmd[1] in rooms[currentRoom]["item"]:
                inventory += [cmd[1]]
                del rooms[currentRoom]["item"]
            else:
                print("Can't get" +cmd[1] + "!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")


def Studio():
    global inventory
    global case
    currentRoom = 9
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Troll_Room():
    global inventory
    global case
    currentRoom = 10
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if "sword" in inventory:
            if cmd == "kill troll":
                ask = input("With what item?")
                if ask == "sword":
                    print("You are still recovering from that last blow, so your attack is ineffective.")
                    if cmd == "kill troll":
                        ask = input("With what item?")
                        if ask == "sword":
                            print("Clang! Crash! The troll parries.")
                            print("The troll's axe barely misses your ear.")
                            if cmd == "kill troll":
                                ask = input("With what item?")
                                if ask == "sword":
                                    print("The troll is confused and can't fight back.")
                                    print("The troll slowly regains his feet.")
                                    if cmd == "kill troll":
                                        ask = input("With what item?")
                                        if ask == "sword":
                                            print("The troll is knocked out!")
                                            if cmd == "kill troll":
                                                ask = input("With what item?")
                                                if ask == "sword":
                                                    print("The unarmed troll cannot defend himself: He dies.")
                                                    print("Almost as soon as the troll breathes his last breath, a cloud of sinister black fog envelops him and when the fog")
                                                    print("lifts, the carcass has disappeared.")
                                                    print("Your sword is no longer glowing.")
        if cmd == "kill troll":
            ask = input("With what item?")
            if ask != "sword":
                print("You are still recovering from that last blow, so your attack is ineffective.")
                print("The troll's axe barely misses your ear.")
                if cmd == "kill troll":
                    ask = input("With what item?")
                    if ask != "sword":
                        print("The troll slashes through your weapon and kills you!")
                        sys.exit()
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def East_West_Passage():
    global inventory
    global case
    currentRoom = 11
    print("East-West Passage", "\n")
    print("This is a narrow east-west passageway. There is a narrow stairway leading down at the north end of the room.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Round_Room():
    global inventory
    global case
    currentRoom = 12
    print("Round Room","\n")
    print("This is a circular stone room with passages in all directions. Several of them have unfortunately been blocked by cave-ins.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Engravings_Cave():
    global inventory
    global case
    currentRoom = 13
    print("Engravings Cave","\n")
    print("You have entered a low cave with passages leading northwest and east.")
    print("There are old engravings on the walls here.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Dome_Room():
    global inventory
    global case
    currentRoom = 14
    print("Dome Room","\n")
    print("You are at the periphery of a large dorm, which forms the ceiling of another room below.")
    print("Protecting you from a precipitous drop is a wooden railing which circles the dome.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if "rope" in inventory:
            if cmd == "tie rope to railing":
                print("The rope drops over the side and comes within ten feet of the floor.")
                if cmd == "go down":
                    currentRoom = 15
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Torch_Room():
    global inventory
    global case
    currentRoom = 15
    print("Torch Room","\n")
    print("This is a large room with a prominent doorway leading to a down staircase.")
    print("Above you is a large dome. Up around the edge of the dome (20 feet up) is a wooden railing.")
    print("In the center of the room sits a white marble pedestal.")
    print("A piece of rope descend from the railing above, ending some five feet above your head.")
    print("Sitting on the pedestal is a flaming torch, made of ivory.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Temple():
    global inventory
    global case
    currentRoom = 16
    print("This is the north end of a large temple. On the east wall is an ancient inscription, probably a prayer in a long-forgotten language.")
    print("Below the prayer is a staircase leading down. The west wall is solid granite.")
    print("The exit to the north end of the room is through huge marble pillars.")
    print("There is a brass bell here.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Egyptian_Room():
    global inventory
    global case
    currentRoom = 17
    print("Egyptian Room","\n")
    print("This is a room which looks like an Egyptian tomb. There is an ascending staircase to the west.")
    print("The solid-gold coffin used for the burial of Ramses II is here.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "take":
            if "item" in rooms[currentRoom] and cmd[1] in rooms[currentRoom]["item"]:
                inventory += [cmd[1]]
                del rooms[currentRoom]["item"]
            else:
                print("Can't get" + cmd[1] + "!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()

        else:
            print("I beg your pardon?")

def Altar():
    global inventory
    global case
    currentRoom = 18
    print("Altar","\n")
    print("This is the south end of a large temple. In front of you is what appears to be an altar.")
    print("In one corner is a small hole in the floor which leads into darkness. You probably could not get back up it")
    print("On the two ends of the altar are burning candles.")
    print("On the altar is a large black book, open to page 569.")
    print("Maybe you should pray to it...")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "pray":
            currentRoom =  19
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Forest_west():
    global inventory
    global case
    currentRoom = 19
    print("Forest(west)","\n")
    print("This is a dimly lit forest, with large trees all around.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Clearing_west():
    global inventory
    global case
    currentRoom = 20
    print("Clearing(west)","\n")
    print("You are in a small clearing in a well marked forest path.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Clearing_north():
    global inventory
    global case
    currentRoom = 21
    print("You are at the end of the extended forest path.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Forest_north():
    global inventory
    global case
    currentRoom = 22
    print("Forest(north)")
    print("The forest is brightly lit and shows a clear path east towards the end of the forest.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Forest_east():
    global inventory
    global case
    currentRoom = 23
    print("Forest(east)")
    print("The end of the forest shows a small clearing to the south.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Clearing_east():
    global inventory
    global case
    currentRoom = 24
    print("Clearing(east)")
    print("The clearing  has a clear view of the white house just west as well as what seems to be a fantastical canyon view just off the horizon.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Canyon_View():
    global inventory
    global case
    currentRoom = 25
    print("Canyon View", "\n")
    print("You are at the top of the Great Canyon on its west wall.")
    print("To the west and south can be seen an immense forest, stretching for miles around. A path leads north.")
    print("It is possible to climb down into the canyon from here.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd == "climb down":
            currentRoom = 26
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Rocky_Ledge():
    global inventory
    global case
    currentRoom = 26
    print("Rocky Ledge","\n")
    print("You are on a ledge about halfway up the wall of the river canyon.")
    print("Blow you is the canyon bottom. Above you is more cliff, which appears climbable.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "climb":
            if cmd[1] == "up":
                currentRoom = 25
            elif cmd[1] == "down":
                currentRoom = 27
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def Canyon_Bottom():
    global inventory
    global case
    currentRoom = 27
    print("Canyon Bottom","\n")
    print("You are beneath the walls of the river canyon which may be climbable here.")
    print("To the north is a narrow path.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def End_of_Rainbow():
    global inventory
    global case
    currentRoom = 28
    print("End of Rainbow","\n")
    print("You are on a small, rocky beach. The beach is narrow. The river canyon opens here and sunlight shines from above.")
    print("A rainbow crosses over the falls.")
    while True:
        cmd = input(">").lower().split()
        if cmd[0] == "go":
            if cmd[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][cmd[1]]
            else:
                print("You can't go that way!")
        if cmd == "drop coffin":
            if "item" in [inventory]:
                inventory.remove("coffin")
            print("Dropped")
            if cmd == "open coffin":
                print("The gold coffin opens.")
                print("A sceptre, possible that of ancient Egypt itself is in the coffin.")
                print("The sceptre is ornamented with colored enamel and tapers to a sharp point")
        if cmd[0] == "take":
            if "item" in rooms[currentRoom] and cmd[1] in rooms[currentRoom]["item"]:
                inventory += [cmd[1]]
                del rooms[currentRoom]["item"]
            else:
                print("Can't get" + cmd[1] + "!")
            if cmd == "wave sceptre":
                print("Suddenly, the rainbow appears to become solid and, I venture, walkable (I think the giveaway was the stairs and bannister.")
                print("A shimmering pot of gold appears at the end of the rainbow.")
        if cmd[0] == "show":
            if cmd[1] == "inventory":
                display_inventory()
        else:
            print("I beg your pardon?")

def main():
    currentRoom = 1
    zork_license()
    starting_room()
    behind_room()
    Kitchen()
    Living_Room()
    Cellar()
    Attic()
    East_of_Chasm()
    Gallery()
    Studio()
    Troll_Room()
    East_West_Passage()
    Round_Room()
    Engravings_Cave()
    Dome_Room()
    Torch_Room()
    Temple()
    Egyptian_Room()
    Altar()
    Forest_west()
    Clearing_west()
    Forest_north()
    Forest_east()
    Clearing_east()
    Canyon_View()
    Rocky_Ledge()
    Canyon_Bottom()
    End_of_Rainbow()

if __name__ == "__main__":
    main()































