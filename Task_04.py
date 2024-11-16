# Rock , Paper and Scissor game
import random

user_wins = 0
computer_wins = 0

option = ["rock","paper","scissor"]

while True:
    user_input = input("Enter Rock/Paper/Scissor or E to exit : ").lower()
    if user_input == "E" or user_input =="e":
        break

    if user_input not in option:
        continue
    random_number =random.randint(0,2)
    #rock = 0 , paper = 1 , scissor = 2
    computer_pick = option[random_number]
    print("Computer picked : ", computer_pick)

    if user_input == 'rock'and computer_pick =='scissor':
        print("You Won ! ")
        user_wins +=1
    elif user_input == 'paper'and computer_pick =='rock':
        print("You Won ! ")
        user_wins +=1
    elif user_input == 'scissor'and computer_pick =='paper':
        print("You Won ! ")
        user_wins +=1
    elif user_input == computer_pick :
        print("Tie !")
    else :
        print("You Lost ! ")
        computer_wins +=1

print("You Won : ",user_wins," Times ")
print("Computer Won : ",computer_wins," Times ")
print("Goodbye !")