import random

user_wins=0
computer_wins=0

options=["rock","paper","scissors"]
 
while True:
    user_input=input("type Rock/Paper/Scissors/q to quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue

    random_number =random.randint(0,2)
    computer_pick=options[random_number]
    print("computer pickes",computer_pick )

    if user_input=="rock" and computer_pick=="scissors":
        print("you won")
        user_wins+=1
    
    elif user_input=="paper" and computer_pick=="rock":
            print("you won")
            user_wins+=1
    elif user_input=="scissors" and computer_pick=="paper":
            print("you won")
            user_wins+=1
    elif user_input==computer_pick:
             print("it's a tie")
    else:
         print("you lost")
         computer_wins+=1

print("you won" ,user_wins , "times")
print("computer won" ,computer_wins , "times")


