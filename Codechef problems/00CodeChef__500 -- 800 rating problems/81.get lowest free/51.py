# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    free=min(a,b,c)
    total=(a+b+c)-free
    print(total)