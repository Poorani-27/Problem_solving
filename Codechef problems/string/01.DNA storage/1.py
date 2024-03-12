t = int(input())

while t > 0:
    n = int(input())
    s = input()
    encoded_str=""
    for i in range (0,n,2):
        pair = s[i:i+2]
        if pair == "00":
            encoded_str +="A"
        elif pair == "01":
            encoded_str +="T"
        elif pair == "10": 
            encoded_str +="C"
            
        elif pair == "11":
            encoded_str +="G"
    print(encoded_str)
    t -= 1
