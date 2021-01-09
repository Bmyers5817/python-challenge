# The task with this challenge is to create a Python script to analyze financial
# records of PyBank for various components.
# Fields: date, Profit/Losses

import os
import csv

# Read and collect path of data source from the Resources folder
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

# Define variables to store data
count_mo = []
profit = []
mo_change = []
date = []

# Initialize variables as needed
count_mo = 0
total_pl = 0
ave_chgs = 0

# Open and set reader for csv file
open with(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Creation of for statement to read and collect data
for row in csvreader:
    # Use count_mo to count the number of months / lines
    count_mo = count_mo + 1
    

# Caluculate total number of months included in the dataset
total_months = len(date)

# Calculate the net total of Profit/Loss over the entire period
total_pl = sum(Profit/Losses)

# Calculate the changes in Profit/Loss over the entire period, then 
# find the average of those changes.
ave_chgs = (total_pl / len(total_pl))

# Determine the greatest increase in profits (date and amount) 
# over the entire period
max_pl = max(Profit/Losses)

# Determine the greatest decrease in losses (date and amount) 
# over the entire period
min_pl = min(Profit/Losses)

# Print anaylsis table to terminal and txt file
print(/n'''/n,"text")
print("Financial Analysis")
print(/n-------------------/n)
print(f'"Total Months:  " total_months')
print(f'"Total:  " total_pl')
print(f'"Average Change:  " avg_chngs')
print(f'"Greatest Increase in Profits:  " max_pl')
print(f'"Greatest Decrease in Profits:  " min_pl')
print(/n'''/n)