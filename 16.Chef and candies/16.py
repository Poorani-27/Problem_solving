# cook your dish here
T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    C = N - X
    if X > N :
        print(0)
    else:
     D = C // 4
     if C % 4 != 0:
        D += 1
     print(D)
