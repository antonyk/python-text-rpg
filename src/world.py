import random
from room import Room
from item import Item


class Creature:
    def __init__(self, name, props, aggro):
        # init properties
        self.name = name
        self.hp = props['hp']
        self.description = props['description']
        self.aggro = aggro

class World:
    # this constructor takes a world definition file
    def __init__(self, rooms, default_room, creatures, use_void=True):
        # init properties
        self.rooms = {}

        # build map
        for r in rooms:
            room = Room(r['uid'], r['name'], r['description'])
            self.rooms[room.uid] = room

        # set up exits and items
        for r in rooms:
            room = self.rooms[r['uid']]

            # add exits
            for e in r['exits']:
                ex = self.rooms.get(e[1], None)
                if ex is not None:
                    room.add_exit(e[0], ex)

            # add items
            for i in r['items']:
                item = Item(i[0], i[2])
                room.add_object(item)

            for n in r['npc']:
                cname = n[0]
                npc = Creature(cname, creatures[cname], n[1])


        self.default_room = self.rooms.get(default_room)
        self.spawn_room = self.default_room

        if use_void and len(self.rooms.keys()) == 0:
            self.__build_void__()

    def __build_void__(self):
        # define Void room
        void_room = {
            'uid': 'void',
            'name': "The Void",
            'description': """This is the Void. If you are here, the world doesn't exist yet""",
            'exits': [
            ],
            'items': [
                ('black hole', 'hole', 'an all-consuming black hole')
            ]
        }

        room = Room(void_room['uid'], void_room['name'],
                    void_room['description'])
        self.rooms[room.uid] = room
        self.default_room = room
        self.spawn_room = self.default_room

    # generate a random world

    def genworld():

        choices = len(content)
        size = 100

        for i in range(1, size):
            rand = random.Random()
            fromCont = rand.choice(content)

            newRoom = Room(fromRoom.name, fromRoom.description)
            exitsCnt = range
            # newRoom.
            # world[str(i)] =

        world = {

        }


# Declare all the rooms

# for i in rooms:
#     print(str(i))

# Link rooms together


# Add items to rooms
# rooms['outside'].add_object(Item('torch', 'a basic torch to light the way'))
# rooms['outside'].add_object(
#     Item('training sword', 'a dull training sword made of wood'))

# rooms['treasure'].add_object(
#     Item('dragon egg', 'a precious dragon egg which may hatch a dragon pet'))


# gameworld.spawn_room = gameworld.rooms['outside']

# print(rooms['foyer'].render_player_perspective())

# generate a random world


# rooms = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),

#     'guardian': Room("Guardian Room", """You come upon a massive creature, clad
#     in plate armor, which seems to be blocking the exit to the north."""),

#     'treehouse': Room("Tree House", """You find yourself in a beautiful tree house. 
#     You can see far away from here."""),

#     'weapons': Room("Weapon Room", """You found your way across the chasm, 
#     and here you are, in a room full of weapons."""),
# }

# content = [
#     (
#         "Outside Cave Entrance",
#         "North of you, the cave mount beckons"
#     ),
#     (
#         "Foyer",
#         """Dim light filters in from the south. Dusty passages run north and east."""
#     ),
#     (
#         "Grand Overlook",
#         """A steep cliff appears before you, falling into the darkness. Ahead to the 
#         north, a light flickers in the distance, but there is no way across the chasm."""
#     ),
#     (
#         "Narrow Passage", 
#         """The narrow passage bends here from west to north. The smell of gold permeates the air."""
#     ),
#     (
#         "Treasure Chamber", 
#         """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied 
#         by earlier adventurers. The only exit is to the south."""
#     ),
#     (
#         "Guardian Room", 
#         """You come upon a massive creature, clad in plate armor, which seems to be blocking the 
#         exit to the north."""
#     ),
#     (
#         "Tree House", 
#         """You find yourself in a beautiful tree house. 
#     You can see far away from here."""
#     ),
#     (
#         "Weapon Room",
#         """You found your way across the chasm, and here you are, in a room full of weapons."""
#     ),
# ]



# rooms['treehouse'].add_exit('e', rooms['overlook'])
# rooms['weapons'].add_exit('s', rooms['overlook'])
# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# rooms['foyer'].add_object(Item('rope','rope to tie things together'))

# rooms['treasure'].add_object(Item('dragon egg', 'a precious dragon egg which may hatch a dragon pet'))
# rooms['treasure'].add_object(Item('wood', 'a couple of planks. what could you do with these?'))

# rooms['treehouse'].add_object(Item('torch', 'a purple torch with a sharp end'))
# rooms['treehouse'].add_object(Item('wood', 'a couple of planks. what could you do with these?'))
# rooms['weapons'].add_object(Item('steel sword', 'a sharp sword made of steel'))
# rooms['weapons'].add_object(Item('bow', 'a powerful bow, but you will need arrows to fire it'))
# rooms['weapons'].add_object(Item('arrow', 'a basic arrow.'))
# rooms['weapons'].add_object(Item('arrow', 'an arrow to go with a bow, but this one is sharper'))
# rooms['weapons'].add_object(Item('arrow', 'an arrow with a tip drenched in poison. this could be useful'))

# rooms['overlook'].add_exit('s', rooms['foyer'])
# rooms['overlook'].add_exit('w', rooms['treehouse'])
# rooms['overlook'].add_exit('n', rooms['weapons'])
