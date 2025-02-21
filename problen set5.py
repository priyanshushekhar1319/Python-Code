# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
words={ "ghadi":"watch",
        "kitab":"book",
        "salaii":"matchbox",
        "kapda":"cloth" }
word=input("enter your words you want meaning off : ")
print(words[word])


# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).
s=set()
d=(input("enter the number1: "))
s.add(int(d))
d=(input("enter the number2: "))
s.add(int(d))
d=(input("enter the number3: "))
s.add(int(d))
d=(input("enter the number4: "))
s.add(int(d))
d=(input("enter the number5: "))
s.add(int(d))
d=(input("enter the number6: "))
s.add(int(d))
d=(input("enter the number7: "))
s.add(int(d))
d=(input("enter the number8: "))
s.add(int(d))
print(s)
   
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s=set()
s.add(18)  # yes we ccan have a set with 18(int) and '18' (str) in it bacause both are of different data types 
s.add('18')
print(s)

# 4. What will be the length of following set 
s = set()
s.add(20)     # bhai dekho ye 20==20.0 comparaison operators se dekho toh same hogye hai 
s.add(20.0)
s.add('20') # length of s after these operations?
print(len(s))

# 5. s = {}
# What is the type of 's'?
s={}
print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
d={}
name=input("enter your name: ")
lang=input("enter your language: ")
d.update({name:lang})
name=input("enter your name: ")
lang=input("enter your language: ")
d.update({name:lang})
name=input("enter your name: ")
lang=input("enter your language: ")
d.update({name:lang})
name=input("enter your name: ")
lang=input("enter your language: ")
d.update({name:lang})
print(d)

# 7. If the names of 2 friends are same; what will happen to the program in problem
# 6?
                          #  it will update the last entry


# 8. If languages of two friends are same; what will happen to the program in problem
# 6?
#  same it will update 



# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [
# it is unchangeble 