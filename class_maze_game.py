import arcade

class Maze_game(arcade.View):
    def __init__(self):
        super().__init__()
        self.wall_list=arcade.SpriteList()
        self.key_list=arcade.SpriteList()
        self.exit_list=arcade.SpriteList()
        self.player_list=arcade.SpriteList()
        self.player=arcade.SpriteList()
        self.game_won=False
        self.back_ground_color=arcade.color.BLACK

    def setup(self):
        pass








    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(self.back_ground_color)

        self.wall_list.draw()



