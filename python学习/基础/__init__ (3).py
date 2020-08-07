"""
    @Time    : 2020/8/5 14:55 
    @Author  : fate
    @Site    : 
    @File    : __init__.py.py
    @Software: PyCharm
"""
# 用python编写一个ATM存取款机的模拟程序，要求如下：
# 1. 添加如下操作主菜单，并实现菜单中的每个功能。
#                  ******************欢迎来到WoniuATM********************
#                    *******************请选择操作菜单*********************
#     *********1. 注册 2. 登录 3. 查询余额  4. 存款  5. 取款   6.转账   7.取卡 *******
# 注意：存取款要求只能是 100 的整数倍。
# 2. 注册时，判断用户名是否已存在，密码长度要大于等于6位，如果输入错误要有相应提示。
# 登录时，要求用户输入用户名和密码，只有当用户名和密码均正确才能提示用户登录成功，否则提示用户名或密码错误。
# 注意，不管是注册阶段还是登录阶段，一旦用户输入错误，都将提示用户重新输入，直到正确为止。
#
# 用户信息分别包含姓名、密码以及余额，保存格式如下：
# user_list = [{'name': 'zhangsan', 'password':'123', 'balance': 0}, {}, {}, ...]
# login_user
# pep8 规范
# 自顶向下的编程方法

login_user = None
user_list = [{'name': 'zhangsan', 'password': '123', 'balance': 1000}]


def operate_atm():
    """
    操作 atm 机函数，由 atm 的所有的功能
    1. 显示操作菜单
    2. 接受用户输入，选择操作菜单
    3. 根据用户选择的菜单，执行对应的功能
    4. 如果用户没有选择取卡操作，继续回到第 1 步
    :return:
    """
    while True:
        # 1. 注册 2. 登录 3. 查询余额  4. 存款  5. 取款   6.转账   7.取卡
        show_menu()
        selection = input("")
        if selection == '1':
            register()
        elif selection == '2':
            login()
        elif selection == '3':
            check_balances(login_user)
        elif selection == '4':
            if login_user:
                deposit(login_user)
            else:
                print("请先登录")
        elif selection == '5':
            if login_user:
                withdrawal(login_user)
            else:
                print("请先登录")
        elif selection == '6':
            if login_user:
                transfer(login_user)
            else:
                print("请先登录")
        elif selection == '7':
            if login_user:
                exit()
            else:
                print("请先登录")
        else:
            print("请选择正确的操作")
    pass  # pass 语句表示什么都不做，只是占位使用


def show_menu():
    """
    显示 atm 机的操作菜单
                  ******************欢迎来到WoniuATM********************
                  *******************请选择操作菜单*********************
     *********1. 注册 2. 登录 3. 查询余额  4. 存款  5. 取款   6.转账   7.取卡 *******
    :return:
    """
    menu = '''                  ******************欢迎来到WoniuATM********************
                  *******************请选择操作菜单*********************
     *********1. 注册 2. 登录 3. 查询余额  4. 存款  5. 取款   6.转账   7.取卡 *******
    '''
    print(menu)
    pass


# 1. 注册 2. 登录 3. 查询余额  4. 存款  5. 取款   6.转账   7.取卡
def register():
    """
    完成用户注册的逻辑
    1. 提示用户输入用户名和密码 （接受用户输入）
    2. 检查用户输入的用户名和密码是否正确 （检查用户输入）
        2.1 检查用户名是否重复
        2.2 检查密码是否大于等于 6 位
        2.3 如果检查通过进行第 3 步，否则提示错误信息，回到第1步
    3. 处理注册的业务逻辑 （处理业务逻辑）
        3.1 把用户名和密码添加到用户信息存储的列表中
    :return:
    """
    while True:
        username = input("请输入用户名")
        password = input("请输入密码")
        if len(password) < 6:
            print("密码长度必须大于6位")
            continue
        for user_info in user_list:
            if username == user_info["name"]:
                print("用户名已经存在")
                break
        else:
            # 密码长度满足要求，并且用户名不重复
            break
    user_list.append({'name': username, 'password': password, 'balance': 0})
    print(f"{username}注册成功!")
    pass


def login():
    """
    完成用户登录的逻辑
    1. 接受用户输入，提示用户输入用户名和密码
    2. 检查用户输入（无）
    3. 处理业务逻辑
        3.1 检查用户名和密码是否和存储列表中的信息匹配
        3.2 如果正确，保持登录状态，把用户登录信息存起来
        3.3 如果错误，提示错误信息，回到第 1 步
    :return:
    """
    global login_user
    while True:
        username = input("请输入用户名")
        password = input("请输入密码")

        for user_info in user_list:
            if username == user_info['name'] and password == user_info['password']:
                login_user = username
                print(f"{username}登录成功！")
                break
        else:
            print("用户名或者密码不正确")
            continue

        # 当用户名密码输入正确，登录成功跳出 while 循环
        break
    pass


def check_balances(username):
    """
    完成查询指定用户的账户余额的逻辑
    1. 检查用户是否已经登录，如果没有登录提示错误信息，返回操作菜单
    2. 如果用户已经登录，从存储用户信息的列表中获取用户的余额，打印余额信息
    :param username: 用户名
    :return:
    """
    if not username:
        print("请先登录账户，再查询账户余额!")
        return None
    for user_info in user_list:
        if user_info["name"] == username:
            print(f"{username}的账户余额为{user_info['balance']}")
            break
    pass


def deposit(username):
    """
    完成存款的逻辑
    1. 接受用户输入，提示输入存款的金额
    2. 检查用户输入，检查存款金额是否是 100 的整数倍，如果有错误，重新输入
    3. 处理业务逻辑，把存款的金额添加到用户信息存储列表中
    :param username: 存款的账户
    :return:
    """
    count = input_count()

    for user_info in user_list:
        if user_info['name'] == username:
            user_info['balance'] += count
            print(f"{username}账户余额为{user_info['balance']}")
    pass


def input_count():
    while True:
        count = input("请输入存款金额")
        if len(count) < 3:
            print("请输入100的整数倍")
            continue
        if not '1' <= count[0] <= '9':
            print("请输入100的整数倍")
            continue
        for c in count[1:]:
            if not '0' <= c <= '9':
                print("请输入100的整数倍")
                break
        else:
            # count 字符可以转换为整数
            count = int(count)
            if count % 100 != 0:
                print("请输入100的整数倍")
                continue
            else:
                break
    return count


def withdrawal(username):
    """
    完成取款的逻辑
    1. 接受用户输入，提示输入取款的金额
    2. 检查用户输入，检查取款金额是否是 100 的整数倍，如果有错误，重新输入
    3. 处理业务逻辑
        3.1 检查取款金额是否大于余额，如果比余额大，提示错误信息，重新输入
        3.2 把取款的金额从用户信息存储列表中减掉
    :param username: 取款的账户
    :return:
    """
    while True:
        count = input_count()
        user_info = find_user_info(username)
        if user_info["balance"] < count:
            print(f"余额不足{count}")
            continue
        else:
            break
    user_info['balance'] -= count
    print(f"取款成功，{username}账户余额还剩{user_info['balance']}")
    pass


def find_user_info(username):
    """
    从用户信息存储列表中查找用户信息存储的字典
    :param username:
    :return:
    """
    for user_info in user_list:
        if user_info["name"] == username:
            return user_info
    else:
        return None


def transfer(username):
    """
    完成转账的逻辑
    1.接受用户输入，输入收款人的账户信息，转账的金额
    2.检查用户的输入
        2.1 检查收款人的账户是否存在，如果不存在提示错误信息，重新输入
        2.2 检查转账的金额是否大于当前账户的余额，如果比余额大，提示错误信息
    3.处理转账的业务逻辑
        3.1 如果没有问题，从当前账户中扣掉转账的金额
        3.2 在收款人的账户中添加上转账的金额
    :param username: 转账的账户
    :return:
    """
    while True:
        to_account = input("请输入收款人的账户信息")
        to_account_user_info = find_user_info(to_account)
        if to_account_user_info is None:
            print("收款人账户信息不存在")
            continue
        else:
            break

    _pass = True
    while _pass:
        count = input("请输入转账金额")
        try:
            count = int(count)
        except:
            print("转账金额请输入整数")
            pass
        else:
            user_info = find_user_info(username)
            if count < user_info["balance"]:
                _pass = False

    to_account_user_info['balance'] += count
    user_info = find_user_info(username)
    user_info['balance'] -= count
    print(f"{username}的账户余额为{user_info['balance']},"
          f"{to_account_user_info['name']}的账户余额为{to_account_user_info['balance']}")

    pass


def exit():
    """
    取卡，退出操作 atm 机
    注销用户登录
    :return:
    """
    global login_user
    login_user = None
    pass


if __name__ == '__main__':
    operate_atm()
