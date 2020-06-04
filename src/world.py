from room import Room

# Declare all the rooms

class World:
  def __init__(self, rooms = {}):
    self.rooms = rooms

  
rooms = {
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


# for i in rooms:
#     print(str(i))

# Link rooms together
rooms['outside'].add_exit('n', rooms['foyer'])

rooms['foyer'].add_exit('s', rooms['outside'])
rooms['foyer'].add_exit('n', rooms['overlook'])
rooms['foyer'].add_exit('e', rooms['narrow'])

rooms['overlook'].add_exit('s', rooms['foyer'])

rooms['narrow'].add_exit('w', rooms['foyer'])
rooms['narrow'].add_exit('n', rooms['treasure'])

rooms['treasure'].add_exit('s', rooms['narrow'])

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']


gameworld = World(rooms)
gameworld.spawn_room = gameworld.rooms['outside']

#print(rooms['foyer'].render_player_perspective())