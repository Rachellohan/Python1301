# Day 2 CS1301-Kearse
# after class today, get homework, attend recitation, read the textbook,
# update code notebook, and review/plan for next class

''' Day 1 we went over the syllabus
# TO DO: students will download Python 3.10 if they can, read the textbook,
# register for recitation, and review/plan for next class
'''


# variables have associated data types based on
# the value currently being stored

# some examples of data types:
# str
# int
# float
# bool


# coding is about naming
# rules for naming identifiers
# ?
# ?
# ?
# ?


# the assignment operator (=) used to create variables uisng expressions
#

age=12

print(age            ) # spaces are allowed around punct
print(type(age))
age = "twenty"

print(age)
print(type(age))

# both type and print are functions
# be aware of when spacing matter and when it doesn't

prof = 12
print(prof)
print(prof)

def check_nr(number):
    ''' return "even" or "odd" based on the value of the parameter'''
    remainder_by2 = number % 2
    if remainder_by2 == 0:
        return 'even'
    else:
        return 'odd'
def get_result(number):
    ''' square the parameter if the called function returns "even"
    or cube the parameter if the called function returns "odd" '''
    if check_nr(number) == 'even':
        print(number **2)
    if check_nr(number) == 'odd':
        print(number *3)
#function calls
get_result(8)
get_result(3)














