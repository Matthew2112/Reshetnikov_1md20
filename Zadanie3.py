y=input('enter year:')
y=int(y)
if (y%4==0 and y%100!=0) or (y%400==0):
    print('This year is leap')
else:
    print('this year is not leap')
