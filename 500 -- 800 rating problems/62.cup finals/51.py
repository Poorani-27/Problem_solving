# cook your dish here
T = int(input())
for _ in range(T):
    X,Y,D=map(int,input().split())
    Diff =abs(X-Y) 
    if Diff<=D :print("Yes")
    else:print("No")
    
    