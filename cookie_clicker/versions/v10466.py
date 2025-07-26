from ..game import Upgrade, Effect

million = 10**6
billion = 10**9
trillion = 10**12

building_names = [
  'Cursor',
  'Grandma',
  'Farm',
  'Factory',
  'Mine',
  'Shipment',
  'Alchemy lab',
  'Portal',
]

base_prices = {
  'Cursor':15,
  'Grandma':100,
  'Farm':500,
  'Factory':3000,
  'Mine':10000,
  'Shipment':40000,
  'Alchemy lab':200000,
  'Portal':1.667*million,
}

base_rates = {
  'Cursor':0.1,
  'Grandma':0.5,
  'Farm':4,
  'Factory':10,
  'Mine':40,
  'Shipment':100,
  'Alchemy lab':400,
  'Portal':6666,
}

# Effects (like, for upgrades, ya' know?)
def gain(x): return Effect(3, lambda r, game: r + x)
def mult(x): return Effect(1, lambda r, game: r * x)
double = Effect(2, lambda r, game: r * 2)
mouse_type = Effect(1, lambda r, game: r + 0.01 * game.building_only_rate())
def fingers_type(x):
  func = lambda r, game: r + x * sum(game.num_buildings[name] for name in game.building_names if name != 'Cursor')
  return Effect(1, func)

# The set of all upgrades. This is what gets passed to game.py.
menu = set()

# Kitten upgrades.
menu.add(Upgrade('Kitten helpers', {}, 9000000, {'all':mult(1.1)}))

# Cursor & mouse upgrades.
menu.add(Upgrade('Reinforced index finger', {'Cursor':1}, 100, {'Cursor':gain(0.1), 'mouse':gain(1)}))
menu.add(Upgrade('Carpel tunnel prevention cream', {'Cursor':1}, 400, {'Cursor':double, 'mouse':double}))
menu.add(Upgrade('Ambidextrous', {'Cursor':10}, 10000, {'Cursor':double, 'mouse':double}))
menu.add(Upgrade('Thousand fingers', {'Cursor':20}, 500000, {'Cursor':fingers_type(0.1), 'mouse':fingers_type(0.1)}))
menu.add(Upgrade('Million fingers', {'Cursor':40}, 50*million, {'Cursor':fingers_type(0.5), 'mouse':fingers_type(0.5)}))

# Mouse only upgrades.
menu.add(Upgrade('Plastic mouse', {}, 50000, {'mouse':mouse_type}))
menu.add(Upgrade('Iron mouse', {}, 5*million, {'mouse':mouse_type}))

# Grandma upgrades.
menu.add(Upgrade('Forwards from grandma', {'Grandma':1}, 1000, {'Grandma':gain(0.3)}))
menu.add(Upgrade('Steel-plated rolling pins', {'Grandma':1}, 10000, {'Grandma':double}))
menu.add(Upgrade('Lubricated dentures', {'Grandma':10}, 100000, {'Grandma':double}))
menu.add(Upgrade('Prune juice', {'Grandma':50}, 5*million, {'Grandma':double}))

# Grandma type upgrades.
menu.add(Upgrade('Farmer grandmas', {'Grandma':1, 'Farm':15}, 50000, {'Grandma':double}))
menu.add(Upgrade('Worker grandmas', {'Grandma':1, 'Factory':15}, 300000, {'Grandma':double}))
menu.add(Upgrade('Miner grandmas', {'Grandma':1, 'Mine':15}, 1*million, {'Grandma':double}))

# Farm upgrades.
menu.add(Upgrade('Cheap hoes', {'Farm':1}, 5000, {'Farm':gain(1)}))
menu.add(Upgrade('Fertilizer', {'Farm':1}, 50000, {'Farm':double}))
menu.add(Upgrade('Cookie trees', {'Farm':10}, 500000, {'Farm':double}))
menu.add(Upgrade('Genetically-modified cookies', {'Farm':50}, 25*million, {'Farm':double}))

# Factory upgrades.
menu.add(Upgrade('Sturdier conveyor belts', {'Factory':1}, 30000, {'Factory':gain(4)}))
menu.add(Upgrade('Child labor', {'Factory':1}, 300000, {'Factory':double}))
menu.add(Upgrade('Sweatshop', {'Factory':10}, 3*million, {'Factory':double}))

# Mine upgrades.
menu.add(Upgrade('Sugar gas', {'Mine':1}, 100000, {'Mine':gain(10)}))
menu.add(Upgrade('Mega drill', {'Mine':1}, 1*million, {'Mine':double}))
menu.add(Upgrade('Ultradrill', {'Mine':10}, 10*million, {'Mine':double}))

# Shipment upgrades.
menu.add(Upgrade('Vanilla nebulae', {'Shipment':1}, 400000, {'Shipment':gain(30)}))
menu.add(Upgrade('Wormholes', {'Shipment':1}, 4*million, {'Shipment':double}))

# Alchemy lab upgrades.
menu.add(Upgrade('Antimony', {'Alchemy lab':1}, 2*million, {'Alchemy lab':gain(100)}))
menu.add(Upgrade('Essence of dough', {'Alchemy lab':1}, 20*million, {'Alchemy lab':double}))

# Portal upgrades.
menu.add(Upgrade('Ancient tablet', {'Portal':1}, 16.667*million, {'Portal':gain(1666)}))
menu.add(Upgrade('Insane oatling workers', {'Portal':1}, 166.667*million, {'Portal':double}))