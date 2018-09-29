"""
Name    : Project 1
Date    : 09/23/2018
Authors : Gabriel Duarte, Elliot Newman
"""

# import libraries
#from __future__ import print_function
#import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import math
import time
import random


def euclids_algo(m, n, count, done):

    # arr.append(euclids_algo(sCount, i, 0, rec))
    # Create the base case for m and n, NOT gcd
    if (int(n) == 0 or int (m) == 0):
        return 0
    else:
        gcd = int(m) % int(n) # gets the remainder
        count += 1

        # Sets the base case for the GCD
        if (gcd == 0):
            return count
        else:
            if (done == int(10)):
                return euclids_algo(n, gcd, count, int(10))
            else:
                return euclids_algo(n, gcd,  count, int(11))

def consec_int_checking(m,n, count, done):

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
        count = int(0)
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

                    return count
                else:
                    n = int(n) - int(1.0)
            else:
                n = int(n) - int(1.0)

def Fib(x, n):

    # Im still working on this
    arr = []
    arr.append(int(0)) # This is for arr[0] = 1
    arr.append(int(1)) # This is for arr[1] = 1

    for i in range(1,x+1):
        arr.append(arr[i-1] + arr[i])
        print(arr[i], end=' ')

    count = int(0)
    ret_count = int(0)

    #GCD(m,n) where m = F(k+1) and n = F(k) for k > 1
    for i in range(1, len(arr)-1):
        ret_count += euclids_algo(arr[i], arr[i-1], count, int(10))

    if (n == 1):
        return ret_count
    if (n == 2):
        return arr
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
        print(primes[i], end=' ')
    print()

def calc_avg(sCount, which_plot, time_count):

    arr = []
    rec = 10

    if (sCount == int(0)):
        return 0

    if (which_plot == 1):
        for i in range(sCount):
            arr.append(euclids_algo(sCount, i, 0, rec))
            rec += 1
    elif (which_plot == 2):
        for i in range(sCount):
            arr.append(consec_int_checking(sCount, i, 0, rec))
            rec += 1
    elif (which_plot == 3):
        for i in range(sCount):
            arr.append(euclids_algo(sCount, i, 0, rec))
            rec += 1
    avg = int(0)
    total = int(0)

    for i, _ in enumerate(arr):
        total += arr[i]

    avg = total / sCount
    return avg

def scatter_plot(arr, avg, sCount, n):
   
    fig, ax = plt.subplots()
   
    ax.grid(True, zorder=0)
    ax.set_ylabel('GCD(n,n) at iteration "i"')
    ax.set_xlabel('Iterations')
    
    for i, _ in enumerate(arr):
        plt.scatter(i, arr[i], c='b', marker='x')
    
    if (n == 1):
        fig.canvas.set_window_title('Euclids Algorithm') 
        ax.set_title('MDavg(n) Scatterplot')
    elif (n == 2):
        fig.canvas.set_window_title('Consecutive Integer Checking Algorithm')         
        ax.set_title('Davg(n) Scatterplot')
    elif (n == 3):
        fig.canvas.set_window_title('Euclids Algorithm') 
        ax.set_title('MDworst(n) Scatterplot (Fib Seq)')

    plt.show()

def common_elements():

    # Initialize variables to have randomness from 0 to 10
    start = int(0)
    end = int(10)

    inp = int(input("How many random numbers do you want to fill the list with to find common elements?"))

    A = []
    B = []
    C = []

    for i in range(inp):
        A.append(random.randint(start,end))
    for i in range(inp):
        B.append(random.randint(start,end))

    A.sort()
    B.sort()

    print("A:",A,"\nB:",B)
    
    i = int(0)
    j = int(0)
    while((i != len(A)-1)  or (j != len(B)-1)):

        if (i == len(A)-1):
            if (A[-1] == B[j]):
                C.append(A[-1])
                A[-1] = int(0)
                break
        if (j == len(B)-1):
            if (B[-1] == A[i]):
                C.append(B[-1])
                B[-1] = int(0)
                break

        if (int(A[i]) == int(B[j]) and (i+1 != None or j+1 != None)):
            C.append(A[i])
            if (i != len(A) or j != len(B)):
                i += int(1)
                j += int(1)

            continue
        if (int(A[i]) > int(B[j])):
            if (j != len(B)-1):
                j += int(1)
            else:
                break

        if (int(A[i]) < int(B[j])):
            if (i != len(A)-1):
                i += int(1)
            else:
                break


        if (i == len(A)-1 and A[-1] <= B[j]):
            continue
        if (j == len(B)-1 and B[-1] <= A[i]):
            continue

    if (A[-1] == B[-1]):
        C.append(A[-1])

    print("C:",C)

    

def main():

    inp = input("Would you like to enter an m and n to show that Euclids and Consecutive checking are working? (y/n)")
    if (inp == "y"):
        m = int(input("Please enter a m:"))
        n = int(input("Please enter a n:"))
        out = euclids_algo(m,n,0,0)
        print("GCD Euclids:", out)


    end = int(input("Please enter a random number to use for Euclids and Consecutive:"))
    #end = int(400)
    newarray = []
    newarray2 = []
    newarray3 = []

    for i in range(0, end, 5):
        out2 = float(calc_avg(i, 1, 0))
        newarray.append(out2)

    x = input("Would you like to see the scatter plot for Euclids Algorithm? (y/n)")
    if (x == 'y'):
        print("Loading Scatterplot for Euclid's Algorithm...")
        scatter_plot(newarray, newarray, end, int(1))
        

    for i in range(0, end, 5):
        out3 = float(calc_avg(i, 2, 0))
        newarray2.append(out3)
    x = input("Would you like to see the scatter plot for Consecutive Integer Checking? (y/n)")
    if (x == 'y'):
        print("Loading Scatterplot for Checking Consecutive Integers Algorithm...")
        scatter_plot(newarray2, newarray2, end, int(2))


    x = int(input("\nWhat position in the Fibonacci sequence would you like to see up to? (998 is the max position) "))
    start = time.time()
    ret_count = Fib(int(x), int(1))
    print("Number of Mod Divisions:", ret_count)

    for i in range(0, x, 5):
        out4 = float(calc_avg(i, 3, 0))
        newarray3.append(out4)
    end = time.time()
    print("\nTime taken to run Fib Seq:",end-start)
    y = input("Would you like to see the scatter plot? (y/n)")

    if (y == 'y'):
        scatter_plot(newarray3, newarray3, x, int(3))
    
    common_elements()


    inp = int(input("\nPlease enter a number to find its primes: "))
    start = time.time()
    sieve(inp)
    end = time.time()
    print("\nTime taken to run sieve of Eratosthenes Algorithm:",end-start)   

main()
