decimal = input("Enter a number: ")
binary = ""
if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal / 2

print("The binary form of the number you entered is " + binary)


exp = 1
l = len(binary)
newdecimal = 0
for i in binary:
    newdecimal = newdecimal + int(i) * (2 ** (l-exp))
    exp = exp + 1

print(newdecimal)

exp = 0
rev_binary = reversed(binary)
newdecimal = 0
for i in rev_binary:
    newdecimal = newdecimal + int(i) * (2 ** exp)
    exp = exp + 1

print(newdecimal)


