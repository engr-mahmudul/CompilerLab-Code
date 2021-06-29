sstr = []
mstr = input('Put a string: ')
sstr = input('Put a sub string :')
array = []
for i in range(len(sstr)):
    array[i] = mstr.count(sstr[i])
max = 9999
for j in range(len(array)):
    if array[j]< max:
        max = array[j]
print(max)

'''main string===  yyytttkkk
                                array[y=10 , t=8 , k= 2]
    substring ====   ytk  '''
