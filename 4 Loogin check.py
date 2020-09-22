# Written by: Pavel Maslo
# Date: September 21, 2020
# Program Name: LoginCheck

#First step to creat 'HTC'

strID=""
strPW=""
intAttempts = 0
while (strID != "Pavel" or strPW != "Password1") and intAttempts<3:
    strID=input("Enter loginID: ")
    strPW=input("Enter Pass: ")
    intAttempts += 1
    if strID == "Pavel" and strPW == "Password1":
        print ("Login successful!")
    else:
        if intAttempts == 3:
            print ("Print Account disabled, call system administrator!")
        else:
            print ("LoginID or password incorrect. Please try again.")