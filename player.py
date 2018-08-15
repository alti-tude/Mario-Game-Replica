import entity
import config
import time
import GLOBAL


class Player(entity.Entity):
    def __init__(self, x, y):
        entity.Entity.__init__(self, x, y, config.player_sprite, 1)

    def jump(self):
        if self.y-7 != 0:
            self.mov(self.x, self.y-7)

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
                    goomba_code = GLOBAL.board.collision_map[self.y + i][self.x + j]
                    break

        if not ch:
            if y > self.y:
                del GLOBAL.enemy_list[goomba_code]
            else:
                self.die()

    def die(self):
        pass


if __name__ == '__main__':
    player = Player(0, 0)
    while True:
        time.sleep(0.02)
        GLOBAL.board.render(0)
        player.gravity()


