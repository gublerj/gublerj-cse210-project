
class collisions():

    def __init__(self):
        pass


    def bullet_player_collision(player_sprites):
        
        for i in player_sprites["bullet"]:
            if player_sprites["zombie"][0][0]._position == i._position:
                # pop zombie



