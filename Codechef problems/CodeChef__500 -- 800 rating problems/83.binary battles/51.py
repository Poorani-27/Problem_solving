# cook your dish here
import math
t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    y=int(math.log2(n))
    c=y*a
    x=(y-1)*b
    print(c+x)