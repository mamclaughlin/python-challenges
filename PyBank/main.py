# The total number of months included in the dataset
# The total amount of revenue gained over the entire period
# The average change in revenue between months over the entire period
# The greatest increase in revenue (date and amount) over the entire period
# The greatest decrease in revenue (date and amount) over the entire period

import os
import csv

# Variables 
# ----------------------
months = 0
revenue = 0

prev_revenue = 0
current_revenue = 0
revenue_change = []

# Main Process 
# ----------------------
csvpath = os.path.join("Resources", 'budget_data_1.csv')

with open(csvpath) as csvfile:

	csvreader = csv.DictReader(csvfile, delimiter=',')
	# next(csvreader, None)

	for row in csvreader:
		#test data is coming through:
		# print(row)

		#total months
		months += 1

		#Add up total revenue
		revenue += int(row["Revenue"])

		#set our current revenue to current iteration point
		current_revenue = int(row["Revenue"])

		#Calculate change in revenue
		revenue_change.append(current_revenue - prev_revenue)

	print("\n\nFinancial Analysis")
	print("============================")	
	print("Number of months: " + str(months))
	print("Total Revenue: $" + str(revenue))
	print("Average change in revenue: $" + str(sum(revenue_change)/len(revenue_change)))
	print("Greatest increase in revenue: " + str(max(revenue_change)))
	print("Greatest decrease in revenue: " + str(min(revenue_change)))



