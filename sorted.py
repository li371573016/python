L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(a):
    return a[0]

def by_sore(a):
    return a[1]

x = sorted(L,key = by_name)
y = sorted(L,key = by_sore,reverse = True)
print('按姓名排:',x)
print('按成绩排:',y)