import datetime
import re
current_time = datetime.datetime.now()

def createhelp():
    with open("help.txt", 'a') as fil:
        fil.write("If you face any issues, you can email us at harisrehmanchugtai@gmail.com")
        fil.write("Cnversly, you can contact us at 0300-XXXXXXX")
        fil.write("**************MEMBERSHIP PLANS****************")
        fil.write("1: 5000 Rs annually /recommended/")
        fil.write("2: 500 Rs monthly")
        fil.write("Note: You can cancel the subscription anytime.")
        fil.write("**************GUIDLINES***********************")
        fil.write("*Take care of your safety and the safety of others while using the parking!")
        fil.write("*Follow the aisle you are being alloted")
        fil.write("*If your car isn't in its designated spot in 5 minutes, you wil be fined 1000 Rs")
        fil.write("*If you park for more than the specified time, you will be fined 200 Rs per hour")
        fil.write("*Make sure you set your account beforehand to prevent trouble")
        fil.write("*Don't park in a disabled people category parking.")
        fil.write("***************PARKING MAP********************")
        file.write("ENTER HERE")
        fil.write("___________________________________________________")
        fil.write("___________________________________________________")
        fil.write("| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |")
        fil.write("                                                   ")
        fil.write("| 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |")
        fil.write("___________________________________________________")
        fil.write("___________________________________________________")
        fil.write("| 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 |")
        fil.write("                                                   ")
        fil.write("| 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |")
        fil.write("___________________________________________________")
        fil.write("___________________________________________________")
        fil.write("| 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 |")
        fil.write("                                                   ")
        fil.write("| 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 |")
        fil.write("___________________________________________________")
        fil.write("___________________________________________________")
        fil.write("Parking ends here*******************************************")

bigloopflag = False
createhelp()
print("********************************************************")
print("1: Use the app to set up account.")
print("2: Use the parking.")
print("********************************************************")
choice = int(input("Choose from the menu above: "))
while (choice!=1 and choice!=2):
    choice = int(input("Invalid choice, try again: "))
    
if choice == 1:
    while bigloopflag == False:
        flag = False
        carnum = input("Enter your car registration number that must be in the form AAA-999: ")
        exp = re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", carnum)
        while (len(exp)==0):
            carnum = input("Invalid input. Must be in the form AAA-999: ")
            exp = re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", carnum)

        print("--------------------------------------------------------")
        print("\t1: Set up a new account.")
        print("\t2: Update your wallet.")
        print("\t3: View your profile.")
        print("\t4: Setup/Cancel Membership.")
        print("\t5: Help")
        print("\t6: Exit")
        print("--------------------------------------------------------")
        choice2 = int(input("Choose from the menu above: "))
        while (choice2!=1 and choice2!=2 and choice2!=3 and choice2!=4 and choice2!=5 and choice2!=6):
            choice2 = int(input("Invalid choice, try again: "))

        if choice2 == 1:
            print("Welcome to the set account center!")
            print("--------------------------------------------------------")
            name = input("Enter your complete name: ")
            line = name + "," + carnum + ","+"NO"  
            with open("Personaldetails.txt", 'a') as fil:
                fil.write(line)

        elif choice2 == 2:
            print("Welcome to the wallet balance updater.")
            print("--------------------------------------------------------")

            money = int(input("How much money do you want to credit in your parking account: "))
            while money<500 or money>20000:
                money = int(input("Enter an amount greater than 500 and less than 20,000: "))

            Line = carnum + "," + str(money)
            with open("Walletdetails.txt", 'a') as fil:
                fil.write(Line)

            print("Updated! You now have ",money, " in your account")

        elif choice2 == 3:
            print("Welcome to your profile page!")
            print("--------------------------------------------------------")
            with open("Personaldetails.txt", 'r') as fil:
                Lines = fil.readlines()         
                for line in Lines:
                    if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum):
                        flag = True
                        line = line.strip()
                        line = line.split(",")
                        print("Name: ", line[0])
                        print("Reg num: ", line[1])
                        print("Membership: ",line[2])

            if flag == False:
                print("No details found, create a new account!")
            else:       
                with open("Walletdetails.txt", 'r') as fil:
                    flag = False
                    Lines = fil.readlines()         
                    for line in Lines:
                        if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum):
                            flag = True
                            line = line.strip()
                            line = line.split(",")
                            print("Money: ", line[1])

        elif choice2 == 4:
            print("--------------------------------------------------------")
            print("1: Cancel Existing membership")
            print("2: Create membership")
            print("--------------------------------------------------------")
            choice3 = int(input("choose from above: "))
            while (choice3!=1 and choice3!=2):
                choice3 = int(input("Invalid choice, try again: "))

            if choice3 == 2:
                print("**************MEMBERSHIP PLANS****************")
                print("1: 5000 Rs annually /recommended/")
                print("2: 500 Rs monthly")
                print("Note: You can cancel the subscription anytime.")
                print("--------------------------------------------------------")
                choice4 = int(input("choose from above: "))
                while (choice4!=1 and choice4!=2):
                    choice4 = int(input("Invalid choice, try again: "))     
                if choice4 == 1:
                    with open("Walletdetails.txt", 'r') as fil:
                        flag = False
                        Lines = fil.readlines()         
                        for line in Lines:
                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum):
                                flag = True
                                line = line.strip()
                                line = line.split(",")
                                mon = int(line[1].strip())
                                temp = mon
                                if mon>5000:
                                    mon = mon - 5000
                                    fil.replace(mon, temp)
                                    with open('Personaldetails.txt', 'r') as filedata :
                                        Lines = filedata.readlines()         
                                        for line in Lines:
                                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum):
                                                line = line.strip()
                                                line = line.split(",")
                                                val = line[2]

                                    filedata = filedata.replace('YES', val)

                                    with open('Personaldetails.txt' 'a') as file:
                                        file.write(filedata)
                                else:
                                    print("Not enough money for membership, add balance to wallet again.")

                if flag == False:
                    print("No details found, create a new account!")
            else: 



        elif choice2 == 5:
            with open("help.txt", 'a') as fil:
                fil.read()

        elif choice2 == 6:
            break

        contchoice = input("Do you want to reuse the app? Enter yes or no: ")
        while(contchoice.lower()!="yes" and contchoice.lower()!="no"):
            contchoice= input("Wrong choice, try again: ")
        if contchoice == "yes":
            bigloopflag = False
        else:
            bigloopflag = True    
    
else:
    while (current_time.hour>=6 and current_time.hour<=24):
        print("--------------------------------------------------------")
        print("WELCOME TO THE PARKING AREA!")
        print("********************************************************")
    


print("********************************************************************")
print("THANK YOU FOR USING OUR SOFTWARE")
print("********************************************************************")
