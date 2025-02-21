# . Write a program to store seven fruits in a list entered by the user.
# Empty list to store fruits
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)
print("The list of fruits you entered is:")
print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.
marks=[]
f1=int(input("enter the marks here : "))
marks.append(f1)
f2=int(input("enter the marks here : "))
marks.append(f2)
f3=int(input("enter the marks here : "))
marks.append(f3)
f4=int(input("enter the marks here : "))
marks.append(f4)
f5=int(input("enter the marks here : "))
marks.append(f5)
f6=int(input("enter the marks here : "))
marks.append(f6)
marks.sort()
print(marks)

# 3. Check that a tuple type cannot be changed in python.
a=(1,2,3,"hello")
a[2]=4
print(a)

# 4. Write a program to sum a list with 4 numbers.
l=[1,2,4,8]
print(sum(l))
# 5. Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9) 
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))