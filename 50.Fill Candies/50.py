# cook your dish here
T = int(input())
for _ in range(T):
    N, K , M = map(int,input().split())
    # N candies , K pocket , M candies in K 
    filled_candies = K*M 
    bag = N // filled_candies
    if N%filled_candies==0: print(bag)
    else :print(bag+1)