import arcade

class Maze_game(arcade.View):
    def __init__(self):
        super().__init__()
        self.wall_list=arcade.SpriteList()
        self.key_list=arcade.SpriteList()
        self.exit_list=arcade.SpriteList()
        self.player_list=arcade.SpriteList()
        self.player=arcade.SpriteList()
        self.player = None
        self.game_won=False
        self.back_ground_color=arcade.color.BLACK

    def setup(self):
        self.game_won=False

        map_matrix = [
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["E", " ", "P", " ", "W", " ", " ", "K", " ", "W", " ", "W"],
            ["W", " ", " ", " ", "W", " ", "W", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", "W", " ", "W", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", "W", " ", "W", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", "W", " ", "W", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", "W", " ", "W", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", "W", " ", "W", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", "W", " ", "W", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", "W", "W", "W", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]
        ]
        TILE_SIZE=32

        for row_idx, row in enumerate(map_matrix):
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

        key_text = "Key: Collected!" if self.player.has_key else "Key: Not Collected"
        arcade.draw_text(
            key_text,
            10,
            self.window.height - 20,
            arcade.color.WHITE,
            14
        )
        if self.game_won:
            arcade.draw_text(
                "YOU WIN!",
                self.window.width // 2,
                self.window.height // 2,
                arcade.color.YELLOW,
                40,
                anchor_x="center",
                anchor_y="center"
            )







