# cook your dish here
t= int(input())
for _ in range(t):
    n= int(input())
    bag = n//10 
    if n%10==0 : print(bag)
    else:print(bag+1)