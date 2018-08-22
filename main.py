import GLOBAL
import Player
import build_level
import config
import threading
import time
import input    

f = 0
for level in range(1,3):
    if f==1:
        break
    GLOBAL.level=level
    # level = 2
    if level==1:
        build_level.gen_level()
        build_level.gen_collectibles()
        build_level.gen_enemies()
        build_level.gen_decor()
    else:
        config.boardWidth = config.dispWidth
        build_level.gen_level()
        GLOBAL.enemy_list[GLOBAL.boss.code] = GLOBAL.boss
        GLOBAL.boss.copy_sprite()

    player = GLOBAL.player


    while True:
        time.sleep(config.tick_size)
        player.gravity()
        player.collision()
        for j in GLOBAL.enemy_list:
            GLOBAL.enemy_list[j].gravity()
            GLOBAL.enemy_list[j].next()

        if level == 2:
            to_del=[]
            for j in GLOBAL.bullet_list:
                oldx = GLOBAL.bullet_list[j].x
                GLOBAL.bullet_list[j].next()
                # GLOBAL.bullet_list[j].collision()

                if oldx == GLOBAL.bullet_list[j].x:
                    to_del.append(j)
            
            for j in to_del:
                del GLOBAL.bullet_list[j]

        a = input.get_input()
        GLOBAL.board.header["points"]=GLOBAL.points
        GLOBAL.board.header["health"]=player.health 
        b = int(player.x/config.boardWidth*100)
        GLOBAL.board.header["progress"]='['+"\033[31m#\033[39m"*+b+"-"*(100-b)+']'
        GLOBAL.board.header["boss health"]=GLOBAL.boss.health

        if player.x >= config.boardWidth-(config.dispWidth)/2 and level!=2:
            fin_score = GLOBAL.points
            print("final score: "+str(fin_score))
            print("loading next level")
            time.sleep(3)
            GLOBAL.enemy_list.clear()
            GLOBAL.coin_list.clear()
            del player
            del GLOBAL.board
            GLOBAL.init()
            GLOBAL.points = fin_score
            break

        if a == 'a':
            player.left()
        elif a == 'd':
            player.right()
        elif a == 'w' and GLOBAL.board.collision_map[player.y+3][player.x] == 10:
            player.jump()
        elif a == 'q':
            f = 1
            break
        elif a == 'x' and level ==2:
            player.fire()

        GLOBAL.board.render(min(max(0, player.x-50), config.boardWidth - config.dispWidth))
        if GLOBAL.boss.health <= 0:
            print("you win")
            break




