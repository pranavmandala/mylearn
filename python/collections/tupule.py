l = []


'''
Definite loop
i = 0
while i < 5:    
    input_num = input("Enter a number   ")
    l.append(int(input_num))

    i = i + 1
'''

flag = True
while flag:    
    input_num = input("Enter a number   ")
    l.append(int(input_num))

    hasMore = input("Do you want to enter more number. Enter Y/N   ")
    flag = bool(hasMore == 'Y')


print(l)
