import datetime
import time


#welcome the user to the ATM machine
# using (======) to help mimick a real life ATM machine
# using time.sleep to slow down process

print("WELCOME TO THE MO INVESTMENT BANK")
time.sleep(1)
print("=====================================")
time.sleep(1)
print("Please wait")
time.sleep(1)
print("------------------")
time.sleep(2)

#Accepting card
print("PLEASE INSERT CARD")
time.sleep(1)
print("------------------")
time.sleep(1)
print("Loading")
time.sleep(1)
print("------------------")
time.sleep(1)

#ensuring correct user input
name = input("What is your name :")
allowedUsers = ["chidi", "joy","mo", "sul"]
if (name not in allowedUsers):
    print("Wrong username, You've been logged out automatically")


allowedPassword = ["chidi111", "joy222", "mo333", "sul444"]

#ensuring password matches with the correct user
if (name in allowedUsers):
    password = input ("Please input password : \n")
    userId = allowedUsers.index(name)


    if password == allowedPassword[userId]:
        print("Welcome \n" + name )
        print("===================")
        time.sleep(1)



#inputting current date and time
        now = datetime.datetime.now()
        print("Today's date and time is :")
        print("..............")
        time.sleep(1)
        print(now.strftime ("%d - %m - %y   %H: %M: %S"))
        print("..................")
        time.sleep(1)

#selection of operation to be performed
        print( "What operation would you like to perform today")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Complaint")

        userOption = int(input("Select operation: \n"))

#For withdrawal operation
        if (userOption == 1):

            withdraw = input ("How much would you like to withdraw? :  \n")
            print("Take your cash")


#For deposit operation
        elif (userOption == 2):

            deposit = input( "How much will you like to deposit? : \n")
            print(" Your Current balance is %s:" %deposit)


#For complaint operation

        elif  (userOption == 3):

            Complaint = input( " What issue will you like to report? : \n ")
            print("Thank you for contacting us")

        else:
            print("Invalid input, Please try again")

