# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.exits = {}
    self.characters = {}
    self.objects = {}

  def __str__(self):
    return self.name

  def add_exit(self, direction, room):
    self.exits[direction] = room

  def render_player_perspective(self, width):
    output = '[ ' + self.name + ' ]\n'
    output += textwrap.fill(self.description, width) + '\n\n'
    dirs = ", ".join([key.upper() for key in self.exits])
    if len(self.exits) > 0:
      output += f"You can move in the [ " + dirs + (" ] directions" if len(self.exits) > 1 else " ] direction")
    else:
      output += f"There are no obvious exits in this room"
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


