def printed_board(checkerboard):
    """打印棋盘（黄底黑色字体）"""
    # 设置字体和背景色格式：\033[显示方式;前景色;背景色m；而后面的\033[0m用来关闭属性，不加会影响后面
    print('\033[1;41m--------------简易五子棋游戏（控制台版）---------------\033[0m')
    print('\033[1;30;43m-------------------------------------------------------')
    print('     1    2    3    4    5    6    7    8    9    10   ')
    for i in range(len(checkerboard)):
        # ord返回字符的ASCII数值，chr再返回字符；end=''设置不换行
        print(chr(ord('A') + i) + '    ', end='')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + '    ', end='')
        print()
    print('-------------------------------------------------------\033[0m')


def update_board(ck_settings, checkerboard, position):
    """更新棋盘信息"""
    if ck_settings.chess_player == 1:
        print('请棋手*输入棋子坐标（例如A1，输入exit可退出程序）：', end='')
        check_input(ck_settings, checkerboard, '*', position)
    else:
        print('请棋手o输入棋子坐标（例如C1，输入exit可退出程序）：', end='')
        check_input(ck_settings, checkerboard, 'o', position)


def check_input(ck_settings, checkerboard, char, position):
    """校验输入数据，正确则把坐标打印到棋盘"""
    inputStr = input()  # 获取输入数据
    if len(inputStr) == 0:
        # 判断空情况
        print('\033[1;31m***请输入坐标（例如A1）！***\033[0m')
    elif inputStr == 'exit':
        # 退出程序
        exit()
    elif not inputStr[1].isdigit():
        # 第二位不为数字情况
        print('\033[1;31m***您输入的坐标不正确，请重新输入（例如A1）！***\033[0m')
    else:
        # 获取棋盘下标
        ch = inputStr[0].upper()  # 获取第一个字符并转换为大写
        i = ord(ch) - 65  # A的ASCII是65
        j = int(inputStr[1:3]) - 1  # 最大允许10，所以必须获取两位
        # 判断是否输入溢出
        if (i < 0 or i > 9 or j < 0 or j > 9):
            print('\033[1;31m***您输入的坐标不正确，请重新输入（例如A1）！***\033[0m')
        # 判断输入的是否已经有棋子
        else:
            if checkerboard[i][j] == '-':
                # 累计步数（两边合计）
                ck_settings.win_number += 1
                # 未落子则替换棋手符号，并转换棋手
                checkerboard[i][j] = char
                ck_settings.chess_player *= -1
                # 合计9步开始校验输赢
                if ck_settings.win_number >= 9:
                    check_stats(ck_settings, checkerboard, (i, j), char, position)
            else:
                print('\033[1;31m***您输入的坐标已经有其他棋子，请重新输入（例如A1）！***\033[0m')


def check_stats(ck_settings, checkerboard, pos, char, position):
    """校验四个方向，是否有了输赢"""
    pos_i, pos_j = pos
    directs = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 横、竖、斜、反斜 四个方向检查
    for direct in directs:
        line_checkerboard = []
        d_i, d_j = direct
        # 横排
        if d_j == 0:
            # 横排成数组
            for j in range(ck_settings.number):
                # 判断是“*”或“o”才添加
                if checkerboard[pos_i][j] == char:
                    line_checkerboard.append(position(pos_i, j))
            # print('横排', line_checkerboard)
            win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char)
        elif d_i == 0:
            # 竖排成数组
            for i in range(ck_settings.number):
                # 判断是“*”或“o”才添加
                if checkerboard[i][pos_j] == char:
                    line_checkerboard.append(position(i, pos_j))
            # print('竖排', line_checkerboard)
            win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char)
        elif d_i == 1 and d_j == 1:
            # 斜线成数组
            # 左部分
            minValue = min(pos_i, pos_j)  # 获取较小值
            for i in range(minValue):
                # 判断是“*”或“o”才添加
                if checkerboard[pos_i - minValue + i][pos_j - minValue + i] == char:
                    line_checkerboard.append(position(pos_i - minValue + i, pos_j - minValue + i))

            # 右部分
            maxValue = max(pos_i, pos_j)
            maxValue = ck_settings.number - maxValue  # 获取可叠加的最大数值
            for i in range(maxValue):
                # 判断是“*”或“o”才添加
                if checkerboard[pos_i + i][pos_j + i] == char:
                    line_checkerboard.append(position(pos_i + i, pos_j + i))
            # print('斜线', line_checkerboard)
            win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char)
        else:
            # 反斜线成数组
            # 左部分
            minValue = min(ck_settings.number - pos_i, pos_j)  # 获取较小值
            for i in range(minValue):
                # 判断是“*”或“o”才添加
                if checkerboard[pos_i + minValue - 1 - i][pos_j - minValue + i] == char:
                    line_checkerboard.append(position(pos_i + minValue - 1 - i, pos_j - minValue + i))

            # 右部分
            maxValue = min(pos_i, ck_settings.number - pos_j)  # 获取可叠加的最大数值
            for i in range(maxValue):
                # 判断是“*”或“o”才添加
                if checkerboard[pos_i - i][pos_j + i] == char:
                    line_checkerboard.append(position(pos_i - i, pos_j + i))
            # print('反斜线', line_checkerboard)
            win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char)


def win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char):
    """判断是否连续5个一样"""
    if len(line_checkerboard) >= 5:
        for i, item in enumerate(line_checkerboard):
            index = i + 4
            if index < len(line_checkerboard):
                # 横排情况
                if d_j == 0:
                    j1 = item.y
                    j2 = line_checkerboard[index].y
                    if (j2 - j1) == 4:
                        printed_board(checkerboard)
                        print('\033[1;32m' + char + '选手获胜！\033[0m')
                        ck_settings.game_active = False
                        break
                # 竖排、斜、反斜情况
                else:
                    i1 = item.x
                    i2 = line_checkerboard[index].x
                    # 取绝对值，因为反斜线是负数
                    if abs(i2 - i1) == 4:
                        printed_board(checkerboard)
                        print('\033[1;32m' + char + '选手获胜！\033[0m')
                        ck_settings.game_active = False
                        break