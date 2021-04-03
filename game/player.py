
from game import constants
import arcade

class Player(arcade.Sprite):
    
    def __init__(self, sprite, scaling):
        super().__init__(sprite, scaling)
        self.player_health = 10
        self.max_health = self.player_health
        self.score = 0
        self.end = False
        self.restart = False
        self.damage = 10
        self.character_face_direction = constants.RIGHT_FACING
        self.cur_texture = 0
        self.scale = constants.CHARACTER_SCALING
        self.main_path = ":resources:images/animated_characters/female_person/femalePerson"
        self.idle_texture_pair = self.load_texture_pair(f"{self.main_path}_idle.png")

        self.walk_textures = []
        for i in range(8):
            texture = self.load_texture_pair(f"{self.main_path}_walk{i}.png")
            self.walk_textures.append(texture)

        self.score_modifier = 0

        #self._sprite = sprite
        #self.set_sprite(self._sprite)
        #self.set_position(constants.SCREEN_WIDTH / 2, 100)


    def update(self):
        """ Move the player """
        self.SCREEN_HEIGHT = constants.SCREEN_HEIGHT
        self.SCREEN_WIDTH = constants.SCREEN_WIDTH
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y
        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
            self.end = True
        elif self.right > self.SCREEN_WIDTH - 1:
            self.right = self.SCREEN_WIDTH - 1
            self.end = True

        if self.bottom < 0:
            self.bottom = 0
            self.end = True
        elif self.top > self.SCREEN_HEIGHT - 1:
            self.top = self.SCREEN_HEIGHT - 1
            self.end = True
        if self.restart == True:
            self.end = False
            self.restart = False




    def player_damage(self, damage):
        """
        When zombie hits player, the player loses health
        """

        self.player_health -= damage

    def get_health(self):
        """
        Returns how much health the player has
        """
        
        return self.player_health

    def get_max_health(self):
        """
        Returns the player's max health. This is used for the health bar.
        """
        return self.max_health

    def add_score(self, points):
        self.score += points * (1 + (self.score_modifier / 10))

    def get_score(self):
        return self.score
      
    def end_point(self):
        return self.end

    def end_restart(self):
        self.restart = True

    def get_damage(self):
        return self.damage

    def load_texture_pair(self, filename):
        """
        Loads the same texture with one version flipped horizontally
        """
        return [
            arcade.load_texture(filename),
            arcade.load_texture(filename, flipped_horizontally=True)
        ]

    def player_animation(self, delta_time: float = 1/60):
        """
        This function deals with the player animations
        """
        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == constants.RIGHT_FACING:
            self.character_face_direction = constants.LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == constants.LEFT_FACING:
            self.character_face_direction = constants.RIGHT_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * constants.UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // constants.UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]

    def set_damage(self, damage):
        self.damage = damage
        
    def add_modifier(self, modifier):
        self.score_modifier = modifier