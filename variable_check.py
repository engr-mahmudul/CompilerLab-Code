import string
str1 = { 'int','float','double','char','string'}
str2 = { '!','@','#','$','%','^','&','*','(',')','_','+',' '}
flag = True
while True:
    try:
        n = input()
        if n in str1 and str2:
            print('Not valid')
        #elif n[0].isdigit():
                    #print('This is number')
        k = len(n)
        elif len(n)< 32:
            if n[0] == '_' or (n >= 'A' and n <= 'Z') or (n >= 'a' and n <= 'z'):
               for j in range(1,len(n)):
                   if n[j] in str2:
                       flag = False
               if flag == False:
                   print('Invalid')
               else:
                   print('Valid')
            else:
                print('Not Valid')

        else:
            print('Not valid')
        flag = True

    except EOFError:
        break

