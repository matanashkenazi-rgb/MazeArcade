import arcade
from class_maze_game import Maze_game  # your Maze_game class file


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Maze Game Test"


def main():



    # Create the window
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Create the Maze_game view
    maze_view = Maze_game()
    maze_view.setup()

    # Show the view
    window.show_view(maze_view)

    # Run the game
    arcade.run()


if __name__ == "__main__":
    main()
