a, b, c = 3, 2, 3

# 1.
if a > b:
    c = a
else:
    c = b
print(c)

# 2.
c = a if a > b else b
print(c)

# 3.
c = [b, a][a > b]
print(c)

# 4.
c = (a > b and [a] or [b])[0]
print(c)
# 改编版
c = (a > b and a or b)
print(c)

# 从前往后找，and找假，or找真
# 前真返后，
print(111 and 222)  # 222
# 前假返前
print(0 and 333)  # 0
# 若x真【x】, x假,y真【y】，xy假【y】,只有前真返回前
print(111 or 222)  # 111
print(0 or 222)  # 222
print('' or 0)  # 0
