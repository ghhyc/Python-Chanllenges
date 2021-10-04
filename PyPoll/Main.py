# module imports
import os
import csv
#
#
cvspath = os.path.join("..", "PyPoll", "Resources", "PyPoll_Resources_election_data.csv")
# set variables
#
# Specify the file to write to
texttosave = os.path.join("..", "PyPoll", "Analysis", "Analysis_Election.txt")
#
tot_votes = 0
candidate = ""  
candidate_list = []
vote_list = {}
percent_lis =[]
winner = ""
vote_ratio = 0
vote_percent = 0
win_count = 0
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

		#count the total voters
		tot_votes += 1

		if row[2] not in candidate_list:
			candidate_list.append(row[2])
			vote_list[row[2]]=0
		
		vote_list[row[2]] += 1

print("Election Results")
print("------------------------")
print(f"Total Votes  {tot_votes}")
print("------------------------")
with open(texttosave,"w") as textfile:
    Summary = (f"\nElection Results\n"
        f"----------------------------------\n"
        f"\nTotal tot_votes: {tot_votes}\n"
        f"----------------------------------\n")
    textfile.write(Summary)

    for candname,votecnt in vote_list.items():  
        votecnt = vote_list.get(candname)
        vote_ratio = float(votecnt)/float(tot_votes) * 100 

        if (votecnt > win_count):
            win_count = votecnt
            winner = candname

        print (f"{candname}:{vote_ratio:.3f}% ({votecnt})")
        textfile.write(f"{candname}:{vote_ratio:.3f}% ({votecnt})\n")
    print ("------------------------")
    # find winner
    
    print(f"Winner:{winner}")

    Summary1 = (
    f"--------------------------------\n" 
    f"\nWinner: {winner}\n"
    )
    textfile.write(Summary1)








