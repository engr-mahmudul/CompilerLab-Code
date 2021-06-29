str1 = {'for','while','if','else','break','continue','int','float','string','double'}
str2 = { '+','-','*','/','=','==','<=','>=','!','!=','<','>','++'}
str3 = {'(',')',',','{','}',';','#'}
keyword = []
operator = []
number = []
variable = []
keyword1 = []
operator1 = []
number1 = []
variable1 = []
word = []
list1 = []
list2 = []
import re
while True:
    try:
        line = input('Put here a line:')
        print("After seperating :", end='')
        list2 = line.split(";;")
        print(list2)
        print(list2)
        for word in list2:
            if word in str1:
                keyword1.append(word)
            elif word in str2:
                operator1.append(word)

            elif word.isnumeric():

                number1.append(word)
            else:
                if word in str3:
                    pass

                else:
                    variable1.append(word)




        print()

        #print('keyword :', keyword1)
        #print('operator :', operator1)
        print('variable :',variable1)
        print('number :',  number1)
        keyword1.clear()
        operator1.clear()
        number1.clear()
        variable1.clear()



    except EOFError:
        break