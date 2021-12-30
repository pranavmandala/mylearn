import time

input_num = input("Enter a number:")

# check num is divisible by any number below n/2
def isPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                # this number is not prime
                return False

        # We didn't have any number divides num
        # hence this number is a prime
        return True

    else: 
        # All numbers < 1 are not prime
        return False 

def listPrimes (x):
    primelist = []
    for i in range(x + 1):
        if isPrime(i):
            primelist.append(i)
    
    return primelist

input_num = int(input_num)
t0 = time.time()
primelist = listPrimes(input_num)
t1 = time.time()
print(primelist)
print("Total prime nmbers "+ str(len(primelist)))
print("Total time for execution: " + str(t1-t0))