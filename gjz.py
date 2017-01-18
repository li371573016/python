def person(name,age,*,city,job):
	print(name,age,city,job)
person('jack',25,city='beijing',job='it')

def person1(name, age, **kw):
	print('name:', name,'age:',age, 'other:',kw)
person1('machael',30)