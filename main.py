def check_palindrom(palindrom):
    pal=[]    
    pal_revers=[]
    for letter in palindrom:
        pal.append(letter.lower())
    for letter in palindrom[::-1]:
        pal_revers.append(letter.lower())
    for i in range(0, len(palindrom)):
        if pal[i]!=pal_revers[i]:
            return False
        else:
            return True

word = "PoTOp"
if check_palindrom(word):
    print(f"\nSłowo '{word}' jest palindromem\n")
else:
    print(f"\nSłowo '{word}' nie jest palindromem\n")