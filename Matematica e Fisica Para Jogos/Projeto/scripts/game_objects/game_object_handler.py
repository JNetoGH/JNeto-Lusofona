from scripts.game_objects.game_objects_classes import *
import os

# ALL GAME OBJECTS CAN BE LOADED AT ONCE USING THIS CLASS
class GameObjectHandler:
    def __init__(self, game):
        self.game = game
        self.game_object_list = []
        self.static_sprites_path = "resources/sprites/static_sprites/"
        self.animated_sprites_path = "resources/sprites/animated_sprites/"

        # game_object map
        add_sprite = self.add_game_object
        add_sprite(StaticSpriteGameObject(game))
        add_sprite(AnimatedSpriteGameObject(game))

    # calls the update of all game
    def update(self):
        [sprite.update() for sprite in self.game_object_list]

    def add_game_object(self, sprite):
        self.game_object_list.append(sprite)