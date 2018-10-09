import os
import math
import csv

budget_csvpath = os.path.join("Resources", "budget_data.csv")


with open(budget_csvpath) as budget_csv:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_csv, delimiter=',')
    next(csvreader)
    data = list(budget_csv)
    month_count = (len(data))
    # data = data.remove("\n")
    # data = str.data.replace('\n','')
    # print(data.stript("\n")))
    print("Total Months: " + str(month_count))
    # print data.replace('\n','')
    print strip("\n")
    # for row in data:
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