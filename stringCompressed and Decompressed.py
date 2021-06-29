n = input('Put a Sequence :')
print('Compressed = ',end='')
p = len(n)
flag = 0
count = 1
pre = None
for i in range(p):
    if i == 0 :
        print(n[i],end='')
        pre = n[i]
    elif i > 0 and n[i] != pre:
        if count == 1:
            print(n[i], end='')
        else:
            print('{}{}'.format(count,n[i]),end='')

        pre = n[i]
        count = 1

    elif i > 0 and n[i] == pre:
        count = count + 1
if count != 1:
    print(count)

print()

n2 = input('Put a compressed string:')
print("Decompreseed = ",end='')
p2 = len(n2)
for i in range(p2):
    if n2[i].isalpha():
        print(n2[i],end='')
    elif n2[i].isnumeric():
        x = int(n2[i])
        if x == 1:
            print(x,end='')
        else:
            for j in range(1,x):
                print(n2[i-1], end='')


