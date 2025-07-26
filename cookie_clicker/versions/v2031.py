from ..game import Upgrade, Effect

million = 10**6
billion = 10**9
trillion = 10**12

building_names = [
  'Cursor',
  'Grandma',
  'Farm',
  'Mine',
  'Factory',
  'Bank',
  'Temple',
  'Wizard tower',
  'Shipment',
  'Alchemy lab',
]

base_prices = {
  'Cursor':15,
  'Grandma':100,
  'Farm':1100,
  'Mine':12000,
  'Factory':130000,
  'Bank':1.4*million,
  'Temple':20*million,
  'Wizard tower':330*million,
  'Shipment':5.1*billion,
  'Alchemy lab':75*billion,
}

base_rates = {
  'Cursor':0.1,
  'Grandma':1,
  'Farm':8,
  'Mine':47,
  'Factory':260,
  'Bank':1400,
  'Temple':7800,
  'Wizard tower':44000,
  'Shipment':260000,
  'Alchemy lab':1.6*million,
}

# Effects (like, for upgrades, ya' know?)
double = Effect(2, lambda r, game: r * 2)
def grandma_type(n): 
  func = lambda r, game: r * (1 + 0.01 * (game.num_buildings['Grandma']//n))
  return Effect(2, func)
def fingers_type(x):
  func = lambda r, game: r + x * sum(game.num_buildings[name] for name in game.building_names if name != 'Cursor')
  return Effect(1, func)
mouse_type = Effect(1, lambda r, game: r + 0.01 * game.building_only_rate())

# The set of all upgrades. This is what gets passed to game.py.
menu = set()

# Cursor & mouse upgrades.
menu.add(Upgrade('Reinforced index finger', {'Cursor':1}, 100, {'Cursor':double, 'mouse':double}))
menu.add(Upgrade('Carpel tunnel prevention cream', {'Cursor':1}, 500, {'Cursor':double, 'mouse':double}))
menu.add(Upgrade('Ambidextrous', {'Cursor':10}, 10000, {'Cursor':double, 'mouse':double}))

# Mouse only upgrades.
menu.add(Upgrade('Plastic mouse', {}, 50000, {'mouse':mouse_type}))

# Grandma upgrades.
menu.add(Upgrade('Forwards from grandma', {'Grandma':1}, 1000, {'Grandma':double}))
menu.add(Upgrade('Steel-plated rolling pins', {'Grandma':5}, 5000, {'Grandma':double}))
menu.add(Upgrade('Lubricated dentures', {'Grandma':25}, 50000, {'Grandma':double}))
menu.add(Upgrade('Prune juice', {'Grandma':50}, 5*million, {'Grandma':double}))
menu.add(Upgrade('Double-thick glasses', {'Grandma':100}, 500*million, {'Grandma':double}))
menu.add(Upgrade('Aging agents', {'Grandma':150}, 50*billion, {'Grandma':double}))

# Grandma type upgrades.
menu.add(Upgrade('Farmer grandmas', {'Grandma':1, 'Farm':15}, 55000, {'Grandma':double, 'Farm':grandma_type(1)}))
menu.add(Upgrade('Miner grandmas', {'Grandma':1, 'Mine':15}, 600000, {'Grandma':double, 'Mine':grandma_type(2)}))
menu.add(Upgrade('Worker grandmas', {'Grandma':1, 'Factory':15}, 6.5*million, {'Grandma':double, 'Factory':grandma_type(3)}))
menu.add(Upgrade('Banker grandmas', {'Grandma':1, 'Bank':15}, 70*million, {'Grandma':double, 'Bank':grandma_type(4)}))
menu.add(Upgrade('Priestess grandmas', {'Grandma':1, 'Temple':15}, 1*billion, {'Grandma':double, 'Temple':grandma_type(5)}))
menu.add(Upgrade('Witch grandmas', {'Grandma':1, 'Wizard tower':15}, 16.5*billion, {'Grandma':double, 'Wizard tower':grandma_type(6)}))
menu.add(Upgrade('Cosmic grandmas', {'Grandma':1, 'Shipment':15}, 255*billion, {'Grandma':double, 'Shipment':grandma_type(7)}))

# Farm upgrades.
menu.add(Upgrade('Cheap hoes', {'Farm':1}, 11000, {'Farm':double}))
menu.add(Upgrade('Fertilizer', {'Farm':5}, 55000, {'Farm':double}))
menu.add(Upgrade('Cookie trees', {'Farm':25}, 550000, {'Farm':double}))
menu.add(Upgrade('Genetically-modified cookies', {'Farm':50}, 55*million, {'Farm':double}))
menu.add(Upgrade('Gingerbread scarecrows', {'Farm':100}, 5.5*billion, {'Farm':double}))
menu.add(Upgrade('Pulsar sprinklers', {'Farm':150}, 550*billion, {'Farm':double}))

# Mine upgrades.
menu.add(Upgrade('Sugar gas', {'Mine':1}, 120000, {'Mine':double}))
menu.add(Upgrade('Mega drill', {'Mine':5}, 600000, {'Mine':double}))
menu.add(Upgrade('Ultradrill', {'Mine':25}, 6*million, {'Mine':double}))
menu.add(Upgrade('Ultimadrill', {'Mine':50}, 600*million, {'Mine':double}))
menu.add(Upgrade('H-bomb mining', {'Mine':100}, 60*billion, {'Mine':double}))

# Factory upgrades.
menu.add(Upgrade('Sturdier conveyor belts', {'Factory':1}, 1.3*million, {'Factory':double}))
menu.add(Upgrade('Child labor', {'Factory':5}, 6.5*million, {'Factory':double}))
menu.add(Upgrade('Sweatshop', {'Factory':25}, 65*million, {'Factory':double}))
menu.add(Upgrade('Radium reactors', {'Factory':50}, 6.5*billion, {'Factory':double}))
menu.add(Upgrade('Recombobulators', {'Factory':100}, 650*billion, {'Factory':double}))

# Bank upgrades.
menu.add(Upgrade('Taller tellers', {'Bank':1}, 14*million, {'Bank':double}))
menu.add(Upgrade('Scissor-resistant credit cards', {'Bank':5}, 70*million, {'Bank':double}))
menu.add(Upgrade('Acid-proof vaults', {'Bank':25}, 700*million, {'Bank':double}))
menu.add(Upgrade('Chocolate coins', {'Bank':50}, 70*billion, {'Bank':double}))

# Temple upgrades.
menu.add(Upgrade('Golden idols', {'Temple':1}, 200*million, {'Temple':double}))
menu.add(Upgrade('Sacrifices', {'Temple':5}, 1*billion, {'Temple':double}))
menu.add(Upgrade('Delicious blessing', {'Temple':25}, 10*billion, {'Temple':double}))

# Wizard tower upgrades.
menu.add(Upgrade('Pointier hats', {'Wizard tower':1}, 3.3*billion, {'Wizard tower':double}))
menu.add(Upgrade('Beardlier beards', {'Wizard tower':5}, 16.5*billion, {'Wizard tower':double}))
menu.add(Upgrade('Ancient grimoires', {'Wizard tower':25}, 165*billion, {'Wizard tower':double}))

# Shipment upgrades.
menu.add(Upgrade('Vanilla nebulae', {'Shipment':1}, 51*billion, {'Shipment':double}))
menu.add(Upgrade('Wormholes', {'Shipment':5}, 255*billion, {'Shipment':double}))

# Alchemy lab upgrades.
menu.add(Upgrade('Antimony', {'Alchemy lab':1}, 750*billion, {'Alchemy lab':double}))