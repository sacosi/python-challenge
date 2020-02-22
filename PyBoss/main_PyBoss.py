#Import methods
import os
import csv

#Dictionary to map state name to state abreviation
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Initiate the lists to later append values to
EmpID=[]
firstName=[]
lastName=[]
dob=[]
ssn=[]
state=[]

#Path to the text file
sourcePath = os.path.join('..','..','..','..','RU-JER-DATA-PT-01-2020','02-Homework','03-Python','ExtraContent','Instructions','PyBoss','employee_data.csv')

#Open the file
with open(sourcePath, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile)

    #Skip the headers
    csvHeaders=next(csvreader)
    
    #Loop through the rows
    for row in csvreader:
        EmpID.append(row[0])    #EmpID doesn't change so just appending it to the list created above

        #Split the name in first and last name and adding them to the respective lists
        nameSplit=row[1].split(" ")
        fname=nameSplit[0]
        lname=nameSplit[1]
        firstName.append(fname)
        lastName.append(lname)

        #Split the DOB and format it as requested
        dobSplit=row[2].split("-")
        year=dobSplit[0]
        month=dobSplit[1]
        day=dobSplit[2]
        dob.append(f'{month}/{day}/{year}')

        #Split the SSN, store the last 4 and format as requested
        ssnSplit=row[3].split("-")
        last4=ssnSplit[2]
        ssn.append(f'***-**-{last4}')

        #Use the state dictionary to map the state name to the state 2 letter abreviation
        state.append(us_state_abbrev[row[4]])

#Agregate all the lists
agregator=zip(EmpID,firstName,lastName,dob,ssn,state)

#Open the csv to write the new way to stor employee data
with open('new_employee_data.csv','w',newline="") as csvw:
    csvwrite=csv.writer(csvw)

    #Headers
    csvwrite.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    #Rows
    csvwrite.writerows(agregator)