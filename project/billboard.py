# #enter file name and write
# file = open("tsvfile.csv" ,"w")
# file.write("1,2,3,4,5,6")
# file.close()
# #write 1,2,3,4,5,6 to the file
# 
# #close the file
# 
# file = open("tsvfile.csv","a")
# file.write (",7")
# file.close()
# 
# file = open("tsvfile.csv","r")
# readMyCSV = file.read()
# file.close()
# print(type(readMyCSV))
# 
# readMyCSV = readMyCSV.split(",")
# print(readMyCSV[1])
# #list comprehension - its a type of loop
# myList = [int(i) for i in readMyCSV]
# print(myList)


# ages = [-4,12,45,77,23,6,53,57,-23]
# print(ages)
# #ages.sort()
#BOTH DO THE SAME THING = ORDER HIGH TO LOW 
#ages.sort(reverse = True)
#ages.reverse()
# for i in ages:
#     if i < 0:
#         ages.remove(i)
#print(ages)
#totalNonError = 0
#countNonError = 0
#for i in ages:
 #   if i >=0:
   #     totalNonError += i
   #     countNonError += 1
# avredgeNonError = totalNonError/countNonError
# countNonError
# print(totalNonError)

# maxValue= max(ages)
# print(maxValue)
# minValue= min(ages)
# print(minValue)

# QUESTIONS PG 80 TASKS
#Q3

# import random 
# randNumb = []
# for i in range (100) :
#     randNumb = random.randint(1,100)
# print ("random numbers :", randNumb)
# 
# file = open("myTextFile.csv", "a")
# file.append(randNumb)


# MIN AND MAX VALUES

# EXAMPLE 1
# myList = [1, 19,27, 8, 5, 9]   
# myList.sort()
# minValue = myList[0]   # THE FIRST VALUE
# maxValue = myList[-1] # THE LAST VALUE
# print(minValue)  
# print(maxValue)

# EXAMPLE 2
# myList = [1, 15, 27, 8, 5, 9]
# minValue = min(myList)
# maxValue = max(myList)
# print(minValue)
# print(maxValue)

# EXAMPLE 3
# myList = [1, 6, 23, 16, 9]
# minValue = myList[0]
# maxValue = myList[0]
# for item in myList:
#     if item < minValue:
#         minValue = item
#     if item > maxValue:
#         maxValue = item
# print(minValue)
# print(maxValue)

# MEAN

# EXAMPLE 1 (manuel mode)
# myList = [1, 12, 19, 43, 21, 8]
# sumValues = 0
# for item in myList:
#     sumValues += item
# average = sumValues/ len(myList)
# print(average)

# EXAMPLE 2 (manual mode 2)
# myList = [2, 4, 23, 12, 7, 9]
# avredge = sum(myList)/ len(myList)
# print(avredge)

# # EXAMPLE 3 (statistics mode)
# import statistics
# myList = [2, 7, 13, 26, 8]
# avredge = statistics.mean(myList)
# print(avredge)

import pandas as pd
#import statistics
from matplotlib import pyplot as plt

df = pd.read_csv("billboard.csv")
print(df)

# i deleted the unnessisary data from my dataset like the current total number of spotify streams
# as it would not benefit my hypothesis 














