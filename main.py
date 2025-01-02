def check_palindrom(palindrom):
    pal=[]    
    pal_revers=[]
    for letter in palindrom:
        pal.append(letter)
    for letter in palindrom[::-1]:
        pal_revers.append(letter)
    for i in range(0, len(palindrom)):
        if pal[i]!=pal_revers[i]:
            return False
        else:
            return True

word = "PoTOp"
if check_palindrom(word.lower()):
    print(f"\nSłowo '{word}' jest palindromem\n")
else:
    print(f"\nSłowo '{word}' nie jest palindromem\n")