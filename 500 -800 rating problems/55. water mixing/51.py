T=int(input())
for _ in range(T):
    A,B,X,Y = map(int,input().split())
    if A==B:print("Yes")
    elif A<B :
        req= B-A 
        if req <=X :print("YES")
        else :print("NO")
    elif A>B :
        req =A-B
        if req <=Y:print("YES")
        else:print("No")