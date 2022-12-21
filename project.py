import datetime
import re
import os
import sys
import fileinput
import random as rd

parkinglist = []

for x in range(60):
    parkinglist.append(False)
    
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
        
def generaterandomspot():
    returnthing = rd.randint(1,60)
    return returnthing
        
def check_spot(spot):
    count = 0
    
    while count <=60:
        if parkinglist[spot] == False:
            parkinglist[spot] = True
            print("You have been alloted parking spot ", spot)
            return True
        else:
            spot = generaterandomspot()
            count+=1
    
    return False
        
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
    boolflag = False
    
    with open("Personaldetails.txt", 'r') as fil:
        lines = fil.readline()
        for line in lines:
            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                year = re.findall(r"[2][0][0-9][0-9]",line)
                year = empt.join(year)
                find = re.findall(r"\-[0-9][0-9]\-",line)
                month = empt.join(find)
                month = month[1:3]
                day = re.findall(r"[0-9][0-9]$",line)   
                day = empt.join(day)

    if membership == "Monthly":            
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

    elif membership == "Yearly":
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
    return True
                
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


carnum = input("Enter your car registration number that must be in the form AAA-999: ")
exp = re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", carnum)
while (len(exp)==0):
    carnum = input("Invalid input. Must be in the form AAA-999: ")
    exp = re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", carnum)
        
if choice == 1:
    while bigloopflag == False:
        flag = False

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
                                        
                                    fil = open('Walletdetails.txt').read().replace(str(temp), str(mon))
                        
                                    with open("Walletdetails.txt", 'w') as file:
                                        file.write(fil)   
                                else:
                                    print("Not enough money for membership, add balance to wallet again.")
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

                                    filedata = open('Personaldetails.txt').read().replace("NO", "YESM")

                                    with open('Personaldetails.txt', 'w') as file:
                                        file.write(filedata)
                                        
                                    fil = open('Walletdetails.txt').read().replace(str(temp), str(mon))
                        
                                    with open("Walletdetails.txt", 'w') as file:
                                        file.write(fil)   
                                    
                                else:
                                    print("Not enough money for membership, add balance to wallet again.")
                                    
                        checkformemberships(carnum, "Monthly")                          
                    if flag2 == False:
                        print("No details found, create a new account!")
            else:  
                txt = "YES"
                flag3 = False
                with open('Personaldetails.txt', 'r') as filedata:
                    Lines = filedata.readlines()         
                    for line in Lines:
                        test = re.findall(r"YES|NO",line)
                        if len(test) == 0 or test[0] != "YES":
                            flag3 = False
                            break
                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                flag3 = True
                            
                if flag3 == True:
                    empty = ""
                    torepl = re.findall(r"[2][0][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]$",line)
                    torepl = empty.join(torepl)
                    filedata = open('Personaldetails.txt').read().replace("YES", "NO").replace(torepl, '\n')

                    with open('Personaldetails.txt', 'w') as file:
                        file.write(filedata)
                else:
                    print("Account not found")

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
    timetostay = int(input("Enter the number of hours you want to park the car: "))
    while timetostay<1 or timetostay>16:
        timetostay = int(input("Invalid input, try again: "))

    while (timetostay + current_time.hour)>24:
        print("You can't park your car as parking will close down.")
        timetostay = int(input("Enter the number of hours you want to park the car. If you want to abort, press 0: "))
        if timetostay == 0:
            break
        while timetostay<1 or timetostay>16:
            timetostay = int(input("Invalid input, try again: "))
            
    countyearly = 0
    countmonthly = 0
    txt = "YES"
    txt2 = "YESM"

    while (current_time.hour>=6 and current_time.hour<=24):
        print("--------------------------------------------------------")
        print("WELCOME TO THE PARKING AREA!")
        print("********************************************************")
        
        spot = generaterandomspot()
        if check_spot(spot) == True:
            print("The car has been alloted its parking space!")
            with open("Personaldetails.txt", 'r') as fil:
                Lines = fil.readlines()         
                for line in Lines:
                    if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):   
                        if re.findall(r"YES|NO",line) == txt.split():
                            countyearly +=1
                            texttowrite = str(carnum)+ ","+ str(countyearly)+"\n"
                            with open("Yearlycountfile.txt", 'a') as filedata:
                                filedata.write(texttowrite)
                                
                            with open("Yearlycountfile.txt", 'r') as filedata:
                                datas =filedata.readline()
                                for data in datas:
                                    teststr = "50"
                                    check = re.findall(r"[0-9]?[0-9]$", data)
                                    if check > teststr.split():
                                        filedata = open('Yearlycountfile.txt').read().replace(check, "0")
                                        with open("Yearlycountfile.txt", 'w') as file:
                                            file.write(fil)   
                                        print("You got a free parking!")                                         
                                    else:
                                        print("You have to pay 200 Rs per hour")
                                        moneytopay = 200*timetostay
                                        with open("Walletdetails.txt", 'r') as fil:
                                            Lines = fil.readlines()                    
                                            for line in Lines:
                                                if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                                    flag2 = True
                                                    line = line.strip()
                                                    line = line.split(",")
                                                    mon = int(line[1])                                        
                                        if mon<moneytopay:
                                            print("You don't have enough money!")
                                        else:
                                            newmon = mon- moneytopay                               
                                            fil = open('Walletdetails.txt').read().replace(str(mon), str(newmon))
                                            with open("Walletdetails.txt", 'w') as file:
                                                file.write(fil) 
                                
                        elif re.findall(r"YES|NO",line) == txt2.split():
                            countmonthly +=1
                            texttowrite = str(carnum)+ ","+ str(countmonthly)+"\n"
                            with open("Monthlycountfile.txt", 'a') as filedata:
                                filedata.write(texttowrite)
                                
                            with open("Monthlycountfile.txt", 'r') as filedata:
                                datas =filedata.readline()
                                for data in datas:
                                    teststr = "90"
                                    check = re.findall(r"[0-9]?[0-9]$", data)
                                    if check > teststr.split():
                                        filedata = open('Monthlycountfile.txt').read().replace(check, "0")
                                        with open("Monthlycountfile.txt", 'w') as file:
                                            file.write(fil)                                           
                                        print("You got a free parking!") 
                                    else:
                                        print("You have to pay 200 Rs per hour")     
                                        moneytopay = 200*timetostay
                                        with open("Walletdetails.txt", 'r') as fil:
                                            Lines = fil.readlines()                    
                                            for line in Lines:
                                                if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                                    flag2 = True
                                                    line = line.strip()
                                                    line = line.split(",")
                                                    mon = int(line[1])                                        
                                        if mon<moneytopay:
                                            print("You don't have enough money!")
                                        else:
                                            newmon = mon- moneytopay                               
                                            fil = open('Walletdetails.txt').read().replace(str(mon), str(newmon))
                                            with open("Walletdetails.txt", 'w') as file:
                                                file.write(fil)                                            
                        else:
                            print("You have to pay 200 Rs per hour")
                            moneytopay = 200*timetostay
                            with open("Walletdetails.txt", 'r') as fil:
                                Lines = fil.readlines()                    
                                for line in Lines:
                                    if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                        flag2 = True
                                        line = line.strip()
                                        line = line.split(",")
                                        mon = int(line[1])                                        
                            if mon<moneytopay:
                                print("You don't have enough money!")
                            else:
                                newmon = mon- moneytopay                               
                                fil = open('Walletdetails.txt').read().replace(str(mon), str(newmon))
                                with open("Walletdetails.txt", 'w') as file:
                                    file.write(fil)                              
                    else:
                        print("Now account found, you can't park")                  
        else:
            print("Sorry! The parking is currently full.")
        
        break

print("********************************************************************")
print("THANK YOU FOR USING OUR SOFTWARE")
print("********************************************************************")
