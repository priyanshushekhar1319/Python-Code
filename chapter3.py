#    Some STRING functions 
name="priyanshu shekhar"
print(len(name))# it gives the leght of the code 
print(name.endswith('shu'))#its says the true or false statement 
print(name.startswith('pri'))#its generally says the letter start with pri or not it will return true or false 
print(name.upper())#it capitalize all the characters 
print(name.strip())#it removes the trailing white space "    priyanshu shekhar    "
print(name.capitalize()) # it capitalize the front letter of the word 
count = name.count("s") # this function actually print the count of the number 
print(count)
index=name.find('shekhar')# this function returns the actual array of the letter that in which array the word is present
print(index)
replace = name.replace("shekhar","Bhagat")# it replaces the word 
print(replace)
print(name.split()) #this funtion split a string into a list based on a seperator(default is space)
print("".join(name))#the above and this is co-related because the above will separate and it will JOIN what above is separated
print(name.title())  # its shows the title 
        # Escape characters 
print('hello\n priyanshu ')  # for new line 
print('hello\tpriyanshu')    # add anew space in the string
print('hello priyanshu:\\')  # backslash
print('it\'s a sunny day my gpt') # to add a ('s) in a sentence 
print(' hello \"priyanshu\"') # to add a double quote ("") in a sentence 
print('hello \rpriyanshu how are you?')#\r it generally moves the cursoon to te beginning of the line (overrites the current line )
print("priyaaa\b!") # \b Removes the character before it   