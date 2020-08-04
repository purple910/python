# -*- coding: utf-8 -*-

'''
Created on 2020年1月2日

@author: Fan Xiaoxin
'''


# 五子棋类的定义
class Gomoku(object):
    def __init__(self, x=15, y=15):
        """初始化"""
        # 棋盘横向变量
        self.x = x
        # 棋盘纵向变量
        self.y = y

        self.str = ''

    def gomoku_board(self):
        """画出棋盘"""
        for y in range(self.y):
            for _ in range(self.x - 1):
                self.str += ' '
                self.str += '-'
            self.str += '\n'
            if y != (self.y - 1):
                for _ in range(self.x):
                    self.str += '| '
                self.str += '\n'
        print
        self.str
        return self.str


# 主函数
if __name__ == '__main__':
    gomoku = Gomoku()
    str = gomoku.gomoku_board()
    print(str)