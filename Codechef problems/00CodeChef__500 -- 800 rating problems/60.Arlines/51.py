t= int(input())
for _ in range(t):
    X,N= map(int,input().split())
    rem = N-(X*100)

    if rem <=0:print(0)
    elif rem > 0:
        c = rem//100 
        if (c*100) == rem:print(c)
        else :print(c+1)