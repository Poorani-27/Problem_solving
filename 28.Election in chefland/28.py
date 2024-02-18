T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for a in A:
        if a >= X:
            count += 1
    print(count)
