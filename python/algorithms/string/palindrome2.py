# Solving using iterative method

s = str(input("Enter a number: "))
ispalindrome = True

for i in range(0, len(s) / 2):
    forward = str(s[i])
    backward = str(s[len(s) - (i + 1)])
    print("index: " + str(i) + " forward = " + forward)
    print("index: " + str(i) + " backward = " + backward)
    if forward == backward:
        ispalindrome = True
    else:
        ispalindrome = False
        break

if ispalindrome:
    print("The entered number is a palindrome")
else:
    print("The entered number is not a palindrome")