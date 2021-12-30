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
