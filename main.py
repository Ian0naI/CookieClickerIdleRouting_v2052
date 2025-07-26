from router import Router
import cookie_clicker.categories as cats

# 建立遊戲與路由器
g = cats.longhaul(player_cps=20)
r = Router()

# 路由規劃模擬
game_over = r.route_GPL(g, lookahead=1)

# 計算最終完成時間與建築數
final_time = game_over.completion_time()
final_time_hours = final_time / 60 / 60  # 轉換成小時

# 螢幕輸出
print('Final time: ' + str(final_time_hours))
print(game_over.num_buildings)
