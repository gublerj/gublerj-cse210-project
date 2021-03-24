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
        wall_list = arcade.SpriteList()
        obstical_list = arcade.SpriteList()
        player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", constants.CHARACTER_SCALING)
        player_sprite.center_x = 100
        player_sprite.center_y = 100
        player_list.append(player_sprite)
        bullet_list = arcade.SpriteList()

        #create boarder or walls or boxes
        for y in (0, constants.SCREEN_HEIGHT - constants.SPRITE_SIZE):
        # Loop for each box going across
            for x in range(0, constants.SCREEN_WIDTH, constants.SPRITE_SIZE):
                if (x != constants.SPRITE_SIZE * 4 and x != constants.SPRITE_SIZE * 5) or y == 0:
                    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", constants.CHARACTER_SCALING)
                    wall.left = x
                    wall.bottom = y
                    wall_list.append(wall)

            # Create left and right column of boxes
            for x in (0, constants.SCREEN_WIDTH - constants.SPRITE_SIZE):
                # Loop for each box going across
                for y in range(constants.SPRITE_SIZE, constants.SCREEN_HEIGHT - constants.SPRITE_SIZE, constants.SPRITE_SIZE):
                    # Skip making a block 4 and 5 blocks up on the right side
                    if (y != constants.SPRITE_SIZE * 4 and x != constants.SPRITE_SIZE * 5) or x == 0:
                        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", constants.CHARACTER_SCALING)
                        wall.left = x
                        wall.bottom = y
                        wall_list.append(wall)

        obstical = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", constants.CHARACTER_SCALING)
        obstical.left = 7 * constants.SPRITE_SIZE
        obstical.bottom = 5 *constants.SPRITE_SIZE
        obstical_list.append(obstical)
        wall_list.append(obstical)
        # all sprites contains all of the lists of sprits created by arcade (contains the player list, bullet list and zombie list)
        player_sprites['player'] = [player_list]
        player_sprites['bullet'] = [bullet_list]
        player_sprites['zombie'] = [zombie_list]
        player_sprites['wall'] = [wall_list]
        player_sprites['obsticals'] = [obstical_list]
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


