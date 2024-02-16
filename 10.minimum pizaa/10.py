# cook your dish here
T = int(input())
for _ in range(T):
    n , x = map(int,input().split())
    total_slices = n*x
    req = total_slices // 4
    if total_slices%4 == 0:
        print(req)
    else:
        print(req+1)

    