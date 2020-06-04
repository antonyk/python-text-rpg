# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room

# sort of like a teleport; transports a player to a specific room  
  def move_to(self, room):
    self.room = room

# move in a particular direction
  def move(self, direction):
    if direction in self.room.exits:
      self.room = self.room.exits[direction]
      return f"You moved {direction} to the {self.room.name}"
    else:
      return f"There is no exit in the {direction} direction!"

  def pickup_item(self, item):
    pass

  def drop_item(self, item):
    pass

  def attack_target(self, target):
    pass

  def render_environment(self):
    # render the world from the player's perspective
    self.room.render_player_perspective(50)

  def render_inventory(self):
    pass


# 