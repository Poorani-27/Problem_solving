T = int(input())  

for _ in range(T):
    N = int(input())  
    
    count = 0 
    
    D = list(map(int, input().split()))  
    
    for i in D:
        if i >= 1000:  
            count += 1  
            
    print(count) 
