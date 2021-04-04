import arcade
from game.player import Player
from game import constants
from game.upgrade import Upgrade
import random

class Set_up:
    def __init__(self):
        self.condition = 0
        self.wall_list = None
        self.position_1 = 0
        self.position_2 = 0

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

        weapon_list = arcade.SpriteList()
        weapon = arcade.Sprite(':resources:images/space_shooter/laserRed01.png', constants.CHARACTER_SCALING)
        weapon.center_x = 0
        weapon.center_y = 0
        weapon_list.append(weapon)

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
        player_sprites['weapon'] = [weapon_list]
        zombie_count = 1
        zombie_modifiers = [1, .125, 1, 1]
        return player_sprites, zombie_modifiers

    def set_up_new(self, player_sprites, modifiers, level):
        player_sprite = player_sprites['player'][0][0]
        player_list = arcade.SpriteList()
        zombie_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        obstical_list = arcade.SpriteList()
        # player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", constants.CHARACTER_SCALING)
        player_sprite.center_x = constants.SCREEN_WIDTH / 2
        player_sprite.center_y = 100
        player_list.append(player_sprite)
        bullet_list = arcade.SpriteList()
        zombie_count = modifiers[0]
        zombie_speed = modifiers[1]
        zombie_health = modifiers[2]

        weapon_list = arcade.SpriteList()
        weapon = arcade.Sprite(':resources:images/space_shooter/laserRed01.png', constants.CHARACTER_SCALING)
        weapon.center_x = 0
        weapon.center_y = 0
        weapon_list.append(weapon)

        option = random.randint(0,2)
        if option == 0:
            zombie_count = zombie_count + 2
        elif option == 1:
            zombie_speed = zombie_speed * 1.5
            player_sprite.add_modifier(1)
        else:
            zombie_health = zombie_health * 1.25
            player_sprite.add_modifier(1)


        #create boarder or walls or boxes based off of previous position
        for y in (0, constants.SCREEN_HEIGHT - constants.SPRITE_SIZE):
            self.set_up_walls_y_hole(y)
        for x in (0, constants.SCREEN_WIDTH - constants.SPRITE_SIZE):
            self.set_up_walls_x_no_hole(x)

        obstical = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", constants.CHARACTER_SCALING)
        obstical.left = 7 * constants.SPRITE_SIZE
        obstical.bottom = 5 *constants.SPRITE_SIZE
        obstical_list.append(obstical)
        self.wall_list.append(obstical)
        # all sprites contains all of the lists of sprits created by arcade (contains the player list, bullet list and zombie list)
        player_sprites['player'] = [player_list]
        player_sprites['bullet'] = [bullet_list]
        player_sprites['zombie'] = [zombie_list]
        player_sprites['wall'] = [self.wall_list]
        player_sprites['obsticals'] = [obstical_list]
        player_sprites['weapon'] = [weapon_list]
        zombie_modifiers = [zombie_count, zombie_speed, zombie_health]
        return player_sprites, zombie_modifiers

    def upgrade_room(self, player_sprites):
        weapon_list = arcade.SpriteList()
        weapon = Upgrade(':resources:images/space_shooter/laserRed01.png', constants.CHARACTER_SCALING, 'power')
        weapon.center_x = constants.SCREEN_WIDTH / 2 - 5
        weapon.center_y = constants.SCREEN_HEIGHT / 2 - 5
        weapon_list.append(weapon)

        weapon = Upgrade(':resources:images/space_shooter/laserRed01.png', constants.CHARACTER_SCALING, 'power')
        weapon.center_x = constants.SCREEN_WIDTH / 2 + 5
        weapon.center_y = constants.SCREEN_HEIGHT / 2 - 5
        weapon_list.append(weapon)

        weapon = Upgrade(':resources:images/space_shooter/laserRed01.png', constants.CHARACTER_SCALING, 'power')
        weapon.center_x = constants.SCREEN_WIDTH / 2
        weapon.center_y = constants.SCREEN_HEIGHT / 2
        weapon_list.append(weapon)

        weapon = Upgrade(':resources:images/space_shooter/laserRed01.png', constants.CHARACTER_SCALING, 'speed')
        weapon.center_x = constants.SCREEN_WIDTH / 3 - 5
        weapon.center_y = constants.SCREEN_HEIGHT / 2 + 5
        weapon.angle -= 45
        weapon_list.append(weapon)

        weapon = Upgrade(':resources:images/space_shooter/laserRed01.png', constants.CHARACTER_SCALING, 'speed')
        weapon.center_x = constants.SCREEN_WIDTH / 3
        weapon.center_y = constants.SCREEN_HEIGHT / 2
        weapon.angle -= 45
        weapon_list.append(weapon)

        weapon = Upgrade(':resources:images/space_shooter/laserRed01.png', constants.CHARACTER_SCALING, 'speed')
        weapon.center_x = constants.SCREEN_WIDTH / 3 + 5
        weapon.center_y = constants.SCREEN_HEIGHT / 2 - 5
        weapon.angle -= 45
        weapon_list.append(weapon)

        player_sprite = player_sprites['player'][0][0]
        player_list = arcade.SpriteList()
        zombie_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        obstical_list = arcade.SpriteList()
        # player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", constants.CHARACTER_SCALING)
        player_sprite.center_x = constants.SCREEN_WIDTH / 2
        player_sprite.center_y = 100
        player_list.append(player_sprite)
        bullet_list = arcade.SpriteList()

        for y in (0, constants.SCREEN_HEIGHT - constants.SPRITE_SIZE):
            self.set_up_walls_y_hole(y)
        for x in (0, constants.SCREEN_WIDTH - constants.SPRITE_SIZE):
            self.set_up_walls_x_no_hole(x)

        obstical = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", constants.CHARACTER_SCALING)
        obstical.left = 0
        obstical.bottom = 0
        obstical_list.append(obstical)
        self.wall_list.append(obstical)

        player_sprites['weapon'] = [weapon_list]
        player_sprites['wall'] = [self.wall_list]
        player_sprites['obsticals'] = [obstical_list]

        return player_sprites




    def set_up_walls_x_hole(self, x):
        for y in range(constants.SPRITE_SIZE, constants.SCREEN_HEIGHT - constants.SPRITE_SIZE, constants.SPRITE_SIZE):
                # Skip making a block 4 and 5 blocks up on the right side
                    if (y != constants.SPRITE_SIZE * 4 and x != constants.SPRITE_SIZE * 5):
                        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", constants.CHARACTER_SCALING)
                        wall.left = x
                        wall.bottom = y
                        self.wall_list.append(wall)

    def set_up_walls_x_no_hole(self, x):
        for y in range(constants.SPRITE_SIZE, constants.SCREEN_HEIGHT - constants.SPRITE_SIZE, constants.SPRITE_SIZE):
                    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", constants.CHARACTER_SCALING)
                    wall.left = x
                    wall.bottom = y
                    self.wall_list.append(wall)

    def set_up_walls_y_hole(self, y):
        for x in range(0, constants.SCREEN_WIDTH, constants.SPRITE_SIZE):
                if (x != constants.SPRITE_SIZE * 8 and x != constants.SPRITE_SIZE * 7):
                    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", constants.CHARACTER_SCALING)
                    wall.left = x
                    wall.bottom = y
                    self.wall_list.append(wall)

    def set_up_wall_y_no_hole(self, y):
        for x in range(0, constants.SCREEN_WIDTH, constants.SPRITE_SIZE):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", constants.CHARACTER_SCALING)
                wall.left = x
                wall.bottom = y
                self.wall_list.append(wall)



