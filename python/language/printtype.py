x = "abc"
y = 123
z = 3.14
b = True
c = False

def printtype(x):
    outstr = ""

    if type(x) is str:
        # print("The data type is string")
        outstr = "string"
    elif type(x) is float:
        #print("The data type is float")
        outstr = "float"
    elif type(x) is bool:
        #print("The data type is boolean")
        outstr = "boolean"
    elif type(x) is int:
        #print("The data type is integer")
        outstr = "integer"
    else:
        #print("The data type is unkwown")
        outstr = "unknown"
    
    print("The variable contains " + outstr +  " data type.")

    # return "The variable contains " + outstr +  " data type."


printtype(x)
printtype(y)
printtype(z)
printtype(b)
printtype(c)