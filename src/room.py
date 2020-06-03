# Implement a class to hold room information. This should have name and
# description attributes.

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

  

class Direction:
  def __init__(self, direction):
    self.direction = direction



directionScheme = {
  'north': ['n', 'north'],
  'east': ['e', 'east'],
  'south': ['s', 'south'],
  'west': ['w', 'west']
}
