# 存放跟游戏有关的所有业务逻辑函数


import sys
import pygame


# 棋
def update_board(ck_settings, cb, index_coordinates, position):
    """更新棋盘信息"""
    # 判断棋手（黑棋或白棋）
    if ck_settings.chess_player == 1:
        ck_settings.prompt_info = '当前棋手：白棋'
        img = cb.black_image
        chess_type = 'black'
    else:
        ck_settings.prompt_info = '当前棋手：黑棋'
        img = cb.white_image
        chess_type = 'white'

    """落棋"""
    dropState = check_at(ck_settings, index_coordinates)
    if dropState:
        i, j = index_coordinates
        chess_x = cb.checkerboard[j][i].x - cb.chess_rect.width / 2
        chess_y = cb.checkerboard[j][i].y - cb.chess_rect.height / 2
        # 累计步数（两边合计）
        ck_settings.win_number += 1
        # 落子并转换棋手
        ck_settings.move_chess.append({'type': chess_type, 'coord': position(i, j)})
        cb.bg_image.blit(img, (chess_x, chess_y))
        ck_settings.chess_player *= -1
        # 合计9步开始校验输赢
        if ck_settings.win_number >= 9:
            check_stats(ck_settings, (i, j))
    else:
        ck_settings.prompt_info = '已经有其他棋子'


# 检查(i,j)位置是否已占用
def check_at(ck_settings, index_coordinates):
    for item in ck_settings.move_chess:
        if index_coordinates == item['coord']:
            return False
    return True


def check_stats(ck_settings, pos):
    """校验四个方向，是否有了输赢"""
    pos_i, pos_j = pos
    directs = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 横、竖、斜、反斜 四个方向检查
    for direct in directs:
        line_checkerboard = []
        d_x, d_y = direct

        last = ck_settings.move_chess[-1]
        line_ball = []  # 存放在一条线上的棋子
        for ball in ck_settings.move_chess:
            # 跟最后落子判断
            if ball['type'] == last['type']:
                x = ball['coord'].x - last['coord'].x
                y = ball['coord'].y - last['coord'].y
                if d_x == 0:
                    if x == 0:
                        line_ball.append(ball['coord'])
                if d_y == 0:
                    if y == 0:
                        line_ball.append(ball['coord'])
                if x * d_y == y * d_x:
                    line_ball.append(ball['coord'])

        if len(line_ball) >= 5:  # 只有5子及以上才继续判断
            sorted_line = sorted(line_ball)
            for i, item in enumerate(sorted_line):
                index = i + 4
                if index < len(sorted_line):
                    if d_x == 0:
                        y1 = item.y
                        y2 = sorted_line[index].y
                        # 此点和第5个点比较y值，如相差为4则连成5子
                        if abs(y1 - y2) == 4:
                            ck_settings.prompt_info = '黑棋获胜' if last['type'] == 'black' else '白棋获胜'
                    else:
                        x1 = item.x
                        x2 = sorted_line[index].x
                        # 此点和第5个点比较x值，如相差为4则连成5子
                        if abs(x1 - x2) == 4:
                            ck_settings.prompt_info = '黑棋获胜' if last['type'] == 'black' else '白棋获胜'
                else:
                    break


# 事件
def check_events(ck_settings, cb, position):
    """监听事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 点击左键
            if event.button == 1:
                pos = pygame.mouse.get_pos()  # 获取点击实际坐标
                # 判断是否溢出
                x_first = cb.checkerboard[0][0].x
                x_last = cb.checkerboard[ck_settings.number - 1][ck_settings.number - 1].x
                y_first = cb.checkerboard[0][0].y
                y_last = cb.checkerboard[ck_settings.number - 1][ck_settings.number - 1].y
                if pos[0] < x_first or pos[0] > x_last or pos[1] < y_first or pos[1] > y_last:
                    ck_settings.prompt_info = '落子位置不正确！'
                else:
                    index_coordinates = to_index(ck_settings, pos)
                    update_board(ck_settings, cb, index_coordinates, position)


def to_index(ck_settings, pos):
    """实际坐标转换为棋盘下标"""
    i = round((pos[1] - ck_settings.bd_top) / ck_settings.bd_space)
    j = round((pos[0] - ck_settings.bd_left) / ck_settings.bd_space)
    return (i, j)