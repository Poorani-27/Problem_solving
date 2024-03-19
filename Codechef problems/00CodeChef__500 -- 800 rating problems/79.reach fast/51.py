# cook your dish here
t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    diff=abs(a-b)
    if a==b :print(0)
    elif k>diff :print(1)
    else:
        if diff%k==0:print(diff//k)
        else :print((diff//k)+1)
    