# The task with this challenge is to create a Python script to analyze financial
# records of PyBank for various components.
# Fields: date, Profit/Losses

import os
import csv

# Read and collect path of data source from the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Define variables to store data
profit = []
date = []

# Initialize variables as needed
count = 0
total_pl = 0
mo_chg_profits = 0
init_profit = 0

# Open and set reader for csv file
with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

 #Reading the first row (to track the changes properly)
    first_row = next(csv_reader)
    total_pl += int(first_row[1])
    mo_chg_profits = int(first_row[1])  
    count += 1 

# Creation of for statement to read and collect data
    for row in csv_reader:
    
        # Use count to count the number of months / lines
        count = count + 1

        # Append date for gathering increase / decrease profits
        date.append(row[0])

        # Capture the changes
        mo_change_profits = int(row[1])-init_profit 
             
        # Calculate the net total of Profit/Loss over the entire period
        profit.append(mo_change_profits)
        init_profit = int(row[1])
        total_pl = total_pl + int(row[1])

        # Calculate the average changes in Profit/Loss over the entire period.
        ave_change = round(sum(profit)/len(profit),2)

    # Determine the greatest increase in profits (date and amount) 
    # over the entire period
    gr_increase = max(profit)
    gr_incr_index = profit.index(gr_increase)
    incr_date = date[gr_incr_index]

    #Determine the greatest decrease in losses (date and amount) 
    #over the entire period
    gr_decrease = min(profit)
    gr_decr_index = profit.index(gr_decrease)
    decr_date = date[gr_decr_index]
    
# Print anaylsis table to terminal 

print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print(" Total Months:  " + str(count))
print(" Total:  " + "$" + str(total_pl))
print(" Average Change:  " + str(ave_change))
print(" Greatest Increase in Profits:  " + str(incr_date) + "   $" + str(gr_increase))
print(" Greatest Decrease in Profits:  " + str(decr_date) + "   $" + str(gr_decrease))

# Print anaylsis table to text file

with open('financial_analy.txt', 'w') as file:
   
    file.write("----------------------------\n")
    file.write("Financial Analysis"+"\n")
    file.write("----------------------------\n")
    file.write(" Total Months:  " + str(count)+"\n")
    file.write(" Total:  " + "$" + str(total_pl)+"\n")
    file.write(" Average Change:  " + str(int(ave_change))+"\n")
    file.write(" Greatest Increase in Profits:  " + str(incr_date) + "   $" + str(gr_increase)+"\n")
    file.write(" Greatest Decrease in Profits:  " + str(decr_date) + "   $" + str(gr_decrease)+"\n")