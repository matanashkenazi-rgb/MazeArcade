import arcade

class Wall(arcade.Sprite):
    def __init__(self, x, y, texture):
        super().__init__()
        self.texture = texture
        self.center_x = x
        self.center_y = y

class ExitDoor(arcade.Sprite):
    def __init__(self, x, y, texture):
        super().__init__()
        self.color = arcade.color.GREEN
        self.texture = texture
        self.center_x = x
        self.center_y = y
