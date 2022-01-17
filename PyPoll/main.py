#PyPoll
import os
import csv

csvPath = os.path.join('Resources','election_data.csv')

#count the number of rows in the csv and set count of votes
with open(csvPath, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    next(reader)

    count = len(list(reader))

#create list of unique candidates
with open(csvPath, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    next(reader)

    candidateList = []
    for row in reader:
        if row[2] not in candidateList:
            candidateList.append(row[2])

#make a dictionary for each candidate and number of votes they recieved
candidateDict = {}
for candidate in candidateList:
    candidateDict[candidate] = None
    
for candidate in candidateList:
    countboy = 0
    with open(csvPath, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        next(reader)
        for row in reader:
            if row[2] == candidate:
                countboy = countboy + 1
            candidateDict[candidate] = countboy

# Find the candidate with the most votes and declare as winner
mostVotes = 0
for candidate in candidateDict:
    if candidateDict[candidate]>mostVotes:
        mostVotes = candidateDict[candidate]
        winner = candidate

# Calculate the percentage of votes each candidate received and create analysis report for each
for candidate in candidateDict:
    perc = int(round((candidateDict[candidate]/count)*100,0))
    candidateDict[candidate] = f'{candidate}: {perc}% ({candidateDict[candidate]})'

#print the results to the terminal
print('Election Results')
print('--------------------------')
print(f'Total Votes: {count}')
print('-------------------------')
for candidate in candidateDict:
    print(candidateDict[candidate])
print('--------------------------')
print(f'Winner: {winner}')
print('--------------------------')

#write the results to a text file
with open('Analysis/PyPoll_analysis.txt','w') as txtFile:
    txtFile.write('Election Results\n')
    txtFile.write('-----------------------\n')
    txtFile.write(f'Total Votes: {count}\n')
    txtFile.write('-----------------------\n')
    for candidate in candidateDict:
        txtFile.write(f'{candidateDict[candidate]}\n')
    txtFile.write('-----------------------\n')
    txtFile.write(f'Winner: {winner}\n')
    txtFile.write('-----------------------\n')