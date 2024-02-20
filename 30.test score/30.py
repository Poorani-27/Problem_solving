T = int(input())
for _ in range(T):
    N,X,Y=map(int,input().split())
    if Y%X!=0 or Y>N*X : print("NO")
    else:print("YES")
    