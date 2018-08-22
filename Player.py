import entity
import config
import time
import GLOBAL


class Player(entity.Entity):
    def __init__(self, x, y):
        entity.Entity.__init__(self, x, y, config.player_sprite)
        self.is_jumping = False
        self.jumping = 0
        self.health = config.player_health

    def jump(self):
        self.is_jumping = True
        self.mov(self.x, self.y-2)
        self.jumping = 1


    def gravity(self):
        if self.is_jumping and self.jumping != 5:
            self.mov(self.x, self.y-1)
            self.jumping += 1
        elif self.jumping == 5 and self.is_jumping:
            self.is_jumping = False

        if not self.is_jumping:
            self.mov(self.x, self.y+1)
        if self.y == 26:
            self.die()

    def right(self):
        self.mov(self.x+1, self.y)

    def left(self):
        self.mov(self.x-1, self.y)

    def mov(self, x, y):
        self.del_sprite()

        ch = False
        if 0 <= y+2 < config.boardHeight and 0 <= x+2 < config.boardWidth:
            ch = True
            for i in range(len(self.shape_mat)):
                for j in range(len(self.shape_mat[0])):
                    if GLOBAL.board.collision_map[y+i][x+j] == 10:
                        ch = False
                        break

        if ch:
            self.x = x
            self.y = y

        self.copy_sprite()


    def collision(self):
        ch = True
        y = self.y
        for i in range(3):
            for j in range(3):
                a = GLOBAL.board.collision_map[self.y + i][self.x + j]
                if a != 10 and  a != 0 and a < 200:
                    ch = False
                    y = i+self.y
                    code = GLOBAL.board.collision_map[self.y + i][self.x + j]
                    break

            if not ch:
                break

        if not ch:
            if code<0 and code != -200:
                del GLOBAL.coin_list[code]
            elif y > self.y and GLOBAL.level == 1:
                del GLOBAL.enemy_list[code]
            elif y>self.y and GLOBAL.level == 2:
                GLOBAL.boss.health -= 1
                self.mov(self.x-5, self.y)
                self.jump()
            else:
                self.die()
                
    def fire(self):
        temp = entity.Bullet(self.x, self.y+1)
        GLOBAL.bullet_list[temp.code] = temp


    def die(self):  
        self.health-=1        
        if self.health>0:
            self.mov(max(0, self.x-10),0)   
        else:
            self.mov(0,0)
            self.health = config.player_health
        


if __name__ == '__main__':
    player = Player(0, 0)
    while True:
        time.sleep(0.02)
        GLOBAL.board.render(0)
        player.gravity()


