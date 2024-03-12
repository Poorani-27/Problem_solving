# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    count =0
    if N %4 !=0:
        print((N//4)+1)
    else:
        print(N//4)