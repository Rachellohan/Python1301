"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
"""
Function Name: product()
Parameters: nums(str)
Returns: product(int)
"""
def product(nums):
    count = 1
    for i in nums:
        count *= int(i)
        int(count)
        if i != 0:
            count *= 1
        else:
            return 0
    return count
        




pass
#########################################
"""
Function Name: recipeCount()
Parameters: recipe(str)
Returns: totalTeaspoons(int)
"""
def recipeCount(recipe):
    count = 0
    for i in (recipe):
        if i in "1234567890":
            count += int(i)
    return count 
          







pass
#########################################
"""
Function Name: instagraminator()
Parameters: usernames(str)
Returns: decodedUsernames(str)
"""
def instagraminator(names):
    newName=""
    for char in names[::-1]:
        if char not in "!@#$%^&*()~+_?":
            newName = char + str(newName)
    return newName





    pass
#########################################
"""
Function Name: studentLoans()
Parameters: loanAmount(int)  WORKS
Returns: forgivenessCount(int)
"""
def studentLoans(debt):
    times = 0
    while (debt > 0):
        debt -= 10000
        times += 1
    return times

    pass
#########################################
"""
Function Name: playoffs()
Parameters: team1name (str), team2name (str), scoreCount (str) 
Returns: winningTeam (str) 
"""
def playoffs(team1name,team2name, scoreCount):
    point1 = 0
    point2 = 0
    for num in scoreCount:
        if num == "1":
            point1 += 1
        if num == "2":
            point2 += 1
    #return (point1,point2)
    if point1 > point2:
        return("{} has won the game!".format(team1name))
        #return (point1,point2)
    elif point2 > point1:        
        return("{} has won the game!".format(team2name))
        #return (point1,point2)
    elif point2 == point1:
        return("It was a tie :(")
        #return (point1,point2)

    pass
    
recipeCount("4 teas , 18 makes")