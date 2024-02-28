sp=''
n=int(input('Enter the number of words: '))
for s in range (n):
    s=input('enter word: ')
    sp += (s + ' ')
    if s=='stop':
        print(sp[:5])
if s!='stop':
    print(sp)


