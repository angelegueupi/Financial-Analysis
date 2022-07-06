import csv
import os
csvpath=os.path.join( "resources","election_data.csv")
print(csvpath)
output_file= os.path.join( "analysis","election_analysis.txt")

#variables
total_vote_cast = 0
canditates_voteslist=[] #empty list
totalvotes_each_cand={}#emty dictionary
winner_count=0
winner_candidate=""


#code to read the data in the file

with open(csvpath)as election_data:
    #create a csv reader object
    csvreader = csv.reader(election_data)

    #read the head row
    header = next(csvreader)
    #read the first row
    firstdatarow= next(csvreader)

    for row in csvreader:
        # add the count of the total months
        total_vote_cast = total_vote_cast+1
        candidate_name= row[2]
        if candidate_name not in canditates_voteslist:
            #add the candidate to the list
            canditates_voteslist.append(candidate_name)
            #add value to dictionary
            totalvotes_each_cand[candidate_name]=0
        totalvotes_each_cand[candidate_name]+=1

    else:
        totalvotes_each_cand[row[2]]+=1

    for cand in totalvotes_each_cand:
        votes = totalvotes_each_cand.get(cand)


        percent_each_candidate = float(votes) / (total_vote_cast)*100.00
        if (votes>winner_count):
            winner_count=votes
            winner_candidate=cand

   # output
    output =(
    f"--------------------------\n"
    f"election results\n"
    f"--------------------------\n"
    f"total number of votes cast= {total_vote_cast }\n"
    f"--------------------------\n"
    f"candidates votes list= ${canditates_voteslist}\n"
     f"--------------------------\n"
    f"percentage of each candidate= ${ percent_each_candidate:.2f}\n"
    f"--------------------------\n"
    f"winner= {winner_candidate}\n"
    f"--------------------------\n"
    f"total number of votes each candidate won= {totalvotes_each_cand}\n"
    f"--------------------------\n")


    print (output)

    with open(output_file,"w") as txt:
         txt.write(output)
