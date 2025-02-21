# Write a python program to display a user entered name followed by Good
# Afternoon using input () function.

# name = input('enter your name  ')
# print(f'good afternoon,{name}')

# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# letter =''' Dear <|Name|>,
#       you are selected!
#       <|Date|>'''
# replace=letter.replace("<|Name|>","priyanshu").replace("<|Date|>","27-01-2025")
# print(replace)

# 3. Write a program to detect double space in a string.
name=('priyanshu is a good coder  ')
print(name.find("  "))

# 4. Replace the double space from problem 3 with single spaces.
print(name.replace("  "," "))
# 5. Write a program to format the following letter using escape sequence
# characters.
print('letter = "Dear Harry,\n\t this python course is nice.\n\t Thanks!"')
