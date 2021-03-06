"""
Name    : Project 1
Date    : 09/23/2018
Authors : Gabriel Duarte, Elliot Newman
"""

# import libraries
#from __future__ import print_function
#import numpy as np
import matplotlib.pyplot as plt
import math

def euclids_algo(m,n, avg, count):

    # Create the base case for m and n, NOT gcd
    if (int(n) == 0 or int (m) == 0):
        return 0
    else:
        gcd = int(m) % int(n) # gets the remainder
        count += 1

        # Sets the base case for the GCD
        if (gcd == 0):
            print('Number of modulo divisions:',count)
            return n
        else:
            #avg += int(n)
            return euclids_algo(n, gcd, avg, count)

def consec_int_checking(m,n, count):
    
    # Initialize the variables
    temp = 0.0
    temp2 = 1.0
    t = 0.0
    original_n = int(n) # Hold our original value of n as n will change

    # Create the base case for m and n
    if (int(n) == 0 or int (m) == 0):
        return 0

    # Create another base case because we check to see the lower of the two
    # variables before finding gcd
    if (int(n) == int(m)):
        return int(m)
    
    # Did a swap instead so that we dont have to rewrite the while loop (below)
    if (int(n) > int(m)):
        swap = int(n)
        n = int(m)
        m = swap
        original_n = int(n) # Hold our original value of n as n will change

    if (int(n) < int(m)):
        while (int(temp2) != 0.0):
            t = int(n)
            temp = int(m) % int(t)
            count += 1

            # Once the algorithm finds that temp = 0, then find gcd for temp2
            if (int(temp) == 0.0):
                temp2 = int(original_n) % int(t)
                count += 1

                # If temp is equal to temp2, then we have found the gcd
                if (int(temp2) == 0.0 and int(temp) == int(temp2)):
                    print("Number of modulo divisions:",count)
                    return t
                else:
                    n = int(n) - int(1.0)
            else:
                n = int(n) - int(1.0)

def Fib():

    # Im still working on this
    x = int(input("What position in the Fibonacci sequence would you like to see up to? "))
    arr = []
    arr.append(int(0)) # This is for arr[0] = 1
    arr.append(int(1)) # This is for arr[1] = 1

    for i in range(1,x+1):
        arr.append(arr[i-1] + arr[i])
        print(arr[i])
    
    count = int(0)
    avg = int(0)

    #euclids_algo()


def sieve(n):

    # Initialize the arrays
    arr = []    # To populate 2 to n
    temp = []   # To populate the multiples
    primes = [] # To populate the primes

    # Creates the array from 2 to n
    for i in range (2,n):
        arr.append(i)

    # Start at 2 to the square root of n so that we dont have to type every case
    # For ex: if n = 25, we don't have to say if n%2 == 0 and n%3 == 0 to n%24 ==0
    #         the square root of n, will cover all such cases from SQRT(n) down to 2
    for i in range(2, int(math.sqrt(n))):
        if (arr[i] != 0): 
            j = i*i                 # Will calculate a multiple of the current element
            while (j <= n):
                temp.append(int(j)) # This will add the multiples to the array
                j += i              # This will go to the next multiple

    # This now populates the primes array with any number that isn't in the multiples list
    for i in range(2, n):
        if (i not in temp):
            primes.append(i)

    # Print the primes
    for i in range(len(primes)):
        print(primes[i])

   
def main():
    avg = 0
    count = 0
    eu_al_m = input("Please enter an integer for m: ")
    eu_al_n = input("Please enter an integer for n: ")

    out = euclids_algo(eu_al_m, eu_al_n, avg, count) # send the two numbers to the f
    print('GCD:', out)

    out = consec_int_checking(eu_al_m, eu_al_n, count)
    print("Consecutive GCD:", out)

    Fib()

    inp = int(input("Please enter a number to find its primes: "))
    sieve(inp)

main()