import arcade
import random
from game import constants

class Collisions:

    def __init__(self):
        pass


    def bullet_zombie_collision(self, player_sprites, zombie_modifier):
        """
        Check for collisions with the bullets and zombies and handle the collision
        """
        bullet_list = player_sprites['bullet'][0]
        zombie_list = player_sprites['zombie'][0]
        zombie_count = zombie_modifier[0]
        move_modifier = zombie_modifier[1]
        zombie_health_modifier = zombie_modifier[2]
        width = constants.SCREEN_WIDTH
        height = constants.SCREEN_HEIGHT
        for bullet in bullet_list:
            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, zombie_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for zombie in hit_list:
                zombie.change_x = 0
                zombie.change_y = 0
                zombie.set_hit(True)
                zombie_health = zombie.set_health(10)
                if zombie_health <= 0:
                    zombie.remove_from_sprite_lists()
                    x = random.randint(0, 10)
                    if x == 1:
                        move_modifier = move_modifier * 1.25
                    if x == 2:
                        zombie_count = zombie_count + 1
                    if x == 3:
                        zombie_health_modifier = zombie_health_modifier * 1.15
                    
            # If the bullet flies off-screen, remove it.
            if bullet.bottom > width or bullet.top < 0 or bullet.right < 0 or bullet.left > width:
                bullet.remove_from_sprite_lists()

        zombie_modifier = [zombie_count, move_modifier, zombie_health_modifier]
        return zombie_modifier



