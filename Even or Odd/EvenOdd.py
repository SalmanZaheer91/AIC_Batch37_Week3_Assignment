from cProfile import label
count = 0
while (count < 2):
    count = count + 1
    print (' ')
    print ("Hello and Welcome to Number Identifier! ")
    print (' ')

    Num1 = int(input('Please Enter the Number = '))
    Content = Num1 % 2
    print (' ')
    if Content == 0:
        print ('The Number you have Entered is Even')
    else:
        print ('The Number you have Entered is Odd') 
    print (' ')
    count = int(input('To Check Another Number please type 1'))
    Answer = count
    break







