import arcade

class Maze_game(arcade.view):
    def __init__(self):
        self.wall_list=[]
        self.key_list=[]
        self.exit_list=[]
        self.player_list=[]
        self.player=[]
        self.game_won=False
        self.backgaroundcolor=arcade.color.black

    def setup(self):