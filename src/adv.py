from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items = ['rock']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items = ['cobweb', 'rock' ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items = ['torch',  'sword']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items = ['torch']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items = ['empty chest', "stray gold piece", 'goblet']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('Scott', room['outside'])
# print(newPlayer.current_room)
directions = ['n', 's', 'e', 'w']
options = ['move', 'look', 'quit']
actions = ['get_item', 'drop_item', 'throw_item']
# Write a loop that:
#
while True:
    print(f"\n***{newPlayer.current_room.name}***\n")
    print(f"\n***{newPlayer.current_room.desc}***\n")
    print(f'***Curent inventory: {newPlayer.inventory}***')
    for i in options:
        print(i)
    userInput = input("\nWhat would you like to do?")
    
    if userInput == 'move':
        movement = input('\nWhere would you like to go?')
        if movement in directions:
            newPlayer.move(movement)
    elif userInput == 'look':
        print(f"As you look around you see some items in the room: \n{', '.join(newPlayer.current_room.items)}")
        itemInput = input('\nWhat action would you prefer?')
        if itemInput == 'pick up item':
            item = input('Which item do you want to pick up?')
            newPlayer.pick_up_item(item)
            newPlayer.current_room.items.remove(item)
            print(f'\nCurrent inventory: {newPlayer.inventory}')
        elif itemInput == 'drop item':
            itemToDrop = input("\nWhat would you like to drop?")
            newPlayer.drop_item(item)
            newPlayer.current_room.items.append(item)
    if userInput == 'quit':
        print('quitting game')
        exit()
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
