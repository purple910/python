import pygame, sys

pygame.init()

size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0
fts = 200

screen = pygame.display.set_mode(size)
pygame.display.set_caption("标题")
ball = pygame.image.load("碰壁游戏.png")
ball_rect = ball.get_rect()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))


    ball_rect = ball_rect.move(speed[0], speed[1])

    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    elif ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = - speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ball_rect)
    pygame.display.update()
    clock.tick(fts)

