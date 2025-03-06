# 1. Write a program using functions to find greatest of three numbers.

# def greatest(a,b,c):
#     if (a > b and a > c):
#         return(a)
#     elif (b > a and b > c):
#         return(b)
#     else:
#         return(c)
# a=int(input("enter the number a: "))  
# b=int(input("enter the number b: "))
# c=int(input("enter the number c: "))
# print(f"the gretest number is :{greatest(a,b,c)}")

# 2. Write a python program using function to convert Celsius to Fahrenheit.

# def celcius_to_farhenheit (C):
#     return ((C*1.8)+32)
# C=float(input("enter the celcius: "))
# print(f"The farhenheit is : {celcius_to_farhenheit (C):.2f}")     # :.2f  ye :.2f likhne se upto 2 decimal places tk dega 

# 3. How python print() function do you prevent a  to print a new line at the end.

# by using end=""

# 4. Write a recursive function to calculate the sum of first n natural numbers.

# def natural_number(n):
#     return n*(n+1)/2
# n=int(input("enter thr number: "))
# print(f"the sum of the number is: {natural_number(n)}")   # this is formula based 
#      now recursion based 
# def sum_natural(n):
#     if n==1:
#         return 1
#     return n + sum_natural(n-1)
# n=int(input("enter thr number: "))
# print(f"the sum of the number is: {sum_natural(n)}")  

# 5. Write a python function to print first n lines of the following pattern:

# ***
# **       # for n = 3
# *

# def pattern(n):
#     for i in range (n): # for rows 
#         for j in range (n-i):  # for star 
#             print("*" ,end="")  
#         print()  
# n=int(input("enter the rows: "))
# print(pattern(n))

# def pattern(n):
#     if n==0:
#         return          # by using recursion
#     print("*" * n)
#     pattern(n-1)
# n=int(input("enter the rows: "))
# pattern(n)



# 6. Write a python function which converts inches to cms.
# def inches_to_cms(n):
#     return (n*2.54)
# n=float(input("enter the inches : "))
# print(inches_to_cms(n),"cms")

#    if we want to convert cms to inches then just do:
# def cms_to_inches(n):
#     return (n/2.54)
# n=float(input("enter the cms : "))
# print(cms_to_inches(n),"inches")

# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.

# i have to do it later 


# 8. Write a python function to print multiplication table of a given number.
# def multiplication(n):
#     for i in range (1,11):
#         print(f"{n} x {i} = {n*i}")
# n=int(input("enter the number: "))
# multiplication(n)