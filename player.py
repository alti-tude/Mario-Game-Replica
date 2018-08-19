import entity
import config
import time
import GLOBAL


class Player(entity.Entity):
    def __init__(self, x, y):
        entity.Entity.__init__(self, x, y, config.player_sprite)
        self.is_jumping = False
        self.jumping = 0


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

    def right(self):
        self.mov(self.x+1, self.y)

    def left(self):
        self.mov(self.x-1, self.y)

    def collision(self):
        ch = True
        y = self.y
        for i in range(3):
            for j in range(3):
                if GLOBAL.board.collision_map[self.y + i][self.x + j] > 10:
                    ch = False
                    y = i+self.y
                    code = GLOBAL.board.collision_map[self.y + i][self.x + j]
                    break

            if not ch:
                break

        if not ch:
            if y > self.y:
                GLOBAL.enemy_list[code].del_sprite()
                del GLOBAL.enemy_list[code]
            else:
                self.die()


    def die(self):
        self.mov(max(0, self.x-10),0)   
        pass


if __name__ == '__main__':
    player = Player(0, 0)
    while True:
        time.sleep(0.02)
        GLOBAL.board.render(0)
        player.gravity()


