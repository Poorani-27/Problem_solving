# cook your dish here
r,o,c =map(int,input().split())
remaining_overs =20-o
play=remaining_overs*6
possible_runs =play*6
max_score=c+possible_runs 
if max_score > r :print("YES")
else:print("NO")