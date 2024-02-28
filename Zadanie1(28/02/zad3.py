n=int(input('Enter the number of words: '))
for s in range (n):
    s=input('Enter word: ')
    if (s.count('Ф')>=1 or s.count('ф')>=1 )==True:
        print("Ого! Это редкое слово!")
    elif (s.count('Ф')==0 or s.count('ф')==0)== True:
        print("Эх, это не очень редкое слово...")