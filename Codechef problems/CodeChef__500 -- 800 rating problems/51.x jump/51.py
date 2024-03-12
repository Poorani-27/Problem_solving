T =int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    a = X//Y 
    if X%Y == 0: print(a)
    else : 
        b = a*Y 
        c=X-b
        answer=(c+a)
        print(answer)