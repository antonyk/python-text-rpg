import random
from room import Room
from item import Item


class World:
    # this constructor takes a world definition file
    def __init__(self, rooms, default_room, use_void=True):
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
