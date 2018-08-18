import GLOBAL
import player
import build_level
import config
import threading
import time
import input    

build_level.gen_level()
build_level.gen_decor()
# build_level.gen_enemies()

player = player.Player(0,0)

# t = threading.Thread(target=input.startIp, args=())
# t.start()
# q = GLOBAL.q
while True:
    time.sleep(config.tick_size)
    player.gravity()
    a = input.get_input()
    
    if a == 'a':
        player.mov(player.x-1, player.y) 
    elif a == 'd':
        player.mov(player.x+1, player.y)

    GLOBAL.board.render(0)
    


