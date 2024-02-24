# cook your dish here
T = int(input())
for i in range(T):
    X = int(input())
    if X <= 100 :
        print(X)
    elif 100<X<=1000 :
        print(X-25)
    elif 1000 <X<=5000:
        print(X-100)
    elif X > 5000 :
        print (X-500)