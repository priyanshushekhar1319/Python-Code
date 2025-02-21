# Write a program to find the greatest of four numbers entered by the user

num1=int(input("enter your number1: "))
num2=int(input("enter your number2: "))
num3=int(input("enter your number3: "))
num4=int(input("enter your number4: "))
greatest = num1
if (num2>greatest):
    greatest=num2
if (num3>greatest):
    greatest=num3
if (num4>greatest):
    greatest=num4
print(f"The greatest number is :{greatest}" )  # bhai f ka use kuch aisa kisi vi variavle ko direct string mein embeded karna 

# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

math=float(input("Enter the marks of maths: "))
phy=float(input("Enter the marks of physics: "))
chem=float(input("Enter the marks of chemistry: "))
total_marks = math+phy+chem 
percentage=(total_marks/300)*100
if percentage>=40 and  math>=33 and phy>=33 and chem>=33 :
    print(f"congratulation! you are passed and your percentage is {percentage:.2f}%")
else:
    print(f" sorry failed your percentage is {percentage:.2f}%") 

# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("enter the comment : ")
if((p1 in message)or (p2 in message)or (p3 in message)or (p4 in message)):
    print("This comment is spam")
else:
    print("Comment is right" ) 

# Write a program to find whether a given username contains less than 10
# characters or not.

a=input("enter your name: ")
if((len(a)<10)):
    print("perfect")
else:
    print("above 10")    

# Write a program which finds out whether a given name is present in a list or not

b=["hello","anuj","priyanshu","shashi","lala","bhaskar"]
name=(input("enter your name: "))
if(name in b):
    print("present")
else:
    print("not present ")

# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks=int(input("enter your marks: "))
if(90<=marks<=100):
    print(" Grade: excellent")
elif(80<=marks<90):
    print("Grade: A")
elif(70<=marks<80):
    print("Grade: B")
elif(60<=marks<70):
    print("Grade: C")  
elif(50<=marks):
    print("Grade: F")  
else:
    print("enter a valid number")    

# Write a program to find out whether a given post is talking about “priyanshu” or not
post=input("enter your post: ")
if("priyanshu" in post):
    print("yes it is present")
else:
    print("not preseent in post")
