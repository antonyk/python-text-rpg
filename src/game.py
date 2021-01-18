import os
import textwrap
from termcolor import colored

from world import World
from player import Player
from content import rooms
from content import creatures
from utils import print_error


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def draw_room(player):
    pass
    # display room name, description
    # display characters in room
    # display objects in room
    # display available exits
    # display available actions?


movement_commands = {
    'n': [],
    'e': [],
    's': [],
    'w': [],
}

commands = {
    'd': {
        'description': 'drop',
        'command': '...'  # lambda
    }  # convert this into a class and have the values be instances of the command class
}


def render_help():
    # clear screen
    print(f"Help menu")


def render_map(size):
    pass


def render_prompt():
    pass


def clear_screen():
    _ = os.system('cls') if os.name == 'nt' else os.system('clear')


def main():
    # create world
    gameworld = World(rooms=rooms, default_room='outside', creatures=creatures)

    prompt = ""
    # get player name and create players
    p_name = input(f"Please enter you character's name: ")
    player = Player(p_name, gameworld.spawn_room)

    print(f"Welcome to the Game, adventurer {player}!\n\n")
    input(f"Press any key to continue...")

    clear_screen()
    print(player.render_environment())
    # main game loop
    while True:
        # direction to move, 'q' to quit or 'a' to attack")
        choice = input(
            f"Enter an action or movement command, 'h' for help or 'q' to quit)\n> ")

        if len(choice) < 1:
            print(colored(f"Please enter a valid input", 'red'))

        elif choice == 'h':
            clear_screen()
            render_help()

        elif choice in movement_commands:
            # perform a move
            result = player.move(choice)
            if result['success']:
                clear_screen()
                print(colored(f"> {result['message']}", 'yellow'))
                # render the new room
                print(player.render_environment())
            else:
                print(colored(result['message'], 'red'))


        elif choice[0] == 'g':
            parts = choice.split(' ', 1)
            found = False
            for item in player.room.objects:
                if item.name == parts[1]:
                    player.pickup_item(item)
                    print(colored(f"Picked up the {parts[1]}", 'yellow'))
                    found = True
                    break
            if not found:
                print(colored(f"No {parts[1]} item found", 'red'))
            # print(player.render_environment())

        elif choice[0] == 'd':
            parts = choice.split(' ', 1)
            found = False
            for item in player.inventory:
                if item.name == parts[1]:
                    player.drop_item(item)
                    print(colored(f"Dropped a {parts[1]}", 'yellow'))
                    found = True
                    break
            if not found:
                print(colored(f"No {parts[1]} item found", 'red'))
            # print(player.render_environment())

        elif choice == 'a':
            # perform 'attack'
            pass

        elif choice == 'm':
            # view current map
            pass

        elif choice == 'l':
            clear_screen()
            # perform a 'look' in the current room
            print(player.render_environment())

        elif choice == 'i':
            print(player.render_inventory())

        elif choice == 'q':
            # exit the game
            print("Thank you for playing!")
            break

        # read prompt
        # perform action
        # redraw and repeat


#action = input(f"Which way do you want to move?")


# actions can be on the room, an object, a player
# actions can be "universal"
# actions


main()
