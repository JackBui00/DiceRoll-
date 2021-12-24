import random
import re


#Take in User Input 
userInput= input("Input a dice\n")

#Debug User Input
#userInput= "1d3+1d4 +1d3+ 33 -1d3 +1d3-  5d5 -5 - 10 + 25"


#Remove Spaceing in User Input 
noSpaceInput = userInput.replace(' ','')
print(noSpaceInput)

#Create Array with Positive User Input Only
positiveUserInputArray = re.split('[+]', noSpaceInput)
print(positiveUserInputArray)

#Creation of Negative User Input Array 
Negative = '-'
negativeNumberMatch = []
splitNegativeNumberMatch= []

negativeNumberMatch = list(filter(lambda x: Negative in x, positiveUserInputArray))
print("negative")
print(negativeNumberMatch)

positiveUserInputArray = [x for x in positiveUserInputArray if "-" not in x]

#Filter Negative Attachment Match, random characters
positiveDiceMatch = [s for s in positiveUserInputArray if s.__contains__("d")]
print("fiter negative attachment match")
print(positiveDiceMatch)

#Positive Integer Values from filter
positiveNumberMatch= []
print(positiveUserInputArray)

#Array for Dice Subtraction
subtractionTotal = []

#Split Apart Array Item 0 to check for dice stuck together
for i in range(0,len(negativeNumberMatch)):
    splitNegativeNumberMatch = negativeNumberMatch[i].split('-')
    if "d" in str(splitNegativeNumberMatch[0]):
        positiveDiceMatch.append(splitNegativeNumberMatch[0])
        for i in range(1,len(splitNegativeNumberMatch)):
            subtractionTotal.append(splitNegativeNumberMatch[i])

    if splitNegativeNumberMatch[0].isdigit():
        positiveNumberMatch.append(splitNegativeNumberMatch[0])
        for i in range(1, len(splitNegativeNumberMatch)):
            subtractionTotal.append(splitNegativeNumberMatch[i])

print("positive dice")
print(positiveDiceMatch)

print("negative subtraction array")
print(subtractionTotal)

#integers to subtract 
finalFilterNegativeValue = []

negativeDiceMatch= [s for s in subtractionTotal if s.__contains__("d")]

#Filter Integer Values in Array to Subtract from Final Dice Total 
for items in subtractionTotal:
    for subitem in items.split():
        if(subitem.isdigit()):
            finalFilterNegativeValue.append(subitem)

#Filter Integer Values in Array to Add To Final Dice Total 
for items in positiveUserInputArray:
    for subitem in items.split():
        if(subitem.isdigit()):
            positiveNumberMatch.append(subitem)
print("split negativenumbermatch")
print(splitNegativeNumberMatch)
print(positiveDiceMatch)
print(finalFilterNegativeValue)

#Convert Each Positive String Integer into a Integer in the Array 
for i in range (0, len(positiveNumberMatch)):
    positiveNumberMatch[i] = int(positiveNumberMatch[i])


#Convert Each Negative String Integer into a Integer in the Array 
for i in range (0, len(finalFilterNegativeValue)):
    finalFilterNegativeValue[i] = int(finalFilterNegativeValue[i])

#Create Positive and Negative Dice
positiveDiceValue = []
negativeDiceValue = []

#Compile Together Values of Positive Dice Rolls
print("Positive Dice Rolls")
for x in range(len(positiveDiceMatch)):
    tempPositiveDice = re.split('d', positiveDiceMatch[x])
    print(tempPositiveDice)
    positiveDiceAmmount = int(tempPositiveDice[0])
    positiveDiceMaxValue = int(tempPositiveDice[1])
    positiveMinimumDiceValue = 1; 
    i = 0; 
    while i < positiveDiceAmmount:
        positiveDiceRollValue = random.randint(positiveMinimumDiceValue, positiveDiceMaxValue)
        i += 1
        positiveDiceValue.append(positiveDiceRollValue)

#Compile Together Values of Negative Dice Rolls
print("Negative Dice Rolls")
for x in range(len(negativeDiceMatch)):
    tempNegativeDice = re.split('d', negativeDiceMatch[x])
    print(tempNegativeDice)
    negativeDiceAmmount = int(tempNegativeDice[0])
    negativeDiceMaxValue = int(tempNegativeDice[1])
    negativeMinimumDiceValue = 1; 
    i = 0; 
    while i < negativeDiceAmmount:
        negativeDiceRollValue = random.randint(negativeMinimumDiceValue, negativeDiceMaxValue)
        i += 1
        negativeDiceValue.append(negativeDiceRollValue)

#Take Sum of Arrays of Integers
additionSum = sum(positiveNumberMatch)
negativeSum = sum(finalFilterNegativeValue)

#Take Sum of Array of Dice Roll Integers
positiveDiceValueSum = sum(positiveDiceValue)
negativeDiceValueSum = sum(negativeDiceValue)

#calculate the total value of all rolls and integers
totalValueOfAll = additionSum - negativeSum + positiveDiceValueSum - negativeDiceValueSum

print(additionSum)
print(negativeSum)
print(totalValueOfAll)
    
        



