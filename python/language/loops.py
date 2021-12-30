a1 = "hello"
print(a1)
a2 = ['H', 'E', 'L', 'L', 'O']
print(a2)
a3 = [1, 2, 3, 4, 5]
print(a3)
a4 = range(0, len(a1))
print(a4)
a5 = range(len(a1)-1, -1, -1)
print(a5)

print("\nFOR LOOP over VALUE")

for x in a1:
    print(x)

print("\nFOR LOOP over INDEX")

for x in a4:
    print(a1[x])

print("\nFOR LOOP over INDEX")

for x in a5:
    print(a1[x])

print("\nWHILE LOOP over INDEX")

i = len(a1)-1
while i > -1:
    print(a1[i])
    i = i - 1


print("\nWHILE LOOP over INDEX")

i = 0
while i < len(a1):
    print(a1[i])
    i = i + 1