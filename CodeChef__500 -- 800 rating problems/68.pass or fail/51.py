# cook your dish here
t = int(input())
for _ in range(t):
    n,x,p =map(int,input().split())
    correct = x*3 
    wrong = (n-x)*1 
    total = correct - wrong 
    if total >= p :print("pass")
    else:print("fail")