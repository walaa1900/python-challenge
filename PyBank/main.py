import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")


text_path ="financial_analysis.txt"
total_months = []
total_profit = []
montthly_avarage= []


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    for row in csvreader:
           

        #  total months and total profit 
        total_months.append(row[0])
        total_profit.append(int(row[1]))


    for i in range(len(total_profit)-1):
        
        # average
        montthly_avarage.append(total_profit[i+1]-total_profit[i])
                                     
    
  
  
  
#  max and min of the the montly profit change 
max_increase_value = max(montthly_avarage)
max_decrease_value = min(montthly_avarage)

max_increase_month = montthly_avarage.index(max(montthly_avarage)) + 1
max_decrease_month = montthly_avarage.index(min(montthly_avarage)) + 1 

#print result
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(montthly_avarage)/len(montthly_avarage),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
    

    #open the text file
with open("financial_analysis.txt", "w")as file:
    file.write("Financial Analysis\n")
    file.write("----------------------\n")
 
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"total months: {sum(total_profit)}\n")
    file.write(f"Average Change: {round(sum(montthly_avarage)/len(montthly_avarage),2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")
