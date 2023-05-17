
import random

def addValues(a, b):
    return a+b

def subctractValues(a, b):
    if(a <= b):
        return 0
    return a-b

def multiplyValues(a, b):
    return a*b

def divideValues(a, b):
    return a//b

modifyValue = {"+":addValues, "-":subctractValues, "*":multiplyValues, "/":divideValues}

def diceRoll(roll):
    helpMessage = """>roll XdY
    X - number of rolls
    Y - dice size, possible Y values: 4, 6, 8, 10, 12, 20
    +, -, *, / (optional) - modify value
    Examples: 1d4+2, 3d20"""
    diceSizes = [4, 6, 8, 10, 12, 20]
    mathSymbols = ["+", "-", "*", "/"]

    if roll == "help":
        return helpMessage
    

    found_d = roll.find("d")
    if(found_d == -1):
        return "Wrong input: wrong input"
    
    numOfRolls = roll[:found_d]
    roll = roll[found_d+1:]

    #Szukanie operacji algebraicznych (+, -, *, /)
    modifierValue = "0"
    modifier = "+"
    for m in mathSymbols:
        foundMath = roll.find(m)
        if(foundMath != -1):
            modifier = m
            rollRange = roll[:foundMath]
            modifierValue = roll[foundMath+1:]
            break
        else:
            rollRange = roll


    inputCheck = numOfRolls.isnumeric() + rollRange.isnumeric() + modifierValue.isnumeric()

    if(inputCheck != 3):
        return "Wrong input: not a number"

    numOfRolls = int(numOfRolls)
    rollRange = int(rollRange)
    modifierValue = int(modifierValue)

    if not rollRange in diceSizes:
        return "Wrong input: dice size"
    

    #Generowanie rzutow i zapisywanie w string
    result = "["
    for i in range(numOfRolls):
        #result = result + str(random.randint(1, rollRange) + modifierValue)
        result = result + str(modifyValue[modifier](random.randint(1, rollRange),  modifierValue))
        if(i != numOfRolls-1):
            result = result + ", "
    result = result + "]"

    return result

if __name__ == "__main__":
    print(diceRoll("2d20"))