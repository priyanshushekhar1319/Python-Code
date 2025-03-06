# Write a program to print multiplication table of a given number using for loop.
# num=int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):  # remember to write capital S then it will return output 
        print("hello",name)

# Attempt problem 1 using while loop.
# num=int(input("enter a number: "))
# i=1
# while(i<=10):
#         print(f"{num} x {i} = {num*i}")
#         i+=1
 
#  4. Write a program to find whether a given number is prime or not.
# n=int(input("enter a number: "))
# for i in range(2,n): # isko sise bhi likh shakte hai [for i in range(2,int(n**0.5)+1)]
#      if(n%i==0):
#           print("number is not prime ")
#           break
# else:
#      print("number is prime")

# 5. Write a program to find the sum of first n natural numbers using while loop.
# n=int(input("enter the number: "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)

# Write a program to calculate the factorial of a given number using for loop.
# n=int(input("enter a number : "))
# factorial=1
# for i in range(1,n+1):
#     factorial = factorial * i
# print(f"the factorial of {n} is {factorial}")

# Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3

# n=int(input("enter the rows: "))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i - 1):

#         print("*", end="")
#     print( )

# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3
# n=int(input("enter the rows: "))
# for i in range(1,n+1):
#     for k in range(i):
#         print("*",end="")
#     for j in range(n-i):
#         print(" ",end="")
#     print()

# Write a program to print the following star pattern.
# * * *
# *   *   for n = 3
# * * *

# n=int(input("enter the rows: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("* "*n,end="")
#     else:
#         print("* ",end="")
#         print("  " *(n-2),end="")
#         print("* ",end="")
#     print()

# 10. Write a program to print multiplication table of n using for loops in reversed
# order.
n=int(input("enter a number: "))
for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")

# 1  10
# 2  9
# 3  8      isme kya dikh rha hai sbhi ka sum 11 aaaraha hai
# 4  7      toh agar hm (11-i) kr de toh nikal shakta hai reversed order 
# 5  6
# 6  5
# 7  4
# 8  3
# 9  2
# 10 1
# or
num=int(input("enter a number: "))
for i in range(10,0,-1):
        print(f"{num} x {i} = {num*i}")



   
