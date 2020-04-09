print('Numbers from 1 to 10')
x= 2
y= int(input('Guess the number: '))
if y==x:
    print('Great! You did it!')
while y!=x:
    y= int(input('Guess the number: '))
    if y==x:
        print('Great! You did it!')
