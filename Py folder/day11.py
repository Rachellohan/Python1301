# day 11 - finishing up strings, starting lists

"""
Announcements
1. exam 1 Monday during regular class time
2. review session Friday 4:30 - 6:00 in Clough (Culc) 144
3. be sure you are keeping up withthe reading including the class handouts


What we did last time (day 10 - notes are uploaded to Canvas)
1. Remember strings are immutable - you have to build a new string to
     change them!  
2. More string indexing and slicing practice
3. String methods - name.lower(), name.upper(), name.replace(ch1,ch2),
.isupper()   .find("c")   name[0].isdigit()  .isalpha()


What we are doing today
1. More string methods: find, format, split and strip
2. Iterating through strings
3. One final reminder that strings are immutable
4. escape sequences: \n, \t, \\, \", \' etc. - not on exam 
5. Introducing the list data type - not on exam

"""
# topic more str methods
##greet = "Hello world. It's 2022!"
##print(greet)
##print("-"*10)
##print("greet.title()->",greet.title())
##print("greet.capitalize()->",greet.capitalize())
##print("greet.lower().title()->",greet.lower().title())
##
##x = "my name isn't Fred"
##print(x.replace("Fred", "Alec").replace("n't", ""))
##print(x.replace("Fred", "Alec").replace("n't", "").title())
##print(x.replace("Fred", "Alec").replace("n't", "").capitalize())
##print("cat1".isalpha())
##print("cat1".isdigit())
##print("cat1".isupper())
##print("cat---1".lower())
##print("cat---1".upper())
##print("cat---1".replace("-","*"))
##print("cat---1".find("C"))

##name = "              Josh Tabb             "
##print(name.find("o"))  # find returns the index of ...?
##print(name.index("o"))  # index returns the index of ...?

##oldstr = "cat{}dog"
##oldstr = oldstr.format(3) # .format returns a new str
##print(newstr)

##name = "josh"
##print(name.find("x") + name.upper().find("JO"))

# change string example
# write a function remove_letter that removes
# all of the second param from the first param returning
# the result
##def remove_letter(astr,ch):
##    pass
##
##print(remove_letter("cat   dog   ","x"))
##print(remove_letter("cat   dog   ","c"))

##letter = """
##Dear {0} {2}.
## {0}, I have an interesting money-making proposition for you!
## If you deposit $10 million into my bank account, I can
## double your money ...
##"""
##
##print(letter.format("Paris", "Whitney", "Hilton"))
##print(letter.format("Bill", "Henry", "Gates"))
##
##
##n1 = "Paris"
##n2 = "Whitney"
##n3 = "Hilton"
##print("Pi {0} to three decimal places is {0:.3f}".format(3.1415926))
##
##print("The integer value {0}\
##\n\t'0:X' converts to hex value {0:X}\
##\n\t'0:b' converts to binary value {0:b}\
##\n\t'0:e' converts to exponential value {0:e}\
##\n\t'0:%' converts to percentage value {0:%}\
##\n\t'0:f' converts to float value {0:f}".format(123456))


##########
### topic escape sequences - not on exam
# 
# \n new line character
# \t tab
# \\   an actual \
# \"   \'   actual quotes

##print("cat\ndog\tbird\n\ndone")
##
##print(len("num1\\num2"))


# strip and split are not on exam 1
##print(name.strip()) # removes the white space at the beginning and end of a str

##phrase = "go jackets beat Ole Miss"
##print(phrase.split())

##alist = phrase.split()
##print(alist)
##print(type(alist))
##for word in alist:
##    print(word)
    
##newlist = [ 1, 5, True, 1.0, 0.0, [1, 2], "cat"]
##print(newlist)

# write a function count_long that returns how many
# words in a sentence are longer than 3 letters long
##def count_long(sentence):
##    pass
##
##print(count_long("I am happy"))  # 1
##print(count_long("I am")) # 0
