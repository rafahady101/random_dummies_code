count = 0
data = {}
candidates = [["Berlin",0],["Paris",0],["Nairobi",0],["Helshinki",0],["Palermo",0]]
while True:

    print("===== VOTING PROGRAM =====\n",
          "1. Voting\n",
          "2. Database\n",
          "3. Change Data\n",
          "4. Candidates Data\n",
          "0. Exit")
    print()

    def voting(name, choose_vote):
        choosen = candidates[choose_vote-1]
        data[name] = choosen
        print()

    def cancounter(x):
        candidates[x-1][1] += 1

    menu = int(input("Choose menu (1/2/0): "))

    if menu == 1:
        count += 1
        name = str(input("input your name: "))
        print()
        print("=== THE CANDIDATES ===")
        print(" 1. Berlin\n","2. Paris\n","3. Nairobi\n","4. Helshinki\n","5. Palermo")

        choose_vote = int(input("Choose your candidates (1/2/3/4/5): "))
        if 0 < choose_vote <= 5:
            cancounter(choose_vote)
            voting(name.title(),choose_vote)
        else:
            print("No option!\n")
        
    elif menu == 2:
        if count == 0:
            print("Data is empty!\n")
        elif count > 0:
            token = str(input("Input token: "))
            if token == "stardust":
                print()
                print("<<< VOTED DATA >>>")
                num = 0
                for key,value in data.items():
                    num += 1
                    print(num,".",key,"votes",value[0])
                print()
            else:
                print("Your token is not correct!\n")
    
    elif menu == 3:
        if count == 0:
            print("Data is empty\n")
        elif count > 0:
            name = str(input("Input your name: "))
            if name.capitalize() in data:
                print()
                print("=== THE CANDIDATES ===")
                print(" 1. Berlin\n","2. Paris\n","3. Nairobi\n","4. Helshinki\n","5. Palermo")
                print(data)
                data[name.capitalize()][1] -= 1
                choose_vote = int(input("Choose your candidates (1/2/3/4/5): "))
                cancounter(choose_vote)
                voting(name.capitalize(),choose_vote)
            elif name not in data:
                print("You haven't voted yet\n")

    elif menu == 4:
        print()
        print("<<< Candidates Data >>>")
        print("Votes for Berlin:",candidates[0][1])
        print("Votes for Paris:",candidates[1][1])
        print("Votes for Nairobi:",candidates[2][1])
        print("Votes for Helshinki:",candidates[3][1])
        print("Votes for Palermo:",candidates[4][1])
        print()

    elif menu == 0:
        print("Thanks for using our program!")
        break

    else:
        print("Choose the correct option, please try again\n")


        
