t=int(input())
for _ in range(t):
    x,y,a,b =map(int,input().split())
    total = {x,y,a,b}
    istotal =[x,y,a,b]
    if len(total) == len(istotal):print(2)
    elif len(total) ==3:print(1)
    else:print(0)