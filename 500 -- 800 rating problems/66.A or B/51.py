# cook your dish here
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    s=x+y
    a = 500 - (x*2) + 1000 - (s*4)
    x,y =y,x 
    r =x+y
    
    b = 1000-(x*4) + 500 - (r*2)
    print(max(a,b))