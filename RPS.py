from random import randint

t = ["Rock","Paper","Scissors"]

computer_asn = t[randint(0,2)]

print(computer_asn)
#User Inputs 
User_Choice = False
while User_Choice == False:
    
    print("Welcome To Rock, Paper, and Scissors")
    User_Choice = input("Rock, Paper, Scissors? ")

    

    if User_Choice == computer_asn:
        print("Tie")
    elif User_Choice == "Rock":
        if computer_asn == "Paper":
            print("You Lose! ",computer_asn,"covers ",User_Choice)

        else:
            print("You win!", User_Choice,"smashes",computer_asn)

    elif User_Choice == "Paper":
        if computer_asn == "Scissors":
            print("You lose!",computer_asn, "cut", User_Choice)
        else:
            print("You win!", User_Choice, "Covers", computer_asn)

    elif User_Choice == "Scissors":
        if computer_asn == "Rock":
            print("You lose...",computer_asn,"smashes",User_Choice)
        else:
            print("You Win", User_Choice,"cut",computer_asn)
    else:
        print("Thats not a valid play. check your spelling!")

    User_Choice = False
    computer_asn = t[randint(0,2)]