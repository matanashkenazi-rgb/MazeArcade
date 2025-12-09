import arcade
from player import Player
from key_class import Key
from wall_and_exitdoor import ExitDoor
from wall_and_exitdoor import Wall



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
        self.key_text_display = None


    def setup(self):
        self.game_won=False

        self.key_text_display = arcade.Text(
            "Key: Not Collected",
            x=10,
            y=580,
            color=arcade.color.WHITE,
            font_size=14
        )

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
        NUM_ROWS = len(map_matrix)

        for row_idx, row in enumerate(map_matrix):
            for col_idx, cell in enumerate(row):
                x = col_idx * TILE_SIZE + TILE_SIZE / 2
                y = (NUM_ROWS - row_idx - 1) * TILE_SIZE + TILE_SIZE / 2

                if cell=="W":
                    self.wall_list.append(Wall(x,y))
                elif cell=="E":
                    self.exit_list.append(ExitDoor(x,y))
                elif cell=="P":
                    self.player_list.append(Player(x,y))
                elif cell=="K":
                    self.key_list.append(Key(x,y))



    def on_draw(self):
        self.clear()
        arcade.set_background_color(self.back_ground_color)

        self.wall_list.draw()
        self.key_list.draw()
        self.exit_list.draw()
        self.player_list.draw()
        self.key_text_display.draw()





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


    def on_update(self, delta_time):
        player = self.player_list[0]
        player.move_with_collision(self.wall_list)

        key_hit_list = arcade.check_for_collision_with_list(player, self.key_list)
        for key in key_hit_list:
            player.has_key = True
            key.remove_from_sprite_lists()

        if player.has_key:
            self.key_text_display.text = "Key: Collected!"
        else:
            self.key_text_display.text = "Key: Not Collected"

        exit_hit_list = arcade.check_for_collision_with_list(player, self.exit_list)
        if exit_hit_list and player.has_key:
            self.game_won = True



