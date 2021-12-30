x = input("Enter a number: ")

def isPrime(x):
    if x > 1:
        # find if any number below n/2 divides x with remainder 0
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                return False

        # We didn't have any numbers divides x 
        return True

    else: 
        return False 

def prime(x):
    for i in range(x + 1):
        if isPrime(i):
            print(str(i) + " is a prime number below " + str(x))

prime(x)