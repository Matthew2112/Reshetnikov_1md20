s=input('Enter word')
if (s.count('Ф')>=1 or s.count('ф')>=1 )==True:
    print("Ого! Это редкое слово!")
if (s.count('Ф')==0 or s.count('ф')==0)== True:
    print("Эх, это не очень редкое слово...")