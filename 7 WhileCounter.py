# Written by: Pavel Maslo
# Date: September 21, 2020
# Program Name: WhileCount

#counter-controlled while loop
intLC = 1 #initialize loop counter(1)
while intLC <=25: #test for completion(2)
    print ("it's still lower than 25", intLC)  #Body of loop(3)
    intLC += 1 #increment loop counter(4)
    #intLC = intLC+1

blnDone = False
while blnDone == False:
    strName = input("Enter ur name: ")
    if strName:
        print ("Hello",strName, "bye!")
        blnDone = True
    else:
        print ("no name")
