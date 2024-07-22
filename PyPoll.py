import os
import csv
import statistics

# Create the CSV Path & Headers
csvpath = os.path.join('Resources', 'election_data.csv')
ballot = []
county = []
candidate = []

with open(csvpath) as pypoll:
    csvreader = csv.reader(pypoll, delimiter = ",")
    #print(csvreader)
    csvheader = next(csvreader)
    #print(f"csvheader: {csvheader}")

    for row in csvreader:
       #print(row)
       ballot.append(row[0])
       county.append(row[1])
       candidate.append(row[2])

# Find total votes
total_votes = len(ballot)

# Find candidate names 
candidate_names = []
for name in range(len(candidate)):
    if candidate[name] not in candidate_names:
        candidate_names.append(candidate[name])

# Find votes for each candidate
votes = []
for name in range(len(candidate_names)):
    votes.append(0)
    for vote in range(len(candidate)):
        if candidate[vote] == candidate_names[name]:
            votes[name] += 1

# Find the % of total votes each candidate received
vote_percent= []
for vote in votes:
    vote_percent.append(round((vote / total_votes) * 100, 2))

# Determine who won
max_vote = max(vote_percent)
i = 0
for vote in vote_percent:
    if vote == max_vote:
        winner = candidate_names[i]
    i += 1

# Show the results including: name, vote% and vote total
election_results = "" 
for name in range(len(candidate_names)):
    election_results += str(candidate_names[name]) + ": " + str(vote_percent[name]) + "% " + "(" + str(votes[name]) + ")" + "\n"

# Print it!
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

print(str(election_results))
print("-------------------------")

print("Winner: " + str(winner))
print("-------------------------")

# Create the ReadMe.txt
export = "Election Results" + "\n-------------------------" + "\nTotal Votes: " + str(total_votes) + "\n-------------------------\n" + str(election_results) + "\n-------------------------" + "\nWinner: " + str(winner) + "\n-------------------------"

with open("Py_Poll.txt", "w") as file:
    file.write(export)