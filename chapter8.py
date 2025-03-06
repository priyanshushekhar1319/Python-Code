# Lets understand the chapter Functions and recursions 
# funtion is basically a block of code whhich only runs when it called .
# Quick Quiz: Write a program to greet a user with “Good day” using functions.
def goodday():
    print("good day buddy")
goodday()

# lets learn types of function in Python:
# 1)  Built in function : these are pre-defined funtion in python 
# exm: len(),sum(),print()
# 2) user-defined funtions : Funtion created by the user to perform specific tasks 
# exm: def goodday():
#     print("good day buddy")
# goodday()

#         # Funtions with argument 
# lest understand with the help of example :
def goodday(name):
    print(f"hello,{name}! ")      # this is the example of an argument , we have inserted the name 
goodday("anuj")
goodday("shashi")
goodday("bhaskar")
goodday("lala")
goodday("nitin")


# Waiter sirf bol raha hai (Print)
def chai():
    print("Yeh lo chai!")
# chai()

# order = chai()
# print(order)  # Output: Yeh lo chai!  \n None

def order(food="Pizza", drink="Coke"):
    print(f"Your order: {food} and {drink}")

order("Burger", "Pepsi")  # Output: Your order: Burger and Pepsi
order("Sandwich")         # Output: Your order: Sandwich and Coke
order()                   # Output: Your order: Pizza and Coke


''' 
lets understand the Topic Recursion
basically recursion is a function which call itself until the base condition meet
lets understand with the example : we will do both the noormal and recursion method example 
exm: def print_number(n):
    for i in range(1,n+1):
        print(i)
print_number(5)# ye aapka normal funtion call hai 
     now, the recursion method 
exm: def print_number(n):
        if n==0:
           return 
        print_number(n-1)  
        print(n)
print_number(5)

'''
# def print_number(n):
#    if n==0:
#       return 
#    print_number(n-1)
#    print(n)
# print_number(5)

# lets do with factorial
def factorial(n):
    if (n==0 or n==1):
        return 1
    return n*factorial(n-1)
n=int(input("enter the number: "))
print(f"The factorial of the number is :{factorial(n)} ")


