T = int(input())
for _ in range(T):
    N,X = map(int,input().split())
    rounds= X//N 
    if rounds*N == X: print("YES")
    else:print("NO")