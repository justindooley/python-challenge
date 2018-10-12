import os
import math
import csv

# Open CSV
election_csvpath = os.path.join("Resources", "election_data.csv")


# starter counters
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0


with open(election_csvpath) as election_csv:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(election_csv, delimiter=',')
    next(csvreader)
    data = list(election_csv)
    vote_count = (len(data))

    # Loop through looking for Votes

    for row in data:
        row = row.split(",")
        Voter_ID , County , Candidate = row

        if "Khan\n" == Candidate:
            khan_count+= 1

        if "Correy\n" == Candidate:
            correy_count+= 1

        if "Li\n" == Candidate:
            li_count+= 1
        
        if "O'Tooley\n" == Candidate:
            otooley_count+= 1

# Calculate Percentages to Round
khan_percent = (khan_count / vote_count)*100
correy_percent = (correy_count / vote_count)*100
li_percent = (li_count / vote_count)*100
otooley_percent = (otooley_count / vote_count)*100


print("Election Results")
print("-------------------------")

# Print all the totals and percentages as strings
print("Total Votes: " + str(vote_count))
print("-------------------------")
print("Khan: " + str(round(khan_percent)) + "% (" + str(khan_count) + ")")
print("Correy: " + str(round(correy_percent)) + "% (" + str(correy_count) + ")")
print("Li " + str(round(li_percent)) + "% (" + str(li_count) + ")")
print("O'Tooley: " + str(round(otooley_percent)) + "% (" + str(otooley_count) + ")")
print("-------------------------")

# for the output text
khan = ("Khan: " + str(round(khan_percent)) + "% (" + str(khan_count) + ")")
correy = ("Correy: " + str(round(correy_percent)) + "% (" + str(correy_count) + ")")
li = ("Li " + str(round(li_percent)) + "% (" + str(li_count) + ")")
otooley = ("O'Tooley: " + str(round(otooley_percent)) + "% (" + str(otooley_count) + ")")

#Pick the winnder!
if ((correy_count) > (khan_count or li_count or otooley_count)):
    winner = "Winner: Correy"
elif ((li_count) > (khan_count or correy_count or otooley_count)):
    winner = "Winner: Li"
elif ((otooley_count) > (khan_count or li_count or correy_count)):
    winner = "Winner: O'Tooley"
elif ((khan_count) > (correy_count or li_count or otooley_count)):
    winner = "Winner: Khan"
print(winner)
print("-------------------------")


with open("Election Results.txt", "w") as text_file:
    print(f'Election Results \n-------------------------\nTotal Votes: {vote_count}\n-------------------------\n'+ khan +'\n' + correy + '\n' + li + '\n' + otooley + '\n-------------------------\n' + winner + '\n-------------------------', file = text_file)
    
