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

        self.wall_list = arcade.SpriteList()
        self.key_list = arcade.SpriteList()
        self.exit_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player = arcade.SpriteList()

        self.key_text_display = arcade.Text(
            "Key: Not Collected",
            x=10,
            y=580,
            color=arcade.color.WHITE,
            font_size=14
        )

        LEVEL_MAP = [
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["E", " ", " ", "W", " ", " ", " ", "W", " ", "K", " ", "W"],
            ["W", "W", " ", "W", " ", "W", " ", "W", " ", "W", " ", "W"],
            ["W", " ", " ", " ", " ", "W", " ", " ", " ", "W", " ", "W"],
            ["W", " ", "W", "W", " ", "W", "W", "W", " ", "W", " ", "W"],
            ["W", " ", " ", "W", " ", " ", " ", "W", " ", " ", " ", "W"],
            ["W", "W", " ", "W", "W", "W", " ", "W", "W", "W", " ", "W"],
            ["W", " ", " ", " ", " ", "W", " ", " ", " ", "W", " ", "W"],
            ["E", "K", "W", "W", " ", "W", "W", "W", " ", "W", " ", "W"],
            ["W", "P", " ", " ", " ", " ", " ", "W", " ", " ", " ", "W"],
            ["W", " ", " ", "W", "W", "W", " ", "W", "W", "W", " ", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]
        ]
        TILE_SIZE=32
        NUM_ROWS = len(LEVEL_MAP)

        for row_idx, row in enumerate(LEVEL_MAP):
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
                800 / 2,
                600 / 2,
                arcade.color.YELLOW,
                40,
                anchor_x="center",
                anchor_y="center"
            )

    def on_update(self, delta_time):
        player = self.player_list[0]

        if not self.game_won:
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



    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.game_won:
            self.setup()
            return  # exit early so we don't move the player this frame


        player = self.player_list[0]

        if key == arcade.key.UP:
            player.change_y = 1
        elif key == arcade.key.DOWN:
            player.change_y = -1
        elif key == arcade.key.RIGHT:
            player.change_x = 1
        elif key == arcade.key.LEFT:
            player.change_x = -1

    def on_key_release(self, key, modifiers):
        player = self.player_list[0]
        if key == arcade.key.UP or key == arcade.key.DOWN:
            player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            player.change_x = 0