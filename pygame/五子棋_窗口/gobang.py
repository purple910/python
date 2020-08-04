# 主函数用来初始化程序，并同步更新程序的信息


import pygame
from settings import Settings
from checkerboard import Checkerboard
from collections import namedtuple
import game_functions as gf
from infopanel import Infopanel


def run_game():
    """运行游戏"""
    # 初始化游戏屏幕
    pygame.init()
    # 创建时钟对象 (可以控制游戏循环频率)
    clock = pygame.time.Clock()
    # 配置实例化
    ck_settings = Settings()
    screen = pygame.display.set_mode((ck_settings.width, ck_settings.height))
    pygame.display.set_caption('五子棋游戏')
    # namedtuple创建类似于元组的数据类型，除了可以用索引访问，能够迭代，还能用属性名访问数据
    position = namedtuple('Position', ['x', 'y'])
    # 创建实例
    cb = Checkerboard(ck_settings, screen, position)

    # 实例化面板信息
    infopanel = Infopanel(ck_settings, screen)

    while ck_settings.game_active:
        # 绘制棋盘
        cb.draw_board()
        # 绘制面板信息
        infopanel.draw_info(ck_settings.prompt_info)
        # 检查玩家事件并更新棋盘
        gf.check_events(ck_settings, cb, position)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

        # 通过时钟对象指定循环频率
        clock.tick(60)  # 每秒循环60次


run_game()