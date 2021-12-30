"""

"""


"""
This function returns a string for any given character (default space) of length.
Parameters:
len   length of the returned string  
char(optional)  desired character in a string
"""
def prepareStr(len, char=" "):
    sp = ""

    for i in range(0, len):
        sp = sp + char
        
    return sp


def subtract(x,y):
    # Determine the difference between minuend(x) and subtrahend(y)
    output = int(x) - int(y)

    # Adding two more spaces for subtraction sumbol
    maxlen = len(str(output)) + 2
    # Concatenating space and minuend
    displayX = prepareStr(maxlen - len(x)) + x
    # Concatenating space and subtrahend
    displayY = "-" + prepareStr(maxlen - len(y) - 1) + y
    # Concatenating space and output
    displayO = prepareStr(2) + str(output)

    # Displaying the Subtraction
    print("5\nSubtraction")
    # Displaying the minuend(x) and subtrahend(y)
    print(displayX)
    print(displayY)
    # Displaying the dashed line
    print(prepareStr(maxlen,"-"))
    # Displaying the output
    print(displayO)
    # Displaying the dashed line
    print(prepareStr(maxlen,"-"))


def add(x,y):
    # Determine the sum of the Addend(x) and Addend(y)
    output = int(x) + int(y)

    # Assuming sum as maxlen of addition
    # Adding two more spaces for addition symbol
    maxlen = len(str(output)) + 2
    # Concatenating space and addend
    displayX = prepareStr(maxlen - len(x)) + x
    # Concatenating addition symbol, space, and addend
    displayY = "+" + prepareStr(maxlen - len(y) - 1) + y
    # Concatenating space and output
    displayO = prepareStr(2) + str(output)

    # Displaying the addition
    print("\nAddition")
    # Displaying the addend and addend
    print(displayX)
    print(displayY)
    # Displaying dashed line
    print(prepareStr(maxlen,"-"))
    # Displaying output
    print(displayO)
    # Displaying dashed line
    print(prepareStr(maxlen,"-"))


def multiply(x,y):
    # Determine the product of the Multiplicand(x) and Multiplier(y).
    output = int(x) * int(y)

    # Assumming product as the max length of total multiplication.
    # Adding two more spaces for multiplication symbol.
    maxlen = len(str(output)) + 2
    # Concantenating space and multiplicand.
    displayX = prepareStr(maxlen - len(x)) + x
    # Concantenating multiplication symbol, space, and multiplier.
    displayY = "x" + prepareStr(maxlen - len(y) - 1) + y
    # Concantenating space and output.
    displayO = prepareStr(2) + str(output)

    # Displaying the multiplication
    print("\nMultiplication")
    # Displaying multiplicand and multiplier
    print(displayX)
    print(displayY)
    
    # Displaying the work when multiplier is more than one digit.
    if len(y) > 1:
        # Displaying dashed line
        print(prepareStr(maxlen,"-"))
        # Creating a variable for index of multiplier array as we are looping via values.
        i = 0
        # Loop string multiplier as an array
        for d in y:
            # Find the product of each multiplier digit
            t1 = str(int(x) * int(d))
            # Display the intermediate products - space + product + space 
            print(prepareStr(maxlen - len(t1) - i) + t1 + prepareStr(i))
            # Increment the index.
            i = i + 1

    # Displaying dashed line.
    print(prepareStr(maxlen,"-"))
    # Displaying the output.
    print(displayO)
    # Displaying dashed line.
    print(prepareStr(maxlen,"-"))


def division(x,y):
    # Determine the quotient of Dividend(x) and Divisor(y)
    output = int(x) / int(y)

    # Adding two more spaces for division symbol
    maxlen = max(len(x), len(y))
    # Concatenating space and dividend
    displayX = prepareStr(maxlen - len(x)) + x
    # Concatenating space and divisor
    displayY = prepareStr(maxlen - len(y)) + y
    # Concatenating space and output
    displayO = str(output)

    # Displaying division
    print("\nDivision")
    # Displaying X
    print(displayX)
    # Getting the number of dashes for the difference
    print(prepareStr(maxlen,"-") + " = " + displayO)
    # Displaying Y
    print(displayY)



x = raw_input("Enter a number:")
y = raw_input("Enter a number:")

x = x.replace("\r", "")
y = y.replace("\r", "")

add(x, y)
subtract(x, y)
multiply(x, y)
division(x, y)





