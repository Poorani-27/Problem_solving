t = int(input())
for _ in range(t):
    str1 = input()
    str12 = list(map(str, str1.split(' ')))
    str13 = ""
    for i in str12:
        if i == i.upper():
            str13 += i.upper() + " "
        else :
            str13 += i.capitalize() + " "
    print(str13.strip())
