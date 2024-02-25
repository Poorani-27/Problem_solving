t = int(input())
for _ in range(t):
    a,x,b,y = map(int,input().split())
    aspeed =a/x 
    bspeed =b/y 
    if aspeed==bspeed :print("Equal")
    elif aspeed<bspeed:print('Bob')
    else :print("Alice")