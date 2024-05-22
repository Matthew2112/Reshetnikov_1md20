
def t1():
    ch = input("Enter your number: ")
    y=ch.isdigit()
    if y==True:
        ch=int(ch)
        if int(ch)%5==0:
            return f"{ch} can be successfully divided by 5 it equals {ch/5}"
        elif int(ch)%5!=0:
            return f"{ch} can't be successfully divided by 5 "
    elif y==False:
        return "You've entered str type!"

def t2():
    c = input("Enter your number: ")
    n=c.isdigit()
    if n== True:
        c=int(c)
        return f"You've successfuly divided 300 by {c} it equals {300/c}"
    elif n==False or c=="0":
        return "You've entered str type or 0 !"
def t3():
    dmy=input("Enter your date: ")
    day,month,year=map(int, dmy.split('.'))
    if day*month==int(str(year)[-2:]):
        return f'{dmy} is a magical date!'
    else:
        return f"{dmy} isn't a magical date!"
def t4():
    b=int(input("Enter your ticket: "))
    k=0
    l=0
    if sum(b[-1])==b[:-4]:
        return f'{b} ticket is lucky!'

    else:
        return f"{b} ticket isn't lucky!"
print(t1())