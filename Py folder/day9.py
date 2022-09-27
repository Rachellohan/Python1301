"""
Announcements
1. Keep up with the reading. We are currently on Chapter 8. don't forget handouts
are testable material and can be found at Canvas > Files > Handouts
2. first exam will given next Monday during class. Get here early!


What we did last time
1. The break statement to exit a loop
2. The continue statement to go back to the top of a loop
3. More practice with counts and totals
4. Practice building a new string


What we are going to do today
1. Nested loops
2. String indexing  # one character
3. String slicing   # one or more characters
"""

from base64 import encode


for hour in range(25):
    print(hour,end=':')
    for min in range(61):
        print(hour, min, end=':')
        for sec in range (61):
             print(hour, min, sec, end=':')
             for milSec in range (101):
                print(hour, min, sec,milSec, end=':')
                


# topic 1: Nexted loops
# if a loop is nested within another loop, the inner loop executes completely
# before each new iteration of the outer loop
##
##write the nested loops for an analog clock

    

##for num1 in range(5):  # 2
##    for num2 in range(10,15): # 10
##        print(num1)
##        print(num2)
##

##count = 0
##for factory in range(10):
##    #print(factory)
##    for div in range(10):
##        #print("count this division which is number " + str(div))
##        count += 1  
##print(count)

##count = 0
##for factory in range(5):
##    if factory == 3:
##        break
##    for div in range(10):
##        count += 1
##print(count)

##count = 0
##for factory in range(5):
##    for div in range(10):
##        if factory == 3:
##            break
##        count += 1
##print(count)

# String slicing
# slicing gives us multiple characters
##
##print("jackets"[2:4])    # 
##
##print("jackets"[0:5:2]) # 
##
### slicing is more forgiving that than indexing
##
##print("jackets"[25])   
##
##print("jackets"[0:26])  # 
##
##print("jackets"[::]) # 
##
##print("jackets"[::-1]) # 
##
##print("jackets"[2:])

                                 
##newstring = ""
##
##for num in range(3):
##    newstring += str(num) * num   
##
##print(newstring)  # 

###
##newstring = ""
##
##for num in range(3): # 
##    newstring += "jackets"[num:num+2]  # 
##
##print(newstring)   #


















    




























      











        

    
    

























        




      

































        
    
    
