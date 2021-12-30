binary = input("Enter a binary number: ")
binary = str(binary)
exp = 1
l = len(binary)
decimal = 0

for i in binary:
    decimal = decimal + int(i) * (2 ** (l - exp))
    exp = exp + 1

print(decimal)

hexadecimal = ""
if decimal == 0:
    hexadecimal = "0"
else:
    while decimal > 0:
        hexadecimal = str(decimal % 16) + hexadecimal
        decimal = decimal / 16

print(hexadecimal)