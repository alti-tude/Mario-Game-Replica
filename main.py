import GLOBAL
import player
import build_level
import config
import threading
import time
import input    

build_level.gen_level()
build_level.gen_decor()
build_level.gen_enemies()

player = player.Player(0,0)


while True:
    time.sleep(config.tick_size)
    player.gravity()
    player.collision()
    for j in GLOBAL.enemy_list:
        GLOBAL.enemy_list[j].next()
        GLOBAL.enemy_list[j].gravity()
    a = input.get_input()
    
    if a == 'a':
        player.left()
    elif a == 'd':
        player.right()
    elif a == 'w' and GLOBAL.board.collision_map[player.y+3][player.x] == 10:
        player.jump()
    elif a == 'q':
        break

    GLOBAL.board.render(max(0, player.x-50))
    


