'''
Day 3  - The basics+

What we did last time
1. Identifiers
2. Data types
3. Expressions

What we're doing this time
1. Data type review
    a. str, int, float, bool
    b. Converting/Casting to Different Types
2. More operator examples
    a. Order of operations
    b. Resulting data types
    c. // and %
    d. Miniquiz
3. Functions
    a. Declaring
    b. Calling
    c. Miniquiz
    d. Intro to Parameters
    e. Coding miniquiz

'''

# === Refresher: Data type review

aStr = 'Fareeda'
print(type(aStr))

anInt = 7
print(type(anInt))

aFloat = 2.5
print(type(aFloat))

aBool = True
print(type(aBool))

print(int(aFloat))
print(float(anInt))

age = 75
age = str(age)

print("I am " + str(age) + " years old." )
print("I am {} years old.".format(age))


# === Order of operations
# PEMDAS -


anum = 4 * 6 - 2 ** 3 / 2
# 24 - 4.0 = 20.0
print(anum)
'''
# === Integer division
# // - int division

'''
print( 8 // 2)
print(5  // 2)

print( 7.0 // 2.0)
print( -15 // 2)
'''

# % - modulo operator

'''
print( 7 % 2)
print ( - 7 % 2)
print(7.0 % 2.0)


# Miniquiz: Integer division


# === Functions

# Basics

# syntax - def functionName():


def countdown():
    print(10)
    print(9)
    print(8)
    print(7)
    print(6)
    print(5)

countdown()

def divideby2():
    print(18 % 2)

def divideby3():
    print(18 % 3)

def divideby6():
    divideby2()
    divideby3()

divideby6()

# Miniquiz: Functions



# Solving a problem


import this
