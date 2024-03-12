# cook your dish here
T=int(input())
for _ in range(T):
    A,B= map(int,input().split())
    A1=A*100/10 
    B1=B*100/20
    if A1==B1:
        print("ANY")
    elif A1 >B1:
        print("FIRST")
    else:
        print("SECOND")