# cook your dish here
T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    N = 2*Y 
    ans= X//N 
    print(ans)
       
    