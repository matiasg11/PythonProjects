def isLeapYear(year):
    if year%4 == 0 or year%400 == 0:
        
        if year%4 == 0 and year%100 == 0:
            print ("Not leap year => {}".format(year))
        else:
            print("Leap year! => {}".format(year))
    else:
        print("Not leap year => {}".format(year))

isLeapYear(2000)
isLeapYear(1999)

isLeapYear(2001)

isLeapYear(2004)

isLeapYear(1900)

isLeapYear(2020)

