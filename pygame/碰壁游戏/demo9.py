import pygame
import sys
from math import pi

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("图形绘制")

PURPLE = 160, 32, 240
GODL = 255, 251, 0
RED = pygame.Color("red")
WHITE = 255, 255, 255
GREEN = pygame.Color('green')

# r1 = pygame.draw.rect(screen, GODL, (100, 100, 200, 100), 5)
# r2 = pygame.draw.rect(screen, RED, (210, 210, 200, 100), 0)

r1 = pygame.draw.ellipse(screen, GREEN, (50, 50, 500, 300), 3)
r2 = pygame.draw.circle(screen, GODL, (200, 180), 30, 5)
r3 = pygame.draw.circle(screen, GODL, (400, 180), 30)
r4 = pygame.draw.rect(screen, RED, (170, 130, 60, 10), 3)
r5 = pygame.draw.rect(screen, RED, (370, 130, 60, 10))
plist = [(295, 170), (285, 250), (260, 280), (340, 280), (315, 250), (305, 170)]
r6 = pygame.draw.lines(screen, PURPLE, True, plist, 2)
r7 = pygame.draw.arc(screen, PURPLE, (200, 220, 200, 100), 1.4*pi, 1.9*pi, 3)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
