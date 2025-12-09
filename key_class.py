import arcade

class Key(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.color = arcade.color.GOLD
        self.center_x=x
        self.center_y=y
        self.texture = arcade.SpriteSolidColor(15, 15, self.color).texture