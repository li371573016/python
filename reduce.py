from functools import reduce
def fn(x,y):
	return x*10+y
print(reduce(fn, [1,2,3,4,5]));


def times(x,y):
	print(x*y)
times(100,6);

