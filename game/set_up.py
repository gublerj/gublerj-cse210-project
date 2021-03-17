import arcade
from game.player import Player
from game import constants

class Set_up:
    def __init__(self):
        pass

    def set_up_start(self, player_sprites, modifiers):
        # Create the Sprite lists
        player_list = arcade.SpriteList()
        zombie_list = arcade.SpriteList()
        player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", constants.CHARACTER_SCALING)
        player_sprite.center_x = 50
        player_sprite.center_y = 50
        player_list.append(player_sprite)
        bullet_list = arcade.SpriteList()
        # all sprites contains all of the lists of sprits created by arcade (contains the player list, bullet list and zombie list)
        player_sprites['player'] = [player_list]
        player_sprites['bullet'] = [bullet_list]
        player_sprites['zombie'] = [zombie_list]
        zombie_count = 1
        zombie_modifiers = [1, .125, 1]
        return player_sprites, zombie_modifiers