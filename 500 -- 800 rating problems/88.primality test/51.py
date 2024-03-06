# cook your dish here
from sympy import isprime 
t=int(input())
for _ in range(t):
    n=int(input())
    if isprime(n) :print("yes")
    else:print("no")