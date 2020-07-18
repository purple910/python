class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息")

    @classmethod
    def show_top_score(cls):
        print("最高分：%d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏了。。。" % self.player_name)


Game.show_help()

Game.show_top_score()

game = Game("Bob")
game.start_game()
# 飞机游戏.show_help()
# 飞机游戏.show_top_score()


Game.start_game(game)
