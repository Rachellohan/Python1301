'''
make a str using a loop,
contaiing the even digits from 2 - 10
'''
##newStr = ''
##for num in range(2,12,2):
##    newStr = newStr + str(num)
##print(newStr)


'''
str of all letters of "jackets"
separated by spaces w/ for
'''
anewStr = ''
count = 0
for ch in "jackets":
    if count < len("jackets")-1:
        anewStr += ch + '-'
    else:
        anewStr += ch
    count += 1
print(anewStr)
'''
str of all letters of "jackets"
separated by spaces w/ while
'''
anewStr = ''
count = 0
while count < len("jackets"):
    if count < len("jackets")-1:
        anewStr +=  "jackets"[count]+ '*'
    else:
        anewStr += "jackets"[count]
    count += 1
print(anewStr)
'''
keeping a total in a loop
what is the total when a customer purchases 5 itmes
'''
##total = 0
##for num in range(5):
##    price = float(input("Enter the item price: "))
##    total += price
##print("You owe ${:.2f}".format(total))




