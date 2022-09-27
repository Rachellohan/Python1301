"""
Day 6 - Conditionals and Booleans
Announcements
1. Keep up with the reading. We are currently on Chapter 6.
2. Don't wait until the last minute to start your homework!

What we did last time
1. functions with input parameters
2. functions that return a value

What we are going to do today
0. Review functions (briefly) followed by miniquiz #1
1. Conditional expressions
	A. if
	B. else
	C. elif
2. Relational/Boolean operators <   >   <=   >=   !=   ==  
3. the in operator
4. nested if statements
"""
# Topic 0 - brief review
# write a function that returns a string of the person's name doubled followed by a !
def double_name(name):
    return name * 2 + "!"
## rewrite with string multiplicaton

print(double_name("Lasya"))
print(double_name("Chris"))

# topic 0 - Conditionals
name = input("Enter your name: ")
if name == "Fareeda":
    print("Head TA")    
elif name == "Chris":
    print("Regular TA")
elif name == "Josh":
    print("Regular TA")
else:
    print("Student")
    
##rewrite with logical operators
   

# topic 2 operators: <   >    <=    >=   ==   !=
# can be combined with:       not   and   or   
print("Chris" == "Chris " or "Chris" != "Chris")

# the in operator works only for compound data structures

print("A" in "cat")
print("a" in "cat" or "b" in "dog" and "c" in "camel")

# put it all together
name = "dog"
if "a" in name or "b" in name:  # bool expression is ?
    print("yaa")
elif "c" in name:               # bool expression is ?
    print("boo")
else:
    print("cat")
print("dog")


#shortcut operators

num = 5
    #   add one to num
print(num)
    # subtract one from num
print(num)

# Topic 4 - Nested if statements
#- only checks inner if statement, if the outer one was True
is_cat = True
is_dog = False
age = 6

if is_cat:
    if age > 9:
        print("old")
    else:
        print("young")
else:
    if age > 10:
        print("old")
    else:
        print("young")
    

# tracing practice
if 3 > 5:       # these are ?
    print("a")
elif 4/2 < 2:   # these are ?
    print("b")
elif 1 == 1:    # these are ?
    print("c")
else:
    print("d")

    
print(2 == 2.0) # these are ?
print(2 == "2") # these are ?




































    
    





    















