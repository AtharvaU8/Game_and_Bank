import random

try:
    with open("your_bank_money.txt") as oro:
            re = oro.read()
    with open("chances_poke.txt") as c:
            chance = c.read()

    chances = int(chance)
    read = int(re)
    if chances == 0 or "-" in chance:
        with open("chances_poke.txt","w") as cw:
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
                with open("chances_poke.txt","w") as wo:
                    wo.write(aw)
            elif a > read:
                print("The money you entered is not available in your bank account")
                exit()
        elif add == "e":
            exit()
    pokemon = random.randint(1,2)
    opokemon = random.randint(1,2)

    yourpokHp = 10
    oppopokHp = 10
    zero = 0

    if pokemon == 1:
        print("\nYour Pokemon,\n\nPokemon: Pikachu\nHP: 10 HP\nAttack: ThunderBolt and ThunderShock\n\n\t\tVS\t\t")
        pokemon = 1
    elif pokemon == 2:
        print("\nYour,Pokemon\n\nPokemon: Squirtle\nHP: 10 HP\nAttack: Bubble and Aquatail\n\n\t\tVS\t\t")
        pokemon = 2


    if opokemon == 1:
        print("\nOpponent's Pokemon,\n\nPokemon: Pikachu\nHP: 10 HP\nAttack: ThunderBolt and ThunderShock\n\n")
        opokemon = 1
    elif opokemon == 2:
        print("\nOpponent's Pokemon,\n\nPokemon: Squirtle\nHP: 10 HP\nAttack: Bubble and Aquatail\n\n")
        opokemon = 2



    while(yourpokHp!=0 or oppopokHp!=0):

        attackop = random.randint(1,2)
        ydamattack = random.randint(0,5)
        opdamattack = random.randint(0,5)
        try:

            if pokemon == 1:
                attack = int(input("\nEnter 1 for ThunderBolt and 2 for ThunderShock:\t"))
            elif pokemon == 2:
                attack = int(input("\nEnter 1 for Bubble and 2 for Aquatail:\t"))
                
            if attack == 1:
                if "-" in str(oppopokHp):
                    oppopokHp = oppopokHp.replace("-","")
                    exit()
                oppopokHp = oppopokHp - ydamattack
                print(f"Opponent's pokemon remained {oppopokHp} HP")   
            elif attack == 2:
                if "-" in str(oppopokHp):
                    oppopokHp = oppopokHp.replace("-","")
                    exit()
                oppopokHp = oppopokHp - ydamattack
                print(f"Opponent's pokemon remained {oppopokHp} HP")
            else:
                print("Please ,Enter 1 or 2 for attack")

            if attackop == 1:
                if "-" in str(yourpokHp):
                    yourpokHp = yourpokHp.replace("-","")
                    exit()
                yourpokHp = yourpokHp - opdamattack 
                print(f"\nOpponent's chance, \nYour pokemon remained {yourpokHp} HP")    
            elif attackop == 2:
                if "-" in str(yourpokHp):
                    yourpokHp = yourpokHp.replace("-","")
                    exit()
                yourpokHp = yourpokHp - opdamattack
                print(f"\nOpponent's chance, Your pokemon remained {yourpokHp} HP")
                
            if yourpokHp == 0 or "-" in str(yourpokHp):
                with open("chances_poke.txt","w") as cr:
                    cr.write(str(chances))
                with open("chances_poke.txt") as y:
                    yr = y.read()
                ym = int(yr) - 1
                with open("chances_poke.txt","w") as yw:
                    yw.write(str(ym))
                print("\nYou Lose!\nYou Lose 1 chance")
                break
                
            elif oppopokHp == 0 or "-" in str(oppopokHp):
                with open("your_bank_money.txt") as y:
                    yr = y.read()
                ym = int(yr) + 1
                with open("your_bank_money.txt","w") as yw:
                    yw.write(str(ym))
                print("\nCongrats,You Win!\nYou got 1 rupee")
                break
        except Exception as error:
            print("Invalid Input, Please Enter Valid Input")

except Exception as erro:
            print(erro)