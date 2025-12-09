import arcade
#
class Wall(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(
            64,
            arcade.color.DARK_BLUE,
            outer_alpha=255
        )
        self.center_x = x
        self.center_y = y

class ExitDoor(arcade.Sprite):
    def __init__(self, x, y, texture):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(
            64,
            arcade.color.GREEN,
            outer_alpha=255
        )
        self.center_x = x
        self.center_y = y
