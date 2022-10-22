try:
    name = None
    points = 0

    with open("your_bank_money.txt") as oro:
            re = oro.read()
    with open("chances.txt") as c:
        chance = c.read()

    chances = int(chance)
    read = int(re)
    if chances == 0 or "-" in chance:
        with open("chances.txt","w") as cw:
            cw.write("0")
        print("\nThe program is ended because your chances are over\n")
        add = input("Enter 'a' to add money\nEnter 'e' to exit\n")
        if add == "a":
            a = int(input("1 rupee = 1 chance\nEnter how many chances you have to add\n"))
            if a <= read:
                sub = read - a
                ss = str(sub)
                with open("your_bank_money.txt","w") as o:
                    o.write(ss)
                aw = str(a)
                with open("chances.txt","w") as wo:
                    wo.write(aw)
            elif a > read:
                print("The money you entered is not available in your bank account")
                exit()
        elif add == "e":
            exit()
        
        chances = chances - 1
        with open("chances.txt","w") as cr:
            cr.write(str(chances))

    while True:
        print("\nWelCome to Quiz Game!!!")
        option = input("\n> Entrer 'S' to Start the Game\n> Enter 'V' to view High Score \n> Enter 'R' to reset the High Score\n> Enter 'H' for help\n> Enter 'F' to view Hall of Fame\n> Enter 'Q' to Quit the Game\n")

        if option == "h":
            print("\n> In this game you have 10 questions and 4 options for each question\n> Choose one option for each question\n> if you got higher score than high score your score will be saved")

        elif option == "v":
            print("")
            with open("quiz_high_score.txt") as l:
                y = l.read()
            print("\nThe High Score is: ",y)
        
        elif option == "r":
            print()
            with open("quiz_high_score.txt","w") as r:
                r.write("0")
            print("The High Score is Reseted")
        
        elif option == "f":
            print("")
            with open("hall_of_fame_Quiz.txt") as f:
                h = f.read()
            print(h)

        elif option == "q":
            print("You Quit the Game\n")
            exit()

        elif option == "s":
            name = input("Enter Your Name: ")

            q1 = input("\n1.Ctrl, Shift and Alt are called which keys?\n(a) modifier\n(b) function\n(c) alphanumeric\n(d) adjustmen\n")
            if q1 == "a":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (a) modifier\n")

            q2 =  input("2.Fastest Shorthand Writer was?\n(a) Dr. G. D. Bist\n(b) J.R.D. Tata\n(c) J.M. Tagore\n(d) Khudada Khan\n")
            if q2 == "a":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (a) Dr. G. D. Bist\n")

            q3 = input("3.MS-Word is an example of_____\n(a) An operating system\n(b) A processing device\n(c) An input device\n(d) Application software\n")
            if q3 == "d":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (d) Application software\n")

            q4 = input("4.National Income estimates in India are prepared by..\n(a) Planning Commission\n(b) Reserve Bank of India\n(c) Central statistical\n(d) Indian statistical Institute\n")
            if q4 == "c":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (c) Central statistical\n")

            q5 = input("5.The tropic of cancer does not pass through which of these Indian states ?\n(a) Madhya Pradesh\n(b) West Bengal\n(c) Rajasthan\n(d) Odisha\n")
            if q5 == "d":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (d) Odisha\n")

            q6 = input("6.Fathometer is used to measure\n(a) Earthquakes\n(b) Rainfall\n(c) Ocean depth\n(d) Sound intensity\n")
            if q6 == "c":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (c) Ocean depth\n")

            q7 = input("7.The purest form of iron is\n(a) wrought iron\n(b) steel\n(c) pig iron\n(d) nickel steel\n")
            if q7 == "a":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (a) wrought iron\n")

            q8 = input("8.Which river of India is called Vridha Ganga?\n(a) Krishna\n(b) Godavari\n(c) Kaveri\n(d) Narmada\n")
            if q8 == "b":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (b) Godavari\n")

            q9 = input("9.Which latitude passes through the middle of India?\n(a) Equator\n(b) Arctic Circle\n(c) Tropic of Capricorn\n(d) Tropic of Cancer\n")
            if q9 == "d":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (d) Tropic of Cancer\n")

            q10 = input("10.The Saka Era was founded by\n(a) Kadphises \n(b) Kanishka\n(c) Alexander\n(d) Menander\n")
            if q10 == "b":
                print("Correct Answer!!!!\n")
                points += 1
            else:
                print("Wrong Answer...The Correct Answer is (b) Kanishka\n")

            print(f"{name} Your Score is: {points}")

            with open("your_bank_money.txt") as y:
               yr = y.read()

            ym = int(yr) + points 

            with open("your_bank_money.txt","w") as yw:
                yw.write(str(ym))

            if points<3:
                print("Try Next Time !")
            elif points<5 and points<3:
                print("Not Bad,Good !!")
            elif points>=5 and points<=7:
                print("Vrey Good Points !!!")
            elif points>7 and points<=9:
                print("!!! Excellent !!!")
            elif points == 10:
                print("!!!! Congratulations, Your Now a Brilliant of Our Quiz and your name is in HALL OF FAME !!!!\n")
                with open("hall_of_fame_Quiz.txt","a") as a:
                    a.write(f"{name}\n")

                break
            

            with open("quiz_high_score.txt") as first:
                highscore = first.read()
            
                if int(highscore)<points:
                    with open("quiz_high_score.txt","w") as a:
                        a.write(str(points))
                        exit()
                else:
                    exit()    

                
except Exception as a:
    print(a)