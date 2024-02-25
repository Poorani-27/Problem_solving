# cook your dish here
T=int(input())
for _ in range(T):
    X1,Y1,X2,Y2 = map(int,input().split())
    X=abs(X1-X2)
    Y=abs(Y1-Y2)
    print(max(X,Y))