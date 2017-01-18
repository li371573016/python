'''
height = float(input('请输入身高：'))

weight = float(input('请输入体重:'))

bmi = float(weight/(height*height))



if bmi >= 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height = float(input('Please enter your height:'))
weight = float(input('Please enter your weight:'))

bmi = float(weight/(height*height))

if bmi >= 32:
    print('你的身高:',height,'米,你的体重:',weight,'KG,您超胖')
elif bmi >= 28:
    print('你的身高:',height,'米,你的体重:',weight,'KG,您肥胖')
elif bmi >= 25:
    print('你的身高:',height,'米,你的体重:',weight,'KG,您过重')
elif bmi >= 18.5:
    print('你的身高:',height,'米,你的体重:',weight,'KG,您正常')
else:
    print('你的身高:',height,'米,你的体重:',weight,'KG,您过轻')