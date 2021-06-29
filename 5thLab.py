import re
operator = {'+','-','*','/'}
list2 = []
while True:
    try:
        line = input('Put here a line:')

        list = re.findall(r'\S+', line)
        n = len(list)

        for i in range(n):
            if list[i] == '/':
                a = int(list[i - 1])
                b = int(list[i + 1])
                list[i - 1] = str(a/b)



                list [i] = 0
                list[i + 1] = 0
            '''elif list[i] == '*':
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
                list[i - 1] = str(a + b)

                list[i] = 0
                list[i + 1] = 0'''

        for j in list:

            if j != 0:
                list2.append(j)
        list = list2

        print(list2)
        list.clear()













    except EOFError:
        break