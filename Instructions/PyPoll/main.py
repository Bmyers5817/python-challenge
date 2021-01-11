# The task with this challenge is to create a Python script to analyze financial
# records of PyBank for various components.
# Fields: date, Profit/Losses

import os
import csv

# Read and collect path of data source from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# Capture list of candidates with votes casted & unique canidate
candidate = []
uniq_cand = []

# Counter for total number of votes
vote_count = 0

# # Variable to capture votes per candidate 
# cand_vote = []

# Variable to capture percent of total votes per candidate
prct_votes = []

# Open and set reader for csv file
with open(election_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

 # Creation of for statement to read and collect data
    for row in csv_reader:
    
        # Use vote_count to count the number of votes cast
        vote_count = vote_count + 1

        # Set candidate list
        candidate.append(row[2])

        # Set unique candidates, x to each unique candidate, y to number of votes / candidate, and z to percentage of votes / candidate
    for x in set(candidate):
        uniq_cand.append(x)
        y = candidate.count(x)
        vote_count.append(y)
        z = (y/vote_count)*100, 3
        #z = round(percentage) - see if 43 works
        prct_votes.append(z)
        # set format for percentage data   
        prct_votes = "%.3f%%" % z

  # Find winner of votes cast
    cand_winner = max(vote_count)
    winner = uniq_cand[vote_count.index(cand_winner)]

# Print results table to terminal 

print("Election Results")
print("-----------------------------------")
print(" Total Votes:  " + str(vote_count))
print("-----------------------------------")
for i in range(len(candidate)):
    print(candidate[i] + ":" + str(prct_votes[i]) +"% (" + str(vote_count[i])+")")
print("-----------------------------------")    
print("The Winner is:  " + winner)
print("-----------------------------------") 

# Print anaylsis table to text file

# with open('financial_analy.txt', 'w') as file:
   
#     file.write("----------------------------\n")
#     file.write("Financial Analysis"+"\n")
#     file.write("----------------------------\n")
#     file.write(" Total Months:  " + str(count)+"\n")
#     file.write(" Total:  " + "$" + str(total_pl)+"\n")
#     file.write(" Average Change:  " + str(int(ave_change))+"\n")
#     file.write(" Greatest Increase in Profits:  " + str(incr_date) + "   $" + str(gr_increase)+"\n")
#     file.write(" Greatest Decrease in Profits:  " + str(decr_date) + "   $" + str(gr_decrease)+"\n")