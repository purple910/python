try:
    num = int(input("输入整数:"))
    result = 8 / num
    print(result)

except ZeroDivisionError:
    print("除零错误！！")
except ValueError:
    print("输入整数!!!")
except Exception as ex:
    print("错误信息：%s" % ex)
else:
    print("没有错误！！")
finally:
    print("end!!!")
