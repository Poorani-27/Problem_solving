t=int(input())
for _ in range(t):
    x,y = map(int,input().split())
    floor_x = (x - 1) // 10 + 1
    floor_y = (y - 1) // 10 + 1
    find = abs(floor_y-floor_x)
    print(find)