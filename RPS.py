import random

computer_asn = random.choice(["Rock","Paper","Scissors"])

Rock = "Rock"
Paper = "Paper"
Scissors ="Scissors"
print(computer_asn)
#User Inputs 
#print("Welcome To Rock, Paper, and Scissors")
#User_Choice = input("Enter Your Choice: ")



# Rock Paper Scissors Logic 
if Rock > Scissors and computer_asn == Rock :  
    print("You have Beaten Scissors" + computer_asn)
elif Rock < Paper and computer_asn == Rock :
    print("You have lost" + computer_asn)
elif Rock == Rock and computer_asn == Rock :
    print(" Its a Tie " + computer_asn)

if Paper > Rock and computer_asn == Paper :
    print("You have beaten Rock " + computer_asn)
elif Paper < Scissors and computer_asn == Paper :
    print("You have lost to Scissors " + computer_asn)
elif Paper == Paper and computer_asn == Paper :
    print("Its a Tie " + computer_asn)

if Scissors > Paper and computer_asn == Scissors :
    print("You Have Beaten Paper " + computer_asn)
elif Scissors < Rock and computer_asn == Scissors :
    print("You have Lost to The Rock " + computer_asn)
elif Scissors == Scissors and computer_asn == Scissors :
    print("Its a Tie " + computer_asn)
     