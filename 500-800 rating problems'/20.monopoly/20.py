# cook your dish here
t = int(input())
for _ in range(t):
    p,q,r,s = map(int, input().split())
    if p > q+r+s or r> p+q+s or q > p+r+s or s> p+q+r:
        print ("yes")
    else:
        print("no")