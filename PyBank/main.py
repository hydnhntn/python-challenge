# PyBank 
import os
import csv

csvPath = os.path.join('Resources','budget_data.csv')

#count the number of rows in the csv and set as Months
with open(csvPath, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    next(reader)

    months = len(list(reader))

#calculate the net total amount of "Profit/Losses" over the entire period
with open(csvPath, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    next(reader)

    total = 0
    for row in reader:
        total = total+int(row[1])
    print(total)


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
with open(csvPath, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    next(reader)
    changeDict = {}
    change = 0
    prevRow = 0

    for row in reader:
        # calculate change from previous row value
        change = int(row[1])-prevRow
        # add row to dictionary with column 1 as key and column 2 as value
        changeDict[row[0]] = change
        # set previous row for next interation of this for loop
        prevRow = int(row[1])   

    # delete the first item in the dictionary since it was just used to calculate the next items change
    del changeDict[str(next(iter(changeDict)))]

    #Calculate the average of all changes (dictionary values)
    avgChange = round(sum(changeDict.values())/len(changeDict),2)

    #calculate the max of all changes
    maxChange = max(changeDict.values())

    #Calculate the min of all changes
    minChange = min(changeDict.values())

    #get the date (dictionary keys) for the min and max values from the dictionary
    maxChangeDate = list(changeDict.keys())[list(changeDict.values()).index(maxChange)]
    minChangeDate = list(changeDict.keys())[list(changeDict.values()).index(minChange)]

#print analysis to the terminal
print("Financial Analysis")
print("------------------------------")
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in profits: {maxChangeDate} (${maxChange})")
print(f"The greatest decrease in profits: {minChangeDate} (${minChange})")

#export analysis to a text file
with open('Analysis/PyBank_analysis.txt', 'w') as txtFile:
    txtFile.write(
        f"Financial Analysis\n------------------------------\nTotal Months: {months}\nTotal: ${total}\nAverage Change: ${avgChange}\nGreatest Increase in profits: {maxChangeDate} (${maxChange})\nThe greatest decrease in profits: {minChangeDate} (${minChange})"
        )


