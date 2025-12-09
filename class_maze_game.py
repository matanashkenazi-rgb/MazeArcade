import arcade
import wall_and_exitdoor
from wall_and_exitdoor import ExitDoor
import key_class


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
        TILE_SIZE=31

        for row_idx, row in enumerate(LEVEL_MAP):
            for col_idx, cell in enumerate(row):
                x = col_idx * TILE_SIZE + TILE_SIZE / 2
                y = (rows - row_idx - 1) * TILE_SIZE + TILE_SIZE / 2
                if cell=="W":
                    self.wall_list.appand(wall(x,y))
                elif cell=="E":
                    self.exit_list.appand(ExitDoor(x,y))
                elif cell=="P":
                    self.player_list.appand(player(x,y))
                elif cell=="K":
                    self.key_list.appand(Key(x,y))









    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(self.back_ground_color)

        self.wall_list.draw()
        self.key_list.draw()
        self.exit_list.draw()
        self.player_list.draw()

        if self.player and self.player.has_key:
            key_text = "Key: Collected!"
        else:
            key_text = "Key: Not collected"

        arcade.draw_text(
            key_text,
            start_x=10,  # מרחק מהצד השמאלי
            start_y=self.window.height - 20,  # למעלה
            color=arcade.color.WHITE,
            font_size=14
        )








