from game.actor import Actor
from game import constants
from game.point import Point

class Player(Actor):
    
    def __init__(self, sprite):
        super().__init__()
        self._sprite = sprite
        self.set_sprite(self._sprite)
        self.set_position(Point(constants.SCREEN_WIDTH / 2, 10))

