from ..game import Upgrade, Effect

million = 10**6
billion = 10**9
trillion = 10**12
quadrillion = 10**15
quintillion = 10**18
sextillion = 10**21
septillion = 10**24
octillion=10**27
nonillion=10**30
decillion=10**33
undecillion=10**36
duodecillion=10**39
tredecillion=10**42
quattuordecillion=10**45
quindecillion=10**48
sexdecillion=10**51
septendecillion=10**54
octodecillion=10**57
novemdecillion=10**60
vigintillion=10**63
unvigintillion=10**66
duovigintillion=10**69

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
  'Portal',
  'Time machine',
  'Antimatter condenser',
  'Prism',
  'Chancemaker',
  'Fractal engine',
  'Javascript console',
  'Idleverse',
  'Cortex baker',
  'You',
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
  'Portal':1*trillion,
  'Time machine':14*trillion,
  'Antimatter condenser':170*trillion,
  'Prism':2.1*quadrillion,
  'Chancemaker':26*quadrillion,
  'Fractal engine':310*quadrillion,
  'Javascript console':71*quintillion,
  'Idleverse':12*sextillion,
  'Cortex baker':1.9*septillion,
  'You':540*septillion,
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
  'Portal':10*million,
  'Time machine':65*million,
  'Antimatter condenser':430*million,
  'Prism':2.9*billion,
  'Chancemaker':22*billion,
  'Fractal engine':150*billion,
  'Javascript console':1.1*trillion,
  'Idleverse':8.3*trillion,
  'Cortex baker':64*trillion,
  'You':510*trillion,
}



# Effects (like, for upgrades, ya' know?)
def multiplier(x):
  func = lambda r, game: r * x
  return Effect(2, func)
def grandma_boost(n): 
  func = lambda r, game: r * (1 + 0.01 * (game.num_buildings['Grandma']//n))
  return Effect(2, func)
def fingers_boost(x):
  func = lambda r, game: r + x * sum(game.num_buildings[name] for name in game.building_names if name != 'Cursor')
  return Effect(1, func)
def percent_boost(p):
  func = lambda r, game: r * (1 + p / 100.0)
  return Effect(0, func)

double = multiplier(2.0)
mouse_boost = Effect(1, lambda r, game: r + 0.01 * game.building_only_rate())


  
# The set of all upgrades. This is what gets passed to game.py.
menu = set()

# Cursor & mouse upgrades.
menu.add(Upgrade('Reinforced index finger', {'Cursor':1}, 100, {'Cursor':double, 'mouse':double}))
menu.add(Upgrade('Carpel tunnel prevention cream', {'Cursor':1}, 500, {'Cursor':double, 'mouse':double}))
menu.add(Upgrade('Ambidextrous', {'Cursor':10}, 10000, {'Cursor':double, 'mouse':double}))
menu.add(Upgrade('Thousand fingers', {'Cursor':25}, 100000, {'Cursor':fingers_boost(0.1), 'mouse':fingers_boost(0.1)}))
menu.add(Upgrade('Million fingers', {'Cursor':50}, 10*million, {'Cursor':fingers_boost(0.4), 'mouse':fingers_boost(0.4)})) # 0.5
menu.add(Upgrade('Billion fingers', {'Cursor':100}, 100*million, {'Cursor':fingers_boost(4.5), 'mouse':fingers_boost(4.5)})) # 5.0
menu.add(Upgrade('Trillion fingers', {'Cursor':150}, 1*billion, {'Cursor':fingers_boost(45), 'mouse':fingers_boost(45)})) # 50
menu.add(Upgrade('Quadrillion fingers', {'Cursor':200}, 10*billion, {'Cursor':fingers_boost(950), 'mouse':fingers_boost(950)})) # 1000
menu.add(Upgrade('Quintillion fingers', {'Cursor':250}, 10*trillion, {'Cursor':fingers_boost(19000), 'mouse':fingers_boost(19000)})) # 20000
menu.add(Upgrade('Sextillion fingers', {'Cursor':300}, 10*quadrillion, {'Cursor':fingers_boost(380000), 'mouse':fingers_boost(380000)})) # 400000...
menu.add(Upgrade('Septillion fingers', {'Cursor':350}, 10*quintillion, {'Cursor':fingers_boost(7.6*million), 'mouse':fingers_boost(7.6*million)})) 
menu.add(Upgrade('Octillion fingers', {'Cursor':400}, 10*sextillion, {'Cursor':fingers_boost(152*million), 'mouse':fingers_boost(152*million)})) 
menu.add(Upgrade('Nonillion fingers', {'Cursor':450}, 10*septillion, {'Cursor':fingers_boost(3.04*billion), 'mouse':fingers_boost(3.04*billion)})) 
menu.add(Upgrade('Decillion fingers', {'Cursor':500}, 10*octillion, {'Cursor':fingers_boost(60.8*billion), 'mouse':fingers_boost(60.8*billion)})) 
menu.add(Upgrade('Undecillion fingers', {'Cursor':550}, 10*nonillion, {'Cursor':fingers_boost(1.216*trillion), 'mouse':fingers_boost(1.216*trillion)})) 

# Mouse only upgrades.
menu.add(Upgrade('Plastic mouse', {}, 50000, {'mouse':mouse_boost}))
menu.add(Upgrade('Iron mouse', {}, 5*million, {'mouse':mouse_boost}))
menu.add(Upgrade('Titanium mouse', {}, 500*million, {'mouse':mouse_boost}))
menu.add(Upgrade('Adamantium mouse', {}, 50*billion, {'mouse':mouse_boost}))
menu.add(Upgrade('Unobtanium mouse', {}, 5*trillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Eludium mouse', {}, 500*trillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Wishalloy mouse', {}, 50*quadrillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Fantasteel mouse', {}, 5*quintillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Nevercrack mouse', {}, 500*quintillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Armythril mouse', {}, 50*sextillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Technobsidian mouse', {}, 5*septillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Plasmarble mouse', {}, 500*septillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Miraculite mouse', {}, 50*octillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Aetherice mouse', {}, 5*nonillion, {'mouse':mouse_boost}))
menu.add(Upgrade('Omniplast mouse', {}, 500*nonillion, {'mouse':mouse_boost}))

# Grandma upgrades.
menu.add(Upgrade('Forwards from grandma', {'Grandma':1}, 1000, {'Grandma':double}))
menu.add(Upgrade('Steel-plated rolling pins', {'Grandma':5}, 5000, {'Grandma':double}))
menu.add(Upgrade('Lubricated dentures', {'Grandma':25}, 50000, {'Grandma':double}))
menu.add(Upgrade('Prune juice', {'Grandma':50}, 5*million, {'Grandma':double}))
menu.add(Upgrade('Double-thick glasses', {'Grandma':100}, 500*million, {'Grandma':double}))
menu.add(Upgrade('Aging agents', {'Grandma':150}, 50*billion, {'Grandma':double}))
menu.add(Upgrade('Xtreme walkers', {'Grandma':200}, 50*trillion, {'Grandma':double}))
menu.add(Upgrade('The Unbridling', {'Grandma':250}, 50*quadrillion, {'Grandma':double}))
menu.add(Upgrade('Reverse dementia', {'Grandma':300}, 50*quintillion, {'Grandma':double}))
menu.add(Upgrade('Timeproof hair dyes', {'Grandma':350}, 50*sextillion, {'Grandma':double}))
menu.add(Upgrade('Good manners', {'Grandma':400}, 500*septillion, {'Grandma':double}))
menu.add(Upgrade('Generation degeneration', {'Grandma':450}, 500*nonillion, {'Grandma':double}))
menu.add(Upgrade('Visits', {'Grandma':500}, 50*decillion, {'Grandma':double}))
menu.add(Upgrade('Kitchen cabinets', {'Grandma':550}, 500*undecillion, {'Grandma':double}))
menu.add(Upgrade('Foam-tipped canes', {'Grandma':600}, 5*tredecillion, {'Grandma':double}))

# Grandma type upgrades.
menu.add(Upgrade('Farmer grandmas', {'Grandma':1, 'Farm':15}, 55000, {'Grandma':double, 'Farm':grandma_boost(1)}))
menu.add(Upgrade('Miner grandmas', {'Grandma':1, 'Mine':15}, 600000, {'Grandma':double, 'Mine':grandma_boost(2)}))
menu.add(Upgrade('Worker grandmas', {'Grandma':1, 'Factory':15}, 6.5*million, {'Grandma':double, 'Factory':grandma_boost(3)}))
menu.add(Upgrade('Banker grandmas', {'Grandma':1, 'Bank':15}, 70*million, {'Grandma':double, 'Bank':grandma_boost(4)}))
menu.add(Upgrade('Priestess grandmas', {'Grandma':1, 'Temple':15}, 1*billion, {'Grandma':double, 'Temple':grandma_boost(5)}))
menu.add(Upgrade('Witch grandmas', {'Grandma':1, 'Wizard tower':15}, 16.5*billion, {'Grandma':double, 'Wizard tower':grandma_boost(6)}))
menu.add(Upgrade('Cosmic grandmas', {'Grandma':1, 'Shipment':15}, 255*billion, {'Grandma':double, 'Shipment':grandma_boost(7)}))
menu.add(Upgrade('Transmuted grandmas', {'Grandma':1, 'Alchemy lab':15}, 255*billion, {'Grandma':double, 'Alchemy lab':grandma_boost(8)}))
menu.add(Upgrade('Altered grandmas', {'Grandma':1, 'Portal':15}, 255*billion, {'Grandma':double, 'Portal':grandma_boost(9)}))
menu.add(Upgrade('Grandmas\' grandmas', {'Grandma':1, 'Time machine':15}, 700*trillion, {'Grandma':double, 'Time machine':grandma_boost(10)}))
menu.add(Upgrade('Antigrandmas', {'Grandma':1, 'Antimatter condenser':15}, 8.5*quadrillion, {'Grandma':double, 'Antimatter condenser':grandma_boost(11)}))
menu.add(Upgrade('Rainbow grandmas', {'Grandma':1, 'Prism':15}, 105*quadrillion, {'Grandma':double, 'Prism':grandma_boost(12)}))
menu.add(Upgrade('Lucky grandmas', {'Grandma':1, 'Chancemaker':15}, 1.3*quintillion, {'Grandma':double, 'Chancemaker':grandma_boost(13)}))
menu.add(Upgrade('Metagrandmas', {'Grandma':1, 'Fractal engine':15}, 15.5*quintillion, {'Grandma':double, 'Fractal engine':grandma_boost(14)}))
menu.add(Upgrade('Binary grandmas', {'Grandma':1, 'Javascript console':15}, 3.55*sextillion, {'Grandma':double, 'Javascript console':grandma_boost(15)}))
menu.add(Upgrade('Alternate grandmas', {'Grandma':1, 'Idleverse':15}, 600*sextillion, {'Grandma':double, 'Idleverse':grandma_boost(16)}))
menu.add(Upgrade('Brainy grandmas', {'Grandma':1, 'Cortex baker':15}, 95*septillion, {'Grandma':double, 'Cortex baker':grandma_boost(17)}))
menu.add(Upgrade('Clone grandmas', {'Grandma':1, 'You':15}, 27*octillion, {'Grandma':double, 'You':grandma_boost(18)}))

# Farm upgrades.
menu.add(Upgrade('Cheap hoes', {'Farm':1}, 11000, {'Farm':double}))
menu.add(Upgrade('Fertilizer', {'Farm':5}, 55000, {'Farm':double}))
menu.add(Upgrade('Cookie trees', {'Farm':25}, 550000, {'Farm':double}))
menu.add(Upgrade('Genetically-modified cookies', {'Farm':50}, 55*million, {'Farm':double}))
menu.add(Upgrade('Gingerbread scarecrows', {'Farm':100}, 5.5*billion, {'Farm':double}))
menu.add(Upgrade('Pulsar sprinklers', {'Farm':150}, 550*billion, {'Farm':double}))
menu.add(Upgrade('Fudge fungus', {'Farm':200}, 550*trillion, {'Farm':double}))
menu.add(Upgrade('Wheat triffids', {'Farm':250}, 550*quadrillion, {'Farm':double}))
menu.add(Upgrade('Humane pesticides', {'Farm':300}, 550*quintillion, {'Farm':double}))
menu.add(Upgrade('Barnstars', {'Farm':350}, 550*sextillion, {'Farm':double}))
menu.add(Upgrade('Lindworms', {'Farm':400}, 5.5*octillion, {'Farm':double}))
menu.add(Upgrade('Global seed vault', {'Farm':450}, 55*nonillion, {'Farm':double}))
menu.add(Upgrade('Reverse-veganism', {'Farm':500}, 550*decillion, {'Farm':double}))
menu.add(Upgrade('Cookie mulch', {'Farm':550}, 5.5*duodecillion, {'Farm':double}))
menu.add(Upgrade('Self-driving tractors', {'Farm':600}, 55*tredecillion, {'Farm':double}))

# Mine upgrades.
menu.add(Upgrade('Sugar gas', {'Mine':1}, 120000, {'Mine':double}))
menu.add(Upgrade('Mega drill', {'Mine':5}, 600000, {'Mine':double}))
menu.add(Upgrade('Ultradrill', {'Mine':25}, 6*million, {'Mine':double}))
menu.add(Upgrade('Ultimadrill', {'Mine':50}, 600*million, {'Mine':double}))
menu.add(Upgrade('H-bomb mining', {'Mine':100}, 60*billion, {'Mine':double}))
menu.add(Upgrade('Coreforge', {'Mine':150}, 6*trillion, {'Mine':double}))
menu.add(Upgrade('Planetsplitters', {'Mine':200}, 6*quadrillion, {'Mine':double}))
menu.add(Upgrade('Canola oil wells', {'Mine':250}, 6*quintillion, {'Mine':double}))
menu.add(Upgrade('Mole people', {'Mine':300}, 6*sextillion, {'Mine':double}))
menu.add(Upgrade('Mine canaries', {'Mine':350}, 6*septillion, {'Mine':double}))
menu.add(Upgrade('Bore again', {'Mine':400}, 60*octillion, {'Mine':double}))
menu.add(Upgrade('Air mining', {'Mine':450}, 600*nonillion, {'Mine':double}))
menu.add(Upgrade('Caramel alloys', {'Mine':500}, 6*undecillion, {'Mine':double}))
menu.add(Upgrade('Delicious mineralogy', {'Mine':550}, 60*duodecillion, {'Mine':double}))
menu.add(Upgrade('Mineshaft supports', {'Mine':600}, 600*tredecillion, {'Mine':double}))

# Factory upgrades.
menu.add(Upgrade('Sturdier conveyor belts', {'Factory':1}, 1.3*million, {'Factory':double}))
menu.add(Upgrade('Child labor', {'Factory':5}, 6.5*million, {'Factory':double}))
menu.add(Upgrade('Sweatshop', {'Factory':25}, 65*million, {'Factory':double}))
menu.add(Upgrade('Radium reactors', {'Factory':50}, 6.5*billion, {'Factory':double}))
menu.add(Upgrade('Recombobulators', {'Factory':100}, 650*billion, {'Factory':double}))
menu.add(Upgrade('Deep-bake process', {'Factory':150}, 65*trillion, {'Factory':double}))
menu.add(Upgrade('Cyborg workforce', {'Factory':200}, 65*quadrillion, {'Factory':double}))
menu.add(Upgrade('78-hour days', {'Factory':250}, 65*quintillion, {'Factory':double}))
menu.add(Upgrade('Machine learning', {'Factory':300}, 65*sextillion, {'Factory':double}))
menu.add(Upgrade('Brownie point system', {'Factory':350}, 65*septillion, {'Factory':double}))
menu.add(Upgrade('"Volunteer" interns', {'Factory':400}, 650*octillion, {'Factory':double}))
menu.add(Upgrade('Behavioral reframing', {'Factory':450}, 6.5*decillion, {'Factory':double}))
menu.add(Upgrade('The infinity engine', {'Factory':500}, 65*undecillion, {'Factory':double}))
menu.add(Upgrade('N-dimensional assembly lines', {'Factory':550}, 650*duodecillion, {'Factory':double}))
menu.add(Upgrade('Universal automation', {'Factory':600}, 6.5*quattuordecillion, {'Factory':double}))

# Bank upgrades.
menu.add(Upgrade('Taller tellers', {'Bank':1}, 14*million, {'Bank':double}))
menu.add(Upgrade('Scissor-resistant credit cards', {'Bank':5}, 70*million, {'Bank':double}))
menu.add(Upgrade('Acid-proof vaults', {'Bank':25}, 700*million, {'Bank':double}))
menu.add(Upgrade('Chocolate coins', {'Bank':50}, 70*billion, {'Bank':double}))
menu.add(Upgrade('Exponential interest rates', {'Bank':100}, 7*trillion, {'Bank':double}))
menu.add(Upgrade('Financial zen', {'Bank':150}, 700*trillion, {'Bank':double}))
menu.add(Upgrade('Way of the wallet', {'Bank':200}, 700*quadrillion, {'Bank':double}))
menu.add(Upgrade('The stuff rationale', {'Bank':250}, 700*quintillion, {'Bank':double}))
menu.add(Upgrade('Edible money', {'Bank':300}, 700*sextillion, {'Bank':double}))
menu.add(Upgrade('Grand supercycle', {'Bank':350}, 700*septillion, {'Bank':double}))
menu.add(Upgrade('Rules of acquisition', {'Bank':400}, 7*nonillion, {'Bank':double}))
menu.add(Upgrade('Altruistic loop', {'Bank':450}, 70*decillion, {'Bank':double}))
menu.add(Upgrade('Diminishing tax returns	', {'Bank':500}, 700*undecillion, {'Bank':double}))
menu.add(Upgrade('Cookie Points', {'Bank':550}, 7*tredecillion, {'Bank':double}))
menu.add(Upgrade('The big shortcake', {'Bank':600}, 70*quattuordecillion, {'Bank':double}))

# Temple upgrades.
menu.add(Upgrade('Golden idols', {'Temple':1}, 200*million, {'Temple':double}))
menu.add(Upgrade('Sacrifices', {'Temple':5}, 1*billion, {'Temple':double}))
menu.add(Upgrade('Delicious blessing', {'Temple':25}, 10*billion, {'Temple':double}))
menu.add(Upgrade('Sun festival', {'Temple':50}, 1*trillion, {'Temple':double}))
menu.add(Upgrade('Enlarged pantheon', {'Temple':100}, 100*trillion, {'Temple':double}))
menu.add(Upgrade('Great Baker in the sky', {'Temple':150}, 10*quadrillion, {'Temple':double}))
menu.add(Upgrade('Creation myth', {'Temple':200}, 10*quintillion, {'Temple':double}))
menu.add(Upgrade('Theocracy', {'Temple':250}, 10*sextillion, {'Temple':double}))
menu.add(Upgrade('Sick rap prayers', {'Temple':300}, 10*septillion, {'Temple':double}))
menu.add(Upgrade('Psalm-reading	', {'Temple':350}, 10*octillion, {'Temple':double}))
menu.add(Upgrade('War of the gods', {'Temple':400}, 100*nonillion, {'Temple':double}))
menu.add(Upgrade('A novel idea', {'Temple':450}, 1*undecillion, {'Temple':double}))
menu.add(Upgrade('Apparitions', {'Temple':500}, 10*duodecillion, {'Temple':double}))
menu.add(Upgrade('Negatheism', {'Temple':550}, 100*tredecillion, {'Temple':double}))
menu.add(Upgrade('Temple traps', {'Temple':600}, 1*quindecillion, {'Temple':double}))

# Wizard tower upgrades.
menu.add(Upgrade('Pointier hats', {'Wizard tower':1}, 3.3*billion, {'Wizard tower':double}))
menu.add(Upgrade('Beardlier beards', {'Wizard tower':5}, 16.5*billion, {'Wizard tower':double}))
menu.add(Upgrade('Ancient grimoires', {'Wizard tower':25}, 165*billion, {'Wizard tower':double}))
menu.add(Upgrade('Kitchen curses', {'Wizard tower':50}, 16.5*trillion, {'Wizard tower':double}))
menu.add(Upgrade('School of sorcery', {'Wizard tower':100}, 1.65*quadrillion, {'Wizard tower':double}))
menu.add(Upgrade('Dark formulas', {'Wizard tower':150}, 165*quadrillion, {'Wizard tower':double}))
menu.add(Upgrade('Cookiemancy', {'Wizard tower':200}, 165*quintillion, {'Wizard tower':double}))
menu.add(Upgrade('Rabbit trick', {'Wizard tower':250}, 165*sextillion, {'Wizard tower':double}))
menu.add(Upgrade('Deluxe tailored wands', {'Wizard tower':300}, 165*septillion, {'Wizard tower':double}))
menu.add(Upgrade('Immobile spellcasting', {'Wizard tower':350}, 165*octillion, {'Wizard tower':double}))
menu.add(Upgrade('Electricity', {'Wizard tower':400}, 1.65*decillion, {'Wizard tower':double}))
menu.add(Upgrade('Spelling bees', {'Wizard tower':450}, 16.5*undecillion, {'Wizard tower':double}))
menu.add(Upgrade('Wizard basements', {'Wizard tower':500}, 165*duodecillion, {'Wizard tower':double}))
menu.add(Upgrade('Magical realisms', {'Wizard tower':550}, 1.65*quattuordecillion, {'Wizard tower':double}))
menu.add(Upgrade('Polymorphism', {'Wizard tower':600}, 16.5*quindecillion, {'Wizard tower':double}))

# Shipment upgrades.
menu.add(Upgrade('Vanilla nebulae', {'Shipment':1}, 51*billion, {'Shipment':double}))
menu.add(Upgrade('Wormholes', {'Shipment':5}, 255*billion, {'Shipment':double}))
menu.add(Upgrade('Frequent flyer', {'Shipment':25}, 2.55*trillion, {'Shipment':double}))
menu.add(Upgrade('Warp drive', {'Shipment':50}, 255*trillion, {'Shipment':double}))
menu.add(Upgrade('Chocolate monoliths', {'Shipment':100}, 25.5*quadrillion, {'Shipment':double}))
menu.add(Upgrade('Generation ship', {'Shipment':150}, 2.55*quintillion, {'Shipment':double}))
menu.add(Upgrade('Dyson sphere', {'Shipment':200}, 2.55*sextillion, {'Shipment':double}))
menu.add(Upgrade('The final frontier', {'Shipment':250}, 2.55*septillion, {'Shipment':double}))
menu.add(Upgrade('Autopilot', {'Shipment':300}, 2.55*octillion, {'Shipment':double}))
menu.add(Upgrade('Restaurants at the end of the universe', {'Shipment':350}, 2.55*nonillion, {'Shipment':double}))
menu.add(Upgrade('Universal alphabet', {'Shipment':400}, 25.5*decillion, {'Shipment':double}))
menu.add(Upgrade('Toroid universe', {'Shipment':450}, 255*undecillion, {'Shipment':double}))
menu.add(Upgrade('Prime directive', {'Shipment':500}, 2.55*tredecillion, {'Shipment':double}))
menu.add(Upgrade('Cosmic foreground radiation', {'Shipment':550}, 25.5*quattuordecillion, {'Shipment':double}))
menu.add(Upgrade('At your doorstep in 30 minutes or your money back', {'Shipment':600}, 255*quindecillion, {'Shipment':double}))

# Alchemy lab upgrades.
menu.add(Upgrade('Antimony', {'Alchemy lab':1}, 750*billion, {'Alchemy lab':double}))
menu.add(Upgrade('Essence of dough', {'Alchemy lab':5}, 3.75*trillion, {'Alchemy lab':double}))
menu.add(Upgrade('True chocolate', {'Alchemy lab':25}, 37.5*trillion, {'Alchemy lab':double}))
menu.add(Upgrade('Ambrosia', {'Alchemy lab':50}, 3.75*quadrillion, {'Alchemy lab':double}))
menu.add(Upgrade('Aqua crustulae', {'Alchemy lab':100}, 375*quadrillion, {'Alchemy lab':double}))
menu.add(Upgrade('Origin crucible', {'Alchemy lab':150}, 37.5*quintillion, {'Alchemy lab':double}))
menu.add(Upgrade('Theory of atomic fluidity', {'Alchemy lab':200}, 37.5*sextillion, {'Alchemy lab':double}))
menu.add(Upgrade('Beige goo', {'Alchemy lab':250}, 37.5*septillion, {'Alchemy lab':double}))
menu.add(Upgrade('The advent of chemistry', {'Alchemy lab':300}, 37.5*octillion, {'Alchemy lab':double}))
menu.add(Upgrade('On second thought', {'Alchemy lab':350}, 37.5*nonillion, {'Alchemy lab':double}))
menu.add(Upgrade('Public betterment', {'Alchemy lab':400}, 375*decillion, {'Alchemy lab':double}))
menu.add(Upgrade('Hermetic reconciliation', {'Alchemy lab':450}, 3.75*duodecillion, {'Alchemy lab':double}))
menu.add(Upgrade('Chromatic cycling', {'Alchemy lab':500}, 37.5*tredecillion, {'Alchemy lab':double}))
menu.add(Upgrade('Arcanized glassware', {'Alchemy lab':550}, 375*quattuordecillion, {'Alchemy lab':double}))
menu.add(Upgrade('The dose makes the poison', {'Alchemy lab':600}, 3.75*sexdecillion, {'Alchemy lab':double}))

# Portal upgrades.
menu.add(Upgrade('Ancient tablet', {'Portal':1}, 10*trillion, {'Portal':double}))
menu.add(Upgrade('Insane oatling workers', {'Portal':5}, 50*trillion, {'Portal':double}))
menu.add(Upgrade('Soul bond', {'Portal':25}, 500*trillion, {'Portal':double}))
menu.add(Upgrade('Sanity dance', {'Portal':50}, 50*quadrillion, {'Portal':double}))
menu.add(Upgrade('Brane transplant', {'Portal':100}, 5*quintillion, {'Portal':double}))
menu.add(Upgrade('Deity-sized portals', {'Portal':150}, 500*quintillion, {'Portal':double}))
menu.add(Upgrade('End of times back-up plan', {'Portal':200}, 500*sextillion, {'Portal':double}))
menu.add(Upgrade('Maddening chants', {'Portal':250}, 500*septillion, {'Portal':double}))
menu.add(Upgrade('The real world', {'Portal':300}, 500*octillion, {'Portal':double}))
menu.add(Upgrade('Dimensional garbage gulper', {'Portal':350}, 500*nonillion, {'Portal':double}))
menu.add(Upgrade('Embedded microportals', {'Portal':400}, 5*undecillion, {'Portal':double}))
menu.add(Upgrade('His advent', {'Portal':450}, 50*duodecillion, {'Portal':double}))
menu.add(Upgrade('Domestic rifts', {'Portal':500}, 500*tredecillion, {'Portal':double}))
menu.add(Upgrade('Portal guns', {'Portal':550}, 5*quindecillion, {'Portal':double}))
menu.add(Upgrade('A way home', {'Portal':600}, 50*sexdecillion, {'Portal':double}))

# Time machine upgrades.
menu.add(Upgrade('Flux capacitors', {'Time machine':1}, 140*trillion, {'Time machine':double}))
menu.add(Upgrade('Time paradox resolver', {'Time machine':5}, 700*trillion, {'Time machine':double}))
menu.add(Upgrade('Quantum conundrum', {'Time machine':25}, 7*quadrillion, {'Time machine':double}))
menu.add(Upgrade('Causality enforcer', {'Time machine':50}, 700*quadrillion, {'Time machine':double}))
menu.add(Upgrade('Yestermorrow comparators', {'Time machine':100}, 70*quintillion, {'Time machine':double}))
menu.add(Upgrade('Far future enactment', {'Time machine':150}, 7*sextillion, {'Time machine':double}))
menu.add(Upgrade('Great loop hypothesis', {'Time machine':200}, 7*septillion, {'Time machine':double}))
menu.add(Upgrade('Cookietopian moments of maybe', {'Time machine':250}, 7*octillion, {'Time machine':double}))
menu.add(Upgrade('Second seconds', {'Time machine':300}, 7*nonillion, {'Time machine':double}))
menu.add(Upgrade('Additional clock hands', {'Time machine':350}, 7*decillion, {'Time machine':double}))
menu.add(Upgrade('Nostalgia', {'Time machine':400}, 70*undecillion, {'Time machine':double}))
menu.add(Upgrade('Split seconds', {'Time machine':450}, 700*duodecillion, {'Time machine':double}))
menu.add(Upgrade('Patience abolished', {'Time machine':500}, 7*quattuordecillion, {'Time machine':double}))
menu.add(Upgrade('Timeproof upholstery', {'Time machine':550}, 70*quindecillion, {'Time machine':double}))
menu.add(Upgrade('Rectifying a mistake', {'Time machine':600}, 700*sexdecillion, {'Time machine':double}))

# Antimatter condenser upgrades.
menu.add(Upgrade('Sugar bosons', {'Antimatter condenser':1}, 1.7*quadrillion, {'Antimatter condenser':double}))
menu.add(Upgrade('String theory', {'Antimatter condenser':5}, 8.5*quadrillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Large macaron collider', {'Antimatter condenser':25}, 85*quadrillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Big bang bake', {'Antimatter condenser':50}, 8.5*quintillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Reverse cyclotrons', {'Antimatter condenser':100}, 850*quintillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Nanocosmics', {'Antimatter condenser':150}, 85*sextillion, {'Antimatter condenser':double}))
menu.add(Upgrade('The Pulse', {'Antimatter condenser':200}, 85*septillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Some other super-tiny fundamental particle? Probably?', {'Antimatter condenser':250}, 85*octillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Quantum comb', {'Antimatter condenser':300}, 85*nonillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Baking Nobel prize', {'Antimatter condenser':350}, 85*decillion, {'Antimatter condenser':double}))
menu.add(Upgrade('The definite molecule', {'Antimatter condenser':400}, 850*undecillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Flavor itself', {'Antimatter condenser':450}, 8.5*tredecillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Delicious pull', {'Antimatter condenser':500}, 85*quattuordecillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Employee minification', {'Antimatter condenser':550}, 850*quindecillion, {'Antimatter condenser':double}))
menu.add(Upgrade('Candied atoms', {'Antimatter condenser':600}, 8.5*septendecillion, {'Antimatter condenser':double}))

# Prism upgrades.
menu.add(Upgrade('Gem polish', {'Prism':1}, 21*quadrillion, {'Prism':double}))
menu.add(Upgrade('9th color', {'Prism':5}, 105*quadrillion, {'Prism':double}))
menu.add(Upgrade('Chocolate light', {'Prism':25}, 1.05*quintillion, {'Prism':double}))
menu.add(Upgrade('Grainbow', {'Prism':50}, 105*quintillion, {'Prism':double}))
menu.add(Upgrade('Pure cosmic light', {'Prism':100}, 10.5*sextillion, {'Prism':double}))
menu.add(Upgrade('Glow-in-the-dark', {'Prism':150}, 1.05*septillion, {'Prism':double}))
menu.add(Upgrade('Lux sanctorum', {'Prism':200}, 1.05*octillion, {'Prism':double}))
menu.add(Upgrade('Reverse shadows', {'Prism':250}, 1.05*nonillion, {'Prism':double}))
menu.add(Upgrade('Crystal mirrors', {'Prism':300}, 1.05*decillion, {'Prism':double}))
menu.add(Upgrade('Reverse theory of light', {'Prism':350}, 1.05*undecillion, {'Prism':double}))
menu.add(Upgrade('Light capture measures', {'Prism':400}, 10.5*duodecillion, {'Prism':double}))
menu.add(Upgrade('Light speed limit', {'Prism':450}, 105*tredecillion, {'Prism':double}))
menu.add(Upgrade('Occam`s laser', {'Prism':500}, 1.05*quindecillion, {'Prism':double}))
menu.add(Upgrade('Hyperblack paint', {'Prism':550}, 10.5*sexdecillion, {'Prism':double}))
menu.add(Upgrade('Lab goggles but like cool shades', {'Prism':600}, 105*septendecillion, {'Prism':double}))

# Chancemaker upgrades.
menu.add(Upgrade('Your lucky cookie', {'Chancemaker':1}, 260*quadrillion, {'Chancemaker':double}))
menu.add(Upgrade('"All Bets Are Off" magic coin', {'Chancemaker':5}, 1.3*quintillion, {'Chancemaker':double}))
menu.add(Upgrade('Winning lottery ticket', {'Chancemaker':25}, 13*quintillion, {'Chancemaker':double}))
menu.add(Upgrade('Four-leaf clover field', {'Chancemaker':50}, 1.3*sextillion, {'Chancemaker':double}))
menu.add(Upgrade('A recipe book about books', {'Chancemaker':100}, 130*sextillion, {'Chancemaker':double}))
menu.add(Upgrade('Leprechaun village', {'Chancemaker':150}, 13*septillion, {'Chancemaker':double}))
menu.add(Upgrade('Improbability drive', {'Chancemaker':200}, 13*octillion, {'Chancemaker':double}))
menu.add(Upgrade('Antisuperstistronics', {'Chancemaker':250}, 13*nonillion, {'Chancemaker':double}))
menu.add(Upgrade('Bunnypedes', {'Chancemaker':300}, 13*decillion, {'Chancemaker':double}))
menu.add(Upgrade('Revised probabilistics', {'Chancemaker':350}, 13*undecillion, {'Chancemaker':double}))
menu.add(Upgrade('0-sided dice', {'Chancemaker':400}, 130*duodecillion, {'Chancemaker':double}))
menu.add(Upgrade('A touch of determinism', {'Chancemaker':450}, 1.3*quattuordecillion, {'Chancemaker':double}))
menu.add(Upgrade('On a streak', {'Chancemaker':500}, 13*quindecillion, {'Chancemaker':double}))
menu.add(Upgrade('Silver lining maximization', {'Chancemaker':550}, 130*sexdecillion, {'Chancemaker':double}))
menu.add(Upgrade('Gambler`s fallacy fallacy', {'Chancemaker':600}, 1.3*octodecillion, {'Chancemaker':double}))

# Fractal engine upgrades.
menu.add(Upgrade('Metabakeries', {'Fractal engine':1}, 3.1*quintillion, {'Fractal engine':double}))
menu.add(Upgrade('Mandelbrown sugar', {'Fractal engine':5}, 15.5*quintillion, {'Fractal engine':double}))
menu.add(Upgrade('Fractoids', {'Fractal engine':25}, 155*quintillion, {'Fractal engine':double}))
menu.add(Upgrade('Nested universe theory', {'Fractal engine':50}, 15.5*sextillion, {'Fractal engine':double}))
menu.add(Upgrade('Menger sponge cake', {'Fractal engine':100}, 1.55*septillion, {'Fractal engine':double}))
menu.add(Upgrade('One particularly good-humored cow', {'Fractal engine':150}, 155*septillion, {'Fractal engine':double}))
menu.add(Upgrade('Chocolate ouroboros', {'Fractal engine':200}, 155*octillion, {'Fractal engine':double}))
menu.add(Upgrade('Nested', {'Fractal engine':250}, 155*nonillion, {'Fractal engine':double}))
menu.add(Upgrade('Space-filling fibers', {'Fractal engine':300}, 155*decillion, {'Fractal engine':double}))
menu.add(Upgrade('Endless book of prose', {'Fractal engine':350}, 155*undecillion, {'Fractal engine':double}))
menu.add(Upgrade('The set of all sets', {'Fractal engine':400}, 1.55*tredecillion, {'Fractal engine':double}))
menu.add(Upgrade('This upgrade', {'Fractal engine':450}, 15.5*quattuordecillion, {'Fractal engine':double}))
menu.add(Upgrade('A box', {'Fractal engine':500}, 155*quindecillion, {'Fractal engine':double}))
menu.add(Upgrade('Multiscale profiling', {'Fractal engine':550}, 1.55*septendecillion, {'Fractal engine':double}))
menu.add(Upgrade('The more they stay the same', {'Fractal engine':600}, 15.5*octodecillion, {'Fractal engine':double}))

# Javascript console upgrades.
menu.add(Upgrade('The JavaScript console for dummies', {'Javascript console':1}, 710*quintillion, {'Javascript console':double}))
menu.add(Upgrade('64bit arrays', {'Javascript console':5}, 3.55*sextillion, {'Javascript console':double}))
menu.add(Upgrade('Stack overflow', {'Javascript console':25}, 35.5*sextillion, {'Javascript console':double}))
menu.add(Upgrade('Enterprise compiler', {'Javascript console':50}, 3.55*septillion, {'Javascript console':double}))
menu.add(Upgrade('Syntactic sugar', {'Javascript console':100}, 355*septillion, {'Javascript console':double}))
menu.add(Upgrade('A nice cup of coffee', {'Javascript console':150}, 35.5*octillion, {'Javascript console':double}))
menu.add(Upgrade('Just-in-time baking', {'Javascript console':200}, 35.5*nonillion, {'Javascript console':double}))
menu.add(Upgrade('cookies++', {'Javascript console':250}, 35.5*decillion, {'Javascript console':double}))
menu.add(Upgrade('Software updates', {'Javascript console':300}, 35.5*undecillion, {'Javascript console':double}))
menu.add(Upgrade('Game.Loop', {'Javascript console':350}, 35.5*duodecillion, {'Javascript console':double}))
menu.add(Upgrade('eval()', {'Javascript console':400}, 355*tredecillion, {'Javascript console':double}))
menu.add(Upgrade('Your biggest fans', {'Javascript console':450}, 3.55*quindecillion, {'Javascript console':double}))
menu.add(Upgrade('Hacker shades', {'Javascript console':500}, 35.5*sexdecillion, {'Javascript console':double}))
menu.add(Upgrade('PHP containment vats', {'Javascript console':550}, 355*septendecillion, {'Javascript console':double}))
menu.add(Upgrade('Simulation failsafes', {'Javascript console':600}, 3.55*novemdecillion, {'Javascript console':double}))

# Idleverse upgrades.
menu.add(Upgrade('Manifest destiny', {'Idleverse':1}, 120*sextillion, {'Idleverse':double}))
menu.add(Upgrade('The multiverse in a nutshell', {'Idleverse':5}, 600*sextillion, {'Idleverse':double}))
menu.add(Upgrade('All-conversion', {'Idleverse':25}, 6*septillion, {'Idleverse':double}))
menu.add(Upgrade('Multiverse agents', {'Idleverse':50}, 600*septillion, {'Idleverse':double}))
menu.add(Upgrade('Escape plan', {'Idleverse':100}, 60*octillion, {'Idleverse':double}))
menu.add(Upgrade('Game design', {'Idleverse':150}, 6*nonillion, {'Idleverse':double}))
menu.add(Upgrade('Sandbox universes', {'Idleverse':200}, 6*decillion, {'Idleverse':double}))
menu.add(Upgrade('Multiverse wars', {'Idleverse':250}, 6*undecillion, {'Idleverse':double}))
menu.add(Upgrade('Mobile ports', {'Idleverse':300}, 6*duodecillion, {'Idleverse':double}))
menu.add(Upgrade('Encapsulated realities', {'Idleverse':350}, 6*tredecillion, {'Idleverse':double}))
menu.add(Upgrade('Extrinsic clicking', {'Idleverse':400}, 60*quattuordecillion, {'Idleverse':double}))
menu.add(Upgrade('Universal idling', {'Idleverse':450}, 600*quindecillion, {'Idleverse':double}))
menu.add(Upgrade('Break the fifth wall', {'Idleverse':500}, 6*septendecillion, {'Idleverse':double}))
menu.add(Upgrade('Opposite universe', {'Idleverse':550}, 60*octodecillion, {'Idleverse':double}))
menu.add(Upgrade('The other routes to Rome', {'Idleverse':600}, 600*novemdecillion, {'Idleverse':double}))

# Cortex baker upgrades.
menu.add(Upgrade('Principled neural shackles', {'Cortex baker':1}, 19*septillion, {'Cortex baker':double}))
menu.add(Upgrade('Obey', {'Cortex baker':5}, 95*septillion, {'Cortex baker':double}))
menu.add(Upgrade('A sprinkle of irrationality', {'Cortex baker':25}, 950*septillion, {'Cortex baker':double}))
menu.add(Upgrade('Front and back hemispheres', {'Cortex baker':50}, 95*octillion, {'Cortex baker':double}))
menu.add(Upgrade('Neural networking', {'Cortex baker':100}, 9.5*nonillion, {'Cortex baker':double}))
menu.add(Upgrade('Cosmic brainstorms', {'Cortex baker':150}, 950*nonillion, {'Cortex baker':double}))
menu.add(Upgrade('Megatherapy', {'Cortex baker':200}, 950*decillion, {'Cortex baker':double}))
menu.add(Upgrade('Synaptic lubricant', {'Cortex baker':250}, 950*undecillion, {'Cortex baker':double}))
menu.add(Upgrade('Psychokinesis', {'Cortex baker':300}, 950*duodecillion, {'Cortex baker':double}))
menu.add(Upgrade('Spines', {'Cortex baker':350}, 950*tredecillion, {'Cortex baker':double}))
menu.add(Upgrade('Neuraforming', {'Cortex baker':400}, 9.5*quindecillion, {'Cortex baker':double}))
menu.add(Upgrade('Epistemological trickery', {'Cortex baker':450}, 95*sexdecillion, {'Cortex baker':double}))
menu.add(Upgrade('Every possible idea', {'Cortex baker':500}, 950*septendecillion, {'Cortex baker':double}))
menu.add(Upgrade('The land of dreams', {'Cortex baker':550}, 9.5*novemdecillion, {'Cortex baker':double}))
menu.add(Upgrade('Intellectual property theft	', {'Cortex baker':600}, 95*vigintillion, {'Cortex baker':double}))

# You upgrades.
menu.add(Upgrade('Obey', {'You':1}, 5.4*octillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':5}, 27*octillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':25}, 270*octillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':50}, 27*nonillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':100}, 2.7*decillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':150}, 270*decillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':200}, 270*undecillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':250}, 270*duodecillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':300}, 270*tredecillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':350}, 270*quattuordecillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':400}, 2.7*sexdecillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':450}, 27*septendecillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':500}, 270*octodecillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':550}, 2.7*vigintillion, {'You':double}))
menu.add(Upgrade('Obey', {'You':600}, 27*unvigintillion, {'You':double}))

# Kitten upgrades.
menu.add(Upgrade('Kitten helpers', {}, 9*million, {'all':percent_boost(12.8)})) #32 achievements.
menu.add(Upgrade('Kitten workers', {}, 9*billion, {'all':percent_boost(24)}))
menu.add(Upgrade('Kitten engineers', {}, 90*trillion, {'all':percent_boost(43.8)}))
menu.add(Upgrade('Kitten overseers', {}, 90*quadrillion, {'all':percent_boost(60)}))
menu.add(Upgrade('Kitten managers', {}, 900*quintillion, {'all':percent_boost(80)}))
menu.add(Upgrade('Kitten accountants', {}, 900*sextillion, {'all':percent_boost(100)}))
menu.add(Upgrade('Kitten specialists', {}, 900*septillion, {'all':percent_boost(120)}))
menu.add(Upgrade('Kitten specialists', {}, 900*octillion, {'all':percent_boost(140)}))
menu.add(Upgrade('Kitten specialists', {}, 900*nonillion, {'all':percent_boost(160)}))
menu.add(Upgrade('Kitten specialists', {}, 900*decillion, {'all':percent_boost(180)}))
menu.add(Upgrade('Kitten specialists', {}, 900*undecillion, {'all':percent_boost(200)}))
menu.add(Upgrade('Kitten specialists', {}, 900*duodecillion, {'all':percent_boost(220)}))
menu.add(Upgrade('Kitten specialists', {}, 900*tredecillion, {'all':percent_boost(240)}))
menu.add(Upgrade('Kitten specialists', {}, 900*quattuordecillion, {'all':percent_boost(260)}))
menu.add(Upgrade('Kitten specialists', {}, 900*quindecillion, {'all':percent_boost(280)}))

# Research.
menu.add(Upgrade('Bingo center', {'Grandma':1}, 1*quadrillion, {'Grandma':multiplier(4.0)}))
menu.add(Upgrade('Specialized chocolate chips', {}, 1*quadrillion, {'all':percent_boost(1)}))
menu.add(Upgrade('Designer cocoa beans', {}, 2*quadrillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Ritual rolling pins', {'Grandma':1}, 4*quadrillion, {'Grandma':double}))
menu.add(Upgrade('Underworld ovens', {}, 8*quadrillion, {'all':percent_boost(3)}))
# TODO
menu.add(Upgrade('Exotic nuts', {}, 32*quadrillion, {'all':percent_boost(4)}))
# TODO
menu.add(Upgrade('Arcane sugar', {}, 128*quadrillion, {'all':percent_boost(5)}))

# Golden Cookie upgrades.
menu.add(Upgrade('Lucky day', {}, 777.778*million, {'all':percent_boost(50)}))
menu.add(Upgrade('Serendipity', {}, 77.778*billion, {'all':percent_boost(100)}))
menu.add(Upgrade('Get lucky', {}, 77.778*trillion, {'all':percent_boost(150)}))


# Flavored cookies.
menu.add(Upgrade('Plain cookies', {}, 999999, {'all':percent_boost(1)}))

menu.add(Upgrade('Sugar cookies', {}, 5*million, {'all':percent_boost(1)}))
menu.add(Upgrade('Oatmeal raisin cookies', {}, 10*million, {'all':percent_boost(1)}))
menu.add(Upgrade('Peanut butter cookies', {}, 50*million, {'all':percent_boost(2)}))
menu.add(Upgrade('Coconut cookies', {}, 100*million, {'all':percent_boost(2)}))
menu.add(Upgrade('Macadamia nut cookies', {}, 100*million, {'all':percent_boost(2)}))
menu.add(Upgrade('Almond cookies', {}, 100*million, {'all':percent_boost(2)}))
menu.add(Upgrade('Hazelnut cookies', {}, 100*million, {'all':percent_boost(2)}))
menu.add(Upgrade('Walnut cookies', {}, 100*million, {'all':percent_boost(2)}))
menu.add(Upgrade('Cashew cookies', {}, 100*million, {'all':percent_boost(2)}))
menu.add(Upgrade('White chocolate cookies', {}, 500*million, {'all':percent_boost(2)}))
menu.add(Upgrade('Milk chocolate cookies', {}, 500*million, {'all':percent_boost(2)}))

menu.add(Upgrade('Double-chip cookies', {}, 5*billion, {'all':percent_boost(2)}))
menu.add(Upgrade('White chocolate macadamia nut cookies', {}, 10*billion, {'all':percent_boost(2)}))
menu.add(Upgrade('All-chocolate cookies', {}, 50*billion, {'all':percent_boost(2)}))
menu.add(Upgrade('Dark chocolate-coated cookies', {}, 100*billion, {'all':percent_boost(5)}))
menu.add(Upgrade('White chocolate-coated cookies', {}, 100*billion, {'all':percent_boost(5)}))
menu.add(Upgrade('Eclipse cookies', {}, 500*billion, {'all':percent_boost(2)}))

menu.add(Upgrade('Zebra cookies', {}, 1*trillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Snickerdoodles', {}, 5*trillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Stroopwafels', {}, 10*trillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Macaroons', {}, 50*trillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Empire biscuits', {}, 100*trillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Madeleines', {}, 500*trillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Palmiers', {}, 500*trillion, {'all':percent_boost(2)}))

menu.add(Upgrade('Palets', {}, 1*quadrillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Sables', {}, 1*quadrillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Gingerbread men', {}, 10*quadrillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Gingerbread trees', {}, 10*quadrillion, {'all':percent_boost(2)}))
menu.add(Upgrade('Pure black chocolate cookies', {}, 50*quadrillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Pure white chocolate cookies', {}, 50*quadrillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Ladyfingers', {}, 100*quadrillion, {'all':percent_boost(3)}))
menu.add(Upgrade('Tuiles', {}, 500*quadrillion, {'all':percent_boost(3)}))

menu.add(Upgrade('Chocolate-stuffed biscuits', {}, 1*quintillion, {'all':percent_boost(3)}))
menu.add(Upgrade('Checker cookies', {}, 5*quintillion, {'all':percent_boost(3)}))
menu.add(Upgrade('Butter cookies', {}, 10*quintillion, {'all':percent_boost(3)}))
menu.add(Upgrade('Cream cookies', {}, 50*quintillion, {'all':percent_boost(3)}))
menu.add(Upgrade('Gingersnaps', {}, 100*quintillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Cinnamon cookies', {}, 500*quintillion, {'all':percent_boost(4)}))

menu.add(Upgrade('Vanity cookies', {}, 1*sextillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Cigars', {}, 5*sextillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Pinwheel cookies', {}, 10*sextillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Fudge squares', {}, 50*sextillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Shortbread biscuits', {}, 100*sextillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Millionaires` shortbreads', {}, 500*sextillion, {'all':percent_boost(4)}))

menu.add(Upgrade('Caramel cookies', {}, 1*septillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Pecan sandies', {}, 5*septillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Moravian spice cookies', {}, 100*septillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Anzac biscuits', {}, 50*septillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Buttercakes', {}, 100*septillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Ice cream sandwiches', {}, 500*septillion, {'all':percent_boost(4)}))

menu.add(Upgrade('Pink biscuits', {}, 1*octillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Whole-grain cookies', {}, 5*octillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Candy cookies', {}, 10*octillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Big chip cookies  ', {}, 50*octillion, {'all':percent_boost(4)}))
menu.add(Upgrade('One chip cookies', {}, 100*octillion, {'all':percent_boost(1)}))
menu.add(Upgrade('Sprinkles cookies', {}, 500*octillion, {'all':percent_boost(4)}))

menu.add(Upgrade('Peanut butter blossoms', {}, 1*nonillion, {'all':percent_boost(4)}))
menu.add(Upgrade('No-bake cookies', {}, 5*nonillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Florentines', {}, 10*nonillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Chocolate crinkles', {}, 50*nonillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Maple cookies', {}, 100*nonillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Persian rice cookies', {}, 500*nonillion, {'all':percent_boost(4)}))

menu.add(Upgrade('Norwegian cookies', {}, 1*decillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Crispy rice cookies', {}, 5*decillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Ube cookies', {}, 10*decillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Butterscotch cookies', {}, 50*decillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Speculaas', {}, 100*decillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Chocolate oatmeal cookies', {}, 500*decillion, {'all':percent_boost(4)}))

menu.add(Upgrade('Molasses cookies', {}, 1*undecillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Biscotti', {}, 5*undecillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Waffle cookies', {}, 10*undecillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Custard creams', {}, 50*undecillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Bourbon biscuits', {}, 100*undecillion, {'all':percent_boost(4)}))
menu.add(Upgrade('Mini-cookies', {}, 500*undecillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Whoopie pies', {}, 1*duodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Caramel wafer biscuits', {}, 3.162*duodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Chocolate chip mocha cookies', {}, 10*duodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Earl Grey cookies', {}, 31.622*duodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Chai tea cookies', {}, 31.622*duodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Corn syrup cookies', {}, 100*duodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Icebox cookies', {}, 316.227*duodecillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Graham crackers', {}, 1*tredecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Hardtack', {}, 3.162*tredecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Cornflake cookies', {}, 10*tredecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Tofu cookies', {}, 31.622*tredecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Gluten-free cookies', {}, 31.622*tredecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Russian bread cookies', {}, 100*tredecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Lebkuchen', {}, 316.227*tredecillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Aachener Printen', {}, 1*quattuordecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Canistrelli', {}, 3.162*quattuordecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Nice biscuits', {}, 10*quattuordecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('French pure butter cookies', {}, 31.622*quattuordecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Petit beurre', {}, 31.622*quattuordecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Nanaimo bars', {}, 100*quattuordecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Berger cookies', {}, 316.227*quattuordecillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Chinsuko', {}, 1*quindecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Panda koala biscuits', {}, 1*quindecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Putri salju', {}, 3.162*quindecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Milk cookies', {}, 10*quindecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Kruidnoten', {}, 31.622*quindecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Marie biscuits', {}, 100*quindecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Meringue cookies', {}, 316.227*quindecillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Yogurt cookies', {}, 1*sexdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Thumbprint cookies', {}, 3.162*sexdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Pizzelle', {}, 10*sexdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Granola cookies', {}, 31.622*sexdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Ricotta cookies', {}, 100*sexdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Roze koeken', {}, 316.227*sexdecillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Peanut butter cup cookies', {}, 1*septendecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Sesame cookies', {}, 3.162*septendecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Taiyaki', {}, 10*septendecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Vanillekipferl', {}, 31.622*septendecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Battenberg biscuits', {}, 100*septendecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Rosette cookies', {}, 316.227*septendecillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Gangmakers', {}, 1*octodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Welsh cookies', {}, 3.162*octodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Raspberry cheesecake cookies', {}, 10*octodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Bokkenpootjes', {}, 31.622*octodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Fat rascals', {}, 100*octodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Ischler cookies', {}, 316.227*octodecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Matcha cookies', {}, 316.227*octodecillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Dalgona cookies', {}, 1*novemdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Spicy cookies', {}, 3.162*novemdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Smile cookies', {}, 10*novemdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Kolachy cookies', {}, 31.622*novemdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Gomma cookies', {}, 100*novemdecillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Vegan cookies', {}, 316.227*novemdecillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Coyotass', {}, 1*vigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Frosted sugar cookies', {}, 3.162*vigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Marshmallow sandwich cookies', {}, 10*vigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Web cookies', {}, 31.622*vigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Havreflarn', {}, 100*vigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Alfajores', {}, 316.227*vigintillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Gaufrettes', {}, 1*unvigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Cookie bars', {}, 3.162*unvigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Snowball cookies', {}, 10*unvigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Sequilhos', {}, 31.622*unvigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Hazelnut swirlies', {}, 100*unvigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Spritz cookies', {}, 316.227*unvigintillion, {'all':percent_boost(5)}))

menu.add(Upgrade('Mbatata cookies', {}, 1*duovigintillion, {'all':percent_boost(5)}))
menu.add(Upgrade('Springerles', {}, 3.162*duovigintillion, {'all':percent_boost(5)}))