import pygame as pg
import sys
import settings
from map import Map
from player import Player
from raycasting import RayCasting
from object_rederer import ObjectRenderer
from sprite_object import SpriteObject

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
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()

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
            self.object_renderer.draw()

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