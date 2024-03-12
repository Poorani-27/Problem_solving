import math
t=int(input())
for _ in range(t):
    h,x,y=map(int,input().split())
    h=h-y
    a=1+math.ceil(h/x)
    print(a)
    

    