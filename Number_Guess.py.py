#This is a Number Guessing Game.
#In this game we are going to generate a random number and see how many guesses does the user takes to guess the correct number.
#We are going to import a random module for this project which would generate the random number.
import random
#By taking user input we decide the range.
range=input("Type a number ")
#We have to make sure user typed a number.
#We are going to validate it by  isdigit method.

if range.isdigit():
    #Converting the uer input which is in String to integer.
    range=int(range)
    #Checking whether user entered the number greater than zero or not.
    if range<=0:
        print("Please type a number larger than Zero 0 next time.")
        quit()
else:
    print("Please type a number next time")
    quit()
#Now we use user input to give the random range with lower bound 0.
random_number=random.randint(0,range)
#Initializing a variable name guesses to keep track of how many attempts user is taking to guess the number.
guesses=0
#Now we will be taking the input from the user as guesses.
while True:
    guesses=guesses+1
    user_guess=input("Make a Guess of Number ")
    if user_guess.isdigit():
        #Converting String to Integer.
        user_guess=int(user_guess)
    else:
        print("Please type a number next time")
        continue
        #Continue brings the execution to top and gives a choice to make a guess again.
    if user_guess == random_number:
        print("You got it")
        break
    else:
        #Giving user some hints.
        #If User is greater than the number or below.
        if user_guess > random_number:
            print("You were above the number ")
        else:
            print("You are below the number")

#Generating the score of the user.
print("You got it in ",guesses," guesses")