import pygame
import sys

pygame.init()

icon = pygame.image.load("home.png")
pygame.display.set_icon(icon)

size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0


# 屏幕模式
# screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
# screen = pygame.display.set_mode(size, pygame.NOFRAME)
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

pygame.display.set_caption("碰壁游戏")
ball = pygame.image.load("碰壁游戏.png")
ball_rect = ball.get_rect()
# 定时棋
fts = 200
clock = pygame.time.Clock()
# 控制小球移动
still = False
# 颜色控制
bkcolor = pygame.Color("black")


def RGBChannel(a):
    return 0 if a < 0 else (255 if a > 255 else int(a))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # 感知窗口的大小变化
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

        # 鼠标
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                ball_rect = ball_rect.move(event.pos[0] - ball_rect.left, event.pos[1] - ball_rect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ball_rect = ball_rect.move(event.pos[0] - ball_rect.left, event.pos[1] - ball_rect.top)

    # 感知窗口的模式(最小化时暂停)
    if pygame.display.get_active() and not still:
        ball_rect = ball_rect.move(speed[0], speed[1])

    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
        # 避免荡鼠标一直处于边缘时的逻辑错误
        if (ball_rect.right > width) and (ball_rect.right + speed[0] > ball_rect.right):
            speed[0] = - speed[0]
    elif ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = - speed[1]
        if (ball_rect.bottom > height) and (ball_rect.bottom + speed[1] > ball_rect.bottom):
            speed[1] = -speed[1]

    # 颜色设置
    bkcolor.r = RGBChannel(ball_rect.left * 255 / width)
    bkcolor.g = RGBChannel(ball_rect.top * 255 / width)
    bkcolor.b = RGBChannel(min(speed[0], speed[1]) * 255 / max(speed[0], speed[1]))
    # screen.fill(BLACK)
    screen.fill(bkcolor)

    screen.blit(ball, ball_rect)
    pygame.display.update()
    clock.tick(fts)
