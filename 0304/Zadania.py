def Z():
    h=int(input('Enter number of task: '))
    if h==1:
        return print(Z1())
    elif h==2:
        return print(Z2())
    elif h==3:
        return print(Z3())
    else:
        return 'Wrong number'
def Z1():
    def A():
        for ct, cap in c.items():
            print( f'Country: {ct} , Capital: {cap}')

    def B():
        n = input('Enter country: ')
        for ct, cap in c.items():
            if n == ct:
                print(f'Capital city of {n} is {cap}')

    def C():
        return sorted(c)

    c = {
        "Russia": "Moskow",
        "USA": "Washington DC",
        "England": "London",
        "Germany": "Berlin",
        "France": "Paris"
    }

    task = int(input("Enter number of task: "))
    if task == 1:
        print(A())
    if task == 2:
        print(B())
    elif task == 3:
        print(C())


def Z2():
    k = 0
    c1 = {'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'}
    c2 = {'Д', 'К', 'Л', 'М', 'П', 'У', 'д', 'к', 'л', 'м', 'п', 'у'}
    c3 = {'Б', 'Г', 'Ё', 'Ь', 'Я', 'б', 'г', 'ё', 'ь', 'я'}
    c4 = {'Й', 'Ы' ,'й', 'ы'}
    c5 = {'Ж', 'З', 'Х', 'Ц', 'Ч', 'ж', 'з', 'х', 'ц', 'ч'}
    c8 = {'Ш', 'Э', 'Ю', 'ш', 'э', 'ю'}
    c10 = {'Ф', 'Щ', 'Ъ', 'ф', 'щ', 'ъ'}
    n = input('Enter your word(in russian): ')
    for c in n:
        if c in c1:
            k += 1
        if c in c2:
            k += 2
        if c in c3:
            k += 3
        if c in c4:
            k += 4
        if c in c5:
            k += 5
        if c in c8:
            k += 8
        if c in c10:
            k += 10
    return f'You score is {k}'

def Z3():
    sl={'Nikolai':{'English', 'German','Chinese'},
        'Gleb':{'English','Japanese','Latin'},
        'Ilia':{'Italian','Chinese'},
        'Anna':{'Spanish','Greek',},
        'Darina':{'English','German'},
        'Viktoria':{'German','Chinese'}}
    all=set()
    for l in sl.values():
        all.update(l)
    print(sorted(all))
    ch=[s for s, l in sl.items()
        if 'Chinese' in l]
    print(f'Students who know Chinese: {ch}')



print(Z())
