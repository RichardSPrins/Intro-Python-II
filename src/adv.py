from room import Room
from player import Player
from item import Item, LightSource


# Declare all the rooms and items

items = {
    'rock_1': Item('Rock1', 'a smooth rock just small enough to fit in your pocket'),
    'rock_2': Item('Rock2', 'a smooth rock just small enough to fit in your pocket'),
    'rock_3': Item('Rock3', 'a smooth rock just small enough to fit in your pocket'),
    'rock_4': Item('Rock4', 'a smooth rock just small enough to fit in your pocket'),
    'web_1': Item('Cobweb1', 'A cobweb clings loosely to the walls just above you..'),
    'web_2': Item('Cobweb2', 'A cobweb clings loosely to the walls just above you..'),
    'coin_1': Item('Coin1', 'A single piece of gold that seems to have lost its luster from aging'),
    'coin_2': Item('Coin2', 'A single piece of gold that seems to have lost its luster from aging'),
    'coin_3': Item('Coin3', 'A single piece of gold that seems to have lost its luster from aging'),
    'coin_4': Item('Coin4', 'A single piece of gold that seems to have lost its luster from aging'),
    'coin_5': Item('Coin5', 'A single piece of gold that seems to have lost its luster from aging'),
    'torch_1': Item('Torch', 'A dimly lit torch that helps you find your way in dark places'),
    'torch_2': Item('Torch', 'A dimly lit torch that helps you find your way in dark places'),
    'sword': Item('Sword', 'A heavy Sword that mysteriously hasn\'t gone dull'),
    'chest': Item('Chest', 'A chest that seems to have once held great treasures, but now is dusty and long since been emptied..'),
    'goblet': Item('Chalice', 'A gold chalice left behind by whoever emptied the treasure chamber')
}


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items = [items['rock_1']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items = [items['web_1'], items['rock_2' ]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items = [items['rock_3'], items['torch_1']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items = [items['web_2'], items['torch_2'], items['coin_1']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items = [items['rock_4'], items['coin_2'], items['coin_3'], items['coin_4'], items['coin_5'], items['goblet'], items['chest']]),
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

print(room['outside'].items)
print(room['foyer'].items)
print(room['overlook'].items)
print(room['narrow'].items)
print(room['treasure'].items)


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


# 
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
Player_1 = Player('Scott', room['outside'])

directions = ['n', 's', 'e', 'w']
options = ['move', 'i', 'take', 'drop', 'quit']
# actions = []

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

    
    for i in Player_1.inventory:
        if i.name == 'Torch':
            player_position.is_light == True

    if len(player_position.items) >=1:
        print(f"As you look around, you see: ")
        for i in player_position.items:
            print(i)

    player_input = input('\nWhat would you like to do?\n')

    if len(player_input.split()) > 1:
        split = player_input.split()
        item = split[1]
    else:
        item = player_input
# * Ask user to enter options based off of given choices
    if player_input == 'move':
        print(f"\nOptions: {', '.join(directions)}\n")
# * If the user enters a cardinal direction, attempt to move to the room there.
        movement = input('Which direction would you like to go?\n')
        Player_1.move(movement)
# * Print an error message if the movement isn't allowed.
    elif player_input == 'i' or player_input == 'inventory':
        print(f'Current Inventory: {Player_1.inventory}\n')
    elif player_input == f"take {item}":
        for i in player_position.items:
            if i.name == item:
                i.on_take()
                Player_1.get_item(i)
                print(f'{Player_1.inventory}')
    elif player_input == f"drop {item}":
        for i in Player_1.inventory:
            if i.name == item:
                i.on_drop()
                Player_1.drop_item(i)
    elif player_input == f'inspect {item}':
        for i in player_position.items:
            if i.name == item:
                i.on_inspect()
# * If the user enters "q", quit the game.
    elif player_input == 'quit' or player_input =='q':
        check = input('Are you sure you want to quit?\n')
        if check == 'y' or check == 'yes':
            print("\ngoodbye..\n")
            break
