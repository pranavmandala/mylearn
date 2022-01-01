def heading(heading):
    print("\n")
    print(heading)
    print("=" * 50)

def checkif(val):
    if val:
        print("if {} is True when {} type is {}".format(val, val, type(val)))
    else:
        print("if {} is False when {} type is {}".format(val, val, type(val)))

# Boolean to String
heading("Boolean to String")
x = True
y = False
z = str(x)
print("Intial Value {} -> Type {}".format(x, type(x)))
print("Converted Value {} -> Type {}".format(z, type(z)))
print("{} == {} (Boolean) is {}".format(z, x, z == x))
# True as a string is not the same as True as a boolean value
print("{} == \"{}\" (String) is {}".format(z, "True", "True" == z))


# Boolean to Number
heading("Boolean to Number")
z = int(x)
print("Intial Value {} -> Type {}".format(x, type(x)))
print("Converted Value {} -> Type {}".format(z, type(z)))
z = int(y)
print("Intial Value {} -> Type {}".format(y, type(y)))
print("Converted Value {} -> Type {}".format(z, type(z)))

# Boolean to Float
heading("Boolean to Float")
z = float(x)
print("Intial Value {} -> Type {}".format(x, type(x)))
print("Converted Value {} -> Type {}".format(z, type(z)))
z = float(y)
print("Intial Value {} -> Type {}".format(y, type(y)))
print("Converted Value {} -> Type {}".format(z, type(z)))

# String to Number
heading("String to Number")
string = ("1")
# we cannot change because the string value to a number if it is a word
newstring = int(string)
print("Intial Value {} -> Type {}".format(string, type(string)))
print("Converted Value {} -> Type {}".format(newstring, type(newstring)))

# String to Float
heading("Stringn to Float")
newstring = float(string)
print("Intial Value {} -> Type {}".format(string, type(string)))
print("Converted Value {} -> Type {}".format(newstring, type(newstring)))

# String to Boolean
s1 = "abc"
s2 = ""
s3 = " "
heading("String to Boolean")
newstring = bool(s1)
print("Intial Value {} -> Type {}".format(s1, type(s1)))
print("Converted Value {} -> Type {}".format(newstring, type(newstring)))
newstring = bool(s2)
print("Intial Value {} -> Type {}".format(s2, type(s2)))
print("Converted Value {} -> Type {}".format(newstring, type(newstring)))
newstring = bool(s3)
print("Intial Value {} -> Type {}".format(s3, type(s3)))
print("Converted Value {} -> Type {}".format(newstring, type(newstring)))

# Number to Boolean
# 0 is converted to False
# > 1 is converted to True
heading("Number to Boolean")
num0 = 0
num1 = 1
num2 = 2
newnum = bool(num0)
print("Intial Value {} -> Type {}".format(num0, type(num0)))
print("Converted Value {} -> Type {}".format(newnum, type(newnum)))
newnum = bool(num1)
print("Intial Value {} -> Type {}".format(num1, type(num1)))
print("Converted Value {} -> Type {}".format(newnum, type(newnum)))
checkif(num0)
checkif(num1)
checkif(num2)

# Number to Float
heading("Number to Float")
newf = float(num1)
print("Intial Value {} -> Type {}".format(num1, type(num1)))
print("Converted Value {} -> Type {}".format(newf, type(newf)))
print("{} (int) == {} (float) is {}".format(num1, newf, num1 == newf))

# Float to String
heading("Float to String")
f = 1.0
newf = str(num0)
print("Intial Value {} -> Type {}".format(f, type(f)))
print("Converted Value {} -> Type {}".format(newf, type(newf)))
print("{} == \"{}\" (String) is {}".format(f, newf, f == newf))


# Float to Boolean
# 0.0 is converted to False
# > 0.1 is converted to True
heading("Float to Boolean")
f0 = 0.0
f1 = 0.1
f2 = 5.0
newf = bool(f0)
print("Intial Value {} -> Type {}".format(f0, type(f0)))
print("Converted Value {} -> Type {}".format(newf, type(newf)))
newf = bool(f1)
print("Intial Value {} -> Type {}".format(f1, type(f1)))
print("Converted Value {} -> Type {}".format(newf, type(newf)))
checkif(f0)
checkif(f1)
checkif(f2)
