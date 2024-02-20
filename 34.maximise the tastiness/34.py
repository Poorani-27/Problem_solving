# cook your dish here
T = int(input())
for _ in range(T):
    a,b,c,d = map(int, input().split())
    A = max(a,b)
    B = max(c,d)
    C= A+B 
    print(C)