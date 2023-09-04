#Railway seat enquiry system.
#In this railway seat enquiry system we will see on the total arrangement of seats in the train.
#Along with the arrangement we would like too see the kind of Seats that are available.
#Vacant and Occupied seats
#Also see the availabiliy of different kinds of seats.
#Probability of Seat Availability.

#Module-1 Berths layout Generation
#In this module we will bring out the basic outlet of the train seats that are available.
#Lets create the list of Seats and berths as well.

Seats=list(range(1,1001))
#We are creating a list of seats ranging from 1 to 1000.
print("The Total number of Seats that are available are ")
print()
#The total number of Seats that are available are determined by the length of the seats.
Total_Seats=len(Seats)
print("The total number of seats are  ")
print(Total_Seats)
print("The seats that are available are ")
print()
print(Seats)


#Module-2 Classification of Bearths Into lower and Window availability seats.
#Creating a list of window berths aand initialized it with the value of 1 and appending the other window seats numbers as well
window=[1]
i=1
count=0
#Chacking whether the seat is window or not and appending it to the window seats list.
while True:
    if i>1000:
        break
    else:
        count=count+1
        if count%3!=0:
            i=i+3
            window.append(i)
        else:
            i=i+2
            window.append(i)

for i in window:
    if i>1000:
        window.remove(i)
#Finally this is the window seats list.
print("The Window berth that are available are ")
print()
print(window)
print("The total number of window seats that are available are ")
Window_Seats=len(window)
print(Window_Seats)


#Module 3 Seats/Berths Occupation availability
print("The total berths available are ")
print()
print(Seats)
print("THe Window seats that are available are ")
print()
print(window)
#Taking the user input for seats numbers .
print("Please enter the seat number that you want to travel with ")
Selected_Seats=[]
while True:
    Seat_number = int(input())
    Selected_Seats.append(Seat_number)
    if Seat_number==-1:
        break
occupied=[]
for i in Selected_Seats:
    if i in Seats:
        print("The seat number ", i, " is Vacant and allocated for you")
        if i in window:
            print(i, " is a Window Seat have a nice journey")
            window.remove(i)
        Seats.remove(i)
        occupied.append(i)
    else:
        print("The requested Seat number ", i, " is Occupied kindly request an other one")
print("The Occupied Seats are ")
print()
print(occupied)
print("The Seats vacant are")
print()
print(Seats)
print("The Window Seats vacant are")
print()
print(window)


#Module 4 Probability and Percentage for Seat Confirmation.
#Dividing the number of available seats(number of favorable outcomes) with the total seats(Total number of Outcomes).
print("Probability of getting a Seat is ")
Probability=len(Seats)/Total_Seats
print()
print(Probability)
print("The Confirmatoin Percentage is ")
print()
Confirmation_Percentage=Probability*100
print(Confirmation_Percentage)
#indow Seat Propability determined by dividing the window seats that are available with the total window seats that are available.
print("The Probability of getting Window seat is ")
Window_Probability=len(window)/Window_Seats
print()
print(Window_Probability)
Window_Percentage=Window_Probability*100
print("The Percentage of Window availability is ")
print()
print(Window_Percentage)
