# import os module to creat file path
import os
# module for reading csv files
import csv

input_path = os.path.join("Resources","budget_data.csv")

# Create empty lists for the following variables
total_months = []
total_profit = []
profit_change = []
 
# improved reading using csv module
with open(input_path,newline="", encoding="utf-8") as csvfile:

# csv reader specifies delimiter and variable that hold contents

    csvreader = csv.reader(csvfile, delimiter=",") 

    header = next(csvreader)  

# loop for each row of data after the header
    for row in csvreader:

        total_months.append(row[0])
        total_profit.append(int(row[1]))

# Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        profit_change.append(total_profit[i+1]-total_profit[i])
        
# max and min of the the montly profit change 
max_increase_value = max(profit_change)
max_decrease_value = min(profit_change)

# use the +1 at the end 
max_increase_month = profit_change.index(max(profit_change)) + 1
max_decrease_month = profit_change.index(min(profit_change)) + 1 

# Print Statements

print("Financial Analysis")

print("----------------------------")

print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# output file
output_path = os.path.join("analysis","Financial_Analysis_Summary.txt")
with open(output_path,"w") as file:
    
# print Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")