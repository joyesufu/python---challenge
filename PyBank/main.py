import os 
import csv 

csvpath = os.path.join("Resources", "budget_data.csv")


with open(csvpath, encoding="utf") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    total_months = 0
    total = []
    monthly_change = []
    profit_increase = 0
    profit_decrease = 0
    dates = []
    
    
    for row in csvreader:
        # Date for each row added to a list
        dates.append(row[0])
        
        # Total Number of months/rows
        total_months += 1

        total.append(int(row[1]))

        

    # csvreader.seek(0)

    for i in range(len(total)-1):
        # Profit change from month to month
        monthly_change.append(total[i+1]-total[i])

        # Total Average Profit Change Over the Entire Period
        avg_change = sum(monthly_change)/(len(total)-1)

    # Greatest Profit increase for one period
    profit_increase = max(monthly_change)

    max_index = monthly_change.index(profit_increase)

    max_month = dates[max_index+1]

    # Greatest Profit decrease for one period
    profit_decrease = min(monthly_change)

    min_index = monthly_change.index(profit_decrease)

    min_month = dates[min_index+1]


        
    
    
    # Print Final Results!
    print("Financial Analysis")
    print("----------------------------")
    
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(sum(total)))
    print(f"Average Change: ${avg_change:.2f}")
    print(f"Greatest Increase in Profits: {max_month} (${profit_increase})")
    print(f"Greatest Decrease in Profits: {min_month} (${profit_decrease})")

output_path = os.path.join("Analysis", "analysis.txt")
with open(output_path, "w") as text:

    text.write("Financial Analysis\n")
    text.write("--------------------------\n")
    text.write("Total Months: " + str(total_months) + "\n")
    text.write("Total: $" + str(sum(total)) + "\n")
    text.write(f"Average Change: ${avg_change:.2f} \n")
    text.write(f"Greatest Increase In Profits: {max_month} (${profit_increase})\n")
    text.write(f"Greatest Increase In Profits: {min_month} (${profit_decrease})\n")
        