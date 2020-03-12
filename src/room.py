# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, desc, n_to=None, s_to=None, e_to=None, w_to=None, items=[], is_light=True):
    self.name = name
    self.desc = desc
    self.n_to = n_to
    self.s_to = s_to
    self.e_to = e_to
    self.w_to = w_to
    self.items = items
    self.is_light = is_light
  
  def __repr__(self):
    return f'Room: {self.name}'

  def light(self):
    for i in self.items:
      if i.name == 'Torch':
        self.is_light = False


  
