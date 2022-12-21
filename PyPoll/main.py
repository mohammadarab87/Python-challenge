# Import os module
import os
# module for readinf csv files
import csv

csvpath = os.path.join("Resources","election_data.csv")

# Declare Variables 
total_votes = 0 
CharlesCasperStockham_votes = 0
DianaDeGette_votes = 0
RaymonAnthonyDoane_votes = 0

# Open csv 
with open(csvpath,newline="", encoding="utf-8") as csvfile:

    
    csvreader = csv.reader(csvfile,delimiter=",") 

    # Skip the header 
    header = next(csvreader)     

    # loop through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and assign to (total_votes) variable
        total_votes +=1

        #count the times it appears and store in a list
        
        if row[2] == "Charles Casper Stockham": 
            CharlesCasperStockham_votes +=1
        elif row[2] == "Diana DeGette":
            DianaDeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            RaymonAnthonyDoane_votes +=1
        

 # make a dictionaryTo find the winner 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [CharlesCasperStockham_votes, DianaDeGette_votes,RaymonAnthonyDoane_votes]

# zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# summary of the analysis
CharlesCasperStockham_percent = (CharlesCasperStockham_votes/total_votes) *100
DianaDeGette_percent = (DianaDeGette_votes/total_votes) * 100
RaymonAnthonyDoane_percent = (RaymonAnthonyDoane_votes/total_votes)* 100


# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {CharlesCasperStockham_percent:.3f}% ({CharlesCasperStockham_votes})")
print(f"Diana DeGette: {DianaDeGette_percent:.3f}% ({DianaDeGette_votes})")
print(f"Raymon Anthony Doane: {RaymonAnthonyDoane_percent:.3f}% ({RaymonAnthonyDoane_votes})")

print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files

output_file = os.path.join("analysis","Election_Results_Summary.txt")
with open(output_file,"w") as file:

# Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {CharlesCasperStockham_percent:.3f}% ({CharlesCasperStockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {DianaDeGette_percent:.3f}% ({DianaDeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {RaymonAnthonyDoane_percent:.3f}% ({RaymonAnthonyDoane_votes})")
    file.write("\n")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")