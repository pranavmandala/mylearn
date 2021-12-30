emptylist = []
for i in range(0,6):
    emptylist.append(i)

# print(emptylist)

testlist = [1,"word",2, True, False, 1.0]
""" print(testlist)

for z in testlist:
    print(z)

for j in range(0, len(testlist)):
    print(testlist[j]) """

""" for k in range(len(testlist)-1, -1, -1):
    print(testlist[k]) """

""" for t in range(-1, (len(testlist) + 1) * -1, -1):
    print(testlist[t]) """

thelist = ["a", "b", "c", "d", "e", "f"]

found = False
for i in range(0, len(thelist)):
    if thelist[i] == "b":
        print("Yes")
        print("Found at the index " + str(i))
        found=True

if not found:
    print("Not found")
