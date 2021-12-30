'''
Python program to print all primes smaller than or equal to n using Sieve of Eratosthenes
'''

import time

input_num = input("Enter a number:")

def SieveOfEratosthenes(n):
    # Create a boolean array "assumed_primes[0..n]" and initialize all entries it as true.
    assumed_primes = []
    for i in range(n+1): 
        assumed_primes.append(True)

    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (assumed_primes[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                assumed_primes[i] = False
        p += 1
 
  
    # A value in assumed_primes[i] will finally be false if i is Not a prime, else true.
    # Print all prime numbers

    primelist = []
    for p in range(2, n+1):
        if assumed_primes[p]:
            primelist.append(p)

    return primelist
 

input_num = int(input_num)
t0 = time.time()
primelist = SieveOfEratosthenes(input_num)
t1 = time.time()
print(primelist)
print("Total prime nmbers "+ str(len(primelist)))
print("Total time for execution: " + str(t1-t0))