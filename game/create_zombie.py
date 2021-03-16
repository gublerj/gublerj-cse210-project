
from game.point import Point

from game import constants
import arcade
import math

class Create_zombie(arcade.Sprite):
    """This class will allow us to create basic zombies with ease"""

    def __init__(self, sprite, scalling):
        super().__init__(sprite, scalling)

    def update(self):
        """ Move the player """
        self.move_speed = constants.STARTING_PLAYER_MOVEMENT_SPEED
        #self.player_sprite = player_sprite
        #self.follow_player()
    def follow_player(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """
        self.player_sprite = player_sprite
        self.center_x += self.change_x
        self.center_y += self.change_y

        start_x = self.center_x
        start_y = self.center_y

            # Get the destination location for the bullet
        dest_x = self.player_sprite.center_x
        dest_y = self.player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
        self.change_x = math.cos(angle) * self.move_speed
        self.change_y = math.sin(angle) * self.move_speed