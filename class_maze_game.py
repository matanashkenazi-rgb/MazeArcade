import arcade

import wall_and_exitdoor
from wall_and_exitdoor import ExitDoor


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
        self.game_won=False

        LEVEL_MAP=("WWWWWWWWWWWW"
                   "E P W W  K W"
                   "W   W W    W"
                   "W   W W    W"
                   "W   W W    W"
                   "W   W W    W"
                   "W   W W    W"
                   "W   W W    W"
                   "W   W W    W"
                   "W   WWW    W"
                   "W          W"
                   "WWWWWWWWWWWW")
        TILE_SIZE=32

        for row_idx, row in enumerate(LEVEL_MAP):
            for col_idx, cell in enumerate(row):
                x = col_idx * TILE_SIZE + TILE_SIZE / 2
                y = (rows - row_idx - 1) * TILE_SIZE + TILE_SIZE / 2
                if cell=="W":
                self.wall_list.appand(wall(x,y))
                elif cell=="E"
                self.exit_list.appand(ExitDoor(x,y))


