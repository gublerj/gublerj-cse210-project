import arcade
from game.player import Player

class Output_service:

    def __init__(self):
        self.HEALTHBAR_HEIGHT = 10
        self.HEALTHBAR_WIDTH = 70
        # self.player_max_hp = player.get_health()

    def execute(self, actors):
        player = actors['player'][0][0]
        zombies = actors['zombie'][0]
        bullets = actors['bullet'][0]
        player.draw()
        for zombie in zombies:
            zombie.draw()
        for bullet in bullets:
            bullet.draw()
        
        # This code displays the health bar in the bottom left.
        self.player_max_hp = player.get_max_health()

        health_width = self.HEALTHBAR_WIDTH * (player.get_health() / self.player_max_hp)

        if player.get_health() < self.player_max_hp:
            arcade.draw_rectangle_filled(50, 20, width=self.HEALTHBAR_WIDTH, height=self.HEALTHBAR_HEIGHT, color=arcade.color.RED)

        arcade.draw_rectangle_filled(50, 20, width=health_width, height=self.HEALTHBAR_HEIGHT, color=arcade.color.GREEN)