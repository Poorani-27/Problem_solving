# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0 or n==1:
        print("1")
    else:
        fact =1
        for i in range(1,n+1):
            fact=i *fact
        print(fact)
            