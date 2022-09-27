"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
"""
Function Name: decodeString()
Parameters: encodedStr(str)
Returns: decodedList(list)
"""
def decodeString(coded):
    nStr=''
    for u in coded[::-1]:
        if u not in "@":
            nStr += u
    nStr = (nStr.upper().lower())
    list(nStr)
    return nStr.split('#')
   




    pass
#########################################
"""
Function Name: goodBrunch()
Parameters: ashList(list), nickList (list)
Returns: brunchDecision(list)
"""
def goodBrunch(ashList,nickList):
    agree=[]
    for word in ashList:
        if word in nickList:
            agree.append(word)
            agree.sort()
    if agree==[]:
        return ("Brunch at home it is!")
    if agree != []:
        if len(agree)==1:
            return agree[0]
        else:
            return agree
    pass
#########################################
"""
Function Name: room_dist()
Parameters: dormMap (list), name1 (str), name2 (str)
Returns: distance (int)
"""
def room_dist(dormMap,name1,name2):
    place1 = 0
    place2 = 0
            
    for i in range(len(dormMap)):
        if name1 in dormMap[i]:
            place1= i
    for i in range(len(dormMap)):
        if name2 in dormMap[i]:
            place2 = i
    dist= abs(place1-place2)
    return dist





    pass
#########################################
"""
Function Name: freshProduce()
Parameters: veggies (list), prices (list)
Returns: veggieList (list)
"""
def freshProduce(veggies, prices):
    buy=[]
    totalPrices=0
    for x in range(len(veggies)):
        if prices[x]<=4.0:
            buy.append(veggies[x])
            totalPrices+=prices[x]
    if len(buy)>1:
        buy.append(totalPrices)
    return buy

    pass
#########################################
"""
Function Name: find_roommate()
Parameters: my_interests(list), candidates (list), candidate_interests(list)
Returns: match (list)
"""
def find_roommate(my_interests,candidates,candidate_interests):
    candid=[]
    for w in range(len(candidate_interests)):
        count = 0
        for word in candidate_interests[w]:
            if word in my_interests:
                count+= 1
        if count>=2:
            candid.append(candidates[w])
          
    return(candid)

        
       
        
            

    pass
    
