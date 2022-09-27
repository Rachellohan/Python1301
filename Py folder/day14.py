"""
# day 14 - Tuples (Chapter 9)

Announcements
1. exams have been returned - you should have gotten an email - regrade policy
2. keep up with the reading - tuples are chapter 9

What we did last time 
1. list methods (remember they return None, not a new list)
2. nested lists

What we're doing this time
0. review aliases and clones
1. a tuple is a new compound data structure
2. similar to a list in that it can be store mixed data types
3. similar to a string in that it is immutable
4. tuples can be contatenated or multiplied
5. tuples are great for swapping values
6. tuples are useful so a function can return multiple values
7. tuples only have two methods .count and .index

"""
biglist =[1,4,'todler',5.99]
# alias (another name for the same thing)

mylist=biglist
biglist.append(999) # both have a 999
print(biglist)
print(mylist)

# clone (a copy)
otherlist = biglist[:] # copy every element of the list separately
biglist.append(888)
print(biglist)
print(otherlist)

# a tuple is a non homogenous immutable compound data structure (iterable)
# creating tuples
empty_tup = ()
tup_with_one = ("cat",)
tup_with_many = (3,5,6,7)
tup1 = ("cat",3,5,1.0,True)

print(tup1)
print(len(tup1))
print(tup1[0])
print(tup1[2:4])
##tup1[0] = "dog" # you can't change a piece of a tuple


# tuples are good for creating a record of related information
student1 = ("Naomi",18,4.0)
student2 = ("Arvin",21,3.0)
students = [student1,student2]
print(students) ##list of tuples


print(type("cat",))     # why? paraentasets
print(type(("cat",)))   # why?

newitem = tuple("cat")
print(type(newitem))
print(newitem)
##
newitem = tuple([1,2,3])
print(type(newitem))
print(newitem)

# tuples can be concatenated
tup1 = (2,3)
tup2 = ("dog","cat")
tup3 = tup1 + tup2
print(tup3)
tup3 = tup3 * 4
print(tup3)


# tuple methods - only these two
tup1 = (2,3)
print(tup1.count(3)) # output? 1
print(tup1.index(3)) # output? [1]

# tuples are nice for assigning values to variables
(counta,countb,countc,countd,count3) = (0,2,4,1,70)
print(counta)

# tuples are nice for swapping values
name1 = "Naomi"
name2 = "Arvin"
(name1,name2) = (name2,name1)
print(name1)      # output ? arvin
print(name2)      # output ? naomi


# most often tuples are used for pieces of info
# within a list

prod1 = ("x35",9.99,1923)
prod2 = ("b35",10.99,109)
prod3 = ("k21",8.99,19992)
##
products = [prod1,prod2,prod3]

# how many total products do I have? 3
total = 0
for prod_tup in products:
    if prod_tup[1] > 10.0:
        total += prod_tup[2]
print(total)


# how many total products do I have that cost over $10? 1
# how many total products do I have? 3
total = 0
for (name,cost,quantity) in products:
    if cost > 10.0:
        total += quantity
print(total)


# which product do I have the most of?
max_tup = ("unknown",0.0,0)
for (name,cost,quantity) in products:
    if quantity > max_tup[2]:
        max_tup = (name,cost,quantity)
(name,cost,quantity) = max_tup
print(name)




















    











































