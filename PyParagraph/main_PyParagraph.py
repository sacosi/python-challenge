#Importing methods
import os
import re

#Initiate the lists to later append values to
words=[]
letters=[]

fileName='paragraph_1.txt'

#Path to the text file
sourcefile1=os.path.join('..','..','..','..','RU-JER-DATA-PT-01-2020','02-Homework',
'03-Python','ExtraContent','Instructions','PyParagraph','raw_data',fileName)

#Open the file
with open(sourcefile1,'r') as textfile:
    textread=textfile.read()

    #Create an array with all the words and calculate the length to find out how many words
    words=textread.split(" ")
    numbWords=len(words)

    #Find out how many letters are in this text file (excluding spaces)
    for word in words:
        for letter in word:
            letters.append(letter)
    numbLetters=len(letters)

    #Calculate number of sentences
    if fileName == 'paragraph_2.txt':
        setences=re.split("\n\n",textread)
    else:
        setences=re.split("(?<=[.!?]) +",textread)
    numbSentences=len(setences)


    #Calculate the "Approximate letter count (per word)"
    avgLetWord=round(numbLetters/numbWords,1)

    #Calculate the "Approximate sentence length (in words)"
    avgWordSetence=round(numbWords/numbSentences,1)

#Create an array with the strings to print
printResults=('Paragraph Analysis',
'------------------',
f'Approximate Word Count: {numbWords}',
f'Approximate Setence Count: {numbSentences}',
f'Average Letter Count: {avgLetWord}',
f'Average Sentence Length: {avgWordSetence}')

#Loop through the array to print the output.
for x in printResults:
    print(x)