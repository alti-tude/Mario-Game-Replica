import entity
import config
import time
import GLOBAL

class Player(entity.Entity):
    def __init__(self, x, y):
        entity.Entity.__init__(self, x, y, config.player_sprite, 1)

    def jump(self):
        if self.y-3 != 0:
            self.mov(self.x, self.y-3)

    def right(self):
        self.mov(self.x+3, self.y)

    def left(self):
        self.mov(self.x-3, self.y)


if __name__ == '__main__':
    player = Player(0, 0)
    while True:
        time.sleep(0.02)
        GLOBAL.board.render(0)
        player.gravity()


