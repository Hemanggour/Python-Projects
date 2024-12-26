# rock/paper = rock
# paper/scissor = paper
# scissor/rock = scissor
# Same Choice = Draw
import random

obj = {
    "rock": 1,
    "paper": 2,
    "scissor": 3
}
userPoint = compPoint = 0
i = 1
while(i < 4):
    user = int(input("1) Rock\n2) Paper\n3) Scissor\nSelect: "))
    comp = random.randint(1, 3)
    if(user == comp):
        print("Draw")
        continue
    elif((user == obj["rock"] and comp == obj["paper"]) or (user == obj["paper"] and comp == obj["scissor"]) or user == obj["scissor"] and comp == obj["rock"]):
        print("User Win This Round!!")
        userPoint+=1
    elif((comp == obj["rock"] and user == obj["paper"]) or (comp == obj["paper"] and user == obj["scissor"]) or comp == obj["scissor"] and user == obj["rock"]):
        print("Computer Win This Round!!")
        compPoint+=1
    else:
        print("Invalid Input!!")
        continue
    print(f"USER Points {userPoint}\nCOMPUTER Points {compPoint}")
    i+=1
if(userPoint > compPoint):
    print("User Won this game!!")
else:
    print("Computer Won this game!!")