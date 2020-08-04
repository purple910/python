# 主要用来绘制背景图和棋格线

import sys
import pygame


class Checkerboard():
    def __init__(self, ck_settings, screen, position):
        self.ck_settings = ck_settings
        self.screen = screen
        self.position = position

        # 颜色和坐标大小
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(ck_settings.fonttype, ck_settings.fontsize)
        # 存储棋子坐标
        self.checkerboard = []
        # 加载背景图、黑棋和白棋（当有图片不存在时，打印错误并退出游戏）
        try:
            self.bg_image = pygame.image.load(ck_settings.checkerboard_bg)
            self.black_image = pygame.image.load(ck_settings.black_chess).convert_alpha()  # convert_alpha背景透明
            self.white_image = pygame.image.load(ck_settings.white_chess).convert_alpha()
            self.chess_rect = self.black_image.get_rect()
        except Exception as e:
            print('error:', e)
            sys.exit()

    def draw_board(self):
        # 存储棋子坐标
        for i in range(self.ck_settings.number):
            self.checkerboard.append([])
            for j in range(self.ck_settings.number):
                self.checkerboard[i].append(self.position(self.ck_settings.bd_left + i * self.ck_settings.bd_space,
                                                          self.ck_settings.bd_top + j * self.ck_settings.bd_space))
        # 绘制棋盘坐标
        for i in range(0, self.ck_settings.number):
            # ord返回字符的ASCII数值，chr再返回字符
            x_text = self.font.render(chr(ord('A') + i), True, self.text_color)  # A-O
            y_text = self.font.render(str(i + 1), True, self.text_color)  # 1-15

            # 绘制xy轴坐标（在棋盘背景图绘制）
            self.bg_image.blit(x_text,
                               (self.checkerboard[i][0].x - x_text.get_width() / 2, self.checkerboard[i][0].y - 20))
            self.bg_image.blit(y_text,
                               (self.checkerboard[0][i].x - 20, self.checkerboard[0][i].y - y_text.get_height() / 2))

            # 绘制横竖线（在棋盘背景图绘制）
            pygame.draw.line(self.bg_image, self.text_color, self.checkerboard[0][i],
                             self.checkerboard[self.ck_settings.number - 1][i])
            pygame.draw.line(self.bg_image, self.text_color, self.checkerboard[i][0],
                             self.checkerboard[i][self.ck_settings.number - 1])
        # 绘制棋盘背景图
        self.screen.blit(self.bg_image, (0, 0))