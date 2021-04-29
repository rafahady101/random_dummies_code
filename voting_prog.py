count = 0
data = {}
candidates = ["Berlin","Paris","Nairobi","Helshinki","Palermo"]
while True:
    
    print("===== VOTING PROGRAM =====\n",
          "1. Voting\n",
          "2. Database\n",
          "0. Exit")
    print()
    
    menu = int(input("Choose menu (1/2/0): "))
    if menu == 1:
        count += 1
        name = str(input("input your name: "))
        print()
        print("=== THE CANDIDATES ===")
        print(" 1. Berlin\n","2. Paris\n","3. Nairobi\n","4. Helshinki\n","5. Palermo")

        choose_vote = int(input("Choose your candidates (1/2/3/4/5): "))
        choosen = candidates[choose_vote-1]
        data[name] = choosen
        print()

    elif menu == 2:
        if count == 0:
            print("Data is empty!\n")
        elif count > 0:
            token = str(input("Input token: "))
            if token == "stardust":
                print()
                print("<<< VOTED DATA >>>")
                for key,value in data.items():
                    print(key,"choose",value)
                print()
            else:
                print("Your token is not correct!")
                print()

    elif menu == 0:
        print("Thanks for using our program!")
        break

    else:
        print("Choose the correct option, please try again")
