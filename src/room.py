import textwrap
from termcolor import colored
from item import Item
from item import Equipment


class Room:
    def __init__(self, uid, name, description):
        self.uid = uid
        self.name = name
        self.description = description
        self.exits = {}
        self.characters = {}
        self.objects = []
        self.visibility = 5

    def __str__(self):
        return self.name

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def render_room(self, width=50):
        output = colored('[ ' + self.name + ' ]', 'white')+'\n'
        output += colored(textwrap.fill(self.description,
                                        width), 'magenta') + '\n\n'
        if len(self.objects) > 0:
            output += colored('You see:', 'cyan') + '\n'
            output += '\n'.join([colored(item.name, 'green')
                                 for item in self.objects]) + '\n\n'
        else:
            output += colored("There is nothing in this room!", 'blue') + '\n'
        return output

        # dirs = ", ".join([key.upper() for key in self.exits])
        # if len(self.exits) > 0:
        #   output += f"You can move in the [ " + dirs + (" ] directions" if len(self.exits) > 1 else " ] direction")
        # else:
        #   output += f"There are no obvious exits in this room"
        # return output

    def render_exits(self, width=50):
        output = ""
        dirs = ", ".join([colored(k.upper(), 'cyan') for k in self.exits])
        if len(self.exits) > 0:
            output += f"You can move in the [ " + dirs + (
                " ] directions" if len(self.exits) > 1 else " ] direction")
        else:
            output += f"There are no obvious exits in this room"

        output = textwrap.fill(output, 70)
        return output


class Direction:
    def __init__(self, direction):
        self.direction = direction


directionScheme = {
    'north': ['n', 'north'],
    'east': ['e', 'east'],
    'south': ['s', 'south'],
    'west': ['w', 'west']
}
