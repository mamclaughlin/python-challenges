# Import a text file filled with a paragraph of your choosing. 
# Approximate word count
# Approximate sentence count
# Approximate letter count (per word)
# Average sentence length (in words)

#Dependencies
# ----------------------
import os

# Variables 
# ----------------------
wordCount = 0
wordCountList = []
letterCount = 0
sentenceLengthList = []

# Main Process 
# ----------------------
txtpath = os.path.join("Resources", 'paragraph_1.txt')
readFile = open(txtpath, "r")

##Original text
original_file = readFile.read()
# print(original_file)

#splits words into items in an array and puts into new variable
wordsFile = original_file.split()

# calculate number of letters in each word and push to array: ex [3,5,6,7,2] ----------
for word in wordsFile:
	wordCountList.append(len(word))

# calculate appx letter count and adds them--------
for letters in wordCountList:
	letterCount += letters

# calculate appx sentence count by separating by period and putting in array ---------
sentenceCount = original_file.split('.')
new_sentenceCount = sentenceCount[:-1]

# calculate sentence length in words -----
#iterates through each sentence and separates by spaces then adds numbers together ------
for numWords in sentenceCount[:-1]:
	sentenceLengthList.append(numWords.count(" "))
	wordCount += numWords.count(" ")

# Printing It All Out... 
print("Word Analysis")
print('===================')
print("Number of words in this passage: " + str(len(wordsFile)))	
print("Approximate sentence count: " + str(len(new_sentenceCount)))	
print("Approximate letter count (per word): " + str(letterCount/len(wordCountList)))	
print("Average sentence length (in words): " + str(wordCount/len(sentenceLengthList)))	


