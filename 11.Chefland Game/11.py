# cook your dish here
T = int(input())
for _ in range(T):
    r1,r2,r3,r4 = map(int,input().split())
    if r1==0 and r2 == 0 and r3==0 and r4==0:
        print("IN")
    else :
        print("Out")