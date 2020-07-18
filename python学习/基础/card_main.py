from 基础 import card_menu

while True:

    card_menu.show_menu()

    # num = int(input("请输入选择："))
    # print("你输入的是%d " % num)
    # if num == 1:
    #     pass
    # elif num == 2:
    #     pass
    # elif num == 3:
    #     pass
    # elif num ==0:
    #     exit(0)

    action_str = input("请输入选择：")
    print("你输入的是%s " % action_str)

    if action_str in ["1", "2", "3"]:

        if action_str == "1":
            card_menu.add_card()
        elif action_str == "2":
            card_menu.query_card()
        elif action_str == "3":
            card_menu.search_card()

    elif action_str == "0":
        exit(0)
    else:
        print("请在(1,2,3,0)选择！！！！")
