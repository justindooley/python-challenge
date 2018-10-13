# Import libraries
import os
import csv

# Finding the path to the budget.csv w/Resources..
budget_csvpath = os.path.join("Resources", "budget_data.csv")

# Creating lists
revenue = []
rev_change = []
date = []

# Opening the csv with the file path
with open(budget_csvpath) as budget_csv:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_csv, delimiter=',')
    # Skip header
    next(csvreader)

    # Fill separate revenue and date lists.
    for row in csvreader:
        date.append(row[0])
        revenue.append(int(row[1]))
    
    # Printing total months & total revenue
    print("Financial Analysis")   
    print("----------------------------")
    month_count = (len(revenue))
    print(f"Total Months: {month_count}") 
    print(f"Total: ${sum(revenue)}") 

    # In this loop I found average revenue change, max revenue change, and min revenue change. 
    avg_rev_change = 0
    max_rev_change = 0
    min_rev_change = 0
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)
        avg_rev_change = round(avg_rev_change,2)
        max_rev_change_date = str(date[rev_change.index(max(rev_change))+ 1])
        min_rev_change_date = str(date[rev_change.index(min(rev_change)) + 1])
    
    # Printing Average Change, Greatest Increace, & Greatest Decrease
    print(f"Avereage Change: $", (avg_rev_change))
    print(f"Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
    print(f"Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")
    
    # Create text file with the results :)
    with open("Financial Results.txt", "w") as text_file:
        print(f'Financial Analysis\n-------------------------\nTotal Months: {month_count}\nTotal: ${sum(revenue)}\nAverage  Change: {avg_rev_change}\nGreatest Increase in Profits: {max_rev_change_date} ($'
        + str(max_rev_change) + ')' + '\nGreatest Decrease in Profits: ' + str(min_rev_change_date) + ' ($' + str(min_rev_change) + ')', file = text_file)
