#Import methods
import csv
import os

#Initiate the lists to later append values to
monthsList=[]
profitsTotal=0
previousProfit=0
profitChange=[]
profitDateChange=[]

#Path to the csv file
sourcePath = os.path.join('..','..','..','..','RU-JER-DATA-PT-01-2020','02-Homework','03-Python','Instructions','PyBank','Resources','budget_data.csv')

#Open the file
with open(sourcePath, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile)
    
    #Skip the headers
    csvHeaders=next(csvreader)
    
    #Loop through the rows
    for row in csvreader:
        #Append the months to the list
        monthsList.append(row[1])
        #add up the profit and losses ammount
        profitsTotal += int(row[1])
        #if it's the first record just append the value to the list
        if previousProfit==0:
            previousProfit=int(row[1])
        else: #If it's not the first value, calculate the difference between the current value and the previous one
            profitChange.append(int(row[1])- previousProfit)
            profitDateChange.append(row[0])
            previousProfit=int(row[1])

#Average change
averagechange=(sum(profitChange)/len(profitChange))

#Month of greatest increase and the value
greatIncProfits=max(profitChange)
greatIncDateIndex=profitChange.index(max(profitChange))
incDate=profitDateChange[greatIncDateIndex]

#Month of greatest decrease and the value
greatDecProfits=min(profitChange)
greatDecDateIndex=profitChange.index(min(profitChange))
decDate=profitDateChange[greatDecDateIndex]

#Create a list with the values to be printed
printresults=['Financial Analysis','------------------',
    f'Total Months: {len(monthsList)}',f'Total: ${(profitsTotal)}',
    f'Average Change: ${(round(averagechange,2))}',
    f'Greatest Increase in Profits: {incDate} (${greatIncProfits})',
    f'Greatest Decrease in Profits: {decDate} (${greatDecProfits})']

#Open the textfile to write and both print it to the terminal and write it in the txt file
with open('Financial_Analysis.txt','w') as textfile:
    for row in printresults:
        print(row)
        textfile.write(f'{row}\n')
        