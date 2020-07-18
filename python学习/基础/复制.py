file1 = open("README")
file2 = open("README[1]", "w")

# 小文件
# file2.write(file1.read())

# 大文件
while True:
    text = file1.readline()

    if not text:
        break

    file2.write(text)

file1.close()
file2.close()
