import arcade
from game.player import Player
from game import constants
import random

class Set_up:
    def __init__(self):
        pass

    def execute(self, player_sprites, modifiers, level):
        if level == 1:
            self.set_up_start(player_sprites, modifiers)
        else:
            self.set_up_new(player_sprites, modifiers)

    def set_up_start(self, player_sprites, modifiers, level):
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

    def set_up_new(self, all_sprites, modifiers, level):
        player = all_sprites['player'][0][0]
        zombies = all_sprites['zombie'][0]
        player.center_x = constants.SCREEN_WIDTH / 2
        player.center_y = 0
        all_sprites['player'][0][0] = player
        all_sprites['zombie'][0] = zombies
        return all_sprites, modifiers


