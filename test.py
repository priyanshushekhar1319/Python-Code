# # # # n=int(input("enter a number"))
# # # # for i in range(2,n):
# # # #     if (n%i==0):
# # # #          print("number is not prime")
# # # #          break
# # # # else:
# # # #     print("number is prime")

# # # #
# # # # n=int(input("enter a number"))
# # # # sum=0
# # # # for i in range(1,n+1):
  
# # # #     sum=sum+i
# # # #     i+=1
# # # print(sum)
# # # # i=1
# # # # sum=0
# # # # while(i<=n):
# # # #     sum+=i
# # # #     i+=1
# # # # print(sum)
# # # # n=int(input("enter a number"))




# # # for i in range(3): #for rows
# # #     for j in range(3):# for coloumn
# # #         print("*", end="")  # No new line after printing "*"
# # #     print()  # Moves to the next line after one row is printed



# # # for i in range(1,4):
# # #     print("***")   # This code is also right but we can also try nested loop for dynamic coding 




# # # n=int(input("enter the rows: "))
# # # for i in range(1,n+1):
# # #     for j in range(n-i):
# # #         print(" ", end="")
# # #     for k in range(i):

# # #         print("*", end="")
# # #     print( )



# # # n=int(input("enter the rows: "))
# # # for i in range(1,n+1):
# # #     for j in range(n-i):
# # #         print(" ", end="")
# # #     for k in range(1,2*i - 1):

# # #         print("i", end="")
# # #     print( )

# # a=4
# # b=3
# # c=8
# # average=(a+b+c)/3
# # print(average)

# # def priyanshu():
# #     print("hello from a funtion")
# # priyanshu()



# # Alright, let's create examples of these patterns to illustrate what they look like. I'll provide a basic example for each. Keep in mind that there are many variations possible, as shown in the question lists.

# # 1. Right-Aligned Triangle

# #     1
# #    12
# #   123
# #  1234
# # 12345
# # 2. Hollow Number Pyramid

# #     1
# #    1 2
# #   1   3
# #  1     4
# # 1 2 3 4 5
# # 3. Number Butterfly Pattern

# # 1        1
# # 12      21
# # 123    321
# # 1234  4321
# # 1234554321
# # 1234  4321
# # 123    321
# # 12      21
# # 1        1
# # 4. Zigzag Number Pattern

# # 1
# #  23
# #   4
# #  56
# #   7
# #  89
# # 5. Hourglass Pattern

# # 12345
# #  234
# #   3
# #  234
# # 12345
# # 6. Palindromic Number Pattern

# #     1
# #    212
# #   32123
# #  4321234
# # 543212345
# # 7. Spiral Number Pattern (Example 4x4)

# # 1  2  3  4
# # 12 13 14 5
# # 11 16 15 6
# # 10 9  8  7
# # 8. X-Shaped Number Pattern

# # 1   1
# #  2 2
# #   3
# #  2 2
# # 1   1
# # 9. Star-Number Mixed Pattern (Example)

# # *****
# # *123*
# # *456*
# # *****
# # 10. Centered Diamond Pattern

# #     1
# #    121
# #   12321
# #  1234321
# # 123454321
# #  1234321
# #   12321
# #    121
# #     1
        

# import random

# # Computer randomly chooses snake(1), water(-1), or gun(0)
# computer = random.choice([1, -1, 0])

# # User input
# youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# # Dictionary for mapping choices
# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDict = {1: "snake", -1: "water", 0: "gun"}

# # Check if user input is valid
# if youstr not in youDict:
#     print("Invalid choice! Please enter 's' for snake, 'w' for water, or 'g' for gun.")
# else:
#     you = youDict[youstr]

#     print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

#     # Determine the winner
#     if computer == you:
#         print("Match Draw!")
#     elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
#         print("You Lose!")
#     else:
#         print("You Win!")

import random

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

def snake_water_gun_game():
    print("Welcome to Snake, Water, Gun Game!")
    choices = ['snake', 'water', 'gun']
    user_choice = input("Enter your choice (snake, water, gun): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please select from snake, water, or gun.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    snake_water_gun_game()
