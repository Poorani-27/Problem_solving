T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A =N //M 
    if A % 2== 0 and N%M==0:
        print("Yes")
    else:
        print("No")
