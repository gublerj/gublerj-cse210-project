"""
Platformer Game
"""
import arcade
import math
import random
from game import constants
from game.player import Player
from game.output_service import Output_service
from game.create_zombie import Create_zombie
from game.input_service import Input_service
from game.collisions import Collisions
from game.set_up import Set_up
from game.game_over import GameOverView
from game.create_bullets import Create_bullet


class Director(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """
        initialized the Director
        """
        #import the constants
        self.SCREEN_HEIGHT = constants.SCREEN_HEIGHT
        self.SCREEN_WIDTH = constants.SCREEN_WIDTH
        self.SCREEN_TITLE = constants.SCREEN_TITLE
        self.CHARACTER_SCALING = constants.CHARACTER_SCALING
        self.SPRITE_SCALING_LASER = constants.SPRITE_SCALING_LASER
        self.BULLET_SPEED = constants.BULLET_SPEED
        self.player_movement_speed = constants.STARTING_PLAYER_MOVEMENT_SPEED
        self.zombie_image = constants.zombie_image

        #imports classes
        self.output_service = Output_service()
        self.input_service = Input_service()
        self.collision = Collisions()
        self.set_up = Set_up()
        self.bullets = Create_bullet()

        #creats variables that will be used
        self.level = 1
        self.room = 0
        #60 = 1 sec
        self.total_time = 600
        #zombie modifiers contains a list used to change zombie stats so that we can make them better the farther we go
        #1 = number of zombies, .125 is a speed modifier
        self.zombie_modifiers = []
        self.zombie_base_modifiers = [1,1.25,1, 1]
        self.create_new_zombie = 0
        self.all_sprites = {}
        self.new_round = True


        # Call the parent class and set up the window
        #super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
        super().__init__()

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.player_list = None
        self.zombie_list = None
        self.bullet_list = None
        self.weapon_list = None
        self.create_zombie = None
        self.player = None
        self.player_sprite = None

        #sets up the first level
        self.all_sprites, self.zombie_base_modifiers = self.set_up.set_up_start(self.all_sprites, self.zombie_base_modifiers, self.level)
        self.player_list = self.all_sprites['player'][0]
        self.zombie_list = self.all_sprites['zombie'][0]
        self.bullet_list = self.all_sprites['bullet'][0]
        self.wall_list = self.all_sprites['wall'][0]
        self.obstical_list = self.all_sprites['obsticals'][0]
        self.weapon_list = self.all_sprites['weapon'][0]
        self.player = self.player_list[0]
        self.zombie_modifiers = self.zombie_base_modifiers

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        #determis if the room is an upgrade room or a level
        if self.room % 2 == 0:
            self.all_sprites = self.set_up.upgrade_room(self.all_sprites)
        else:
            self.all_sprites, self.zombie_base_modifiers = self.set_up.set_up_new(self.all_sprites, self.zombie_base_modifiers, self.level)
            self.level = self.level + 1
            self.new_round = True
            self.player.end_restart()
            self.collision.restart()
        # reassigns the lists and variables that change from level to lever or that are reset
        self.player_list = self.all_sprites['player'][0]
        self.zombie_list = self.all_sprites['zombie'][0]
        self.bullet_list = self.all_sprites['bullet'][0]
        self.player = self.player_list[0]
        self.zombie_modifiers = self.zombie_base_modifiers
        self.room = self.room + 1

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.output_service.execute(self.all_sprites)
        #self.bullet_list.draw()
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        self.player_sprites = self.input_service.on_press(key, modifiers, self.all_sprites, self.player_movement_speed)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        self.player_sprite = self.input_service.on_release(key, modifiers, self.all_sprites)


    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse button is clicked. """
        self.bullets.start_shooting()
        #self.all_sprites = self.input_service.on_click(x, y, button, modifiers, self.all_sprites, self.BULLET_SPEED, self.SPRITE_SCALING_LASER)

    def on_mouse_release(self, x, y, button, modifiers):
        """called whenever teh mouse button is realeased"""
        self.bullets.cease_fire()

    def on_mouse_motion(self, x, y, dx, dy):
        """updates as the mouse moves accross the screen"""
        self.bullets.set_x(x)
        self.bullets.set_y(y)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player.player_animation()

        # resets  the timer for the round
        if self.new_round == True:
            self.total_time = 600 + (30 * self.level)
        
        #updates the individual lists
        self.player_list.update()
        self.zombie_list.update()
        self.bullet_list.update()
        for zombie in self.zombie_list:
            zombie.follow_player(self.all_sprites)
            zombie.zombie_animation()


        #creates the bullets from the player
        self.bullets.make_bullet(self.all_sprites)

        #check for collisions
        self.zombie_modifiers, self.create_new_zombie = self.collision.bullet_zombie_collision(self.all_sprites, self.zombie_modifiers)
        self.collision.zombie_player_collision(self.all_sprites)
        self.collision.player_upgrade_collision(self.all_sprites, self.bullets)

        #creates and updates physics engines
        self.PhysicsEngineSimple = arcade.PhysicsEngineSimple(self.all_sprites['player'][0][0], self.all_sprites['zombie'][0])
        self.PhysicsEngineSimple_2 = arcade.PhysicsEngineSimple(self.all_sprites['player'][0][0], self.all_sprites['wall'][0])
        for zombie in self.all_sprites['zombie'][0]:
            physics = arcade.PhysicsEngineSimple(zombie, self.all_sprites['obsticals'][0])
            physics.update()
        self.PhysicsEngineSimple.update()
        self.PhysicsEngineSimple_2.update()
        
        if self.total_time <= 0:
            self.create_new_zombie = 0
            if len(self.all_sprites['zombie'][0]) == 0:
                end = False
                if self.player.end_point() == True:
                    self.player.end_restart()
                    self.setup()
        self.create_zombies()
        if self.player_list[0].get_health() <= 0:
            game_over = GameOverView(self.player.get_score())
            self.window.show_view(game_over)
        self.total_time = self.total_time - 1

    def create_zombies(self):
        """ creates a zombie when needed"""
        if self.new_round == True:
            for x in range(self.zombie_modifiers[0]):
                zombie_sprite = Create_zombie(self.zombie_image, self.CHARACTER_SCALING, self.zombie_modifiers)
                zombie_sprite.center_x = random.randint(0, self.SCREEN_WIDTH)
                zombie_sprite.center_y = random.randint(0, self.SCREEN_HEIGHT)
                self.zombie_list.append(zombie_sprite)
                self.new_round = False
                self.total_time = 600
        if self.create_new_zombie != 0:
            for x in range(0, self.create_new_zombie):
                zombie_sprite = Create_zombie(self.zombie_image, self.CHARACTER_SCALING, self.zombie_modifiers)
                location = random.randint(1,4)
                if location == 1:
                    zombie_sprite.center_x = random.randint(0, self.SCREEN_WIDTH)
                    zombie_sprite.center_y = 0
                if location == 2:
                    zombie_sprite.center_x = 0
                    zombie_sprite.center_y = random.randint(0, self.SCREEN_HEIGHT)
                if location == 3:
                    zombie_sprite.center_x = self.SCREEN_WIDTH
                    zombie_sprite.center_y = random.randint(0, self.SCREEN_HEIGHT)
                if location == 4:
                    zombie_sprite.center_x = random.randint(0, self.SCREEN_WIDTH)
                    zombie_sprite.center_y = self.SCREEN_HEIGHT
                
                self.zombie_list.append(zombie_sprite)
        self.all_sprites["zombie"] = [self.zombie_list]

    def execute(self):
        """ Main method """
        self.setup()
        self.create_zombies()
        arcade.run()