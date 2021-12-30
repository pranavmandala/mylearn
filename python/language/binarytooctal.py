binary = input("Enter a binary number: ")
binary = str(binary)
exp = 1
l = len(binary)
decimal = 0

for i in binary:
    decimal = decimal + int(i) * (2 ** (l - exp))
    exp = exp + 1

print(decimal)

octal = ""
if decimal == 0:
    octal = "0"
else:
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal / 8

print(octal)