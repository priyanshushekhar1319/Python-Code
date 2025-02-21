# Write a program to print 1 to 50 using a while loop.
i=1
while(i<=50):
    print(i)
    i+=1

# Write a program to print the content of a list using while loops
l=["anuj","shashi",'bhaskar','lala',]
i=0
while(i<len(l)):
    print(l[i])
    i+=1

# program  to print the multiplication of tables 

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    


# program to check (for else loop )    without break 
for i in range(11):
    print(i)
else:
    print("code run succesfully !")

# program to check (for else loop )    with break 
for i in range(11):
    if i==5:
        print("loop breaking at",i)
        break
    print(i)
else:
        print("loop finished successfully")

# program to check continue statement 
for i in range (100):
     if i==59:
          print("skipping",i)
          continue 
     print(i)

#  printing of right angle traiangle 
n = 10
for i in range(1, n+1):
     print("*" * i)


