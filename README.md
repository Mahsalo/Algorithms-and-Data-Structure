# Algorithms-and-Data-Structure
This repository contains my modules to tackle the basic algorithmic design problems 

-gcd.py:
In this module we find the Greatest Common Divisor of two integers using Euclidean
Algorithm. Find the remainder and replace the reaminder with the quotient until 
you hit 0 in the remainder.  


-lcm.py:
In this module we find the Least Common Multiple of tw integers. 
There are 3 ways to do so:
    1) Iterate through all multiples of each number and detect the smallest common one
    2) Find the common prime factors and try to include them all in one number
    3) lcm(a,b)=a*b/gcd(a,b)
We implemented the easiest one, the third one.

-Fibonacci.py:
In this module we find the n_th Fibonacci number

-Fibonacci_last_digit.py:
In this module we find the last digit of the n_th Fibonacci number. 
In finding the next number we can only use the last digits of the
last two numbers to avoid overflow.

-Fibonacci_sum.py:
In this module we find the last digit of the sum of Fibonacci numbers

-Fibonacci_pisano.py:
In this module, we find the (Fn mod m), the remainder of a Fibonacci number divided 
by an integer m. n could be really big so it's better not to use the array-implementation 
of Fibonacci numbers. We make use of Pisano Period length since (Fn mod m)
iterates after Pisano period length of m.
F2015 mod 3= F7 mod 3=1 
Since 2015 mod 8=7 and 8 is the Pisano Period of 3.

-Fib_sum_part.py:
In this module we find the last digit of the sum of the Fibonacci numbers in a range [m,n]
If the input numbers are not that big, we can use the array implementation of the Fibonacci numbers
Since we can prove that S[n]=F[n+2]-1 we can also prove that S=F[n+2]-F[m+1] in a range [m,n]


-Fib_sum_sq.py:
In this module we find the sum of the squares of the Fibonacci numbers.
The easiest way to find the sum of Squares of the first n Fibonacci numbers is
to find F(n+1)*F(n) (The area of a rectangle formed by Fibonacci numbers)

