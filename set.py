# set  无序，不重复 ，可嵌套
'''
student = {'tom' , 'jim' , 'merry' , 'jack' , 'rose'}
print(student)
if('rose' in student):
	print('rose在集合中')
else:
	print('rose在集合中')

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
print ("我叫 %s 今年 %d 岁!" %('小明', 10))
for x in [1, 2, 3]:
	print(x)
'''

# name = {}#空集合
# print(name)
# s = set()
# s1 = set([1,2,3,4,5,6,7])
# s1.clear()#清除集合
# s.add(12135)#增加元素
# print(s1,s)
# li = [1,2,3]
# li.insert(1,4)
# print(li)
s1 = {1,2,3,4}
s2 = {2,3,4,5}
# s = s1.difference(s2)#A中存在B中不存在的元素
# s3 = s1.symmetric_difference(s2)#取出2个集合中非交集的元素
#
# s1.discard(4)#移除s1中指定元素
# s2.remove(5)
#
# print(s,s2)
# print(s3,s1)
s3 = s1.intersection(s2)#取交集
print(s3)