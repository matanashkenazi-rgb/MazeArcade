import arcade

class Key(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.center_x=x
        self.center_y=y
        self.texture = arcade.SpriteSolidColor(30, 20, arcade.color.YELLOW).texture