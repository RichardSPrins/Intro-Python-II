# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
  def __str__(self):
    return f"Room: {self.name}. Details: {self.desc}"
  # def __repr__(self):
  #   return f"Room({repr(self.name)})"

newRoom = Room('first room', 'this is the first room')


print(newRoom)