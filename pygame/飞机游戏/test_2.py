import pygame
from plane_sprites import *

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
# pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect初始化飞机位置
hero_rect = pygame.Rect(150, 300, 102, 128)

# 创建敌机的精灵
enemy = GameSprite("./data/alien3.png")
enemy1 = GameSprite("./data/alien2.png", 2)

# 敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    # 指定代码执行频率
    clock.tick(60)

    # 监听
    for event in pygame.event.get():
        # 判断是否为退出
        if event.type == pygame.QUIT:
            print("游戏退出！！！")
            pygame.quit()
            exit()

    # 位置自减
    hero_rect.y -= 1

    # 判断飞机位置
    if hero_rect.y <= 0:
        hero_rect.y = 700

    # 绘制
    screen.blit(bg, (126 * 0, 0))
    screen.blit(bg, (126, 0))
    screen.blit(bg, (126 * 2, 0))
    screen.blit(hero, hero_rect)

    # 精灵组调用
    enemy_group.update()
    enemy_group.draw(screen)

    # 刷新
    pygame.display.update()


