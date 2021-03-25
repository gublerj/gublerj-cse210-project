
from game import constants
import arcade

class Player(arcade.Sprite):
    
    def __init__(self, sprite, scaling):
        super().__init__(sprite, scaling)
        self.player_health = 10
        self.end = False
        self.restart = False
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
            self.end = True
        elif self.right > self.SCREEN_WIDTH - 1:
            self.right = self.SCREEN_WIDTH - 1
            self.end = True

        if self.bottom < 0:
            self.bottom = 0
            self.end = True
        elif self.top > self.SCREEN_HEIGHT - 1:
            self.top = self.SCREEN_HEIGHT - 1
            self.end = True
        if self.restart == True:
            self.end = False
            self.restart = False




    def player_damage(self, damage):
        """
        When zombie hits player, the player loses health
        """

        self.player_health -= damage

    def get_health(self):
        """
        Returns how much health the player has
        """
        
        return self.player_health

    def end_point(self):
        return self.end

    def end_restart(self):
        self.restart = True
