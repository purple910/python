import pygame.freetype
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("文字绘制")
PURPLE = 160, 32, 240

fp = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 36)
# frect = fp.render_to(screen, (200, 160), "世界和平", fgcolor=PURPLE, size=50)
fsurf, srect = fp.render("世界和平", fgcolor=PURPLE, size=50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(fsurf, (200, 160))
    pygame.display.update()
