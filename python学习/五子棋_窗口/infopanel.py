# 主要用来绘制棋盘右边提示信息（暂时只有显示下棋方和获胜信息）

import pygame.font


class Infopanel():
    def __init__(self, ck_settings, screen):
        """初始化属性"""
        self.settings = ck_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置文字颜色和字体大小
        self.info_color = (217, 8, 10)
        self.font = pygame.font.SysFont(ck_settings.fonttype, 16)

    def draw_info(self, info):
        """将文字渲染为图像，并定位到右边水平居中"""
        self.info_image = self.font.render(info, True, self.info_color)
        self.info_image_rect = self.info_image.get_rect()
        self.info_image_rect.right = self.screen_rect.right - (
                    self.screen_rect.width - 536 - self.info_image_rect.width) / 2
        self.info_image_rect.top = 50
        # 绘制到屏幕
        self.screen.blit(self.info_image, self.info_image_rect)