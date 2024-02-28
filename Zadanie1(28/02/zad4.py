import random
n=int(input('Enter number of task'))
x=random.randint(1,n)
y=random.randint(1,n)
t=0
k=0
m=0
print(f'{x}''+'f'{y}')
n1=int(input('Enter your answer:'))
if n1==x+y:
    print('Правильно!')
    k+=1
    t+=1
if n1!=x+y:
    print('Ответ неверный')
    m+=1
    t+=1
if m==3:
    print('Игра окончена. Правильных ответов:'f'{k}')
if t==n:
    print('Игра завершена. Правильных ответов:'f'{k}''Неправильных ответов: 'f'{m}' )