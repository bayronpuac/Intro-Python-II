from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

player = Player(input('You name: '), room['outside'])

print(f"Hello, {player.name}! You are in {player.player_room}. Come on in!")

# movements = ['n', 'e', 's', 'w']
# leave_game = 'q'
# Write a loop that:
#
 
while True:
    cmd = input("-> ").lower()
    if cmd in ['n', 's', 'e', 'w']:
        player.move(cmd)
    elif cmd == "q":
        print("Goodbye!")
        exit()
    else: 
        print('Sorry, try usimg n, s, e, w')





# while True:
#     player_move = input('~~> ')
#     if player_move == leave_game:
#         print('Goodbye!!!')
#         break
#     if bayron.player_room is room['outside']:
#         if player_move == movements[0]:
#             bayron.player_room = room['foyer']
#             print(f"{room['outside'].n_to.name} \n {room['outside'].n_to.description}")
#         else: 
#             print('sorry, wrong way!')
#     elif bayron.player_room is room['foyer']:
#         if player_move == str(movements[2]):
#             bayron.player_room = room['outside']
#             print(f"{room['foyer'].s_to.name} \n {room['foyer'].s_to.description}")
#         elif player_move == str(movements[0]):
#             bayron.player_room = room['overlook']
#             print(f"{room['foyer'].n_to.name} \n {room['foyer'].n_to.description}")
#         elif player_move == str(movements[1]):
#             bayron.player_room = room['narrow']
#             print(f"{room['foyer'].e_to.name} \n  {room['foyer'].e_to.description}")
#         else:
#             print('Sorry, wrong way!')
#     elif bayron.player_room is room['overlook']:
#         if player_move == str(movements[2]):
#             bayron.player_room = room['foyer']
#             print(f"{room['overlook'].s_to.name} \n  {room['overlook'].s_to.description}")
#         else:
#             print('Sorry, wrong way!')
#     elif bayron.player_room is room['narrow']:
#         if player_move == str(movements[0]):
#             bayron.player_room = room['treasure']
#             print(f"{room['narrow'].n_to.name} \n  {room['narrow'].n_to.description}")
#         elif player_move == str(movements[3]):
#             bayron.player_room = room['foyer']
#             print(f"{room['narrow'].w_to.name} \n  {room['narrow'].w_to.description}")
#         else:
#             print('Sorry, wrong way!')
#     elif bayron.player_room is room['treasure']:
#         if player_move == str(movements[2]):
#             bayron.player_room = room['narrow']
#             print(f"{room['treasure'].s_to.name} \n  {room['treasure'].s_to.description}")
#         else:
#             print('Sorry, wrong way!')


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
