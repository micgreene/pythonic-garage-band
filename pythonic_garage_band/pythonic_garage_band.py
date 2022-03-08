class Band:
  _instances = list()

  def __init__(self, name, members):
    self.name = name
    self.members = members
    self._instances.append(self)

  def __str__(self):
    return f'The band {self.name}'

  def __repr__(self):
    return f'Band instance. name={self.name}, members={self.members}'

  def play_solos(self):
    ret_list = []
    for member in self.members:
     ret_list.append(member.play_solo())
    
    return ret_list

  @classmethod
  def to_list(cls):
    return cls._instances


class Musician:
  def __init__(self, name):
    self.name = name    

  def __str__(self):
    return f'The musician, {self.name}'

  def __repr__(self):
    return f'Musician(name: {self.name})'

  def get_instrument(self):
    return self.instrument


class Guitarist(Musician):
  def __init__(self, name, instrument='guitar'):
    self.name = name
    self.instrument = instrument

  def __str__(self):
    return f'My name is {self.name} and I play {self.instrument}'

  def __repr__(self):
    return f'Guitarist instance. Name = {self.name}'

  def play_solo(self):
    return 'face melting guitar solo'


class Bassist(Musician):
  def __init__(self, name, instrument='bass'):
    self.name = name
    self.instrument = instrument

  def __str__(self):
    return f'My name is {self.name} and I play {self.instrument}'

  def __repr__(self):
    return f'Bassist instance. Name = {self.name}'

  def play_solo(self):
    return 'bom bom buh bom'


class Drummer(Musician):
  def __init__(self, name, instrument='drums'):
    self.name = name
    self.instrument = instrument

  def __str__(self):
    return f'My name is {self.name} and I play {self.instrument}'

  def __repr__(self):
    return f'Drummer instance. Name = {self.name}'

  def play_solo(self):
    return 'rattle boom crash'


# guitarist = Guitarist('George', 'guitar')
# bassist = Bassist('Bob', 'bass')
# drummer = Drummer('Charley', 'drums')

# metal = Band('Godsmack', [guitarist, bassist, drummer])
# jazz = Band('WoodWind Jive', ['Daddy Mack', 'Fast Freddy', 'Scatman Cruthrs'])
print(Band.to_list())
Band("The Nobodies", [])
print(len(Band.to_list()))

