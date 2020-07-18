# 用来定义一些必须的基本属性和初始值

class Settings():
    def __init__(self):
        """初始化的游戏配置"""
        # 屏幕宽高
        self.width = 700
        self.height = 554
        # 文字颜色和大小
        self.fontsize = 14
        self.fonttype = 'simsunnsimsun'
        # 棋盘格数
        self.number = 15
        # 棋盘左边距、上边距和间隔
        self.bd_left = 30
        self.bd_top = 30
        self.bd_space = 36
        # 判断游戏是否结束（默认开始）
        self.game_active = True
        # 判断哪方下棋（默认黑子先写）
        self.chess_player = 1
        self.prompt_info = '当前棋手：黑棋'
        # 开始校验输赢（两边合计9，因为已经有一边5步）
        self.win_number = 0
        # 设置背景图、黑棋图片、白棋图片路径
        self.checkerboard_bg = 'images/bk.png'
        self.black_chess = 'images/black_chess.png'
        self.white_chess = 'images/white_chess.png'
        # 存储落子数据
        self.move_chess = []
