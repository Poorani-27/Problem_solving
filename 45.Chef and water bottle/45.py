T = int(input())

for _ in range(T):
    N, X, K = map(int, input().split())
    bottles_filled = min(N, K // X)
    print(bottles_filled)
