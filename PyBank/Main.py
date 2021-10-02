# module imports
import os
import csv
#
#
cvspath = os.path.join("..", "pybank", "resources", "budget_data.csv")
filetosave = os.path.join("..", "pybank", "analysis", "analysis_doc.txt")
# set variables
#
tot_months = 0
tot_profit_loss = 0
Previous_profit_loss = 0

month_change = 0
tot_month_change = 0
ave_month_change = 0

greatest_increase = 0
greatest_increase_month = ""

greatest_decrease = 0
greatest_decrease_month = ""
#
#
#open CVS file
with open(cvspath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	# 
	# read the header row
	csv_header = next(csvreader)
	#
	#read each row of sheet
	for row in csvreader:
		#count the total number of months
		tot_months += 1

		# add total profit/loss
		tot_profit_loss += int(row[1])

		#compute change in profit/loss current month to previous month
		if tot_months > 1:
			month_change = int(row[1]) - Previous_profit_loss

		# add the tot monthly change for calculate average
		tot_month_change += month_change

		# set profit/loss to previous month
		Previous_profit_loss = int(row[1])

		# compute greatest increase
		if month_change > greatest_increase:
			greatest_increase = month_change
			greatest_increase_month = row[0]

		# compute greatest decrease - losses
		if month_change	< greatest_decrease:
			greatest_decrease = month_change
			greatest_decrease_month = row[0]

ave_month_change = tot_month_change/ (tot_months -1)	

#print the analysis to terminal and write to textfile

with open(filetosave,"w") as textfile:
	Results	 = (f"\nFinancial Analysis\n" 
	f"------------------------\n"
	f"Total Months:  {tot_months}\n"
	f"Total:$ {tot_profit_loss}\n"
	f"Average Change: $ {ave_month_change:.2f}\n"
	f"Greatest Incease in Profits: {greatest_increase_month}  ${greatest_increase:.2f}\n"
	f"Greatest Decrease in Profits: {greatest_decrease_month}  ${greatest_decrease:.2f}\n"
	)
	print(Results)
	textfile.write(Results)

#



