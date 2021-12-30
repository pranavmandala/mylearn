# Printing ascii character map

# Ascii character set are 7 bit characters
# For 7 bits, we can represent a total of 128 characters
for i in range(1, 128):
    print("ASCII character for {} = {}".format(str(i), chr(i)))
