import random

def Z():
    h=int(input('Enter number of task: '))
    if h==1:
        return print(Z1())
    elif h==2:
        return print(Z2())
    elif h==3:
        return print(Z3())
    elif h==4:
        return print(Z4())
    else:
        return 'Wrong number'
def Z1():
    s='1 2 3 4 5'
    u=input('Enter number: ')
    if u in s:
        return 'Congratulations, you got it right!'
    else:
        return 'Unfortunately your guess is wrong'
def Z2():
    my_list=[1,2,3,4,5,6,7,8,8,9,0]
    def find_duplicates(lst):
        duplicates = []
        for items in lst:
            if lst.count(items)>1 and items not in duplicates:
                duplicates.append(items)
        return duplicates
    duplicate_element=find_duplicates(my_list)
    if duplicate_element:
        print ('Duplicates:')
        for element in duplicate_element:
            return (element)
    else:
        return ('No duplicates')
def Z3():
    days=('Monday','Tuesday','Wensday','Thursday','Friday','Saturday','Sunday')
    n=int(input('Enter a number of weekend you want: '))
    return f'your weekends are {days[-n:]} and your working days are {days[:-n]}'
def Z4():
    s1=['Ivanov', 'Malkiel', 'Kuchev', 'Blizgarev', 'Semenov', 'Levchenko', 'Koombaev', 'Petrov', 'Ratushnii', 'Olhovik']
    s2=['Ivanov', 'Kluchnikov', 'Sviridenko', 'Kaziev', 'Sokolenko', 'Bondarev', 'Kazarian', 'Makarov', 'Babichev', 'Matveev']
    s3=[]
    d=()
    s3.append(random.shuffle(s1))
    s3.append(random.shuffle(s2))
    s3=sorted(s3)
    d.__add__(tuple(sorted(s3)))
    print(s1,s2,d[-15:])
    print(len(d[-15:]))
print(Z())
