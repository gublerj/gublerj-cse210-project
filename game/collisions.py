import arcade
import random
from game.create_bullets import Create_bullet
from game import constants

class Collisions:

    def __init__(self):
        self.center_x = None
        self.center_y = None
        self.did_hit = False


    def bullet_zombie_collision(self, player_sprites, zombie_modifier):
        """
        Check for collisions with the bullets and zombies and handle the collision
        called in director in update method
        """
        player = player_sprites['player'][0][0]
        bullet_list = player_sprites['bullet'][0]
        zombie_list = player_sprites['zombie'][0]
        walls = player_sprites['wall'][0]
        zombie_count = zombie_modifier[0]
        move_modifier = zombie_modifier[1]
        zombie_health_modifier = zombie_modifier[2]
        width = constants.SCREEN_WIDTH
        height = constants.SCREEN_HEIGHT
        create_zombies = 0
        for bullet in bullet_list:
            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, zombie_list)
            wall_hit_list = arcade.check_for_collision_with_list(bullet, walls)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            
            if len(wall_hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every zombie that is hit, reduce health of zombie
            for zombie in hit_list:
                zombie.change_x = 0
                zombie.change_y = 0
                zombie.set_hit(True)
                zombie_health = zombie.set_health(player.get_damage())
                # if the zombie dies, check to see if we upgrade the zombie and add a score
                if zombie_health <= 0:
                    zombie.remove_from_sprite_lists()
                    x = random.randint(0, 10)
                    if x == 1:
                        move_modifier = move_modifier * 1.25
                    if x == 2:
                        zombie_count = zombie_count + 1
                    if x == 3:
                        zombie_health_modifier = zombie_health_modifier * 1.15
                    zombie_count = random.randint(0,1)
                    if zombie_count == 1:
                        create_zombies = 2
                    else:
                        create_zombies = 1
                    player.add_score(100)

                    
            # If the bullet flies off-screen, remove it.
            if bullet.bottom > width or bullet.top < 0 or bullet.right < 0 or bullet.left > width:
                bullet.remove_from_sprite_lists()

        zombie_modifier = [zombie_count, move_modifier, zombie_health_modifier]
        return zombie_modifier, create_zombies


    def zombie_player_collision(self, player_sprites):
        """
        When zombie hits player, player loses hp
        """

        player = player_sprites['player'][0]
        player_sprite = player[0]
        zombie_list = player_sprites['zombie'][0]

        #if the player is hit by the zombie reduce the player's health
        for zombie in zombie_list:

            hit_list = arcade.check_for_collision_with_list(zombie, player)

            if len(hit_list) > 0:
                player_sprite.player_damage(zombie.get_damage())
                zombie.set_hit_player()

    def player_upgrade_collision(self, player_sprites, bullet):
        """If the player interacts with an upgrade, give him the upgrade"""
        weapon_list = player_sprites['weapon'][0]
        player_sprite = player_sprites['player'][0]
        player = player_sprites['player'][0][0]
        for weapon in weapon_list:
            hit_list = arcade.check_for_collision_with_list(weapon, player_sprite)

            if len(hit_list) > 0:
                name = weapon.get_name()
                if self.did_hit == False:
                    if name == 'speed':
                        speed = bullet.get_fire_rate()
                        bullet.set_fire_rate(speed - 1)
                    elif name == 'power':
                        power = player.get_damage()
                        player.set_damage(power + 10)
                    self.did_hit = True


                for weapons in weapon_list:
                    weapons.remove_from_sprite_lists()

    def restart(self):
        """restarts the upgrades so that we can get more"""
        self.did_hit = False
            


                