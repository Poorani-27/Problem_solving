# cook your dish here
T = int(input())
for _ in range(T):
    
    N,X = map(int,input().split())
    
    
    if N ==X :
        print("0")
    else :
        flip = min(X,N-X) 
        print(flip)