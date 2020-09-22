# Written by: Pavel Maslo
# Date: September 21, 2020
# Program Name: WhileBrakefast

blnDone = False
while blnDone ==False:
    print (
    """
    1) Bacon & eggs
    2) Outmeal
    3) Tost
    4) Pancakes
    """)

    strChoice = input("What would you like: ")

    if strChoice == "1":
        print ("Enjoy your Bacon & eggs!")
        blnDone = True
    elif strChoice == "2":
        print ("Enjoy your Outmeals!")
        blnDone = True
    elif strChoice == "3":
        print ("Enjoy your Tost!")
        blnDone = True
    elif strChoice == "4":
        print ("Enjoy your Pancakes!")
        blnDone = True
    else:
        print ("You are going to srave, choose bla bla!")