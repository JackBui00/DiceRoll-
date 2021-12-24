import random 
import re


#Take in User Input 
userInput= input("Input a dice\n")

#Remove Spaceing in User Input 
noSpaceInput = userInput.replace(' ','')
print(noSpaceInput)

#Create Array with Positive User Input Only
positiveUserInputArray = re.split('[+]', noSpaceInput)
print(positiveUserInputArray)





