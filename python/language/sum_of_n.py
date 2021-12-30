"""
This progam takes an input N and prints out its sum of N numbers
"""

# get the user input into n
n = input ("Enter a number: ")
n = int(n)

# defining sum as 0
sum = 0

# add the number by iterating from 0 to n 
for x in range(n+1):
    # add to the sum
    sum = sum + x

print("The sum of first " + str(n) + " numbers are " + str(sum))
