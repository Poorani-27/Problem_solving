# cook your dish here
T = int(input())
for i in range(T):
    N=int(input())
    income =N*50
    sugarcane = int(income*(20/100))
    salt_mint = int(income*(20/100))
    shop_rent = int(income*(30/100))
    Total = income - (sugarcane+salt_mint+shop_rent)
    print(Total)