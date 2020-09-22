# Written by: Pavel Maslo
# Date: January 30, 2013
# Program Name: Program #3

#2 assignment. count forwards from 1 to 10 by 1.  

intNumb = 1 #initialize loop counter
intCount = 1
while intNumb <=10: #test for completion
    print (intNumb ,intCount) #Body of loop
    intNumb += 1 #increment loop counter
    intCount += 1
print

#3 assignment. count forwards from 1 to 101 by 10’s.
    
intNumb = 1 #initialize loop counter
intCount = 1
while intNumb <=101: #test for completion
    print (intNumb ,intCount) #Body of loop
    intNumb += 10 #increment loop counter
    intCount += 1
print

#4 assignment. count backwards from 1000 down to 0 by 100.
    
intNumb = 1000 #initialize loop counter
intCount = 1
while intNumb >=0: #test for completion
    print (intNumb ,intCount) #Body of loop
    intNumb -= 100 #increment loop counter
    intCount += 1
print

#5 assignment. input from 1-10 and return the English word .

intEnt = int(input("Enter number 1 - 10: "))
if intEnt==1:
    print ("\nOne\n")
elif intEnt==2:
    print ("\nTwo\n")
elif intEnt==3:
    print ("\nThree\n")
elif intEnt==4:
    print ("\nFour\n")
elif intEnt==5:
    print ("\nFive\n")
elif intEnt==6:
    print ("\nSix\n")
elif intEnt==7:
    print ("\nSeven\n")
elif intEnt==8:
    print ("\nEight\n")
elif intEnt==9:
    print ("\nNine\n")
elif intEnt==10:
    print ("\nTen\n")
else:
    print ("Denied enter. Wrong number.\n")

#6 assignment. write  login and password.

strLog=""
strPass=""
while (strLog != "jhon doe" or strPass != "fopwpo"):
    strLog=input("Enter login: ")
    strPass=input("Enter Password: ")
    if strLog == "jhon doe" and strPass == "fopwpo":
        print ("Login successful")
    else:
        print ("Login or password incorrect. Please try again.\n")
        


