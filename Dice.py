
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

#TODO: wypisywanie sumy rzutów, modyfikowanie (+,-,*,/) pojedyńczych rzutów lub sumy

def diceRoll(diceRoll):
    helpMessage = """>roll XdY
    X - number of rolls
    Y - dice size, possible Y values: 4, 6, 8, 10, 12, 20
    +, -, *, / (optional) - modify value
    Examples: 1d4+2, 3d20"""
    diceSizes = [4, 6, 8, 10, 12, 20]
    mathSymbols = ["+", "-", "*", "/"]

    if diceRoll == "help":
        return helpMessage
    

    found_d = diceRoll.find("d")
    if(found_d == -1):
        return "Wrong input: wrong input"
    
    numOfRolls = diceRoll[:found_d]
    rollRange = diceRoll[found_d+1:]

    #Szukanie operacji algebraicznych (+, -, *, /)
    modifyTotal = False
    modifierValue = "0"
    modifier = "+"
    for m in mathSymbols:
        foundMath = rollRange.find(m)
        if(foundMath != -1):
            modifier = m
            rollRange = rollRange[:foundMath]
            modifierValue = rollRange[foundMath+1:]
            foundHash = modifierValue.find("#")
            if(foundHash != -1):
                modifierValue = modifierValue[:foundHash]
                afterHashOption = modifierValue[foundHash:]
                if(afterHashOption == "#t"):
                    modifyTotal = True
                elif(afterHashOption == "#e"):
                    modifyTotal = False
                else:
                    return "Wrong input: wrong option after #"
            
            break

    inputCheck = numOfRolls.isnumeric() + rollRange.isnumeric() + modifierValue.isnumeric()

    if(inputCheck != 3):
        return "Wrong input: not a number"

    numOfRolls = int(numOfRolls)
    rollRange = int(rollRange)
    modifierValue = int(modifierValue)

    if not rollRange in diceSizes:
        return "Wrong input: dice size"
    

    #Generowanie rzutow i zapisywanie w string
    totalSum = 0
    result = "rolls: ["
    for i in range(numOfRolls):
        #result = result + str(random.randint(1, rollRange) + modifierValue)
        if(foundMath == -1):
            roll = random.randint(1, rollRange)
        elif(modifyTotal == False):
            roll = modifyValue[modifier](random.randint(1, rollRange),  modifierValue)
            result = result + str(roll)
            totalSum = totalSum + roll
        else:
            roll = random.randint(1, rollRange)
            result = result + str(roll)
            totalSum = totalSum + roll

        if(i != numOfRolls-1):
            result = result + ", "

    if(modifyTotal == True):
        result = result + "]\tsum: [" + str(sum) + "]"
    else:
        result = result + "]\tsum: [" + str(sum) + "]"

    return result

if __name__ == "__main__":
    print(diceRoll("2d20"))