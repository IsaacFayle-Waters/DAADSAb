import csv
#import tennisTools
#import menuFunctions
#import worldSpecific
#import resetOverallToZero
import sortLists

statsList = []
#statsList2 = []
#worldFile = worldSpecific.fileSelect(menuFunctions.createOrOpenWorld())

#print(worldFile)


##with open('worlds\Big old tiiiits\playerStates\FEMALE_PLAYER_STATS_OVERALL.csv', "r") as readStats:
##    thesePlayers = csv.reader(readStats, delimiter =',', quotechar='|' )
##    for players in thesePlayers:
##        statsList.append(players)
##        statsList2.append(players)
##
###Find max
##maxWinner = statsList[0][1]
##FUCK = statsList[0][0]
##print(FUCK)
##max = int(statsList[0][1])
##for count in range(len(statsList)):
##    if int(statsList[count][1]) > max:
##        max = int(statsList[count][1])
##        maxWinner = statsList[count]
####        if int(statsList[count][1]) == int(maxWinner[1]):
####            print(statsList[count][2], maxWinner[2])
####            if int(statsList[count][2]) < int(maxWinner[2]):
####                print('hch')
####    
##    
##        
##        
##
##print(maxWinner)
##
##
##
###Find max Looser
##maxLoser = statsList2[0][2]
##print(maxLoser)
##maxLo = int(statsList2[0][2])
##for count in range(len(statsList2)):
##    if int(statsList[count][2]) > maxLo:
##        maxLo = int(statsList2[count][2])
##        maxLoser = statsList2[count]
##
##print(maxLoser[0])
##
###print("SendPath: " + worldSpecific.sendPath)
##
##
###resetOverallToZero.wipeTempMain()
##
###print(statsList)

index = 1

with open('worlds\seedtest2\playerStates\FEMALE_PLAYER_SEED.csv', "r") as readStats:
    thesePlayers = csv.reader(readStats, delimiter =',', quotechar='|' )
    for players in thesePlayers:
        statsList.append(players)

for i in range(len(statsList)):
    print(statsList[i][index])


#sortLists.enterSorting(statsList)

#halfLength = int(len(statsList) / 2)

#for player in range(halfLength):
 #   print(player)
