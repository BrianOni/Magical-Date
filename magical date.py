#Brian Onieal
#Question 2

#Is your date the magical date?

magicalMonth=float(input("Input the numerical month: "))    
magicalDay=float(input("Input the day: "))                  
magicalYear=float(input("Input the last 2 numbers of the year: "))

dayMonth=magicalDay * magicalMonth    #Multiplying the day and the month

if dayMonth == magicalYear:             #If the day times the month equals
    print("You have a magical date!!")  #the year, it's magical    
else:
    print("Your date isn't magical. Sorry.")  #If the day times the month
                                              #don't equal the year, it's not
                                              #magical
