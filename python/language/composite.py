input_num = input("Enter a number: ")

def isComposite(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                return True

        return False

    else: 
        return False 

def composite(x):
    compList = []
    for i in range(x + 1):
        if isComposite(i):
            compList.append(i)

    return compList

list = composite(input_num)
print(list)