#This is restaurant management system
#First of all we would be displaying menu along with that we would like to take the name and date of birth of Customers as well.
#In the first module using basic data types like lists and dictionaries we would be taking and storing the order of the Customers.
#After that we would be proceeding to the billling module and chacking if it is the birthday of customer.
#If so wiping of the bill, if not genrating the bill along with the taxes.
#Generating the Discounts
#Finally taking the Customer FeedBack from Customers.
from datetime import date

#Restaurant Management System
#In this restaurant management system we will try to create some modules such as taking the orders generating the bills and more.
print("Kindly Enter your name")
name=input()
print("Dear ",name," Welcome to the restuarant")
#Hotel menu

Menu={"Thali":300,"Pizza":230,"Burgure":150,"Biryani":350,"Cocacola":20,"Thickshake":120}
print(Menu)
print("Kindly Enter your Date of Birth")
print("Enter the date in year month day format exaple 2023-12-23")
Birthday=input()
s=date.today()
l=str(s)

#Initializing bill as Zero
bill = 0



# Module 1 Taking the Order from the user
print("Kindly give your order")
# Creating a list for taking the orders

k = []
v = []
while True:
        O = input()
        # In Order to avoid ambiguitites in orders we have made the first letter as capital of every order.To match the items in menu.
        c = O.capitalize()
        if c in Menu:
            print("Enter the Quantity you want")
            i = int(input())

            k.append(c)
            v.append(i)
        elif O == "Stop":
            break
        else:
            print("The requested item is not available")

Order = dict(zip(k, v))
print("Your Order Summary is")
print(Order)
print(k)
print(v)

# Module 2 Generating the bill for the order.

if l==Birthday:
    bill=0
    print("Many more happy returns of the day ", name," on this occasion we would like to wipe off your bill kindly enjoy our treat as your bill is ", bill)

else:
    for i in k:
        d = Menu[i]
        c = k.index(i)
        bill = bill + (v[c] * d)

    print("Your bill without tax was ")
    print(bill)
    total=bill

    # Checking if the bill containing Beverage or not.
    if "Cocacola" in k:
        print("As you have requested for soft drink there was 18% gst on the bill along with tax of 10% on beverage")
        # Getting the gst value
        gst = bill * 0.18
        # Getting the tax incured in Beverage
        beverage_tax = Menu['Cocacola'] * 0.10
        # Adding the tax to the bill
        bill = bill + gst + beverage_tax
        print("The total bill is ", bill)


    else:
        print("As Beverage is not requested there would be a normal gst of 18% on overall bill")
        gst = bill * 0.18
        bill = bill + gst
        print("The total bill is ", bill)

#Module 3 Offer Module
#As a part of the startup in the initial days of service most of the restaurants have a practice of give aways

if bill>1500 and bill<2000:
    print("As you have crossed the bill of rupees 1500 we would like to give a 15 % discount on the bill")
    bill=bill-(bill*0.15)
    print("Your bill after the 15% discount is ",bill)
elif bill>=2000:
    print("As you have crossed the bill of 2000 we would like to provide a discount of 20% on your bill")
    bill=n=bill-(bill*0.2)
    print("Your bill after 20% discount is ",bill)


#Moudule-4 At last it was time for the feedback module
#Most of the Hotels have the habit of collecting the feedback from Customers
print("Dear ",name," Please provide your feedback on a scale of 1 to 10")
f=int(input())
if f>=1 and f<=5:
    print("We are extremely sorry for the Poor Service Sir/Madam kindly excuse us we will rectify it")
elif f>5 and f<=7:
    print("That was great meeting you sir next time we would performe even more better kindly visit again")
elif f>7  and f<=10:
    print("We are absolutely happy that you are satisfied with our service sir keep an eye on our offer s and kindly visit again")

print("Thank You")
