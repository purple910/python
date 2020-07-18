from 五子棋_控制台.test_settings import Settings
from 五子棋_控制台.test_checkerboard import Checkerboard
from collections import namedtuple
from 五子棋_控制台 import test_functions as gf


def run_game():
	"""运行游戏"""
	# 配置实例化
	ck_settings = Settings()
	# 棋盘实例化并调用绘制方法
	ck = Checkerboard(ck_settings)
	checkerboard = ck.draw()
	# namedtuple创建类似于元组的数据类型，除了可以用索引访问，能够迭代，还能用属性名访问数据
	position = namedtuple('Position', ['x', 'y'])

	while ck_settings.game_active:
		# 打印棋盘
		gf.printed_board(checkerboard)
		# 更新棋盘
		gf.update_board(ck_settings, checkerboard, position)

run_game()