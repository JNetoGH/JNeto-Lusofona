from game_objects_classes import *
import os



# ALL GAME OBJECTS ARE MANAGED BY THIS CLASS
class GameObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprites_path = "../"