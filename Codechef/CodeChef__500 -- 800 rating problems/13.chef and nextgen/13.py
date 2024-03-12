# cook your dish here
T = int(input())
for _ in range(T):
    A,B,X,Y =map(int,input().split())
    C=A*B 
    D=X*Y 
    if D >=C:
        print("Yes")
    else:
        print("No")