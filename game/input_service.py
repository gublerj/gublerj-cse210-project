import arcade
import math
import random

class Input_service:
    
    def __init__(self):
        pass

    def on_release(self, key, modifiers, player_sprites):
        player_sprite = player_sprites["player"][0][0]
        if key == arcade.key.UP or key == arcade.key.W:
            player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            player_sprite.change_x = 0
        return player_sprite

    def on_press(self, key, modifiers, player_sprites, movement_speed):
        player_sprite = player_sprites["player"][0][0]
        if key == arcade.key.UP or key == arcade.key.W:
            player_sprite.change_y = movement_speed
        elif key == arcade.key.DOWN or key == arcade.key.S:
            player_sprite.change_y = -movement_speed
        elif key == arcade.key.LEFT or key == arcade.key.A:
            player_sprite.change_x = -movement_speed
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            player_sprite.change_x = movement_speed
        return player_sprite


    def on_click(self, x, y, button, modifiers, player_sprites, BULLET_SPEED, SPRITE_SCALING_LASER):
        """ Called whenever the mouse button is clicked. """
        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

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
        dest_x = x
        dest_y = y

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
        bullet.change_x = (math.cos(angle)) * BULLET_SPEED
        bullet.change_y = (math.sin(angle)) * BULLET_SPEED

        # Add the bullet to the appropriate lists
        bullet_list.append(bullet)
        player_sprites['bullet'] = [bullet_list]

        return player_sprites

        
