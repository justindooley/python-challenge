import os
import math
import csv

budget_csvpath = os.path.join("Resources", "budget_data.csv")

data = []
revenue = []
rev_change = []
date = []

with open(budget_csvpath) as budget_csv:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_csv, delimiter=',')
    csv_header = next(csvreader)

    # Fill data with csv rows and headers
    for row in csvreader:
        data.append({
            csv_header[0]: row[0], csv_header[1]: int(row[1])
        })
   
    #This fills separate revenue and date lists.
        date.append(row[0])
        revenue.append(int(row[1]))
    
    print("Financial Analysis")   
    print("----------------------------")
    month_count = (len(data))
    print(f"Total Months: {month_count}")   

    total = 0
    for data1 in data:
        total += data1['Profit/Losses']
    print(f"Total: ${total}") 

    avg_rev_change = 0
    max_rev_change = 0
    min_rev_change = 0
    #in this loop I found average revenue change, max revenue change, and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)
        avg_rev_change = round(avg_rev_change,2)
        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print(f"Avereage Change: $", (avg_rev_change))
    print(f"Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
    print(f"Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")
    
    
    with open("Financial Results.txt", "w") as text_file:
        print(f'Financial Analysis\n-------------------------\nTotal Months: {month_count}\nAverage  Change: {avg_rev_change}\nGreatest Increase in Profits: {max_rev_change_date} ($' + str(max_rev_change) + ')' + '\nGreatest Decrease in Profits: ' + str(min_rev_change_date) + '($' + str(min_rev_change) + ')', file = text_file)
  
