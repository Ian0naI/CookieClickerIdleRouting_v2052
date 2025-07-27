from router import Router
import cookie_clicker.categories as cats

g = cats.longhaul(player_cps=20) #choose a def in categories.py
r = Router()

game_over = r.route_GPL(g, lookahead=1)

final_time = game_over.completion_time()
final_time_hours = final_time / 60 / 60 

print('Final time: ' + str(final_time_hours))
print(game_over.num_buildings)

txt_output1='Final time: ' + str(final_time_hours)
txt_output2=game_over.num_buildings
with open('output.txt', 'a', encoding='utf-8') as f:
    f.write(f"{txt_output1},\n,{txt_output2}")
