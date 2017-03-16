name = "my name is {0},age is {1}".format("lilong",28)
name1 = "my name is {0},age is {1}".format(*["lilong",28])
name2 = "my name is {name},age is {age}".format(name="lilong",age=28)
dic = {"name":"lilong","age":28}
name3 = "my name is {name},age is {age}".format(**dic)

print(name)
print(name1)
print(name2)
print(name3)
print("%s, %s ,%s, %s" %(name,name1,name2,name3))

