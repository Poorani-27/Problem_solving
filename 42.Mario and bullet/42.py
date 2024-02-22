# cook your dish here
T = int(input())
for _ in range(T):
    X,Y,Z= map(int, input().split())
    A= Y//X 
    B=Z-A
    if B>=0:
        print(B)
    else:
        print("0")
        