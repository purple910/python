import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化！！！")
        # 设置窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 设置时钟
        self.clock = pygame.time.Clock()
        # 创建精灵族
        self.__creat_sprites()
        # 设置敌机定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置子弹定时器事件
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __creat_sprites(self):
        """创建背景精灵与精灵组"""
        # 创建背景
        # bg1 = BackGround("./data/background.gif")
        # bg2 = BackGround("./data/background.gif")
        # bg3 = BackGround("./data/background.gif")
        # bg4 = BackGround("./data/background.gif")
        # bg5 = BackGround("./data/background.gif")
        # bg6 = BackGround("./data/background.gif")
        bg1 = BackGround()
        bg2 = BackGround()
        bg3 = BackGround()
        bg4 = BackGround(True)
        bg5 = BackGround(True)
        bg6 = BackGround(True)
        bg1.rect.x = bg2.rect.width * 0
        bg2.rect.x = bg2.rect.width * 1
        bg3.rect.x = bg2.rect.width * 2
        bg4.rect.x = bg2.rect.width * 0
        bg5.rect.x = bg2.rect.width * 1
        bg6.rect.x = bg2.rect.width * 2
        # bg4.rect.y = - bg4.rect.height
        # bg5.rect.y = - bg4.rect.height
        # bg6.rect.y = - bg4.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2, bg3, bg4, bg5, bg6)

        # 创建敌机
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始！！！")
        while True:
            # 设置刷新帧率
            self.clock.tick(60)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self) -> object:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出来")
                # 创建敌机精灵
                enemy = Enemy()
                # 降低及精灵加入到敌机精灵组
                self.enemy_group.add(enemy)
            # 使用事件来捕获键盘按键
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("右键按下！！")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘模块捕获键盘按键
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            print("右键按下")
            self.hero.speed = 2
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        # 如果没有则必须在左右移动
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 英雄被敌机撞毁 返回敌机的列表
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group, True)
        if len(enemies):
            # 英雄牺牲
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        # 更行背景的位置
        self.back_group.update()
        self.back_group.draw(self.screen)

        # 更行敌机的位置
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 更行英雄
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 更新子弹
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束！！")
        pygame.quit()
        exit()



if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
