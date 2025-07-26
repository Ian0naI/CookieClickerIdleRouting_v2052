from router import Router
import cookie_clicker.categories as cats

g = cats.longhaul(player_cps=20)
r = Router()

game_over = r.route_GPL(g, lookahead=1)

final_time = game_over.completion_time()
final_time_hours = final_time / 60 / 60 

print('Final time: ' + str(final_time_hours))
print(game_over.num_buildings)
