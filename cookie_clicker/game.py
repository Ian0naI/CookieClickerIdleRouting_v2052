import math

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


### Essentially a tuple of name, requirements, purchase price, and effects.
class Upgrade:
  def __init__(self, name, req, price, effects):
    self.name = name
    self.req = req
    self.price = price
    self.effects = effects
  def __hash__(self): return hash(self.name)


### Effects need a priority to be applied in the right order.
### Higher priorities are applied first.  
class Effect:
  def __init__(self, priority, func):
    self.priority = priority
    self.func = func
  def __lt__(self, other): return self.priority < other.priority


### This is the class that actually simulates Cookie Clicker.
class Game:

  price_rate = 1.15

  def __init__(self, version, parent=None):
    if parent is None:
      # Version data.
      self.building_names = list(version.building_names)
      self.base_prices = dict(version.base_prices)
      self.base_rates = dict(version.base_rates)
      self.menu = set(version.menu)
      # Gameplay data.
      self.num_buildings = {name:0 for name in self.building_names}
      self.effects = {name:[] for name in self.building_names}
      self.effects['mouse'] = []
      self.effects['all'] = []
      self.total_cookies = 0
      self.time_elapsed = 0
      self.player_cps = 0
      self.player_delay = 0
      # Speedrun data.
      self.target_cookies = 0
      self.hardcore_mode = False
      self.history = []
    else:
      # Version data from 'parent'.
      # (Disregards 'version' argument entirely.)
      self.building_names = list(parent.building_names)
      self.base_prices = dict(parent.base_prices)
      self.base_rates = dict(parent.base_rates)
      self.menu = set(parent.menu)
      # Gameplay data.
      self.num_buildings = dict(parent.num_buildings)
      self.effects = {name:list(parent.effects[name]) for name in parent.effects}
      self.total_cookies = parent.total_cookies
      self.time_elapsed = parent.time_elapsed
      self.player_cps = parent.player_cps
      self.player_delay = parent.player_delay
      # Speedrun data.
      self.target_cookies = parent.target_cookies
      self.hardcore_mode = parent.hardcore_mode
      self.history = list(parent.history)

  def spack(self, x): return str(x) if len(str(x)) == 1 else '(' + str(x) + ')'
  def __str__(self): 
    data = [self.num_buildings[name] for name in self.building_names]
    return ''.join(self.spack(x) for x in data)
  def __repr__(self): return str(self)



  ### Router required methods

  # Returns current cookies per second.
  def rate(self): return self.building_only_rate() + self.mouse_rate()

  # Prints an informative blurb about the current game state.
  def speak(self):
    last_purchase = self.history[-1]
    if last_purchase in self.building_names:
      last_purchase += ' [' + str(self.num_buildings[last_purchase]) + ']'

    # The list of information we want displayed.
    data = [
      (last_purchase + ' '*24)[:24],
      round(self.time_elapsed / 60, 2), # Print in hours.
      "{:.2e}".format(self.total_cookies),
      "{:.2e}".format(self.rate()),
    ]

    # And just throw it all in one line.
    print('  '.join(str(x) for x in data))
    txt_output='  '.join(str(x) for x in data)
    with open('output.txt', 'a', encoding='utf-8') as f:
      f.write(f"{txt_output},\n")

  # This is just so the router doesn't have to use the word "cookies".
  def currency_produced(self): return self.total_cookies

  # Iterate over possible successive game states.
  def children(self): 
    for name in self.building_names:
      child = Game(version=None, parent=self)
      if not child.purchase_building(name): continue
      yield child
    for upgrade in self.menu:
      child = Game(version=None, parent=self)
      if not child.purchase_upgrade(upgrade): continue
      yield child

  # Returns the final time of this game if played out with no further purchases.
  def completion_time(self):
    if self.total_cookies >= self.target_cookies: 
      return self.time_elapsed
    if not self.rate(): return None
    remaining_cookies = self.target_cookies - self.total_cookies
    return self.time_elapsed + remaining_cookies / self.rate()



  ### Query methods.

  # Returns the cookies per second of single building of a given type.
  def building_rate(self, building_name):
    r = self.base_rates[building_name]
    building_effects = sorted(self.effects[building_name], reverse=True)
    for effect in building_effects: r = effect.func(r, self)
    return r

  # Returns the cookies per second produced by all buildings.
  def building_only_rate(self):
    r = 0

    # Add up each building's rate.
    for name in self.building_names:
      r += self.building_rate(name) * self.num_buildings[name]

    # Then apply any global effects (like kittens).
    for effect in self.effects['all']: r = effect.func(r, self)
    
    return r

  # Returns the cookies per second made by the players clicking.
  def mouse_rate(self):
    r = 1.0
    for effect in self.effects['mouse']: r = effect.func(r, self)
    return r * self.player_cps

  # Returns the current price of a single building of a given type
  def building_price(self, building_name):
    num_building = self.num_buildings[building_name]
    base_price = self.base_prices[building_name]
    return math.ceil(base_price * self.price_rate**num_building)

  # Checks if this game owns certain amounts of some buildings.
  def has_satisfied(self, req):
    for building_name, amount in req.items():
      if self.num_buildings[building_name] < amount: return False
    return True



  ### Gameplay methods.

  # Spends a given amount of cookies. Also updates time and other such.
  # This code is the most heavily commented because it is most suspected
  # of not working.
  def spend(self, price):
    # Make sure we don't overshoot our target.
    if self.total_cookies + price > self.target_cookies: return False
    self.total_cookies += price

    # How long would it take to save up 'price' with just buildings?
    if self.building_only_rate():
      building_only_time = price / self.building_only_rate()
    else:
      building_only_time = None

    # This simulates the loss of cookies during a purchase when you
    # have to take your mouse off the big cookie.
    if building_only_time is None or building_only_time > self.player_delay:
      # This is the case for when the player purchase delay is longer than
      # time it would take to save up for the purchase with only buildings.
      # Ergo, the mouse will provide some amount of clicks towards this
      # purchase.
      shared_mouse_price = price - self.player_delay * self.building_only_rate()
      # The amount of time during saving up for which the mouse and the
      # buildings are both contributing
      mouse_active_time = shared_mouse_price / self.rate()
      self.time_elapsed += mouse_active_time + self.player_delay
    else:
      # This is the case when the purchase is saved up for so quickly, that
      # there's no point in even removing the mouse from the store to 
      # slide it back over to the big cookie.
      self.time_elapsed += building_only_time
    
    return True

  # Purchase a single building of a given type. True if successful.
  def purchase_building(self, building_name):
    price = self.building_price(building_name)
    if not self.spend(price): return False
    self.num_buildings[building_name] += 1
    self.history.append(building_name)
    return True

  # Purchase a given upgrade. True if successful.
  def purchase_upgrade(self, upgrade):
    if self.hardcore_mode: return False
    if not self.has_satisfied(upgrade.req): return False
    if not self.spend(upgrade.price): return False
    for building_name, effect in upgrade.effects.items():
      self.effects[building_name].append(effect)
    self.history.append(upgrade.name)
    self.menu.remove(upgrade)
    return True
