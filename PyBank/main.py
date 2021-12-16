#Import Modules
import os
import csv

#Creating file paths
csvpath="Resources/budget_data.csv"
output_path="PyBank/analysis.txt"

#Define Variables
revenue_change=[]
monthly_changes=[]
greatest_increase=["",0]
greatest_decrease=["",0]

month_count=0
net_total=0
previous_month=0
current_month=0
rev_change=0
revenue_avg=0

#Opening CSV File
with open (csvpath,"r") as file:
    csvreader=csv.reader(file, delimiter=",")
    
    next(csvreader)

    for row in csvreader:

        #Total Months
        month_count=month_count + 1
        
        #Net Total amount of Profit/Losses
        current_month=int(row[1])
        net_total= net_total + current_month

        #Revenue Change
        rev_change=int(row[1]) - previous_month
        previous_month=int(row[1])
        revenue_change=revenue_change + [rev_change]
        monthly_changes=monthly_changes + [row[0]]
       
        #Greatest increase in Profits
        if rev_change > int(greatest_increase[1]):
            greatest_increase[1]=rev_change
            greatest_increase[0]=row[0]

        #Greatest decrease in Profits
        if rev_change < int(greatest_decrease[1]):
            greatest_decrease[1]=rev_change
            greatest_decrease[0]=row[0]

    #Average Change of Profits/Loss
    revenue_avg=sum(revenue_change)/len(revenue_change)
    print(revenue_avg)
            
#Budget Summary
    print(f"Financial Analysis\n")
    print(f"-----------------------\n")
    print(f"Total Months: {month_count}\n")
    print(f"Total Net Amount: ${net_total}\n")
    print(f"Average Change: {revenue_avg}\n")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} ({greatest_increase[1]})\n")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} ({greatest_decrease[1]})\n")

#Exporting in new file
with open(output_path, "w") as text:
    text.write(f"Financial Analysis\n")
    text.write("-----------------------\n")
    text.write(f"Total Months: {month_count}\n")
    text.write(f"Total Net Amount: ${net_total}\n")
    text.write(f"Average Change: ${revenue_avg}\n")
    text.write(f"Greatest Increase in Profits: {greatest_increase[0]}, ({greatest_increase[1]})\n")
    text.write(f"Greatest Decrease in Profits: {greatest_decrease[0]}, ({greatest_decrease[1]})\n")
    