real_num = 25
count = 0

for i in range(10):
    if count < 3:
        guess_num = input("请输入你猜的数字：").strip() #过滤空格和enter字符
        if len(guess_num) == 0:
            continue
        if guess_num.isdigit(): #判断是否为数字
            guess_num = int(guess_num)
        else:
            print("你需要输入一个真正的数字--")
            continue

        if guess_num > real_num:
            print("你猜的数字过大--")

        elif guess_num < real_num:
            print("你猜的数字过小--")
        else:
            print("恭喜猜对了--")
            break
    else:
        #print("猜的次数过多：")
       # break
        continue_confirm = input("请继续输入继续请输入y或者Y：")
        if continue_confirm == "y" or continue_confirm == "Y" :
            count = 0
            continue
        else:
            print("bye")
            break
    count += 1
