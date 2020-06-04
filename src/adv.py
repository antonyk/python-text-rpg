from world import gameworld
from player import Player
import textwrap

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

def render_help():
    # clear screen
    print(f"Help menu")

def render_map(size):
    pass

def render_room(player):
    print(player.render_environment())

def render_inventory():
    pass

def render_prompt():
    pass

def main():
    # create world

    prompt = ""
    # get player name and create players
    p_name = input(f"Please enter you character's name:")
    player = Player(p_name, gameworld.spawn_room)

    print(f"Welcome to the Game, adventurer {player}!\n\n")
    input(f"Press any key to continue...")
    render_room(player)

    # main game loop
    while True:

        choice = input(f"Enter an action or movement command, 'h' for help or 'q' to quit)\n> ") # direction to move, 'q' to quit or 'a' to attack")

        if choice == 'h':
            render_help()
            
        elif choice in movement_commands:
            print(player.move(choice))
            #perform a move
            #render the new room
            render_room(player)

        elif choice == 'g':
            #perform get item
            pass

        elif choice == 'a':
            #perform attack
            pass

        elif choice == 'm':
            #draw current map
            pass

        elif choice == 'l':
            render_room(player)

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