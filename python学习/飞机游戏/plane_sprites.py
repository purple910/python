import random

import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 126 * 3, 480)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的方法转换
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class BackGround(GameSprite):
    """游戏背景"""

    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵的创建
        super().__init__("./data/background.gif")
        # 判断是否是交替图像
        if is_alt:
            self.rect.y = - self.rect.height

    def update(self):
        super().update()
        # 判断是否一处屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 创建敌机精灵
        super().__init__("./data/enemy.png")
        # 指定敌机的初始化速度 1-3
        self.speed = random.randint(1, 3)
        # 指定敌机随机位置
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        self.rect.bottom = 0

    def update(self, *args):
        # 保持垂直飞行
        super().update()
        # 判断是否废除屏幕
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机飞出屏幕")
            self.kill()

    def __del__(self):
        print("敌机挂了 %s " % self.rect)


class Hero(GameSprite):
    """英雄飞机"""
    def __init__(self):
        super().__init__("./data/alien1.png", 0)
        # 位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 50
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed
        # 判断英雄不能一处屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("shot !!!!")
        # 创建子弹精灵
        for i in (0, 1, -1):
            bullet = Bullet()
            # 创建精灵位置
            bullet.rect.bottom = self.rect.y - 10
            bullet.rect.centerx = self.rect.centerx + i * 15
            # 将精灵加载精灵组
            self.bullets.add(bullet)



class Bullet(GameSprite):
    """子弹"""

    def __init__(self):
        super().__init__("./data/shot.gif", -2)

    def update(self, *args):
        super().update()
        # 判断子弹飞出
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")