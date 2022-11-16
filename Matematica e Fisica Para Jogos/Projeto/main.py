import pygame as pg
import sys
import settings
import map
import player
import raycasting

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(settings.RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = map.Map(self)
        self.player = player.Player(self)
        self.raycasting = raycasting.RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(settings.FPS)
        # frame caption shows the game frame production per second
        pg.display.set_caption(f"FPS: {self.clock.get_fps():.1f}")

    def draw(self):
        # clears screen
        self.screen.fill("black")
        # render the game
        #self.map.draw()
        #self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.KEYDOWN):
                pg.quit()
                sys.exit()

    # Holds the game loop
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()