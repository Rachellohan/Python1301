"""
#day 7 repetition(loops)
Announcements
1. Keep up with the reading. We are currently on Chapter 7.
2. start chapter 8
3. exam prep materials uploaded to
canvas > files > exam prep materials

What we are going to do today
1. while loops
2. for each loops
3. the range function works with the for each loop
4. keeping a count within a loop
5. indexing strings

"""

# review functions that return bool values

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

number = 4
if is_even(number):
    print("wow")
        
# Topic 1 - While loops
# continues to loop while a condition is True
""" Stand loop structure
1. initialize control value
2. check control condition
3. update control value
"""
name=input("enter your name")
while name != "J@ck3ts":
    print ("incorrect")
    name=input("enter your name")   

# while num is less than 10, print num


# while name is not J@ck3ts, print Incorrect


# another kind of loop is a for loop
# repeats for some number of times
# using specific range(start, stop, step)
# using in operator

##
##word = "jackets"
##for ch in word:
##    print(ch)
##
### what if I want to count from 1 to 20?
### the range function generates a range of ints
##for num in range(1,6): #
##    print(num)
##for num in range(7):  # 
##    print(num)
##for num in range(1,6,2): # 
##    print(num)
##for num in range(7,1,-4):  # 
##    print(num)


# counting in a loop
##vowel_count = 0                # 
##for letter in "jackets":       #
##    if letter in "aeiouAEIOU":
##        vowel_count += 1       #
##print(vowel_count)              
##
##even_count = 0                 #
##for number in range(100):      #
##    if number % 2 == 0:        
##        even_count += 1        #
##print(even_count)


# Indexing strings

##name = "Charles"
##print(name[0])   # C
##print(name[2])   #
##print(name[9])   #
##print(name[-2])  #
##print(name[-5])  #
##print(name[3] + name[2] + name[0])  #
























