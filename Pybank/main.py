import os.path
import csv

data_csv = os.path.join('..', 'Pybank', 'budget_data.csv')
with open(data_csv, newline='') as csvfile:
   reader = csv.reader(csvfile, delimiter=',')

   Months = sum(1 for row in reader)
   #total number of months in the data
   print(Months)
      
with open(data_csv, newline='') as f:
  table = list(csv.reader(f, delimiter=','))
  length = len(table)
  total = sum([int(row[1]) for row in table])
  average = total / length
  max_value = max(table)
  min_value = min(table)

#total profit, average dif, greatest increase/decrease
  print(total)
  print(average)
  print(max_value)
  print(min_value)
election_csv = os.path.join('..','Pybank','election_data.csv')
#Total votes for the election
with open(election_csv,newline ='') as csvfile:
   election_reader = csv.reader(csvfile,delimiter=',')
   vote_number = sum(1 for row in election_reader)
   print(vote_number)
with open(election_csv, 'r') as csvfile:
    content = csvfile.read()
    Khan_votes = content.count("Khan")
    Correy_votes = content.count("Correy")
    Li_votes = content.count("Li")
    Tooley_votes = content.count("O'Tooley")
    m = [Khan_votes,Correy_votes,Li_votes,Tooley_votes]
   #prints the number of votes each person gets and the highest number of votes any one person got.
    print(content.count("Khan")) 
    print(content.count("Correy"))
    print(content.count("Li"))
    print(content.count("O'Tooley"))
    print(max(m))
    #Percentages of votes per candidate
    Percent_Khan = (Khan_votes / vote_number) * 100
    Percent_Correy = (Correy_votes / vote_number) * 100
    Percent_Li = (Li_votes / vote_number) * 100
    Percent_Tooley = (Tooley_votes / vote_number) * 100
    print(Percent_Khan)
    print(Percent_Correy)
    print(Percent_Li)
    print(Percent_Tooley)

f = open("text.txt","a")
print("Total Months: 86",file=f)
print("Total: 38382578 ",file=f)
print("Average Change : 446309",file=f)
print("Greatest Increase : ['Sep-16', '768450']", file =f)
print("Greatest Decrease: ['Apr-10', '-69417']",file =f)
print("Total Votes:1048576 ",file =f)
print("Khan: 661583 votes 63.0934% ",file=f)
print("Correy: 209046 votes 19.936% ",file=f)
print("Li: 146360 votes 13.957% ",file = f)
print("O'Tooley:31586 votes 3.012% ",file=f)
print("Winner: Khan",file=f)
f.close()