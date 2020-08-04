"""
    @Time    : 2020/2/22 10:49
    @Author  : fate
    @Site    : 
    @File    : __init__.py.py
    @Software: PyCharm
"""
# 1.给定一个成绩单（字典，姓名为键，成绩为值），找出最高分和最低分，并求出平均成绩。成绩自己定义！
temp = {"张三": 88, "王五": 66, "李四": 58, "李丽": 92, "史蒂夫": 74}
ma = 0
mi = 100
avg = 0
for key, value in temp.items():
    if ma < temp[key]:
        ma = temp[key]
    if mi > temp[key]:
        mi = temp[key]
    avg += temp[key]
print(ma, mi, avg / len(temp.keys()))

# 2.输入一个成绩序列，以字典形式输出对应等级的人数。
score = [45, 98, 65, 87, 43, 83, 68, 74, 20, 75, 85, 67, 79, 99]
# 等级 A:（90~100） B:(80~89)  C:(70~79) D:(70以下)
score.sort()
A = 0
B = 0
C = 0
D = 0
for i in score:
    if i < 70:
        D += 1
    elif i < 80:
        C += 1
    elif i < 90:
        B += 1
    elif i <= 100:
        A += 1
s = {"A": A, "B": B, "C": C, "D": D}
print(s)
