class Item:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc

  # def __str__(self):
  #   return f'{self.name}'

  def __repr__(self):
    return f'{self.name}'

  def on_take(self):
    print(f'\nYou have picked up {self.name}\n')

  def on_drop(self):
    print(f'\nYou have dropped {self.name}\n')

  def on_inspect(self):
    print(f'\nYou take a closer look at the {self.name}')
    print(f'\n{self.desc}\n')


class LightSource(Item):
  def __init__(self, name, desc, is_lit=False):
    super().__init__(name, desc)
    self.is_lit = is_lit

  def on_drop(self):
    print(f'\nYou have dropped {self.name}\n')
    print('\nIt\'s not wise to drop your source of light!!\n')