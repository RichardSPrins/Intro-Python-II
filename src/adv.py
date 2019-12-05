from room import Room
from player import Player
from item import Item


# Declare all the rooms and items

items = {
    'rock': Item('Rock', 'a smooth rock just small enough to fit in your pocket'),
    'web': Item('Cobweb', 'A cobweb clings loosely to the walls just above you..'),
    'coin_1': Item('Gold Coin', 'A single piece of gold that seems to have lost its luster from aging'),
    'coin_2': Item('Gold Coin', 'A single piece of gold that seems to have lost its luster from aging'),
    'coin_3': Item('Gold Coin', 'A single piece of gold that seems to have lost its luster from aging'),
    'coin_4': Item('Gold Coin', 'A single piece of gold that seems to have lost its luster from aging'),
    'coin_5': Item('Gold Coin', 'A single piece of gold that seems to have lost its luster from aging'),
    'torch': Item('Lit Torch', 'A dimly lit torch that helps you find your way in dark places'),
    'sword': Item('Sword', 'A heavy Sword that mysteriously hasn\'t gone dull'),
    'chest': Item('Empty Chest', 'A chest that seems to have once held great treasures, but now is dusty and long since been emptied..'),
    'goblet': Item('Chalice', 'A gold chalice left behind by whoever emptied the treasure chamber')
}


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items = [items['rock']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items = ['cobweb', 'rock' ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items = [items['rock'], items['torch']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items = [items['web'], items['torch'], items['coin_1']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items = [items['rock'], items['coin_2'], items['coin_3'], items['coin_4'], items['coin_5'], items['goblet'], items['chest']]),
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

# Link items to rooms
# room['outside'].items.append(items['rock'])
# room['foyer'].items.append(items['rock'])
# room['foyer'].items.append(items['web'])
# room['overlook'].items.append(items['rock'])
# room['overlook'].items.append(items['torch'])
# room['narrow'].items.append(items['web'])
# room['narrow'].items.append(items['torch'])
# room['treasure'].items.append(items['rock'])
# room['treasure'].items.append(items['coin'])
# room['treasure'].items.append(items['coin'])
# room['treasure'].items.append(items['coin'])
# room['treasure'].items.append(items['coin'])
# room['treasure'].items.append(items['goblet'])
# room['treasure'].items.append(items['chest'])


# print(room['foyer'].items)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
Player_1 = Player('Scott', room['outside'])

directions = ['n', 's', 'e', 'w']
options = ['move', 'i', 'take', 'drop', 'quit']
actions = []

# Write a loop that:
while True:
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    player_position = Player_1.current_room
# * Prints the current room name
    print(f'\nCurrent Room: {player_position}\n')
# * Prints the current description (the textwrap module might be useful here).
    print(f'{player_position.desc}\n')
# * Waits for user input and decides what to do.
    print(f"Options: {', '.join(options)}\n")

    

    if len(player_position.items) >=1:
        print(f"As you look around, you see: ")
        for i in player_position.items:
            print(i)

    player_input = input('What would you like to do?\n')
    if len(player_input.split()) > 1:
        split = player_input.split()
        item = split[1]
# * Ask user to enter options based off of given choices
    if player_input == 'move':
        print(f"\nOptions: {', '.join(directions)}\n")
# * If the user enters a cardinal direction, attempt to move to the room there.
        movement = input('Which direction would you like to go?\n')
        Player_1.move(movement)
# * Print an error message if the movement isn't allowed.
    elif player_input == 'i' or player_input == 'inventory':
        print(f'Current Inventory: {Player_1.inventory}')
    elif player_input == f"take {item}":
        for i in player_position.items:
            if i.name == item:
                Player_1.get_item(i)           
    elif player_input == f"drop {item}":
        for i in player_position.items:
            if i.name == item:
                Player_1.drop_item(i) 
# * If the user enters "q", quit the game.
    elif player_input == 'quit' or player_input =='q':
        check = input('Are you sure you want to quit?\n')
        if check == 'y' or check == 'yes':
            print("goodbye..\n")
            break
