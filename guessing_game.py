from random import randint

guess_number = int (input("Please enter a number between 1 - 10 : "))

randomNumber = randint (1,10)
if guess_number == randomNumber :
     print ("Congrats you win the match")
else :
     print ("Oppo you lost the match")