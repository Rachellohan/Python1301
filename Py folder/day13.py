# day 13 - advanced lists - chapter 11
"""
Announcements
1. exam 1 grades will be released over the weekend
 

What we did last time 
1. assigning values to lists
2. looping through lists
3. indexing into loops, slicing lists
4. nested lists 
5. concatenating lists together
6. appending onto lists, inserting into a list


What we're doing today
1. Removing and deleting from a list    del and .remove()
2. other list methods - .reverse(), .sort() these return None
5. coding miniquiz
"""

alist = ["Happy",3,5.5]

#.remove() removes the first occurrence of a specific value from a list
alist = ["Happy",3,5.5]

alist.remove("Happy")
print(alist)
del alist[1]
print(alist)
#del is not a method, delete a single index, a slice, or the complete list


#.reverse() reverses the order of the list




#.sort() sorts the list items in ascending ASCII table decimal value order 
# where capital letters come before lower case letters
# and digits come before capital letters
nums = [3, 5.5, 7, 0]
nums.sort()
print(nums)

names = ["Josh", "Chris","1dog", "chris","112","20","ab","abb"]
names.sort()
print(names)


# nested lists need nested for loops usually
main_list = [[1,2,3],[2,3,4],[4,5,6]]
print(len(main_list)) #
##
for sublist in main_list:
    for number in sublist:
        print(number)
        
# write a loop that goes through main_list and prints
# out the item from each sublist that is at the
# current index of main_list


main_list = [[1,2,3],[2,3,4],[4,5,6]]
def sublist():
    for u in range(len(main_list)):
        for same in sublist == u:
            print (same-1)
            


