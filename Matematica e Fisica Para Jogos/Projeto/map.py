import pygame as pg

# digits are walls
# bools are space
_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        # dictionary that holds the coordinates of only numeric values, spaces are ignored
        self.world_map_not_null_obj_coordinates = {}
        self.get_map()

    # generates
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map_not_null_obj_coordinates[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, "gray", (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in self.world_map_not_null_obj_coordinates]
