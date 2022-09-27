def availableDate(date,isWeekend):
    int(date)
    bool(isWeekend) == True 
    if isWeekend == True :# found the run time but may have a catcatenation errror
        print( ("Available on"),date,("!"))
    elif date % 2 == 0:
        print(( "Available on"),date,("!"))
    else: print("Not available:(") 
    if isWeekend == "False":
        print("Not available:(")  
