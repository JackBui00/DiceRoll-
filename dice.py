import random 
import re


#Take in User Input 
#userInput= input("Input a dice\n")
userInput= "1d3+1d4 +1d3 -1d3 +1d3"


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

#Filter Negative Attachment Match
positiveDiceMatch = [s for s in positiveUserInputArray if s.__contains__("d")]
print(positiveDiceMatch)

PositiveNumberMatch= []
print(positiveUserInputArray)

subtractionTotal = []

for i in range(0,len(negativeNumberMatch)):
    splitNegativeNumberMatch = negativeNumberMatch[i].split('-')
    if "d" in str(splitNegativeNumberMatch[0]):
        positiveDiceMatch.append(splitNegativeNumberMatch[0])
        for i in range(1,len(splitNegativeNumberMatch)):
            subtractionTotal.append(splitNegativeNumberMatch[i])

    if splitNegativeNumberMatch[0].isdigit():
        PositiveNumberMatch.append(splitNegativeNumberMatch[0])
        for i in range(1, len(splitNegativeNumberMatch)):
            subtractionTotal.append(splitNegativeNumberMatch[i])

print("positive dice")
print(positiveDiceMatch)

print("negative subtraction array")
print(subtractionTotal)





