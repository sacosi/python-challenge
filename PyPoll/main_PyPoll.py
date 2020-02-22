#Import Methods
import csv
import os

#Initiate the lists to later append values to
voters=0
candidatesList=[]
countVotes=[]

#Path to the csv file
sourcePath = os.path.join('..','..','..','..','RU-JER-DATA-PT-01-2020','02-Homework','03-Python','Instructions','PyPoll','Resources','election_data.csv')

#Open the file
with open(sourcePath, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile)
    
    #Skip the headers
    csvHeaders=next(csvreader)

    #Loop through the rows
    for row in csvreader:
        #Checking if the candidate is already in the list of candidates
        #If the candidate is already in the list just add one more vote to the index of that candidate
        if row[2] in candidatesList:
            countVotes[candidatesList.index(row[2])] += 1       
        else: #If the candidate is not in the list add to it and add 1 to the same index as the candidate
            candidatesList.append(row[2])
            countVotes.append(1)

#Total Votes & percent of votes
totalVotes=sum(countVotes)
percentVotes=[round((x/totalVotes*100),3) for x in countVotes]

#List of strings to print
printResults=[
    'Election Results',
    '----------------',
    f'Total Votes: {totalVotes}','----------------'
]
#Add to the print results list the different candidates and the respective number of votes
for index,candidate in enumerate(candidatesList):
    printResults.append(f'{candidate}: {percentVotes[index]}% ({countVotes[index]})')

#Add the final strings values to the list of printresults
printResults.extend(
    ['----------------',
    f'Winner: {candidatesList[countVotes.index(max(countVotes))]}',
    '----------------'])

#Print the results and write them in a textfile as well
with open('Election Results.txt','w') as textfile:
    for row in printResults:
        print(row)
        textfile.write(f'{row}\n')
