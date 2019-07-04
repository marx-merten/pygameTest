import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.pos = (x, y)
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 255, 255))
        pygame.draw.line(self.surf, (29, 93, 22), (20, 22), (99, 88), 4)
        self.rect = self.surf.get_rect()
        print(self.rect)

    def draw(self, screen):
        screen.blit(self.surf, self.pos)


class Game:
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.player = Player(20, 20)
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.clock.tick(2)
            print(self.clock.get_fps())
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                elif event.type == QUIT:
                    self.running = False
            self.player.draw(self.screen)
            pygame.display.flip()
