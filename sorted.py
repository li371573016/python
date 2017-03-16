L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(a):
    print(a[0])
    return a[0]

def by_sore(a):
    print(a[1])
    return a[1]

x = sorted(L,key = by_name)
y = sorted(L,key = by_sore,reverse = True)
print('按姓名排:',x)
print('按成绩排:',y)
def f1(x,y):
    return x+y

z = f1(3,6)
print(z)
print(L[0])