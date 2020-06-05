from termcolor import colored

class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room
    self.can_see = True
    self.vision = 5
    self.inventory = []
    # self.actions = {
    #   'g', 
    # }
#    self.body

  def __str__(self):
    return self.name

# sort of like a teleport; transports a player to a specific room  
  def move_to(self, room):
    self.room = room

# move in a particular direction
  def move(self, direction):
    if direction in self.room.exits:
      self.room = self.room.exits[direction]
      return f"You moved {direction.upper()} to the {self.room.name}"
    else:
      return f"There is no exit in the {direction.upper()} direction!"

  def pickup_item(self, item):
    self.inventory.append(item)
    self.room.remove_object(item)

  def drop_item(self, item):
    self.room.add_object(item)
    self.inventory.remove(item)

  def attack_target(self, target):
    pass

  def render_environment(self):
    # render the world from the player's perspective
    output = ""
    # print room name, desc
    output += self.room.render_room()
    # print exits (if can see)
    if self.can_see:
      output += self.room.render_exits()
    else:
      output += f"You are unable to see this room's exits"
    # print objects
    # print chars
    return output

  def print_environment(self):

    pass

  def render_inventory(self):
    output = colored('My Inventory:', 'cyan') + '\n'
    if len(self.inventory) > 0:
      output += '\n'.join([colored(item.name, 'green') for item in self.inventory]) + '\n\n'
    else:
      output += colored("You are not carrying anything!", 'red') + '\n'

    return output

