"""
Platformer Game
"""
import arcade
from game import constants
from game.player import Player
from game.output_service import Output_service
from game.create_zombie import Create_zombie


class Director(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        """
        initialized the Director
        """
        #import the constants and all classes that are going to be used
        self.SCREEN_HEIGHT = constants.SCREEN_HEIGHT
        self.SCREEN_WIDTH = constants.SCREEN_WIDTH
        self.SCREEN_TITLE = constants.SCREEN_TITLE
        self.CHARACTER_SCALING = constants.CHARACTER_SCALING
        self.player_movement_speed = constants.STARTING_PLAYER_MOVEMENT_SPEED
        self.output_service = Output_service()
        self.create_zombie = None
        self.player = None
        self.all_sprites = {}


        # Call the parent class and set up the window
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.player_list = None
        self.zombie_list = None
        self.zombie_image = constants.zombie_image


        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.zombie_list = arcade.SpriteList()
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", self.CHARACTER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.output_service.execute(self.player_list, self.zombie_list)
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = self.player_movement_speed
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -self.player_movement_speed
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -self.player_movement_speed
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = self.player_movement_speed

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
            
    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_list.update()

        

    def create_zombies(self):
        """ creates a zombie when needed"""
        for x in range(1):
            zombie_sprite = Create_zombie(self.zombie_image, self.CHARACTER_SCALING)
            zombie_sprite.center_x = self.SCREEN_WIDTH / 2
            zombie_sprite.center_y = self.SCREEN_HEIGHT - 50
            self.zombie_list.append(zombie_sprite)

            #zombie = Create_zombie()
            #zombie_sprite = arcade.Sprite(zombie.get_sprite(), self.CHARACTER_SCALING)
            #zombie_position = zombie.get_position()
            #zombie_sprite.center_x = zombie_position.get_x()
            #zombie_sprite.center_y = zombie_position.get_y()
            #self.zombie_list.append(zombie_sprite)


    def execute(self):
        """ Main method """
        self.setup()
        self.create_zombies()
        arcade.run()