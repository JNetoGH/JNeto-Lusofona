import pygame as pg
import sys

from settings import settings
from scripts.map import Map
from scripts.player import Player
from scripts.pseudo_3d_engine.raycasting import RayCasting
from scripts.renderer import Renderer
from scripts.game_objects.game_object_animated_sprite import GameObjectAnimatedSprite
from scripts.game_objects.game_object_static_sprite import GameObjectStaticSprite
from scripts.game_objects.game_object_animated_fixed_on_screen_sprite import GameObjectAnimatedFixedOnScreen


class Tree(GameObjectStaticSprite):
    def __init__(self, game, pos):
        super().__init__(game, "resources/sprites/static_sprites/tree.png", initial_pos_tile_matrix=pos, scale=2, height_shift=-0.25)


class Weapon(GameObjectAnimatedFixedOnScreen):
        pass


# todo paths that are hard coded, sky and walls in renderer, sprite in game_object_handler
class Game:

    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)  # mouse visibility is set to false
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

        # GAME OBJECTS
        self.static_sprite_gmObj = GameObjectStaticSprite(self)
        self.animeted_sprite_gmObj = GameObjectAnimatedSprite(self)
        self.weapon = GameObjectAnimatedFixedOnScreen(self)
        self.tree1 = Tree(self, [11, 5])
        self.tree2 = Tree(self, [11, 5.5])
        self.tree3 = Tree(self, [11, 6])

    def update(self):
        self.player.update()
        self.raycasting.update()

        # GAME OBJECTS
        self.static_sprite_gmObj.update()
        self.animeted_sprite_gmObj.update()
        self.tree1.update()
        self.tree2.update()
        self.tree3.update()
        self.weapon.update()

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
            # GAME OBJECTS
            self.weapon.draw()

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
            self.player.single_fire_event(event)

    # Holds the game loop
    def run(self):
        while True:
            self.check_events()
            self.update()

            pg.display.flip()
            self.delta_time = self.clock.tick(settings.FPS_TARGET)
            pg.display.set_caption(f"FPS: {self.clock.get_fps():.1f}")

            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
