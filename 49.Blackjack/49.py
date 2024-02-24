# cook your dish here
T = int(input())
for _ in range (T):
    A,B = map(int,input().split())
    C = 21 - (A+B)
    if 1<=C<=10:
        print(C)
    else:print(-1)