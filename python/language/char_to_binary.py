"""
This program takes a string and prints its decimal and binary code
"""
def dump(c) :
    print(outstr.format(c, ord(c), bin(ord(c))))

x = "abcdefghijklmnopqrstuvwxyz"
outstr = "This char is = {}, its decimal code {}, its binary code {}"

for c in x:
    # print("This char is = " + c)
    # print(outstr.format(c, ord(c), bin(ord(c))))
    dump(c)
    c = c.upper()
    # print(outstr.format(c, ord(c), bin(ord(c))))
    dump(c)