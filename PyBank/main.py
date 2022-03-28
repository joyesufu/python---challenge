import os 
import csv 

csvpath = os.path.join("Resources", "budget_data.csv")

months = []
month_change = []
profit_loss = []
pl_change = 0
total_profit = 0
pre_profit = 0
x = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        x = x + 1

        months.append(row[0])
        profit_loss.append(row[1])

        total_profit = total_profit + int(row[1])

        end_profit = int(row[1])
        monthly_profit = end_profit - pre_profit

        month_change.append(monthly_profit)
        pl_change = pl_change + monthly_profit
        pre_profit = end_profit

        avg_change = (pl_change/x)

        great_increase = max(month_change)
        great_decrease = min(month_change)

        high_date = months[month_change.index(great_increase)]
        low_date = months[month_change.index(great_decrease)]


print("Financial Analysis")
print("-----------------------------------")
print("Total Months: " + str(x))
print(f"Total: ${total_profit}")
print("Average Change: $" + str(int(avg_change)))
print("Greatest Increase In Profits: " + str(high_date) + " ($" + str(great_increase) + ")")
print("Greatest Decrease In Profits: " + str(low_date) + " ($" + str(great_decrease) + ")")

output_path = os.path.join("Analysis", "analysis.txt")
with open(output_path, "w") as text:

    text.write("Financial Analysis\n")
    text.write("--------------------------------------------------\n")
    text.write("Total Months: " + str(x) + "\n")
    text.write("Total: $" + str(total_profit) + "\n")
    text.write("Average Change: $" + str(int(avg_change)) + "\n")
    text.write("Greatest Increase In Profits: " + str(high_date) + " ($" + str(great_increase) + ")\n")
    text.write("Greatest Increase In Profits: " + str(low_date) + " ($" + str(great_decrease) + ")\n")
        