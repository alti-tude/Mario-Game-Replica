import entity
import config
import GLOBAL
import random


class Enemy(entity.Entity):
    code = 20

    def __init__(self, x, y, sprite):
        entity.Entity.__init__(self, x, y, sprite, Enemy.code)
        self.code = Enemy.code
        Enemy.code+=1 
        

class Goomba(Enemy):
   
    def __init__(self, x, y):
        Enemy.__init__(self, x,y,config.goomba_sprite)
        self.direction = 'L'

    def next(self):
        if self.direction == 'L':
            oldx = self.x
            oldy = self.y
            self.mov(self.x-1, self.y)
            if oldx == self.x and oldy == self.y:
                self.direction = 'R'

        if self.direction == 'R':
            oldx = self.x
            oldy = self.y
            self.mov(self.x + 1, self.y)
            if oldx == self.x and oldy == self.y:
                self.direction = 'L'
 
    def __del__(self):
        self.del_sprite()
        GLOBAL.points += config.goomba_points


class FastRoomba(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x,y,config.fastroomba_sprite)
    
    def next(self):
        if abs(GLOBAL.player.x - self.x) > config.dispWidth/4:
            return

        if GLOBAL.player.x < self.x:
            oldx = self.x
            self.mov(self.x - 1, self.y)
            if oldx == self.x:
                if GLOBAL.board.collision_map[self.y-1][self.x] == 0:
                    self.mov(self.x-1, self.y-5)
        
        elif GLOBAL.player.x > self.x:
            oldx = self.x
            self.mov(self.x + 1, self.y)
            if oldx == self.x:
                if GLOBAL.board.collision_map[self.y-1][self.x] == 0:
                    self.mov(self.x+1, self.y-5)
        
        else:
            a = random.randint(0, 1)
            if a==0:
                self.mov(self.x+1, self.y)
            else:
                self.mov(self.x-1, self.y)   
    
    def __del__(self):
        self.del_sprite()
        GLOBAL.points += config.fastroomba_points


class Boss(entity.Entity):
    
    def __init__(self, x,y):
        entity.Entity.__init__(self,x, y, config.boss_sprite, -200)
        self.health = 10
        self.ap_countdown = 76
        self.disap_countdown = 0
        self.f='a'
        self.dead = False
        self.code = -200

    def next(self):
        
        if self.f=='d' and not self.dead:
            a = random.randint(0, config.boardWidth-1)
            b = random.randint(0, config.boardHeight-1)
            self.mov(a,b)
            self.disap_countdown-=1
            self.ap_countdown+=2
            self.del_sprite()
            if self.disap_countdown == 0:
                self.f='a'

        else:
            if GLOBAL.player.x < self.x:
                oldx = self.x
                self.mov(self.x - 1, self.y)
                if oldx == self.x:
                    if GLOBAL.board.collision_map[self.y-1][self.x] == 0:
                        self.mov(self.x-1, self.y-5)
        
            elif GLOBAL.player.x > self.x:
                oldx = self.x
                self.mov(self.x + 1, self.y)
                if oldx == self.x:
                    if GLOBAL.board.collision_map[self.y-1][self.x] == 0:
                        self.mov(self.x+1, self.y-5)
            self.ap_countdown-=1
            self.disap_countdown+=0.5
            self.copy_sprite()
            if self.ap_countdown == 0:
                self.f = 'd'

if __name__=='__main__':
    for i in range(100):
        a = FastRoomba(0,0)
        del a