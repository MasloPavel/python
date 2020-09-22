# Written by: Pavel Maslo
# Date: September 21, 2020
# Program Name: SmallTalk + Calculation

#start the meet
print ("\"Hi, my name is Pavel!\"" " said Pavel")
strangerName = input("What is your name? ")

#ask about ages
print ("\nHi " + strangerName + ", nice to meet you!")
print ("I'm 29.",)
strangerAge = int(input ("How old are you? "))

#how long guest live
x = strangerAge * 365 * 24 * 60 * 60
print ("\n" + strangerName + ", did you know you are", x, "second old?")

#repeat guest name
print ("\n" + strangerName * 100)

#calculate problems
print ("\n130 / 10 =", 130.0 / 10)
print ("233 / 3.3 =", 233 / 3.3)
print ("233 / 3 =", 233 / 3)
print ("The remainder for 233 /3 =", 233%3)
print ("2 to the power of 32 =", 2 ** 32)
print ("(456.782/45.1)-78.9 =",(456.782/45.1)-78.9)

#example of concatenation and continuation
print ("\nbla","Pla","bla","Pla","bla","Pla","bla"+"Pla"+"bla"+"Pla"+"bla"+"Pla"+"bla")
