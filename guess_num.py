import random

real_num = random.randrange(10)
for i in range(6):
    guess_num = input("请输入你猜的数字：").strip()
    if len(guess_num) == 0:
        continue
    if guess_num.isalnum():
        guess_num = int(guess_num)
    if guess_num > real_num:
        print("错了，你猜的数字过大")
    elif guess_num < real_num:
        print("错了，你猜的数字过小")
    else:
        print("恭喜！猜对了！")
        break
else:
    print("真实数字为：", real_num)



