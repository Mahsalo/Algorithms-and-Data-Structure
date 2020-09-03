# Algorithms-and-Data-Structure
This repository contains my modules to tackle the basic algorithmic design problems 

# gcd.py:
In this module we find the Greatest Common Divisor of two integers using Euclidean
Algorithm. Find the remainder and replace the reaminder with the quotient until 
you hit 0 in the remainder.  


# lcm.py:
In this module we find the Least Common Multiple of tw integers. 
There are 3 ways to do so:
    1) Iterate through all multiples of each number and detect the smallest common one
    2) Find the common prime factors and try to include them all in one number
    3) lcm(a,b)=a*b/gcd(a,b)
We implemented the easiest one, the third one.

# Fibonacci.py:
In this module we find the n_th Fibonacci number

# Fibonacci_last_digit.py:
In this module we find the last digit of the n_th Fibonacci number. 
In finding the next number we can only use the last digits of the
last two numbers to avoid overflow.

# Fibonacci_sum.py:
In this module we find the last digit of the sum of Fibonacci numbers

# Fibonacci_pisano.py:
In this module, we find the (Fn mod m), the remainder of a Fibonacci number divided 
by an integer m. n could be really big so it's better not to use the array-implementation 
of Fibonacci numbers. We make use of Pisano Period length since (Fn mod m)
iterates after Pisano period length of m.
F2015 mod 3= F7 mod 3=1 
Since 2015 mod 8=7 and 8 is the Pisano Period of 3.

# Fib_sum_part.py:
In this module we find the last digit of the sum of the Fibonacci numbers in a range [m,n]
If the input numbers are not that big, we can use the array implementation of the Fibonacci numbers
Since we can prove that S[n]=F[n+2]-1 we can also prove that S=F[n+2]-F[m+1] in a range [m,n]


# Fib_sum_sq.py:
In this module we find the sum of the squares of the Fibonacci numbers.
The easiest way to find the sum of Squares of the first n Fibonacci numbers is
to find F(n+1)*F(n) (The area of a rectangle formed by Fibonacci numbers)


# MaxAdRevenue.py:
In this module, we find the best permutations of two vectors such that the inner
product is maximized, It is called maximum Ad revenue such that the biggest Ad slot
is allocated to the most profitable Ad.
inputs:
    -number of Ads
    -Profit per Ad: a
    -Slot size: b
output:
    -Maximum a.b 
    
# MaxPrize.py:
In this module we try to find th4e best pattern of summation of K 
integers that would sum up to fixed value "n".

# moneyChange.py:
In this module, we find the optimal solution of the coin change problem using
Greedy Algorithm, with a set of 1,5,10 cents we would like to choose a pattern
with the minimum number of coins that sum up to "m" which is given as an input

# maxLoot.py:
In this module, we try to find the best combination of items that 
the sum of the value would be maximum (Knapsack problem).
The input: First Line: maximum number of items allowed and the full capacity
The next lines show the weight and the value of the items
The output: The maximum value put in the bag
The solution would be to sort in terms of value-per-weight

# carFuel.py:
In this module we try to find the minimum number of times that a car needs a
refill if the destination is d miles away and a full-tank helps with m miles each time.
"n" is the number of stations available on the way 

# maxSalary.py:
In this module we try to find the best pattern of given digits so that it will 
represent the biggest value possible.

# binarySearch.py:
In this module, we implement the binary search algoithm
in order to find k elements in an array, the output is the index 
of the elements in the array and -1 if there is none in the array

# majorityVote.py:
In this module, we try to find the maximum vote in an array
using divide and conquer method with runtime O(nlog n), if the 
frequency of occurance of any element in an array is more than n/2
that element wins the maximum vote
We can also implement the Moore method to achieve an even better
performance with O(n)  

# randQuickSort.py:
In this module, we try to improve the quick sort algorithm 
so that it would be  able to handle the case when there are too
many equal elements in the array, this case would be the worst 
case with O(n^2) for quick sort but we just solve it with 3 way partitioning


