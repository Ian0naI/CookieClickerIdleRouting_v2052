from cookie_clicker.game import Game
from cookie_clicker.versions import v2048, v2031, v10466, v10466_xmas, v2052

million = 10**6
billion = 10**9
trillion = 10**12


# The generic speedrun to 1 million cookies baked.
def fledgling(version=v2031, player_cps=8, player_delay=1):
  game = Game(version)
  game.target_cookies = 1*million
  game.player_cps = player_cps
  game.player_delay = player_delay

  # Buy a cursor to unlock the mouse/cursor upgrades. The router is short-sighted.
  for _ in range(10): game.purchase_building('Cursor')

  return game


# Bake 1 million cookies while only clicking the big cookie by hand 15 times.
def neverclick(version=v2031, player_cps=0, player_delay=0):
  game = Game(version)
  game.target_cookies = 1*million
  game.player_cps = player_cps
  game.player_delay = player_delay

  # Simulate a single cursor purchase.
  # These initial values match up exactly with DHA's spreadsheets.
  game.num_buildings['Cursor'] = 1
  game.total_cookies = 15
  game.time_elapsed = 1.2

  return game


# Bake 1 trillion cookies with no upgrades.
def hardcore(version=v2048, player_cps=8, player_delay=1):
  game = Game(version)
  game.target_cookies = 1*billion
  game.player_cps = player_cps
  game.player_delay = player_delay
  game.hardcore_mode = True
  return game


# To 40 achievements. We just aim for a large amount of cookies
# and assume that will be enough to get 40.
def forty(version=v10466, player_cps=8, player_delay=1):
  game = Game(version)
  game.target_cookies = 30*million
  game.player_cps = player_cps
  game.player_delay = player_delay

  # Buy a cursor to unlock the mouse/cursor upgrades. The router is short-sighted.
  game.purchase_building('Cursor')

  return game


# The 40 achievement run but in holiday mode. Christmas is fastest.
def forty_holiday(version=v10466_xmas, player_cps=8, player_delay=1):
  game = Game(version)
  game.target_cookies = 4*million
  game.player_cps = player_cps
  game.player_delay = player_delay

  # We buy a few santa upgrades before doing anything else to ensure we get at 
  # least 2 or 3 good upgrades. The time loss is worth the good rng.11
  game.total_cookies = 60
  game.time_elapsed = 15

  # Buy a cursor to unlock the mouse/cursor upgrades. The router is short-sighted.
  game.purchase_building('Cursor')

  return game

# A short speedrun for testing purposes.
def short(version=v2031, player_cps=8, player_delay=1):
  game = Game(version)
  game.target_cookies = 1000
  game.player_cps = player_cps
  game.player_delay = player_delay
  return game

# Route to the first optimal ascension for long-term playthrough.
def longhaul(version=v2048, player_cps=20, player_delay=0.01):
  game = Game(version)
  game.target_cookies = 1000 * v2048.unvigintillion
  game.player_cps = player_cps
  game.player_delay = player_delay
  game.purchase_building('Cursor')
  return game
