
"""
Announcements
1. Keep up with the reading. Read chapters 7 and 8.
2. Exam 1 topic list has been posted

What we did last time
1. while loops
2. for each loops     for letter in "jackets":
3. the range function      for num in range(1,11):  
4. keeping a count within a loop
5. intro to string indexing


What we are going to do today
1. Building a string using a loop
2. keeping a total within a loop
3. The break statement to exit a loop
4. The continue statement to go back to the top of a loop
5. More practice with counts and totals
6. string indexing in a loop

"""


###count the number of vowels in a string (from Wed.)
count = 0 # initalize
for blah in "jackets":
        if blah in "aeiouAEIOU":
         count += 1
print(count) # don't print or return the count until after the loop
##
##
### building a string using a loop
### create a string containing the even digits between 2 and 10
### "246810"
##newstring = ""  # initialize
##for num in range(2,12,2):
##    newstring += str(num) # concatenate onto the end
##print(newstring)
##
### build a string containing all the letters of "jackets"
### separated by spaces like this "j a c k e t s"
##astring = ""
##for letter in "jackets":
##    astring += letter + " "
##print(astring)
##
##
##
### we can find out the length of the string using the len function
##print(len("jackets"))
##
### how can we get rid of the extra space on the end
##astring = ""
##lettercount = 0
##for letter in "jackets":
##    if lettercount < len("jackets") - 1:
##        astring += letter + " "
##    else:
##        astring += letter
##    lettercount += 1
##print(astring)
##print(len(astring))
##
##
### keeping a total in a loop
### what is the total cost when a customer purchases 5 items
##cost_total = 0.0
##for num in range(5):
##    price = float(input("Enter price: "))
##    cost_total += price
##print("You owe {}".format(cost_total))


### breaking out of a loop with break
##
##cost_total = 0.0
##for num in range(5):
##    price = float(input("Enter price: "))
##    cost_total += price
##    if cost_total > 100.0:
##        break # exits the loop immediately
##print("You owe {}".format(cost_total))

# continue is sort of like break, but it says
# immediately go back to the start of the loop
##
##for num in range(10):
##    print(num)
##    if num %2 == 1:
##        continue # go back to the start of the loop
##    print(num * 2)
##    print()


# this is useful for checking for divide by zero errors!
for num in range(-3,3):
    if num == 0:
        continue   # get the next data item
    print(100 / num)
    

# indexing into a string within a loop

word = "jackets"
for num in range(6,0,-1):
    print(word[num])





    








    
    












    

    










    




    
