x = input("Enter a number:")

def isPrime(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                print(str(x) + " is not a prime number")
                return False
            
        print(str(x) + " is a prime number")
        return True

    else: 
        print(str(x) + " is not a prime number")
        return False 

isPrime(int(x))


