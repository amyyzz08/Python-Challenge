#Import Modules
import csv
import os

#Creating paths
file_path="Resources/election_data.csv"
output_path="PyPoll/analysis.txt"

#Define Variables
candidates=[]
vote_count=[]
percent_votes=[]

total_votes=0
winning_count=0
winner=""
votes=0

#Opening csv File
with open(file_path, "r") as file:
    csvreader=csv.reader(file, delimiter=",")
    
    next(csvreader)

    for row in csvreader:

        #Total vote count
        total_votes = total_votes + 1

        #Candidates who received votes
        candidate = row[2]

        #Tally up votes for each candidate and add to list
        if candidate not in candidates:
            candidates.append(row[2])
            candidate_index = candidates.index(candidate)
            vote_count.append(1)
            
        else:
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1

    #Generate percentage of vote for each candidate
    for votes in vote_count:
        percent=(votes/total_votes) * 100
        percent = round(percent)
        percent = "%.3f%%" % percent
        percent_votes.append(percent)

   #Finding Winning candidate
    winner=max(vote_count)
    winner_index=vote_count.index(winner)
    winning_candidate=candidates[winner_index]

#Election Summary
    print("Election Results\n")
    print("-------------------------\n")
    print(f"Total Votes: {total_votes}\n")  
    print("-------------------------\n")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent[i])} ({str(vote_count[i])})")
    print("--------------------------\n")
    print(f"Winner: {winning_candidate}\n")
    print("--------------------------\n")       

#Exporting in new file
with open(output_path, "w") as text:
    text.write(f"Election Results\n")
    text.write("-----------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("------------------------\n")
    for i in range(len(candidates)):
        text.write(f"{candidates[i]}: {str(percent[i])} ({str(vote_count[i])})")
    text.write("------------------------\n")
    text.write("Winner: {}\n")
    text.write("------------------------\n")