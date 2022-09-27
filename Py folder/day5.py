'''
Day 5 Outline

What we did last time
1. Parameters
2. Return
3. Functions
4. Print vs Return


What we're doing this time
1. Boolean Expressions and Conditionals
    a. Why do we need them?
    b. Relational Operators
    c. if, elif, else
    d. Using Conditionals In Functions
    e. Logical Operators
'''

# === Boolean expressions and conditionals
# Why?

nMasks = 0
if nMasks < 10 and nMasks != 0:
    print("It's time to restock!")
elif nMasks > 100:
    print("Stop ordering masks!")
else: nMasks == 0
print("Emergency! You are out!")
"""
# Relational operators
# Relational operations result in booleans
"""
"""
< less than
> greater than
<= less than or equal to
>= greater than or equal to
== equals
!= not equals
""

"""
print('78 < 3: ',78 < 3)
print('3 <= 3: ',3 <= 3)
print('"Hello" == "hello": ',"Hello" == "hello")
print('"Hello" == " Hello": ',"Hello" == " Hello")
print('"4" == 4: ',"4" == 4)
#print('"4" <= 4: ',"4" <= 4)
print('5.0 == 5: ',5.0 == 5)

a = 10
b = 20
c = a > b
print(c)
"""
# === Building conditional blocks, msking decisions
# if and else
"""
nMasks = 11
if nMasks < 10:
    print("It's time to restock!")
else:
    print("You are cool for now.")
"""
"""
# === How are conditional blocks executed?
nMasks = 9
if nMasks < 10:
    print("It's time to restock!")
elif nMasks < 20:
    print("Stop ordering masks!")
else:
    print("Something else here")
"""

# === Conditionals in functions
"""
def isDog(pet):
    ''' if the parameter value is Husky or Poodle,then "it's a dog"
    will be displayed, otherwise "sorry, not a dog" will be displayed.
    '''
    if pet == "Husky" or pet == "Poodle":
        print("it's a dog")
    else:
        print("sorry, not a dog")

isDog("Poodle")
"""
# === Logical operators (not, and, or)
"""
print(2 > 3 and 3 <4) # 
print(2 > 3 or 3 <4) # 
print(2 > 3 or not 3 <4) # 

