T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    if  A <= B and C <= B:
        print("Yes")
    else:
        print("No")
