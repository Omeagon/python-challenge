import os
import csv
import statistics

# Create the CSV path 
csvpath = os.path.join('Resources', 'budget_data.csv')
date = []
profit_loss = []

with open(csvpath) as pybank:
    csvreader = csv.reader(pybank, delimiter = ",")
    print(csvreader)
    csvheader = next(csvreader)
    print(f"csvheader: {csvheader}")

    for row in csvreader:
       date.append(row[0])
       profit_loss.append(int(row[1]))
     
# Prep data
total_months = len(date)
total = sum(profit_loss)
net_change = []

# Find net change in profit/loss
for index in range(len(profit_loss)-1): 
    net_change.append(int(profit_loss[index+1]) - int(profit_loss[index]))
avg_net_change = round(statistics.mean(net_change),2)

# Find Max and Min changes
max_change = max(net_change)
min_change = min(net_change)
for index in range(len(net_change)):
    if net_change[index] == max_change:
        max_change_date = date[index+1]
    elif net_change[index] == min_change:
        min_change_date = date[index+1]

# Print it! 
print("Financial Analysis")
print("--------------------")

print("Total Months: " + str(total_months))
print("Total: $" + str(total))
print("Average Change: $" + str(avg_net_change))
print("Greatest Increase in Profits: " + str(max_change_date) + "  $" + str(max_change))
print("Greatest Decrease in Profits: " + str(min_change_date) + "  $" + str(min_change))

# Create the ReadMe.txt
export = "Financial Analysis" + "\n--------------------" + "\nTotal Months: " + str(total_months) + "\nTotal: $" + str(total) + "\nAverage Change: $" + str(avg_net_change) + "\nGreatest Increase in Profits: " + str(max_change_date) + "  $" + str(max_change) + "\nGreatest Decrease in Profits: " + str(min_change_date) + "  $" + str(min_change)

with open("Py_Bank.txt", "w") as file:
    file.write(export)