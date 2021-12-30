"""
This progam takes a users inputed number and prints multiples up to n
"""
# Taking users input
x = input ("Enter a number:")

# Multiplying users input by the numbers in the range
for r in range(1, 10):
    p = x * r
    print( str(x) + " x " +  str(r) + " = " + str(p) )
    
