import arcade

class Wall(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = arcade.color.BLUE
        self.texture = arcade.SpriteSolidColor(30, 30, self.color).texture
        self.center_x = x
        self.center_y = y

class ExitDoor(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = arcade.color.GREEN
        self.texture = arcade.SpriteSolidColor(30, 30, self.color).texture
        self.center_x = x
        self.center_y = y
