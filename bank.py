import random


try:

    with open("your_bank_money.txt") as yb:
        yourm = yb.read()
    yourmoney = int(yourm)

    an = random.randint(100000000,999999999)
    n = random.randint(0,20)

    register = input("\nYou have to make new account to continue:\nEnter 'c' if you have to create an account\nEnter 'e' to exit\n")


    if register == "e":
        exit()
    elif register == "c":
        print(f"Your accout number is: {an}")
        pin = int(input(f"Enter Your Pin: "))
        print("Your account is ready")
        with open(f"bankac_no{n}.txt","w+") as e:
            e.write(f'{an}')
        with open(f"bankac_pin{n}.txt","w+") as n:
            n.write(f'{pin}')





    while True:
        choice = input("\nWhat you want to do:\nEnter 'w' to Withdaraw Cash\nEnter 'b' to Check Your balance\nEnter 'd' to Deposite Cash\nEnter 'e' to exit\n")

        if choice == "b":
            print(f"\n{yourmoney}")
        elif choice == "d":
            with open("your_cash.txt") as r:
                ym = r.read()
            yourcash = int(ym)
            deposite = int(input("\nEnter a Amount: "))
            if deposite <= yourcash:
                yourcash -= deposite
                yourmoney += deposite
                with open("your_bank_money.txt","w") as yb:
                    yb.write(str(yourmoney))
                with open('your_cash.txt','w') as yc:
                    yc.write(str(yourcash))
                print("Your money is sucessful deposited")
            elif yourcash < deposite:
                print("The money you entered in the bank is not have available you")
        elif choice == 'w':
            with open("your_cash.txt") as r:
                yc = r.read()
            yourcash = int(yc)
            bankac = int(input("\nEnter your bank account number: "))
            pining = int(input("Enter your bank account pin: "))            
            if an != bankac or pin != pining:
                print("\nInvalid pin or bank account number, Please Try Again")
            elif an == bankac and pin == pining:
                amount = int(input("\nEnter how much cash you want to withdraw: "))
                if amount > yourmoney:
                    print("\ninvalid amount, please valid amount: ")
                elif amount <= yourmoney:
                    yourmoney -= amount
                    yourcash += amount
                    with open("your_bank_money.txt","w") as t:
                        t.write(str(yourmoney))
                    with open("your_cash.txt","w") as t:
                        t.write(str(yourcash))
                    print("You withdrawed, Your money")

        elif choice == "e":
            exit()
except Exception as w:
    print(w)