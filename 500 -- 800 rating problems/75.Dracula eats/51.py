t=int(input())
for _ in range(t):
    n=int(input())
    a=0
    if n==1:print(0)
    else:
        for i in range(2,n+1,7):
            a +=1
        print(a)