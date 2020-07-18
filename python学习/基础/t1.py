# 生成器 可以面对大数据的数据流动
def gen(n):
    for i in range(n):
        yield i ** 2


print(gen(5))
print(type(gen(5)))
for i in gen(5):
    print(i, " ", end="")


print()


# 列表解析
def square(n):
    ls = [i ** 2 for i in range(n)]
    return ls


print(square(5))
print(type(square(5)))
for i in square(5):
    print(i, " ", end="")


print()
L = [i**2 for i in range(1, 11) if i >= 4]
print(L)


L1 = ['x', 'y', 'z']
L2 = [1, 2, 3]
L3 = [(a, b) for a in L1 for b in L2]
print(L3)
