import re
operator = {'+','-','*','/'}
list2 = []
list3 = []

def calculation(list):
    n = len(list)

    for i in range(n):
        if list[i] == '/':
            a = int(list[i - 1])
            b = int(list[i + 1])
            list[i - 1] = str(a / b)

            list[i] = 0
            list[i + 1] = 0
        elif list[i] == '*':
            a = int(list[i - 1])
            b = int(list[i + 1])
            list[i - 1] = str(a * b)

            list[i] = 0
            list[i + 1] = 0
        elif list[i] == '-':
            a = int(list[i - 1])
            b = int(list[i + 1])
            list[i - 1] = str(a - b)

            list[i] = 0
            list[i + 1] = 0
        elif list[i] == '+':
            a = int(list[i - 1])
            b = int(list[i + 1])
            list[i - 1] = str(a / b)

            list[i] = 0
            list[i + 1] = 0
        return list

while True:
    try:
        line = input('Put here a line:')

        list = re.findall(r'\S+', line)
        n = len(list)

        list3 = calculation(list)

        '''for j in list:

            if j != 0:
                list2.append(j)
        list = list2'''

        print(list3)
        list.clear()













    except EOFError:
        break