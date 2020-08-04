class Settings():
    def __init__(self):
        """初始化的游戏配置"""
        # 棋盘格数
        self.number = 10
        # 判断游戏是否结束（默认开始）
        self.game_active = True
        # 判断哪方下棋
        self.chess_player = 1
        # 开始校验输赢（两边合计9，因为已经有一边5步）
        self.win_number = 0
