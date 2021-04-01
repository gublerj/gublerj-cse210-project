import arcade
from game.player import Player

class Output_service:

    def __init__(self):
        self.HEALTHBAR_HEIGHT = 10
        self.HEALTHBAR_WIDTH = 70
        # self.player_max_hp = player.get_health()

    def execute(self, actors, actor_list):
        players = actors['player'][0]
        zombies = actors['zombie'][0]
        bullets = actors['bullet'][0]
        walls = actors['wall'][0]
        obsticals = actors['obsticals'][0]
        weapons = actors['weapon'][0]

        for weapon in weapons:
            weapon.draw()
        for player in players:
            player.draw()
        for zombie in zombies:
            zombie.draw()
        for bullet in bullets:
            bullet.draw()
        for wall in walls:
            wall.draw() 
        for obstical in obsticals:
            obstical.draw()
        # for count in range(0, len(actor_list)):
        #     if len(actors[actor_list[count]][0]) == 0:
        #         actors[actor_list[count]][0][0].draw()
        #     else:
        #         for number in range(0, len(actors[actor_list[count]][0])):
        #             if actors[actor_list[count]][0][number] == -1:
        #                 pass
        #             else:
        #                 actors[actor_list[count]][0][number].draw()
        
        arcade.draw_text(f"Score: {player.get_score()}", 10, 630, arcade.color.WHITE, 14)

        # This code displays the health bar in the bottom left.
        self.player_max_hp = player.get_max_health()

        health_width = self.HEALTHBAR_WIDTH * (player.get_health() / self.player_max_hp)

        if player.get_health() < self.player_max_hp:
            arcade.draw_rectangle_filled(50, 20, width=self.HEALTHBAR_WIDTH, height=self.HEALTHBAR_HEIGHT, color=arcade.color.RED)

        arcade.draw_rectangle_filled(50, 20, width=health_width, height=self.HEALTHBAR_HEIGHT, color=arcade.color.GREEN)