import arcade


class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.speed = 3
        self.has_key = False

        self.texture = arcade.make_circle_texture(20, arcade.color.YELLOW)

    def move_player(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


    def move_with_collision(self, blocker_list):
        old_x = self.center_x
        old_y = self.center_y
        self.move_player()


        collisions = arcade.check_for_collision_with_list(self, blocker_list)
        if collisions:
            self.center_x = old_x
            self.center_y = old_y



