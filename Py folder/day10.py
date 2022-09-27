# day 10 - advanced string slicing, string methods
"""
Announcements
1. Keep up with the reading. Chapter 8 and Indexing Handout!
2. Review session for exam 1 Friday 4:30 to 6

What we did last time
1. Nested loops
2. String indexing  # one character
3. String slicing   # one or more characters

What we are going to do today
1. String indexing and slicing in a loop
2. More practice building and "changing" strings
3. String methods
"""

# reviewing string slicing
from operator import truediv


print("Spongebob"[-8:-6:2])  #
print("Sponge"[-3:-5]) # 

# Coding example from last lecture:

#### Write a function called has_three that returns True if the
####   the str parameter has three of the same characters in a row and False
####   otherwise

#def has_three(astr):
 #   for char in astr:
        #if char.count()==3 in astr:
           #return True
       # else:
     #      return False
   ## pass
    
#print(has_three("caaat"))   # 
#print(has_three("ccaatt"))   # 



# topic 1 string indexing and slicing in loop
# write a function get_letters that takes a string
# and returns the first n letters and the last n letters concatenated together
# where n is the second input parameter - assume there are at least n letters

def get_letters(astr,n):
    for char in astr:
        if len(n>= n*2):
            print (astr[:n] + astr[:2:-1])
    pass    

print(get_letters("basketball",3)) #  basall


# topic 2 - building and changing strings
# strings are immutable, they cannot be changed
##name = "What's Up"
##name = name + "!"   #
##print(name)
##name[0] = "m"  # 
##name = "m" + name[1:]  # 
##print(name)

# write a function that changes all the vowels in a phrase to "X" - return
# the changed phrase

##def change_phrase(astr):
##    pass
##
##print(change_phrase("jackets"))

# Topic 3 str methods

# a method is a special type of function that works only with one particular
# data type and that are called using the . operator (dot notation)
# str methods do not change the str, they create a new str

### these return a new str:
##print("cat".upper())
##print("cat".replace("a","X"))
##
##
### some str methods return an int or a bool
##word = "jackets"
##print(word[0].isdigit())
##print(word[0].islower())
##print(word.find("x")) # 

##word = "tent"
### find the first "t" in word
##print(word.find("t"))
### find the second "t" in word
##print(word.find("t"))
### find all the "t"s in the word
##def findall(word,letter):
##    pass























        
        
    












    
# topic 
