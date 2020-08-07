"""
    @Time    : 2020/8/5 14:55 
    @Author  : fate
    @Site    : 
    @File    : __init__.py.py
    @Software: PyCharm
"""
# 1. 定义一个学生类。
# 该类的属性如下：
# - 姓名 字符串
# - 年龄 整型
# - 成绩（语文，数学，英语) 字典，科目名称为键，成绩为值
#
# 该类的方法：
# - 获取学生的姓名：get_name() 返回类型:str
# - 获取学生的年龄：get_age() 返回类型:int
# - 返回3门科目中最高分数的课程。get_course()
# - 返回该学生的平均成绩get_avg()
#


class Student(object):

    def __init__(self, name: str, age: int, **score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        keys = list(self.score.keys())
        values = list(self.score.values())
        max1 = max(values)
        cource = []
        for i in range(len(values)):
            if max1 == values[i]:
                cource.append(keys[i])
        return cource

    def get_avg(self):
        values = self.score.values()
        return sum(values) / len(values)


s = Student('zs', 15, **{'语文': 80, '数学': 90, '英语': 85})
print(s.get_name())
print(s.get_age())
print(s.get_avg())
print(s.get_course())


# 2. 写一个游戏机器人自动游戏比赛，定义一个类：AutoRobot，类中存在一个全局类 成员gameDic = ['石头','剪刀','布']，
# 然后需要定义一个分数值 Score记录比赛分数。
# 谁赢谁加1分，打平双方不加分。比赛规则为 石头>剪刀>布>石头 然后定义一个play方法让两个机器人出拳，可以指定比赛局数。
# 完成两个机器人之间的比赛！
import random


class AutoRobot:
    gameDic = ['石头', '剪刀', '布']

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.play_game = 0

    def play(self):
        self.play_game = random.randint(0, 2)

    def score_add(self):
        self.score += 1

    def score_reduce(self):
        self.score -= 1


def play_games(robot_A, robot_B, times):
    for i in range(times):
        robot_A.play()
        robot_B.play()

        if robot_A.play_game == robot_B.play_game:
            print("本轮平局，不加分")
        elif robot_A.play_game - robot_B.play_game == -1 or robot_A.play_game - robot_B.play_game == 2:
            print(f"{robot_A.name}本轮胜出，加一分")
            robot_A.score_add()
            robot_B.score_reduce()
        else:
            print(f"{robot_B.name}本轮胜出，加一分")
            robot_B.score_add()
            robot_A.score_reduce()

        print(f"{robot_A.name}当前分数：{robot_A.score}---{robot_B.name}当前分数：{robot_B.score}")
        print()

    print(f"{robot_A.name}当前分数：{robot_A.score}---{robot_B.name}当前分数：{robot_B.score}")
    if robot_A.score > robot_B.score:
        print(f"{robot_A.name}获胜")
    elif robot_A.score < robot_B.score:
        print(f"{robot_B.name}获胜")
    else:
        print("双方比分相同，不分胜负")
    print("游戏结束！")


robot1 = AutoRobot('robotA', 100)
robot2 = AutoRobot('robotB', 100)
play_games(robot1, robot2, 10)
