"""
    @Time    : 2020/8/6 10:30 
    @Author  : fate
    @Site    : 
    @File    : pd1.py
    @Software: PyCharm
"""


# l1=[1,3,6,8,10,11,17]，请仅使用map,reduce,filter对l1依次进行如下三次操作：
#
# a.剔除掉所有的偶数后打印;
#
# b.对剩下的数字每个数字进行平方后打印;
#
# c.对数组求和后打印
# from functools import reduce
#
# l1 = [1, 3, 6, 8, 10, 11, 17]
#
# i = list(filter(lambda x: x % 2 == 1, l1))
# print(list(i))
# iterator = list(map(lambda x: x ** 2, i))
# print(list(iterator))
# print(reduce(lambda occ, x: occ + x, iterator))


# - 读取指定的文件，并使用split()函数以空白为字符串分隔得到文件中所有的单词。
#
# - 完成一个名为mimic_dict的函数：
# 以出现在文件中的单词(全都小写化)为键(key)，
# 文件中所有紧跟在单词后面的一个单词组成的列表为值(value)。
# 单词列表可以是任意顺序的，也可以包含重复的值。
# 例如，键“and”可能有列表["then", "best", "then", "after", ...]，
# 此列表包括了所有的文件中在'and'后面的单词

def mimic_dict(poem: list):
    # print(poem)
    p = {}
    v = []
    for i in range(len(poem)):
        # print(poem[i])
        for j in range(len(poem[i])-1):
            lower = poem[i][j].lower()
            # print(lower)
            if p.get(lower) is None:
                p[lower] = [poem[i][j+1]]
            else:
                p[lower].append(poem[i][j+1])
    print(p)


if __name__ == '__main__':

    with open('text', 'r', encoding='utf-8') as fp:
        s = fp.readlines()
        fp.close()
        file = []
        for i in s:
            i = i.replace("\n", "")
            if ',' in i:
                i = i.replace(',', '')
            if '.' in i:
                i = i.replace('.', '')
            # print(i)
            if '' is not i:
                l = i.split()
                file.append(l)
        # print(file)
        mimic_dict(file)
