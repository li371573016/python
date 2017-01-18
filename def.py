'''
def mark(n):
    def action(x):
        return x / n
    return action
f = mark(2)
print(f(4))

def f1():
    x = 88
    f2(x)
def f2(x):
    print(x)
f1()
'''
"""
x = 99
def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()
"""
'''
def f1():
    x = 99
    def f2():
        def f3():
            print(x)
        f3()
    f2()
f1()
'''

