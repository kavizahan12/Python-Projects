from random import *

used=[]

inputOne=int(input("Enter the number 1 to play: "))
number=randint(1,11)

while number<21:
    if number<21 and inputOne==1:
        print("Your number is", number)
        inputOne=int(input("Enter the number 1 to play again: "))
        number2=randint(1,11)
        number=number+number2
    if number>21 and inputOne==1:
        print("Your number is", number)
        print("You lose!!!")
    if number==21 and inputOne==1:
        print("Your number is", number)
        print("You win")
    if inputOne!=1:
        print("Game over")
