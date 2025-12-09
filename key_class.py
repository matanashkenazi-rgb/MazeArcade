import arcade

class Key(arcade.Sprite):
    def __init__(self,x,y):
        self.center_x=x
        self.center_y=y
        self.texture=