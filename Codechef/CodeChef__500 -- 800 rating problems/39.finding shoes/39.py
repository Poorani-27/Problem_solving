
t = int(input())
for _ in range (t):
    n ,m = map(int, input().split())
    if n >m :
        total =( n*2 -m)
        print(total)
    else :
        print(n)