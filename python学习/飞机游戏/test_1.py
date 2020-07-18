import pygame

pygame.init()

# 创建窗口
screen = pygame.display.set_mode((126 * 3, 480))

# 加载背景图片
bg = pygame.image.load("./data/background.gif")

# blit绘制图片 (x,y)
screen.blit(bg, (126 * 0, 0))
screen.blit(bg, (126, 0))
screen.blit(bg, (126 * 2, 0))

# 刷新
# pygame.display.update()

# 加载飞机
hero = pygame.image.load("./data/alien1.png")
screen.blit(hero, (150, 300))

# 刷新
pygame.display.update()

while True:
    if int(input(":")) == 0:
        break

pygame.quit()

