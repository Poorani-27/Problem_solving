# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(str,input().split()))
    s=a.count("START38")
    l=a.count("LTIME108")
    print(s, l)