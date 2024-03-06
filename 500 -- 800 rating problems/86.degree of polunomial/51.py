
t = int(input())
for _ in range(t):
    n = int(input())
    coefficients = list(map(int, input().split()))
    degree = n- 1 - coefficients[::-1].index(next((c for c in coefficients[::-1] if c != 0)))
    print(degree)
