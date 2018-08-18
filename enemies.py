import entity
import config


class Goomba(entity.Entity):
    co = 20

    def __init__(self, x, y):
        entity.Entity.__init__(self, x, y, config.goomba_sprite, Goomba.co+1)
        Goomba.co = Goomba.co + 1
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
