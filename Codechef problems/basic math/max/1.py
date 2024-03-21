t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    
    total_money = x * 5 + y * 10
    

    chocolates_bought = total_money // z
    
    
    print(chocolates_bought)
    
    t -= 1
