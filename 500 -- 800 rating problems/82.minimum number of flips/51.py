# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n&1==1: print(-1)
    else: print(abs(sum(a))//2)
    