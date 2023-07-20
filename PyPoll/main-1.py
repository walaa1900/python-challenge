import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

text_path ="Election Results.txt"

csvpath=os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    data = list (csvreader)
    row_count=len(data)
    winner =0
    
    
    
candilist = []
tally = []

#alist for candidate
for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candilist: 
            candilist.append(candidate)
candicount = len(candilist)

#The total number of votes cast
votes=[]
percentage =[]

for j in range (0,candicount):
     name = candilist[j]
     votes.append(tally.count(name))
     vprct = votes[j]/row_count
     percentage.append(vprct)

print (f"total vote: {row_count:,}")
print (f"{candilist[0]}: {percentage[0]:.3%} ({votes[0]:,})")
print (f"{candilist[1]}: {percentage[0]:.3%} ({votes[0]:,})")
print (f"{candilist[2]}: {percentage[0]:.3%} ({votes[0]:,})")
print (f"Winner: {candilist[winner]}")
 

#The winner   
winner = votes.index(max(votes)) 
with open("Election Results.txt", "w")as file:
     file.write("Election Results\n")

     file.write("------------------------------------\n")

     file.write(f"total vote: {row_count:,}\n")

     file.write("-------------------------------------\n")
     file.write(f"{candilist[0]}: {percentage[0]:.3%} ({votes[0]:,})\n")
     file.write(f"{candilist[1]}: {percentage[0]:.3%} ({votes[0]:,})\n")
     file.write(f"{candilist[2]}: {percentage[0]:.3%} ({votes[0]:,})\n")

     file.write("--------------------------------------\n")

     file.write(f"Winner: {candilist[winner]}\n")

     file.write("--------------------------------------\n")




  

   





   