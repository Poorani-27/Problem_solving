n= int(input())
player1=0
player2=0
winner=0
max_lead=0
for i in range(n):
    score1,score2=map(int,input().split())
    player1 +=score1
    player2 +=score2
    lead = abs(player1-player2)
    if lead>max_lead:
        max_lead=lead 
        if player1 >player2 : winner =1 
        elif player2 >player1 :winner=2 
print(winner,max_lead)
    