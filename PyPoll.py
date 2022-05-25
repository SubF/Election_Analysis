#Requirements
#1. Total votes cast
#2. list of candidates with votes
#3. percentage of votes each candidate recieved
#4. total votes for each candidate
#5. winner of the election 

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

#print the header row
    headers = next(file_reader)
    print(headers)
