import csv

csvFile=open('login.csv')
csvFileContent=(csvFile)
next(csvFile)

DatabaseList=[]

for row in csvFileContent:

    database=row.strip().split(",")
    heading=['Username','Password']
    data=zip(heading,database)
    DataDict=dict(data)
    DatabaseList.append(DataDict)

## print(DatabaseList)

import random

def main():
    player1sum=0
    player2sum=0
    for i in range(5):
        nextroll=""
        while nextroll!='Roll':
            nextroll=input("\nPlease enter 'Roll' to roll the dice")
        if nextroll=='Roll':
            player11=random.randrange(1,7)
            player12=random.randrange(1,7)
            player21=random.randrange(1,7)
            player22=random.randrange(1,7)
    
            player1sum=player1sum+player11+player12
            player2sum=player2sum+player21+player22
 
            print("\nPlayer 1 rolled a",player11, " and a" ,player12)
            print("Player 2 rolled a",player21, " and a" ,player22)

            ## updating new sum for calculations
            roundSums=doubles(player1sum,player2sum,player11,player12,player21,player22)
            player1sum=roundSums[0]
            player2sum=roundSums[1]
            
            roundSums=oddandeven(player1sum,player2sum)
            player1sum=roundSums[0]
            player2sum=roundSums[1]
    winner(player1sum,player2sum)
     
def doubles(player1sum,player2sum,player11,player12,player21,player22):
     if player11==player12:
          player13=random.randrange(1,7)
          player1sum=player1sum+player13
          print("\nPlayer 1 rolled doubles giving them a third dice roll")
          print("Player 1 rolled an extra",player13)

     if player21==player22:
          player23=random.randrange(1,7)
          player2sum=player2sum+player23
          print("\nPlayer 2 rolled doubles giving them a third dice roll")
          print("Player 2 rolled an extra",player23)

     return player1sum, player2sum

def oddandeven(player1sum,player2sum):
     if player1sum%2==0:
          player1sum=player1sum+10
          print("\nPlayer 1's total is even giving them an extra 10 points")
     else:
          player1sum=player1sum-5
          print("\nPlayer 1's total is odd giving them 5 less points")

     if player2sum%2==0:
          player2sum=player2sum+10
          print("\nPlayer 2's total is even giving them an extra 10 points")
     else:
          player2sum=player2sum-5
          print("\nPlayer 2's total is odd giving them 5 less points")

     if player1sum<0:
          player1sum=0

     if player2sum<0:
          player2sum=0

        
     print("\nPlayer 1's total score is " ,player1sum)
     print("Player 2's total score is " ,player2sum)
     return player1sum, player2sum

def winner(player1sum,player2sum):
    if player1sum>player2sum:
          print("Player 1 wins")
    elif player1sum<player2sum:
          print("Player 2 wins")
    else:
        print("Both players draw")
    
    save=input("Please enter 'save' to save your scores to the leaderboard")
    if save=="save":
        leaderboards(player1sum,player2sum)

def login(Username,Password):
    for user in DatabaseList:
        if user['Username']==Username and user["Password"]==Password:
            print("Valid login")
            main()
            break

leaderboard=[]

def leaderboards(player1sum,player2sum):
    playermessage="Player 1, please enter your name :"
    score=player1sum
    count=0
    while count!=2:
        if count==1:
            playermessage="Player 2, please enter your name :"
            score=player2sum
        name=input(playermessage)
        leaderboarddata={'Name':name,'Score':score}
        leaderboard.append(leaderboarddata)
        count=count+1
        print(leaderboard)


    saveData()

def saveData():
    try:
        fileHandle=open('leaderboard.csv','r+')
        fileContent=fileHandle.read()
        print(fileContent)
        if fileContent.strip()=='':
            fileHandle.write('Name,Score\n')
        for item in leaderboard:
            fileHandle.write('{Name},{Score}'.format(**item))
            fileHandle.write('\n')
        fileHandle.close()
    except OSError:
        print('Can\'t write to file')



## program start
Username=input("Please enter your username")
Password=input("Please enter your password")
login(Username,Password)




newleaderboard=[]

csvFile=open('leaderboard.csv')
csvFileContent=(csvFile)

for row in csvFileContent:
    x=row.split(",")
    heading=['Name','Score']
    data=zip(heading,x)
    leaderboardDataDict=dict(data)
    newleaderboard.append(leaderboardDataDict)

##print(newleaderboard)

import operator

## prints top 5 players based on score
newleaderboard.sort(key=operator.itemgetter('Score'))

for x in range(5):
    for x in newleaderboard:
        print(x["Name"],x["Score"])

    
    
