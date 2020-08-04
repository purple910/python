import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("事件处理")
fts = 1
clock = pygame.time.Clock()
num = 1

while True:
    # 自定义事件
    uevent = pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_SPACE, "mod": pygame.KMOD_ALT})
    pygame.event.post(uevent)
    num += 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.unicode == "":
                print("[KEYDOWN]", "#", e.key, e.mod)
            else:
                print("[KEYDOWN]", e.unicode, e.key, e.mod)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            print("[mouse button down]", e.pos, e.button)
        elif e.type == pygame.MOUSEMOTION:
            print("[mouse button motion]", e.pos, e.rel, e.buttons)
        elif e.type == pygame.MOUSEBUTTONUP:
            print("[mouse button up]", e.pos, e.button)

    pygame.display.update()
    clock.tick(fts)
