import pygame


class Grid:
    def __init__(self, game):
        self.game = game
        self.length = self.game.screen_res[0]/15
        self.width = (self.game.screen_res[1]/15)-3

        self.nodes = [[Node(self, [row, col + 3]) 
                      for row in xrange(self.length)]
                      for col in xrange(self.width)]


class Node:
    def __init__(self, grid, pos):
        self.grid = grid
        self.game = self.grid.game

        self.pos = pos
        self.blit_pos = [i*15 for i in self.pos]
        self.color = [0, 0, 0]

        self.image = pygame.Surface((15, 15))

        self.rect = self.image.get_rect(topleft=self.blit_pos)

        self.solid = 0
        self.in_path = False
        self.checked = False

    def fill(self, screen):
        self.image.fill(self.color)
        screen.blit(self.image, self.rect)
