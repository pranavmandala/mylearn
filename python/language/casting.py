# Boolean to String
print("Boolean to String")
x = True
y = False
z = str(x)
print("Intial Value {} -> Type {}".format(x, type(x)))
print("Converted Value {} -> Type {}".format(z, type(z)))
print("{} == {} (Boolean) is {}".format(z, x, z == x))
# True as a string is not the same as True as a boolean value
print("{} == {} (String) is {}".format("True", z, "True" == z))


# Boolean to Number
print("\n")
print("Boolean to Number")
z = int(x)
print("Intial Value {} -> Type {}".format(x, type(x)))
print("Converted Value {} -> Type {}".format(z, type(z)))
z = int(y)
print("Intial Value {} -> Type {}".format(y, type(y)))
print("Converted Value {} -> Type {}".format(z, type(z)))

# Boolean to Float
print("\n")
print("Boolean to Float")
z = float(x)
print("Intial Value {} -> Type {}".format(x, type(x)))
print("Converted Value {} -> Type {}".format(z, type(z)))
z = float(y)
print("Intial Value {} -> Type {}".format(y, type(y)))
print("Converted Value {} -> Type {}".format(z, type(z)))

# String to Number
string = ("1")
print("\n")
print("String to Number")
# we cannot change because the string value to a number if it is a word
newstring = int(string)
print("Intial Value {} -> Type {}".format(string, type(string)))
print("Converted Value {} -> Type {}".format(newstring, type(newstring)))

# String to Float
print("\n")
print("Stringn to Float")
newstring = float(string)
print("Intial Value {} -> Type {}".format(string, type(string)))
print("Converted Value {} -> Type {}".format(newstring, type(newstring)))

# Number to Boolean
num0 = 0
num1 = 1
num2 = 2
print("\n")
print("Number to Boolean")
newnum = bool(num0)
print("Intial Value {} -> Type {}".format(num0, type(num0)))
print("Converted Value {} -> Type {}".format(newnum, type(newnum)))
newnum = bool(num1)
print("Intial Value {} -> Type {}".format(num1, type(num1)))
print("Converted Value {} -> Type {}".format(newnum, type(newnum)))
newnum = bool(num2)
print("Intial Value {} -> Type {}".format(num2, type(num2)))
print("Converted Value {} -> Type {}".format(newnum, type(newnum)))

# Number to Float
print("\n")
print("Number to Float")
newnum = float(num)
print("Intial Value {} -> Type {}".format(num, type(num)))
print("Converted Value {} -> Type {}".format(newnum, type(newnum)))

# Float to String
f = 1
print("\n")
print("Float to String")
newf = str(num0)
print("Intial Value {} -> Type {}".format(f, type(f)))
print("Converted Value {} -> Type {}".format(newf, type(newf)))

#Float to Boolean
f0 = 0.0
f1 = 0.1
f2 = 0.2
print("\n")
print("Float to Boolean")
newf = bool(f0)
print("Intial Value {} -> Type {}".format(f0, type(f0)))
print("Converted Value {} -> Type {}".format(newf, type(newf)))
newf = bool(f1)
print("Intial Value {} -> Type {}".format(f1, type(f1)))
print("Converted Value {} -> Type {}".format(newf, type(newf)))
newf = bool(f2)
print("Intial Value {} -> Type {}".format(f2, type(f2)))
print("Converted Value {} -> Type {}".format(newf, type(newf)))

