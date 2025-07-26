class Router:

  # Brute-forces the optimal playthrough of 'game' with depth-first-search.
  def route_DFS(self, game):
    return game
  
  # Finds a decent playthrough of 'game' by minimizing payoff load locally.
  def route_GPL(self, game, lookahead=1):
    num_moves = 0
    while True:
      child = self.GPL_child(game, generation=lookahead)
      if child is None: break
      game = child
      num_moves += 1
      game.speak()
      if num_moves % 10 == 0: print(' ')
    return game

  # Returns the child of 'game' with the lowest payoff load.
  # (an easy heuristic giving locally optimal routing in simple cases)
  def GPL_child(self, game, generation=1):
    game_rate = game.rate() # Calculate this once to save computer power.
    best_child = best_pl = None
    for child in game.children():
      best_descendant_pl = None
      for descendant in self.descendants(child, generation-1):
        # What changed from 'game' to this descendant?
        time_change = descendant.time_elapsed - game.time_elapsed
        rate_change = descendant.rate() - game_rate
        # Make sure the CpS actually went up.
        if rate_change == 0: continue
        # Payoff load calculation.
        price = game_rate * time_change
        #price = child.currency_produced() - game.currency_produced()
        payoff_load = price * (1 + game_rate / rate_change)
        # Record the best descendant of this 'child'.
        if best_descendant_pl is None or payoff_load < best_descendant_pl:
          best_descendant_pl = payoff_load
      # If there were no descendants just move on to the next child.
      if best_descendant_pl is None: continue
      # Record the child with the best descendant.
      if best_pl is None or best_descendant_pl < best_pl:
        best_child = child
        best_pl = best_descendant_pl
    return best_child

  # Macro for Game's "children" method.
  # Yields all descendants of a game object of a given generation.
  # Recursive.
  def descendants(self, game, generation=1):
    # Generation 0 just means return the game that was passed in.
    if generation == 0:
      yield game
      return
    # Recursive call. Call "descendants" on game's children.
    for child in game.children():
      for descendant in self.descendants(child, generation-1):
        yield descendant