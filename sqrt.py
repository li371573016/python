'''
请定义一个函数 ’quadratic(a,b,c)‘，接收三个参数，返回一元二次方程: 
ax² + bx + c = 0 
的两个解。（提示：计算平方根可以调用math.sqrt()函数）
'''
import math
def quadratic(a,b,c):
#	if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
	if not isinstance(a,(int,float)):
		raise TypeError('Bad operand type')
	if not isinstance(b,(int,float)):
		raise TypeError('Bad operand type')
	if not isinstance(c,(int,float)):
		raise TypeError('Bad operand type')
	d = b*b-4*a*c
	if (a == 0):
		if (b == 0):
			if (c == 0):
				return "方程为全体实数"
			else:
				return "方程无解"
		else:
			x1 = - c/b
			x2 = x1
			return x1,x2
	else:
		if (d < 0):
			return "方程无解"
		elif (d == 0):
			x1 = x2 = -b/(2*a)
			return x1,x2
		else:
			x1 = (-b + math.sqrt(d))/2/a 
			x2 = (-b - math.sqrt(d))/2/a
			return x1,x2
a = int(input("请输入a:"))
b = int(input("请输入b:"))
c = int(input("请输入c:"))

print(quadratic(a,b,c))