# name=["anuj","shashi","bhaskar","lala", 7, 3.28, True, False] 
# print(name[6])# thats the list 
# name[5]=6.2888888888  # thats we have to remember list are mutable and strings are notmutable.
# print(name[5])
name=[1,2,3,4,5]
name.pop(2)  # removes and return a element from a specific index 
name.append(6)  # adds a  single elemnent at the end of the list 
name.insert(2,4)# inseert a element at a specific index 
name.remove(4)# remove the first occurence of a specified value  
name.reverse() # its just reverse the number 
name.sort()# its just sort in ascending order 
name.extend([7,8]) # its just extend the order 
print(name.count(2))  # returns the number of times a specific elements apperar in the list 
# print(name.index(1))  wrong answer is given later on i will sort this matter 
print(len(name)) # it gives the length of the list 
print(name)
#  #               TUPLES              ##
# tuples is basically an ordered immutable collections of elements 
name=(1,2,3,4,"tarun",True)  
print(name)
#  most used Tuples: 
t1=(1,2,3)  # example concatenation
t2=(8,5,6)
t3=t1+t2
print(t3)
boss=(1,2,2,3,7,8,9)
print(boss.index(1))# find element position and return first occurence of the element 
print(boss.count(2)) # kon sa element kitni baar aaya hai 
print(len(boss))# shows the lenght 
print(boss[1:5])
print(boss[1::2])
print(boss[: : -2])
print(boss*3)
