def fib(num):
    a=0
    b=1
    print(a,b, end=" ")
    for i in range (num-2):
        c=a+b
        print(c, end=" ")
        a,b =b,c

num=int(input())
fib(num)
#Time Complexity: O(n)  \\ Space Complexity: O(1)

#--------------------------------------------------------------------------------------------------------

def fib(num):
    fib_series=[]
    a=0
    b=1

    for i in range(num):
        if i == 0 or i==1:
            fib_series.append(i)
        else :
            a,b=b,a+b
            fib_series.append(b)
    print(fib_series)

fib(5)
#Time Complexity: O(n)  //  Space Complexity: O(n)