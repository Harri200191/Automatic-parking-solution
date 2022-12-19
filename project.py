import datetime
import re
import os
import sys
import fileinput

current_time = datetime.datetime.now()

def createhelp():
    with open("help.txt", 'w') as fil:
        fil.write("If you face any issues, you can email us at harisrehmanchugtai@gmail.com\n")
        fil.write("Conversly, you can contact us at 0300-XXXXXXX\n")
        fil.write("**************MEMBERSHIP PLANS****************\n")
        fil.write("1: 5000 Rs annually /recommended/\n")
        fil.write("2: 500 Rs monthly\n")
        fil.write("Note: You can cancel the subscription anytime.\n")
        fil.write("**************GUIDLINES***********************\n")
        fil.write("*Take care of your safety and the safety of others while using the parking!\n")
        fil.write("*Follow the aisle you are being alloted\n")
        fil.write("*If your car isn't in its designated spot in 5 minutes, you wil be fined 1000 Rs\n")
        fil.write("*If you park for more than the specified time, you will be fined 200 Rs per hour\n")
        fil.write("*Make sure you set your account beforehand to prevent trouble\n")
        fil.write("*Don't park in a disabled people category parking.\n")
        fil.write("***************PARKING MAP********************\n")
        fil.write("ENTER HERE\n")
        fil.write("___________________________________________________\n")
        fil.write("___________________________________________________\n")
        fil.write("| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |\n")
        fil.write("                                                   \n")
        fil.write("| 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |\n")
        fil.write("___________________________________________________\n")
        fil.write("___________________________________________________\n")
        fil.write("| 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 |\n")
        fil.write("                                                   \n")
        fil.write("| 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |\n")
        fil.write("___________________________________________________\n")
        fil.write("___________________________________________________\n")
        fil.write("| 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 |\n")
        fil.write("                                                   \n")
        fil.write("| 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 |\n")
        fil.write("___________________________________________________\n")
        fil.write("___________________________________________________\n")
        fil.write("Parking ends here*******************************************\n")
        
def clearall():
    with open("Personaldetails.txt", 'w') as fil:
        fil.write(" ")
    with open("Walletdetails.txt", 'w') as fil:
        fil.write(" ")
        
def checkformemberships(carnum, membership):
    year = ""
    month = ""
    day = ""
    empt = ""
    txt = "YES"
    
    with open("Personaldetails.txt", 'r') as fil:
        lines = fil.readline()
        for line in lines:
            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                if re.findall(r"YES|NO",line) == txt.split():
                    year = re.findall(r"[2][0][0-9][0-9]",line)
                    year = empt.join(year)
                    find = re.findall(r"\-[0-9][0-9]\-",line)
                    month = empt.join(find)
                    day = re.findall(r"[0-9][0-9]$",line)   
                    day = empt.join(day)
     
    if membership = "Monthly":            
        if ((current_time.month == int(month)+1) or (month == 1 and current_time.month == 12)) and (int(date) == currentime_day):
            with open("Walletdetails.txt", 'r') as fil:
                Lines = fil.readlines()                    
                        for line in Lines:
                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                line = line.strip()
                                line = line.split(",")
                                mon = int(line[1])
                                temp = mon - 500
                    
            fil = open('Walletdetails.txt').read().replace(str(mon), str(temp))                    
            with open("Walletdetails.txt", 'w') as file:
                file.write(fil)
        
    elif membership = "Yearly":
        if ((current_time.year == int(year)+1)) and (int(date) == currentime_day) and (int(month) == current_month):
            with open("Walletdetails.txt", 'r') as fil:
                Lines = fil.readlines()                    
                        for line in Lines:
                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                line = line.strip()
                                line = line.split(",")
                                mon = int(line[1])
                                temp = mon - 5000
                    
            fil = open('Walletdetails.txt').read().replace(str(mon), str(temp))                    
            with open("Walletdetails.txt", 'w') as file:
                file.write(fil)
                
clearall()
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
            line = name + "," + carnum + ","+"NO\n"  
            with open("Personaldetails.txt", 'a') as fil:
                fil.write(line)

        elif choice2 == 2:
            print("Welcome to the wallet balance updater.")
            print("--------------------------------------------------------")
    
            with open("Personaldetails.txt", 'r') as fil:
                flag4=False
                Lines = fil.readlines()         
                for line in Lines:
                    if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):   
                        flag4 = True
                        money = int(input("How much money do you want to credit in your parking account: "))
                        while money<500 or money>20000:
                            money = int(input("Enter an amount greater than 500 and less than 20,000: ")) 

                        Line = carnum + "," + str(money)+"\n"
                        with open("Walletdetails.txt", 'a') as fil:
                            fil.write(Line)

                        print("Updated! You now have added",money, "in your account")
                 
                if flag4 == False:
                    print("No account found.")

        elif choice2 == 3:
            print("Welcome to your profile page!")
            print("--------------------------------------------------------")
            with open("Personaldetails.txt", 'r') as fil:
                Lines = fil.readlines()         
                for line in Lines:
                    if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                        flag = True
                        line = line.strip()
                        line = line.split(",")
                        print("Name: ", line[0])
                        print("Reg num: ", line[1])
                        print("Membership: ",line[2])

            if flag == False:
                print("No details found, create a new account!")
            else:   
                tempmoney = 0
                with open("Walletdetails.txt", 'r') as fil:
                    flag = False
                    Lines = fil.readlines()         
                    for line in Lines:
                        if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                            flag = True
                            line = line.strip()
                            line = line.split(",")
                            tempmoney = tempmoney + int(line[1])
                    print("Money: ", tempmoney)
                    
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
                        flag2 = False
                        Lines = fil.readlines()                    
                        for line in Lines:
                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                flag2 = True
                                line = line.strip()
                                line = line.split(",")
                                mon = int(line[1])
                                temp = mon
                                if mon>5000:
                                    mon = mon - 5000                                  
                                    with open('Personaldetails.txt', 'r') as filedata :
                                        Lines = filedata.readlines()         
                                        for line in Lines:
                                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                                line = line.strip()
                                                line = line.split(",")
                                                val = line[2]
                                    
                                    timestr = ","+str(current_time.year) +"-"+ str(current_time.month)+"-" + str(current_time.day)
                                    filedata = open('Personaldetails.txt').read().replace("NO", "YES").replace('\n', timestr)

                                    with open('Personaldetails.txt', 'w') as file:
                                        file.write(filedata)
                                else:
                                    print("Not enough money for membership, add balance to wallet again.")
                                    
                        fil = open('Walletdetails.txt').read().replace(str(temp), str(mon))
                        
                        with open("Walletdetails.txt", 'w') as file:
                            file.write(fil)
                            
                        checkformemberships(carnum, "Yearly")    
                    if flag2 == False:
                        print("No details found, create a new account!")
                elif choice4 == 2:
                    with open("Walletdetails.txt", 'r') as fil:
                        flag2 = False
                        Lines = fil.readlines()                    
                        for line in Lines:
                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                flag2 = True
                                line = line.strip()
                                line = line.split(",")
                                mon = int(line[1])
                                temp = mon
                                if mon>500:
                                    mon = mon - 500                                   
                                    with open('Personaldetails.txt', 'r') as filedata :
                                        Lines = filedata.readlines()         
                                        for line in Lines:
                                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                                line = line.strip()
                                                line = line.split(",")
                                                val = line[2]

                                    filedata = open('Personaldetails.txt').read().replace("NO", "YES")

                                    with open('Personaldetails.txt', 'w') as file:
                                        file.write(filedata)
                                else:
                                    print("Not enough money for membership, add balance to wallet again.")
                                    
                        fil = open('Walletdetails.txt').read().replace(str(temp), str(mon))
                        
                        with open("Walletdetails.txt", 'w') as file:
                            file.write(fil)   
                            
                        checkformemberships(carnum, "Monthly")
                    if flag2 == False:
                        print("No details found, create a new account!")
            else: 
                flag3 = False
                with open('Personaldetails.txt', 'r') as filedata :
                    Lines = filedata.readlines()         
                    for line in Lines:
                        if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                            flag3 = True
                
                if flag3 == True:
                    empty = ""
                    torepl = re.findall(r"[2][0][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]$",line)
                    torepl = empty.join(torepl)
                    filedata = open('Personaldetails.txt').read().replace("YES", "NO").replace(torepl, '\n')

                    with open('Personaldetails.txt' 'w') as file:
                        file.write(filedata)

        elif choice2 == 5:
            with open("help.txt") as fil:
                print(fil.read())

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
        break

print("********************************************************************")
print("THANK YOU FOR USING OUR SOFTWARE")
print("********************************************************************")
