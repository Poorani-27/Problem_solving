# cook your dish here
def cost(N,X):
    Subscription = N // 6
    if N% 6 != 0:
        Subscription +=1  
    total_cost = Subscription*X
    return (total_cost)
T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    print(cost(N,X))