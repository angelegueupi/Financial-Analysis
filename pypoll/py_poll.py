import csv
import os
csvpath=os.path.join("election_data.csv")
print(csvpath)

#variables
total_vote_cast = 0
canditates_voteslist=[] #empty list
percent_each_candidate=0
totalvotes_each_cand={}#emty dictionary
winner_candidate=0
votes=[]

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
        if row[2] not in canditates_voteslist:
            #add the candidate to the list
            canditates_voteslist.append(row[2])
            #add value to dictionary
            totalvotes_each_cand[row[2]]=1
        else:
            totalvotes_each_cand[row[2]]+=1
    for canditates_voteslist in totalvotes_each_cand:
        votes = canditates_voteslist.get(totalvotes_each_cand)
        print(votes)



       # percent_each_candidate = float("total_vote_cast") / (float("totalvotes_each_cand"))*100.00

    #print(percent_each_candidate)


    print("-----------------")
    print("Election Results")
    print("-----------------")
    print(total_vote_cast)
    #print("-----------------")
    #print("list of candidate who received votes")
    print(canditates_voteslist)
    print("-----------------")
    print("canditates votes list")
    print(totalvotes_each_cand)
    print("-----------------")
    print(percent_each_candidate)
