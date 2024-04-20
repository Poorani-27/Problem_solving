def nthFibonacci(n):
        # code here
        a=0
        b=1
        fib_series=[]
        
        for i in range(n+1):
            if i ==0 or i==1:
                fib_series.append(i)
            else :
                a,b =b,a+b
                fib_series.append(b)
                
        return fib_series[n]
print(nthFibonacci(1))  


