
from game import constants
from game.point import Point
import arcade

class Player(arcade.Sprite):
    
    def __init__(self, sprite, scalling):
        super().__init__(sprite, scalling)
        #self._sprite = sprite
        #self.set_sprite(self._sprite)
        #self.set_position(constants.SCREEN_WIDTH / 2, 100)
        


    def update(self):
        """ Move the player """
        self.SCREEN_HEIGHT = constants.SCREEN_HEIGHT
        self.SCREEN_WIDTH = constants.SCREEN_WIDTH
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y
        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > self.SCREEN_WIDTH - 1:
            self.right = self.SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > self.SCREEN_HEIGHT - 1:
            self.top = self.SCREEN_HEIGHT - 1

