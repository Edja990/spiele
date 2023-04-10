import pygame as pg
import sys

class Game():
    def __init__(self, res, map_list, fps=None):
        pg.init()
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.fps = fps
        self.map = map_list
        self.newgame()
    def newgame(self):
        self.Map = Map(self,self.map)
    def draw(self):
        self.screen.fill("black")
        self.Map.draw()
    def update(self):
        pg.display.flip()
        fps = self.fps
        if fps:
            self.clock.tick(fps)
            pg.display.set_caption(f"{self.clock.get_fps():.1f}")
    def checkgame(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
    def run(self):
        while True:
            self.checkgame()
            self.update()
            self.draw()

# Maps
class  Map():
    def __init__(self, game , map):
        self.game = game
        self.map = map
        self.world = {}
        self.get_map()
    def get_map(self):
        for j, row in enumerate(self.map):
            for i, value in enumerate(row):
                if value:
                    self.world[(i, j)] = value
    def draw(self):
        [pg.draw.rect(self.game.screen, 'white', (pos[0] * 50, pos[1] * 50,50,50) , 2) for pos in self.world]



