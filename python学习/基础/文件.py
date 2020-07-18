# 打开文件
file = open("README", "r+")


# 读取文件
# text = file.read()
# print(text)

while True:
    text = file.readline()

    if not text:
        break

    print(text, end="")


# 写入文件
file.write("\ralabama")


# 关闭文件
file.close()
