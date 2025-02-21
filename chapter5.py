#    dictionary and sets
marks= {
    "anuj":100,
    "shashi":82,
    "bhaskar":91,
    "lala":80
     }
print(marks,type(marks)) # example of dictionaries
# methods of dictionaries
print(marks.items())  # returns a list of (key,value) tuples
print(marks.keys())# returns a list containing dictionaries keys 
marks.update({"anuj":99,"nitin":79}) # updates the dictionaries with supplied key value pairs 
print(marks)
print(marks.get("anuj")) # returns thevalue of the specified key  abd the returns the keys 
print(marks["anuj"]) # difference is written in the copy 
print(marks.pop("nitin"))  # ye (.pop)[specific key ko hatakar uski value ko return karta hai ] 
print(marks)

    #  most used dictionaries 
# get()	Safe retrieval of values
# keys()	Fetch all keys
# values()	Fetch all values
# items()	Fetch key-value pairs (best for loops)
# update()	Modify or merge dictionaries
# pop()	Remove a specific key
# popitem()	Remove last inserted item
# clear()	Empty the dictionary
    #   SET
s={1,2,1,3,3,8,75}
print(s)
s.add(85) # add 
print(s)
s.remove(85)#remove
print(s)
s.pop() # pop
print(s)
p={1,2,3,4,5,6,7,8,9}# new set for clear example 
print(p)
p.clear()
print(p)
   # union and intersection 
s1={1,2,4,5}
s2={5,4,3,1}
print(s1.union(s2))  #union do sets ko merge karta hai aur duplicate hatata hai 
print(s1.intersection(s2))# intersection just common element batata hai 
print(s1.difference(s2))   # differece - ek set ke wo elemnt jo dusre mein nhi hai 
#   Agar ek element add karna ho → add(x)
# Agar ek element delete karna ho (safe way) → discard(x)
# Agar dono sets ka combination chahiye → union()
# Agar sirf common elements chahiye → intersection()
# Agar sirf unique elements chahiye → difference()
# Agar dono sets ke uncommon elements chahiye → symmetric_difference()
# Agar set ko empty karna ho → clear()

