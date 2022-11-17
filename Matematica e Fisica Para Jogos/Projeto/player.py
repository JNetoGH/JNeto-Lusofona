import settings
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = settings.PLAYER_INITIAL_POS
        self.angle = settings.PLAYER_ANGLE

    def move_and_rotate(self):
        # increments in x-axis and y-axis
        dx, dy = 0, 0

        # makes the increment having in count the player's angle
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        speed = settings.PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        # applying increments/decrements to the coordinates if there is no wall adding the increment
        if self.no_walls_at(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.no_walls_at(int(self.x), int(self.y + dy)):
            self.y += dy

        # increments/decrements the rot angle using arrow < > keys, basically rotates player
        if keys[pg.K_LEFT]:
            self.angle -= settings.PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += settings.PLAYER_ROT_SPEED * self.game.delta_time
        # makes sure the angle remains in 2pi
        self.angle %= math.tau

    def no_walls_at(self, x, y):
        return (x, y) not in self.game.map.world_map_not_null_obj_coordinates

    def draw(self):
        # the line that represents where the player is looking at, represents the angle line
        pg.draw.line(self.game.screen, "blue", (self.x * 100, self.y * 100),
                     (self.x * 100 + settings.SCREEN_WIDTH * math.cos(self.angle),
                      self.y * 100 + settings.SCREEN_WIDTH * math.sin(self.angle)),
                     2)
        # represents the player as a ball
        pg.draw.circle(self.game.screen, "green", (self.x * 100, self.y * 100), radius=15)

    def update(self):
        self.move_and_rotate()

    @property
    def pos(self):
        return self.x, self.y

    # which tile of the map
    @property
    def tile_map_pos(self):
        return int(self.x), int(self.y)