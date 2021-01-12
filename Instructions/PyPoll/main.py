# The task with this challenge is to create a Python script to analyze financial
# records of PyBank for various components.
# Fields: date, Profit/Losses

import os
import csv

# Read and collect path of data source from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# Capture list of candidates with votes cast and count of votes
candidates = []
vote_count = []

# Open and set reader for csv file
with open(election_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

# Creation of for statement to read and collect data
    for row in csv_reader:
        # Check and capture unique candidates 
        if row[2] not in candidates:
            candidates.append(row[2])
            # Append vote count by candidate
            vote_count.append(1)
        else:
            # Use of voteindex to capture votes upon candidate change
            # * vote_count[voteindex] was not working without the +=, which was researched with various sites (CodeAcademy/SlackOverflow)
            voteindex = candidates.index(row[2])
            vote_count[voteindex] += 1

    # Count for total number of votes
    total_votes = sum(vote_count)

    # Capture percent of total votes per candidate
    votepercent = [round(vote_count[i]/total_votes*100,4) for i in range(0,len(vote_count))]

    
# Print results table to terminal 

print("-----------------------------------")
print("Election Results")
print("-----------------------------------")
print(" Total Votes:  " + str(total_votes))
print("-----------------------------------")

for i in range(len(candidates)):
    print(f'{candidates[i]}:  {votepercent[i]}% ({vote_count[i]})')

print("-----------------------------------")    
print(f"The Winner is:  {candidates[vote_count.index(max(vote_count))]}")
print("-----------------------------------") 

# Print anaylsis table to text file

with open('election_results.txt', 'w') as file:
   
    file.write("----------------------------\n")
    file.write("Election Results"+"\n")
    file.write("----------------------------\n")
    file.write(" Total Votes:  " + str(total_votes)+"\n")
    file.write("----------------------------\n")
    for i in range(len(candidates)):
       file.write(f'{candidates[i]}:  {votepercent[i]}% ({vote_count[i]})''\n')
    file.write("----------------------------\n") 
    file.write(f"The Winner is:  {candidates[vote_count.index(max(vote_count))]}"+"\n")
    file.write("----------------------------\n") 