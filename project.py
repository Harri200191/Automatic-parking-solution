import datetime
import re
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
    returnthing = rd.randint(0,59)
    return returnthing
        
def check_spot(spot):
    count = 0
    
    while count <60:
        if parkinglist[spot] == False:
            parkinglist[spot] = True
            print("You have been alloted parking spot", spot)
            return True
            break          
        else:
            spot = generaterandomspot()
            count+=1
    
    return False
        
        
def testfunc(carnum):
    txtstr = carnum + ",0\n"
    with open("Personaldetails.txt", 'w') as fil:
        fil.write(" ")
    with open("Walletdetails.txt", 'w') as fil:
        fil.write(txtstr)
    with open('Monthlycountfile.txt','w') as fil:
        fil.write(" "+carnum+ ",0\n")
    with open('Yearlycountfile.txt','w') as fil:
        fil.write(" "+carnum+ ",0\n")
        
def checkformemberships(carnum, membership, years, month, day):
    txt = "YES"
    boolflag = False

    years = int(years)
    if membership == "Monthly":            
        if (current_time.month == int(month)+1) or (month == 1 and current_time.month == 12) and (int(date) == currentime_day):
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
        if (current_time.year == years +1) and (int(date) == currentime_day) and (int(month) == current_month):
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

##MAIN FUNCTION STARTS HERE
bigloopflag = False
bigloop2 = False
countyearly = 0
countmonthly = 0
createhelp()

carnum = input("Enter your car registration number that must be in the form AAA-999: ")
exp = re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", carnum)
while (len(exp)==0):
    carnum = input("Invalid input. Must be in the form AAA-999: ")
    exp = re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", carnum)
    
#clearall(carnum)
testfunc(carnum)

while bigloop2 == False:
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
                line = " "+ name + "," + carnum + ","+"NO\n"  
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
                            
                            with open("Walletdetails.txt", 'r') as file:
                                Lines = file.readlines()         
                                for line in Lines:
                                    if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):  
                                        oldmon = re.findall(r"[0-9]*$", line)
                                        oldmon = oldmon[0].strip()
                            
                            money = money + int(oldmon)
                            filtowrite = open('Walletdetails.txt').read().replace(oldmon, str(money))
                            with open("Walletdetails.txt", 'w') as file:
                                file.write(filtowrite)                                 

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
                flag10 = False
                print("--------------------------------------------------------")
                print("1: Cancel Existing membership")
                print("2: Create membership")
                print("--------------------------------------------------------")
                choice3 = int(input("choose from above: "))
                while (choice3!=1 and choice3!=2):
                    choice3 = int(input("Invalid choice, try again: "))

                if choice3 == 2:
                    print("**************MEMBERSHIP PLANS****************")
                    print("1: 5000 Rs annually /recommended")
                    print("2: 500 Rs monthly")
                    print("Note: You can cancel the subscription anytime.")
                    print("--------------------------------------------------------")
                    choice4 = int(input("choose from above: "))
                    while (choice4!=1 and choice4!=2):
                        choice4 = int(input("Invalid choice, try again: "))     
                    if choice4 == 1:
                        with open("Walletdetails.txt", 'r') as fil:
                            flag2 = False
                            Linesx = fil.readlines()                    
                            for linex in Linesx:
                                if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", linex) == carnum.split()):
                                    flag2 = True
                                    mon = re.findall(r"[0-9]*$", linex)
                                    mon = mon[0].strip()
                                    mon = int(mon)
                                    temp = int(mon)
                                    if mon>5000:
                                        mon = mon - 5000                                  
                                        with open('Personaldetails.txt', 'r') as filedata :
                                            Lines = filedata.readlines()         
                                            for line in Lines:
                                                if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                                    flag10 = True
                                                    timestr = ","+str(current_time.year) +"-"+ str(current_time.month)+"-" + str(current_time.day)
                                                    filedata = open('Personaldetails.txt').read().replace("NO", "YES").replace('\n', timestr)
                                 
                                                    with open('Personaldetails.txt', 'w') as file:
                                                        file.write(filedata)

                                                    filez = open('Walletdetails.txt').read().replace(str(temp), str(mon))

                                                    with open("Walletdetails.txt", 'w') as filezes:
                                                        filezes.write(filez)  
                                                        
                                                    with open('Personaldetails.txt', 'r') as filedatainfo:
                                                        Linestoread = filedatainfo.readlines()         
                                                        for linez in Linestoread:
                                                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", linez) == carnum.split()):
                                                                years = re.findall(r"[2][0][0-9][0-9]",linez)
                                                                years = years[0].strip()
                                                                find = re.findall(r"\-[0-9]?[0-9]\-",linez)
                                                                month = find[0].strip()
                                                                month = month[1:2]
                                                                day = re.findall(r"[0-9]?[0-9]$",linez)   
                                                                day = day[0].strip()
                                                                            
                                                    checkformemberships(carnum, "Yearly", years, month,day)   
                                                    print("You are now a member!!!")
                                            if flag10 == False:
                                                print("Account not found")
                                    else:
                                        print("Not enough money for membership, add balance to wallet again.")
                                        
                    elif choice4 == 2:
                        with open("Walletdetails.txt", 'r') as fil:
                            flag2 = False
                            Lines = fil.readlines()                    
                            for line in Lines:
                                if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                    flag2 = True
                                    mon = re.findall(r"[0-9]*$", line)
                                    mon = mon[0].strip()
                                    mon = int(mon)
                                    temp = int(mon)
                                    if mon>500:
                                        mon = mon - 500                                  
                                        with open('Personaldetails.txt', 'r') as filedata :
                                            Lines = filedata.readlines()         
                                            for line in Lines:
                                                if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                                    flag10 = True
                                                    timestr = ","+str(current_time.year) +"-"+ str(current_time.month)+"-" + str(current_time.day)
                                                    filedata = open('Personaldetails.txt').read().replace("NO", "YESM").replace('\n', timestr)
                                 
                                                    with open('Personaldetails.txt', 'w') as file:
                                                        file.write(filedata)

                                                    filez = open('Walletdetails.txt').read().replace(str(temp), str(mon))

                                                    with open("Walletdetails.txt", 'w') as filezes:
                                                        filezes.write(filez)  
                                                        
                                                    with open('Personaldetails.txt', 'r') as filedatainfo:
                                                        Linestoread = filedatainfo.readlines()         
                                                        for linez in Linestoread:
                                                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", linez) == carnum.split()):
                                                                years = re.findall(r"[2][0][0-9][0-9]",linez)
                                                                years = years[0].strip()
                                                                find = re.findall(r"\-[0-9]?[0-9]\-",linez)
                                                                month = find[0].strip()
                                                                month = month[1:2]
                                                                day = re.findall(r"[0-9]?[0-9]$",linez)   
                                                                day = day[0].strip()
                                                                            
                                                    checkformemberships(carnum, "Monthly", years, month,day)   
                                                    print("You are now a member!!!")
                                            if flag10 == False:
                                                print("Account not found")
                                    else:
                                        print("Not enough money for membership, add balance to wallet again.")
                else:  
                    txt = "YES"
                    txt2 = ",YESM,"
                    flag3 = False
                    with open('Personaldetails.txt', 'r') as filedata:
                        Lines = filedata.readlines()         
                        for line in Lines:
                            if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", line) == carnum.split()):
                                test = re.findall(r"YES|NO|YESM",line)
                                test = test[0].strip()
                                if test == txt or test== txt2:

                                    torepl = re.findall(r"\,[2][0][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]$",line)
                                    torepl = torepl[0].strip()
                                    if test[0] == ",YESM,":
                                        filedata = open('Personaldetails.txt').read().replace("YESM", "NO").replace(torepl, '\n')
                                    else:
                                        filedata = open('Personaldetails.txt').read().replace("YES", "NO").replace(torepl, '\n')

                                    with open('Personaldetails.txt', 'w') as file:
                                        file.write(filedata)
                                    print("You have been removed as a member.")
                                else:
                                    print("You are not a member")
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
            if contchoice == "no":
                bigloopflag = True

    else:
        timetostay = int(input("Enter the number of hours you want to park the car: "))
        while timetostay<1 or timetostay>18:
            timetostay = int(input("Invalid input, try again: "))

        while (timetostay + current_time.hour)>24:
            print("You can't park your car as parking will close down.")
            timetostay = int(input("Enter the number of hours you want to park the car. If you want to abort, press 0: "))
            if timetostay == 0:
                break
            while timetostay<1 or timetostay>18:
                timetostay = int(input("Invalid input, try again: "))

        txt = "YES"
        txt2 = "YESM"

        while (current_time.hour>=6 and current_time.hour<=24):
            print("--------------------------------------------------------")
            print("WELCOME TO THE PARKING AREA!")
            print("********************************************************")

            spoty = generaterandomspot()
            if check_spot(spoty) == True:
                with open('Personaldetails.txt', 'r') as y:
                    Lines2 = y.readlines()         
                    for linex in Lines2:
                        if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", linex) == carnum.split()):                            
                            if re.findall(r"YES|NO",linex) == txt.split():                                
                                with open('Yearlycountfile.txt', 'r') as datatoread:
                                    datas =datatoread.readlines()
                                    for data in datas:
                                        teststr = "50"
                                        if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", data) == carnum.split()):
                                            check = re.findall(r"[0-9]?[0-9]$", data)
                                            check = check[0].strip()
                                            countyearly +=1
                                            filedatawrite = open("Yearlycountfile.txt").read().replace(check, str(countyearly))
                                            with open("Yearlycountfile.txt", 'w') as filedata:
                                                filedata.write(filedatawrite)
                                            if int(check) > int(teststr):
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

                            elif re.findall(r"YESM|NO",linex) == txt2.split():
                                with open('Monthlycountfile.txt', 'r') as datatoread:
                                    datas =datatoread.readlines()
                                    for data in datas:
                                        teststr = "100"
                                        if (re.findall(r"[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9]", data) == carnum.split()):
                                            check = re.findall(r"[0-9]?[0-9]?[0-9]$", data)
                                            check = check[0].strip()
                                            countyearly +=1
                                            filedatawrite = open("Monthlycountfile.txt").read().replace(check, str(countmonthly))
                                            with open("Monthlycountfile.txt", 'w') as filedata:
                                                filedata.write(filedatawrite)
                                            if int(check) > int(teststr):
                                                filedata = open('Monthlycountfile.txt').read().replace(check, "0")
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
                            print("No account found, you can't park")      
                            break
            else:
                print("Sorry! The parking is currently full.")

            break

    bigloopflag = False
    contchoice2 = input("Do you want to reuse the PARKING SOFTWARE? Enter yes or no: ")
    while(contchoice2.lower()!="yes" and contchoice2.lower()!="no"):
        contchoice2= input("Wrong choice, try again: ")
    if contchoice2 == "yes":
        bigloop2 = False
        
    else:
        bigloop2 = True 

print("********************************************************************")
print("THANK YOU FOR USING OUR SOFTWARE")
print("********************************************************************")
