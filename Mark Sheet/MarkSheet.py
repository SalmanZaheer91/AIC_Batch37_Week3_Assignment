# from cProfile import label
#count = 0
# while (count != q):
#     count = count + 1
print (' ')
print ("Hello and Welcome to Mark Sheet Printer! ")
print (' ')

Sub1 = int(input('Please Enter the Numbers Obtained for Physics = '))
print (' ')
Sub2 = int(input('Please Enter the Numbers Obtained for Chemistry = '))
print (' ')
Sub3 = int(input('Please Enter the Numbers Obtained for Mathematics = '))
print (' ')
Sub4 = int(input('Please Enter the Numbers Obtained for English = '))
print (' ')
Sub5 = int(input('Please Enter the Numbers Obtained for Urdu = '))
print (' ')
Sub6 = int(input('Please Enter the Numbers Obtained for Islamiat = '))
print (' ')
Sub7 = int(input('Please Enter the Numbers Obtained for Pakistan Studies = '))
print (' ')
print ("|----------------------------------------------------------------|")
print ("|-+-+-+-+-+-+-+-+-+-+-+-+- Mark Sheet -+-+-+-+-+-+-+-+-+-+-+-+-+-|")
print ("|----------------------------------------------------------------|")
print ("|      SUBJECT                TOTAL             OBTAINED         |")
print ("|----------------------------------------------------------------|")
print ('|      Physics                100             ',  Sub1,'               |')
print ('|                                                                |')
print ('|      Chemistry              100             ',  Sub2,'               |')
print ('|                                                                |')
print ('|      Mathematics            100             ',  Sub3,'               |')
print ('|                                                                |')
print ('|      English                100             ',  Sub4,'               |')
print ('|                                                                |')
print ('|      Urdu                   100             ',  Sub5,'               |')
print ('|                                                                |')
print ('|      Islamiat               100             ',  Sub6,'               |')
print ('|                                                                |')
print ('|      Pakistan Studies       100             ',  Sub7,'               |')
print ('|                                                                |')
print ("|----------------------------------------------------------------|")

Result = int(Sub1 + Sub2 + Sub3 + Sub4 + Sub5 + Sub6)
Percent = int ((Result / 700) * 100)
print (' ')
print (' ')
print ('Overall Percentage = ', Percent)
print (' ')
if Percent >= 90: 
    print ('Overall Grade obtained is A+')
    print (' ')
elif Percent >= 80:
    print ('Overall Grade obtained is A ') 
    print (' ')
elif Percent >= 70:
    print ('Overall Grade obtained is B ') 
    print (' ')
elif Percent >= 60:
    print ('Overall Grade obtained is C ') 
    print (' ')
elif Percent >= 50:
    print ('Overall Grade obtained is D ') 
    print (' ')
else :
    print ('The Student has Failed and need to Retake the Course.') 
    print (' ')
    print ('Thank you for your using our Mark Sheet Printer.')
    print (' ')
    print (' ')
        
#    count = (input('To Print Another Timesheet please press any other key or enter "q" to Quit'))
#    Answer = count
#    break
