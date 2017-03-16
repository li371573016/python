salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("invaid data type" )
welcome_msg = "Welcome to my shopping".center(100,'-')
print(welcome_msg)
shopping_list = [
    ("iphone",5999),
    ("thinkpad",4999),
    ("watch",19999),
    ("xiaomi",899),
    ("apple watch",3999),
    ("huawei",1699)
]
flag = False
shopping_buy = []
while not flag:
    print("shopping list".center(100,'-'))
    for item in enumerate(shopping_list):
        index = item[0]
        shopping_name = item[1][0]
        shopping_price = item[1][1]

        print(index,'.',shopping_name,shopping_price)
    user_choice = input("[q=quit,c=check]what do you want to buy?:")
    if user_choice.isdigit():#判断是否是数字
        user_choice = int(user_choice)
        if user_choice < len(shopping_list):
            product_item = shopping_list[user_choice]
            if product_item[1] <= salary:#钱是否够
                shopping_buy.append(product_item)#选择的商品放入购物车
                salary -= product_item[1]#余下多少钱
                print("you buy \033[44;37m%s\033[0m into shopping_buy,current balance is \033[41;36m%s\033[0m" %(product_item,salary))
            else:
               # print("your balance is", salary)
                print("your balance is %d" %salary)
    else:
        if user_choice == 'q' or user_choice == 'quit':
            print("buy products list".center(100,'*'))
            for shopping in shopping_buy:
                print(shopping)
            print("end".center(100,'*'))
            print("your balance is \033[40;32m%d\033[1m" %salary)
            flag = True
        elif user_choice == 'c' or user_choice == 'check':
            print("buy products list".center(100,'*'))
            for shopping in shopping_buy:
                print(shopping)
            print("end".center(100,'*'))
            print("your balance is \033[40;32m%d\033[1m" %salary)


