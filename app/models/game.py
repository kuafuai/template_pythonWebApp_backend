from enum import Enum


class GameState(Enum):
    running = 1
    over = 2
    win = 3


class Snake:
    def __init__(self, position):
        self.position = position

    def move(self):
        # code to move the snake's position
        pass


class Game:
    def __init__(self):
        self.state = GameState.running

    def update_direction(self):
        # code to update player's direction input
        pass

    def update_game_state(self):
        # code to update game state
        pass

    def update_snake_position(self):
        # code to update snake's position
        pass
