import arcade
import math
from game import constants

class Create_bullet:

    def __init__(self):
        self.fire = False
        self.x = 0
        self.y = 0
        self.fire_rate = 10
        self.cooldown = self.fire_rate

    def make_bullet(self, player_sprites):
        """work"""
        if self.fire == True:
            if self.cooldown == 0:
                # Create a bullet
                bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", constants.SPRITE_SCALING_LASER)

                player_sprite = player_sprites["player"][0][0]
                bullet_list = player_sprites['bullet'][0]
                # Position the bullet at the player's current location
                start_x = player_sprite.center_x
                start_y = player_sprite.center_y
                bullet.center_x = start_x
                bullet.center_y = start_y

                # Get from the mouse the destination location for the bullet
                # IMPORTANT! If you have a scrolling screen, you will also need
                # to add in self.view_bottom and self.view_left.
                dest_x = self.x
                dest_y = self.y

                # Do math to calculate how to get the bullet to the destination.
                # Calculation the angle in radians between the start points
                # and end points. This is the angle the bullet will travel.
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

                # Angle the bullet sprite so it doesn't look like it is flying
                # sideways.
                bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet.change_x = (math.cos(angle)) * constants.BULLET_SPEED
                bullet.change_y = (math.sin(angle)) * constants.BULLET_SPEED

                # Add the bullet to the appropriate lists
                bullet_list.append(bullet)
                player_sprites['bullet'] = [bullet_list]
                self.cooldown = self.fire_rate
            else:
                self.cooldown -= 1

        return player_sprites

    def start_shooting(self):
        self.fire = True

    def cease_fire(self):
        self.fire = False

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_fire_rate(self, fire_rate):
        self.fire_rate = fire_rate

    def get_fire_rate(self):
        return self.fire_rate
