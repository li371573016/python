number,guess = 7,-1
print("数字猜谜游戏")
while (guess != number):
	guess = int(input("请输入你猜的数字："))
	if (guess == number):
		print("恭喜，你猜对了！")
	elif (guess < number):
		print("数字猜小了。。。。")
	elif (guess > number):
		print("数字猜大了。。。")
	