card_list = []


def show_menu() -> object:
    """显示菜单"""
    print("*" * 49)
    print("")
    print("1.新增名片")
    print("2.查询全部")
    print("3.搜索名片")
    print("0.退出系统")
    print("")
    print("*" * 49)


def add_card() -> object:
    """查询全部"""
    name = input("请输入名字：")
    age = input("请输入年纪：")
    email = input("请输入邮箱：")

    card_dict = {
        "name": name,
        "age": age,
        "email": email
    }

    card_list.append(card_dict)
    print(card_list)
    print("已经添加 %s" % name)


def search_card() -> object:
    """搜索名片"""
    print("-" * 49)

    find_name = input("请输入查找的名字：")

    for card_dict in card_list:
        if find_name == card_dict["name"]:
            print("name\t\tage\t\temail\t\t")
            print("=" * 49)
            print("%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["age"], card_dict["email"]))

            deal_card(card_dict)
            break
    else:
        print("没有此人！！")


def query_card() -> object:
    """查询全部"""
    if len(card_list) == 0:
        print("没有名片,请添加！！！")
        return

    for name in ["name", "age", "email"]:
        print(name, end="\t\t")
    print("")
    print("-" * 49)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t" % (card_dict["name"], card_dict["age"], card_dict["email"]))


def deal_card(find_card) -> object:
    """
    修改名片
    :param find_card: 名片信息
    """
    print(find_card)
    action_str = input("请输入操作：[1]修改  [2]删除  [0]返回:")

    if action_str == "1":
        # find_card["name"] = input("name:")
        # find_card["age"] = input("age:")
        # find_card["email"] = input("email:")

        find_card["name"] = input_card(find_card["name"], "name[回车不修改]:")
        find_card["age"] = input_card(find_card["age"], "age[回车不修改]:")
        find_card["email"] = input_card(find_card["email"], "email[回车不修改]:")

    elif action_str == "2":
        card_list.remove(find_card)


def input_card(dict_value, tip_message) -> object:
    """
    输入名片
    :param dict_value:原有值
    :param tip_message:输入提示
    :return:dict_value or tip_message
    """
    result_str = input(tip_message)
    if len(result_str) == 0:
        return dict_value
    else:
        return result_str
