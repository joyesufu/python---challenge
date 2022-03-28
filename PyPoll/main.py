import os
import csv

totalvotes = []
percent_of_votes = []
candidates = []
count = 0

csvpath = os.path.join("Resources", "election_data.csv")

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            totalvotes.append(1)

        else:
            candidate_votes = candidates.index(row[2])
            totalvotes[candidate_votes] += 1

    for votes in totalvotes:
        percentage_of_votes = (votes / count) * 100
        percentage_of_votes = float(percentage_of_votes)
        percent_of_votes.append(percentage_of_votes)

        winner = max(totalvotes)
        candidate_votes = totalvotes.index(winner)
        winning_candidate = candidates[candidate_votes]


print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(count))
print("-------------------------------------")

for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_of_votes[i])} ({str(totalvotes[i])})")


print("-------------------------------------")
print("Winner: " + str(winning_candidate))
print("-------------------------------------")