"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: availableDate()
Parameters: date(int), isWeekend(bool)
Returns: availability(str)
"""
def availableDate(date,isWeekend):
    if isWeekend or date % 2 == 0:
        return( ("Available on {}!".format(date)))
    else:
        return("Not available :(") 
        

    
##works!!!!



    
    pass

#########################################

"""
Function Name: buyGame()
Parameters: gameTitle(str), budget(float), cost(float), positiveRating(float)
Returns: None(NoneType)
"""
def buyGame (gameTitle , budget , cost , positiveRating):
    if budget <= cost:
        print((gameTitle),"is over ${}!".format(budget))
    elif positiveRating >= .70 :
        print("Sasuke will buy "+gameTitle+"!")
    else: 
        print("Let's find another game.")
   
    pass

#########################################

"""
Function Name: foodTime()
Parameters: restaurant(str), time(int)
Returns: howLong(float or int)
"""
def foodTime( restaurant, time ):
    if restaurant == "Cafe Leblanc" and time-30.5>=0:
        return (time-30.5)
    elif restaurant =="The Roost" and (time-37.5)>=0:
        return(time-37.5)
    elif restaurant =="Lumpy Pumpkin" and (time-43.25)>=0:
        return(time-43.25)
    elif restaurant == "The Milk Bar" and (time-43.0)>=0:
        return(time-43.0)
    else: 
        return(-1)

#Im not sure if lumpy pumkin is working

    pass

#########################################

"""
Function Name: restaurantReservation()
Parameters: total(int), toSave(int), average(int)
Returns: canReserve(bool)
"""
def restaurantReservation(total,totalSave,average):
    return (totalSave + (average * 2)) <= total

##works!!!
#########################################

"""
Function Name: halloweenHeist()
Parameters: num1(int), num2(int), name(str)
Returns: message(str)
"""
def halloweenHeist(num1,num2,name):
    if num1-num2>0:
        return (str(name)+" has the package.")
    if num1-num2==0:
        return (str(name)+" has taken over.")
    else: 
        return (str(name)+" does not have the package.")



    pass

