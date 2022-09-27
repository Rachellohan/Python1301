"""
Georgia Institute of Technology - CS1301
HW01 - Functions & Expressions
"""


#########################################

"""
Function Name: tasteOfTech()
Parameters: N/A
Returns: None
"""
def tasteOfTech():
    
    name = input ("what is your name? ")
    tinD = float(input("How much did you spend at Tin Drum?") )
    walHouse = float(input("How much did you spend at Waffle House?") )
    buffWW = float(input("How much did you spend at Buffalo Wild Wings?") )
    
    moneySpent=tinD+walHouse+buffWW
    
    
    doge = (14.57)
    totalDoge = moneySpent * doge
    roundTotalDoge = round(totalDoge,2)
    roundMoneySpent = round(moneySpent,2)
    print ("Congratulations "+str(name)+"! You spent $"+str(roundMoneySpent)+" in total and earned "+str(roundTotalDoge)+" DOGE.")
        
   
    
        
    pass

#########################################

"""
Function Name: shoppingMoney()
Parameters: N/A
Returns: None
"""
def shoppingMoney():
    totalMonth = int(input("How much money have you made this month?") )#plans to take total amount earned subtract 1020, multiple by .6 for total saving and the remainder will be thespending money
    expenses = int(1020)
    afterExpenses = totalMonth - expenses
    percent = .6
    totalSaving = afterExpenses * percent
    spendingMon = afterExpenses- totalSaving
    roundTotalSaving = round(totalSaving,1)
    roundSpendingMon = round(spendingMon,1)
    print ("You can save $"+str(roundTotalSaving)+" and spend the remaining $"+str(roundSpendingMon)+" on anything this month.")
    
    pass

    
#########################################

"""
Function Name: houseParty()
Parameters: N/A
Returns: None
"""
def houseParty():
    nugs = int(input ("How many chicken nuggets will each guest eat?") )
    rings = int(input ("How many onion rings will each guest eat?") )#getting estimated consumption of each to multible by number of guests
    donut = int(input("How many donuts will each guest eat?") )
    cook = int(input("How many cookies will each guest eat?") )
    totalGuest = int(input ("How many guests are you expecting at the party?") )
    totalNugs=nugs*totalGuest
    totalRings=rings*totalGuest
    totalDonut=donut*totalGuest
    totalCook=cook*totalGuest
    
    print ('You need to buy',totalNugs,'chicken nuggets,',totalRings,'onion rings,',totalDonut,'donuts and',totalCook,"cookies for" ,totalGuest, "guests.")
    
    
    pass

#########################################

"""
Function Name: spareTime()
Parameters: N/A
Returns: None
"""
def spareTime():
    totalTime = 112
    credit = int(input ("how many credits are you taking?"))#ask for total credits,multiply by 3 
    unfree = credit * 4
    free = totalTime - unfree
    perDay = free / 7
    minutes = 60
    totalMin = perDay * minutes
    realMin = totalMin % 60
    roundRealMin = round(realMin,1)
    hours = int(totalMin / 60)
    print ('You have',hours,"hours and",roundRealMin,"minutes per day to spare for other activities.")
    
    pass

#########################################

"""
Function Name: ratsNight()
Parameters: N/A
Returns: None
"""
def ratsNight():
    vidGames = int(input("How many slots would you like to book for video games?") )
    triv = int(input("How many slots would you like to book for trivia time?") )
    art = int(input("How many slots would you like to book for arts/crafts?") )
    slotVG = vidGames * 30
    slotTrv = triv * 10
    slotArt = art * 45
    totalTime = slotVG + slotTrv + slotArt
    hours = int(totalTime//60)
    minutes = totalTime % 60
    print ("You will spend",hours,"hours and",minutes,"minutes at Rats Night.")
    pass

