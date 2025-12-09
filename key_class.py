import arcade

class Key(arcade.Sprite):
    def __init__(self,x,y)
        super().__init__()
        self.center_x=x
        self.center_y=y
        self.texture=arcade.make_soft_square_texture(
            size,                 # Width and height of the square
            arcade.color.GOLD,    # Color
            outer_margin=255      # Margin parameter (usually left at 255 for solid)
        )