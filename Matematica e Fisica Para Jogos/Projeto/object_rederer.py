import pygame as pg
import settings


# RENDERS ALL OBJS IN THE GAME
class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        # holds a dictionary with all textures
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_game_objects()

    # draws the resulting texture of the objects to render list
    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    # loads a texture from the path and return a scaled img
    @staticmethod
    def get_texture(path, res=(settings.TEXTURE_SIZE, settings.TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    # returns a dictionary in which the texture number is the key and the texture is value
    # at map.py, the numbers refers to what texture might be applied to the walls
    def load_wall_textures(self):
        return {
            1: self.get_texture("resources/textures/1.png"),
            2: self.get_texture("resources/textures/2.png"),
            3: self.get_texture("resources/textures/3.png"),
            4: self.get_texture("resources/textures/4.png"),
            5: self.get_texture("resources/textures/5.png")
        }
