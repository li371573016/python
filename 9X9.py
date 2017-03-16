#左下三角格式：

for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d" %(i,j,i*j),end='\t')
    print("")
print("间隔符".center(105,"*"))

#左上三角格式：

for i in range(1,10):
    for j in range(i,10):
        print("%d * %d = %d" %(i,j,i*j),end='\t')
    print("")
print("间隔符".center(105,"*"))

#右上三角格式：

for i in range(1,10):
    for k in range(1,i):
        print (end="       ")
    for j in range(i,10):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print("")
print("间隔符".center(105,"*"))
#右下三角格式：

for i in range(1,10):
    for k in range(1,10-i):
        print(end="       ")
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print(" ")
print("间隔符".center(105,"*"))

#矩形格式：

for i in range(1,10):
    for j in range(1,10):
        print("%d*%d=%2d" %(i,j,i*j),end="\t")
    print("")



