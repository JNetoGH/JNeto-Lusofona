import os
import pygame as pg
import sys
from settings import settings
from scripts.map import Map
from scripts.player import Player
from scripts.pseudo_3d_engine.raycasting import RayCasting
from scripts.renderer import Renderer
from scripts.game_objects.game_objects_classes import StaticSpriteGameObject, AnimatedSpriteGameObject
from scripts.game_objects.game_object_handler import GameObjectHandler


# todo paths that are hard coded, sky and walls in renderer, sprite in game_object_handler

class Game:

    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False) # mouse visibility is set to false
        self.view_mode = settings.ViewMode.VIEW_3D  # pseudo-3d or 2d render
        self.screen = pg.display.set_mode(settings.RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.renderer = Renderer(self)
        self.raycasting = RayCasting(self)

        # without the handler, each kind of game object must be called unitary
        # self.object_handler = GameObjectHandler(self)
        self.static_sprite_gmObj = StaticSpriteGameObject(self)
        self.animeted_sprite_gmObj = AnimatedSpriteGameObject(self)


    def update(self):
        self.player.update()
        self.raycasting.update()

        # without the handler, each kind of game object must be called unitary
        # self.object_handler.update()
        self.static_sprite_gmObj.update()
        self.animeted_sprite_gmObj.update()

        pg.display.flip()
        self.delta_time = self.clock.tick(settings.FPS_TARGET)
        # frame caption shows the game frame production per second
        pg.display.set_caption(f"FPS: {self.clock.get_fps():.1f}")

    def draw(self):
        # clears screen
        self.screen.fill("black")

        # renders the game 2D pre 3D projection
        if self.view_mode == settings.ViewMode.VIEW_2D:
            self.map.draw()
            self.player.draw()
        # renders the game with 3d Projection
        elif self.view_mode == settings.ViewMode.VIEW_3D:
            self.renderer.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                if self.view_mode == settings.ViewMode.VIEW_2D:
                    self.view_mode = settings.ViewMode.VIEW_3D
                elif self.view_mode == settings.ViewMode.VIEW_3D:
                    self.view_mode = settings.ViewMode.VIEW_2D

    # Holds the game loop
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
