# cook your dish here
T = int(input())
for _ in range(T):
    W,X,Y,Z =map(int,input().split())
    A = [X,Y,Z,X+Y,Y+Z,Z+X,X+Y+Z]
    if W in A :print("Yes")
    else :print("No")