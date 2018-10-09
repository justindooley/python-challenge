import os
import math
import csv

budget_csvpath = os.path.join("Resources", "budget_data.csv")

data = []

with open(budget_csvpath) as budget_csv:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_csv, delimiter=',')
    csv_header = next(csvreader)

    # Fill data with csv rows and headers
    for row in csvreader:
        data.append({
            csv_header[0]: row[0], csv_header[1]: int(row[1])
        })
        
    # Create new lists for higher maths
    revenue = []
    rev_change = []
    date = []
   
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
    
    #in this loop I found total revenue change, max revenue change, and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $", (avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")
    
    
    #average = 0
    #for data2 in data:
    #    average = total / month_count
    #print(f"Average  Change: ${average}")

    # print(data)

    # greatest = 0
    # for data3 in data:
    #     greatest >= data3['Profit/Losses']
    # print(f'The Greatest Increase in Profits: {greatest}')

    # data = list(budget_csv)
    # csv_header = next(csvreader)
    # data = data.remove("\n")
    # data = str.data.replace('\n','')
    # print(data.stript("\n")))
    # print data.replace('\n','')
    # print(data(remove("\n"))
    # print strip("\n")
    # for row in csvreader:
    #     row = row.split(",")
    #     date , profit = row
        # data = data.strip('\n')
        # data = data.replace('\n', '')
        # profitlist = float(profit)
        # profitlist = math.fsum(profit)
        # print(sum(profitlist)
        # profits = (int(profit))
        # print(sum(profits))
        # print(profit)
        # print(data)
        # total_profits = sum(profits)
        # print("" + str(total_profits))
