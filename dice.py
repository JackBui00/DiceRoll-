import random 
import re


#Take in User Input 
#userInput= input("Input a dice\n")
userInput= "1d3+1d4 +1d3+ 33 -1d3 +1d3-  5d5 -5 - 10 + 25"


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

