"""
    @Time    : 2020/2/22 10:49
    @Author  : fate
    @Site    : 
    @File    : __init__.py.py
    @Software: PyCharm
"""

print("******************欢迎来到WoniuATM********************")
print("*******************请选择操作菜单*********************")

# user_list = [{'name': 'zs', 'password': '123456', 'balance': 1000}]
user_list = []
with open('atm.txt', 'r') as fp:
    u = eval(fp.readline())
    user_list.append(u)
    fp.close()

isLogin = False
u = {}


def getUser(name):
    for i in user_list:
        if i.get('name') == name:
            arr = {'name': i['name'], 'password': i['password'], 'balance': i.get('balance')}
            return arr
    return None


def delBalance(num):
    if num % 100 == 0:
        if num <= u['balance']:
            u['balance'] = u['balance'] - num
            for i in user_list:
                if i['name'] == u['name']:
                    i['balance'] = i['balance'] - num
                    return 1
        else:
            print('余额不足!!')
            return 0
    else:
        print('存取款要求只能是100的整数倍')
        return 0


def addBlance(dict, num):
    dict['balance'] = dict['balance'] + num
    for i in user_list:
        if i['name'] == dict['name']:
            i['balance'] = i['balance'] + num
            break


while True:
    print(" *********1. 注册 2. 登录 3. 查询余额  4. 存款  5. 取款   6.转账   7.取卡 *******")
    temp = int(input("请输入:"))
    if temp == 1:
        while True:
            name = input("name:")
            if getUser(name) is not None:
                print("用户名已经存在,请重新输入!!")
                continue
            password = input("password:")
            if len(password) < 6:
                print("密码长度要大于等于6位!!")
                continue
            balance = int(input("balance:"))
            if balance < 0:
                print("余额不可以为负数!!")
                continue
            user = {'name': name, 'password': password, 'balance': balance}
            user_list.append(user)
            # print(user_list)
            break
    elif temp == 2:
        if isLogin:
            print('已经有用户在登录')
            continue
        while True:
            name = input("name:")
            arr = getUser(name)
            # print(arr)
            if arr is None:
                print('用户不存在')
                continue
            password = input("password:")
            if arr['password'] != password:
                print('密码不正确')
                continue
            u = arr
            isLogin = True
            print('登录成功')
            # print(u)
            break
    elif temp == 3:
        if isLogin:
            print('{}的余额:{}'.format(u['name'], u['balance']))
        else:
            print('你还未登录!!')
    elif temp == 4:
        if isLogin:
            num = int(input('请输入存款金额:'))
            if num % 100 == 0:
                addBlance(u, num)
            else:
                print('存取款要求只能是100的整数倍')
        else:
            print('你还未登录!!')
    elif temp == 5:
        if isLogin:
            num = int(input('输入取款金额:'))
            if delBalance(num) == 1:
                print('取款成功')
        else:
            print('你还未登录!!')
    elif temp == 6:
        if isLogin:
            un = input('请输入要转账的用户名:')
            arr = getUser(un)
            if arr is not None:
                num = int(input('输入转账金额:'))
                if delBalance(num) == 1:
                    addBlance(arr, num)
            else:
                print('用户不存在')
        else:
            print('你还未登录!!')
    elif temp == 7:
        isLogin = False
        u.clear()
        with open('atm.txt','w+') as fp:
            for i in user_list:
                fp.write(str(i))
                fp.write('\n')
            fp.close()
        break
    else:
        print("输入错误!!")
