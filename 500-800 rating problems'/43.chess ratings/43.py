
T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    if X>=Y:
        print(0)
    else:
        games_needed = (Y - X) // 8
        if (Y - X) % 8 != 0:
            games_needed += 1
        print(games_needed)