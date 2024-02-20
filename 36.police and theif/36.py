T=int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    C=abs(X-Y)
    D=abs(Y-X)
    if X==Y:print("0")
    elif X<Y:print(C)
    else:print(D)
        