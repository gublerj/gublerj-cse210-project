from arcade import check_for_collision_with_list
from game import constants
import arcade

class Collisions():

    def __init__(self):
        self.center_x = None
        self.center_y = None
        pass


    def bullet_player_collision(self, player_sprites):
        
        for i in player_sprites["bullet"]:
            if player_sprites["zombie"][0][0]._position == i._position:
                # pop zombie
                pass

    def zombie_player_collision(self, player_sprites, player_health, actors):
        """
        When zombie hits player, player loses hp
        """

        player = player_sprites["player"][0]
        player_sprite = player[0]
        zombies = player_sprites["zombie"][0]

        for zombie in zombies:

            hit_list = arcade.check_for_collision_with_list(player_sprite, zombie)

            if len(hit_list) > 0:
                player_sprites.player_damage(zombie.get_damage())