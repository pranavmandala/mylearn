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


input_num = int(input_num)
if isPrime(input_num):
    print(str(input_num) + " is a prime number")
else:
    print(str(input_num) + " is not a prime number")






