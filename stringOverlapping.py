
import re

a = input('string 1 :')
b = input('string 2 :')
#c = input('string 3 :')

final_str = ''
final_str2 = ''
res = ''
res2 = ''

for char in range(len(a)):

    if b.startswith(a[char:]):
        res = a[char:]
        break

#print('res is =',res)
if res in a:
    a = a.replace(res,'')
if res in b:
    b = b.replace(res,'')

if  not res:
    final_str = a+b
else:
    final_str = a+res+b


'''for char1 in range(len( final_str)):

    if c.startswith( final_str[char1:]):
        res2 =  final_str[char1:]
        break
if res2 in final_str:
    final_str = final_str.replace(res2,'')
if res in c:
    c = c.replace(res2,'')

if  not res2:
    final_str2 = final_str+c
else:
    final_str2 = final_str+res+c'''
print(final_str)