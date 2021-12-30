# Solving using reversing a string

input1 = input("Enter a number: ")
s = str(input1)

# Reversing string using slice method
sr = s[::-1]

if s == sr:
    print("The entered number is a palindrome.")
else:
    print("The entered number is not a palindrome.")


