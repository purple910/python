import pygame
import sys
import pygame.freetype

pygame.init()

size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0
PURPLE = 160, 32, 240
pos = [230, 160]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("font")
fp = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
frect = fp.render_to(screen, pos, "世界和平", fgcolor=PURPLE, size=50)

fts = 200
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pos[0] < 0 or pos[0] + frect.width > width:
        speed[0] = - speed[0]
    elif pos[1] < 0 or pos[1] + frect.height > height:
        speed[1] = - speed[1]
    pos[0] += speed[0]
    pos[1] += speed[1]

    screen.fill(BLACK)
    frect = fp.render_to(screen, pos, "世界和平", fgcolor=PURPLE, size=50)
    pygame.display.update()
    clock.tick(fts)

