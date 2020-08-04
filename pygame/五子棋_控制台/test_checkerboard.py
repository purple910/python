class Checkerboard():
    def __init__(self, ck_settings):
        self.number = ck_settings.number

    def draw(self):
        # 绘制棋盘
        checkerboard = []
        for i in range(self.number):
            checkerboard.append([])
            for j in range(self.number):
                checkerboard[i].append('-')
        return checkerboard
