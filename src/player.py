# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room, inventory=[]):
    self.name = name
    self.current_room = current_room
    self.inventory = inventory

  def __str__(self):
    return f'Player: {self.name}\nRoom: {self.current_room}'

  def move(self, direction):
    if getattr(self.current_room, f'{direction}_to'):
      self.current_room = getattr(self.current_room, f'{direction}_to')
    else:
      print('Cannot go that way!')

  def get_item(self, item):
    self.inventory.append(item)
    self.current_room.items.remove(item)

  def drop_item(self, item):
    print(f'Dropped {item}')
    self.inventory.remove(item)
    self.current_room.items.append(item)