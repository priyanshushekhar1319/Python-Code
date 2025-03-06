'''
time to build the SNAKE WATER GAME Which we have played in childhood 
lets denote 
1 = snake 
-1 = water
0 = gun
'''
import random
computer=random.choice([1,-1,0])
youstr=input("enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1: "snake", -1: "water" , 0: "gun"}
if youstr not in youDict :
    print("invalid choice! please select 's' for snake 'w' for water, 'g' for gun.")
else:
    you = youDict[youstr]
    print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")
    if(computer==you):

        print("match draw!")
    elif(computer==1 and you==-1):
        print("you loose!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you loose!")
    elif(computer==0 and you==1):
        print("you loose!")
    elif(computer==0 and you==-1):
        print("you win!")
    else:
        print("something went wrong!")


# lets do it with another method
import random 
def get_computer_choice ():
    return random.choice(['snake','water','gun'])
def determine_winner(user,computer):
    if(computer==user):
        return ("match tie!")
    elif(user=='snake' and computer=='water')or \
        (user=='water' and computer=='gun')or \
        (user=='gun' and computer=='snake' ):
        return("you wins! buddy")
    else:
        return("computer wins!")
def snake_water_gun_game():
    print("wlcome to snake,water,gun game!")
    choice=['snake','water','gun']
    user=input("enter your choice('snake','water','gun'): ")
    if(user not in  choice):
        print("invalid choice please choose for('snake','water','gun')")
        return
    computer_choice = get_computer_choice()
    print(f"computer choose:{computer_choice}")
    result=determine_winner(user,computer_choice)
    print(result)
if __name__== "__main__":
    snake_water_gun_game()    




# import random
# def get_computer_choice():
#     return random.choice(['snake','water','gun'])
# def determine_winner(user_choice,computer_choice):
#     if(computer_choice==user_choice):
#         return("match tie! buddy")
#     elif(user_choice=='snake' and computer_choice=='water') or\
#         (user_choice=='water' and computer_choice=='gun') or\
#         (user_choice=='gun' and computer_choice=='snake'):
#         print("you wins! buddy")
#     else:
#         print("you loose! buddy")
# def snake_water_gun_game():
#     print("welcome to snake_water_gun_game")
#     choice=['snake','water','gun']
#     user_choice=input("enter your choice['snake','water','gun']: ")
#     if (user_choice not in choice):
#         print("invalid choice choose for ['snake','water','gun']")
#         return
#     computer_choice=get_computer_choice()
#     print(f"computer choose: {computer_choice}")
#     result=determine_winner(user_choice,computer_choice)
#     print(result)
# if __name__=="__main__":
#     snake_water_gun_game()

import random
computer_choice=random.choice([1,-1,0])
user_str=input("choose for [s:'snake',w:'water',g:'gun]: ")
user_dict={'s':1,'w':-1,'g':0}
reverse_dict={1:'snake',-1:'water',0:'gun'}
if user_str not in user_dict:
    print("invalid choice ! pls choose from ['snake','water','gun]")
else:
    user_choice = user_dict[user_str]  
    print(f"you choose:{reverse_dict[user_choice]}\n computer choose:{reverse_dict[computer_choice]}")
if(computer_choice==user_choice):
    print("matchh tie !")
elif(user_choice==1 and computer_choice==-1) or\
    (user_choice==-1 and computer_choice==0) or\
    (user_choice==0 and computer_choice==1):
    print("you win buddy!")
else:
    print("you loose!buddy")
    