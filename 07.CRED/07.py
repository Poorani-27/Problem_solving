T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    Coins = X * Y 
    bags = 0
    if Coins >= 100:
        bags = Coins // 100
    print(bags)
