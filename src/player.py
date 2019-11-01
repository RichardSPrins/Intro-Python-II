# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room, inventory=[]):
    self.name = name
    self.current_room = current_room
    self.inventory = inventory

  def move(self, direction):
    # self.current_room = direction
    # print(f"moving to {direction}")
    if getattr(self.current_room, f"{direction}_to"):
      self.current_room = getattr(self.current_room, f"{direction}_to")
    else:
      print('Cannot go this way')

  def pick_up_item(self, item):
    self.inventory.append(item)

  def drop_item(self, item):
    self.inventory.remove(item)

  # def __str__(self):
  #   return f"{self.name} is currently in {self.room}"
  def __repr__(self):
    return f"Player({repr(self.name, self.current_room)})"