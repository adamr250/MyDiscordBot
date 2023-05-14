
import random

def diceRoll(roll):
    helpMessage = """>roll XdY+Z 
    X - number of rolls;
    Y - dice size, possible Y values: 4, 6, 8, 10, 12, 20;
    Z - number added to all rolls (optional);
    Examples: 1d4+2, 3d20"""
    diceSizes = [4, 6, 8, 10, 12, 20]

    if roll == "help":
        return helpMessage
    

    found_d = roll.find("d")
    if(found_d == -1):
        return "Wrong input: wrong input"
    
    numOfRolls = roll[:found_d]
    roll = roll[found_d+1:]

    foundPlus = roll.find("+")
    addValue = "0"
    if(foundPlus == -1):
        rollRange = roll
        #print("roll range: ", rollRange)
    else:
        rollRange = roll[:foundPlus]
        addValue = roll[foundPlus+1:]
        #print("roll range plus: ", rollRange)

    inputCheck = numOfRolls.isnumeric() + rollRange.isnumeric() + addValue.isnumeric()
    #print(numOfRolls.isnumeric(), " + ", rollRange.isnumeric(), " + ", addValue.isnumeric())

    if(inputCheck != 3):
        return "Wrong input: not a number"

    numOfRolls = int(numOfRolls)
    rollRange = int(rollRange)
    addValue = int(addValue)

    if not rollRange in diceSizes:
        return "Wrong input: dice size"
    
    result = "["
    for i in range(numOfRolls):
        result = result + str(random.randint(1, rollRange) + addValue)
        if(i != numOfRolls-1):
            result = result + ", "
    result = result + "]"

    return result

#print(diceRoll("10d4+2"))
#print(diceRoll("10d4+2"))
#print(diceRoll("4d4+1"))