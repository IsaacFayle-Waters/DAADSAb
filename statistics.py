import csv
import ranking
import tennisTools
import worldSpecific


#1.Total Number of wins (Overall and by margins) for a player
def playerStatistics(gender):
    worldFile = worldSpecific.sendPath
    statsList = []
    currentWinners = tennisTools.currentWinners
    currentLosers = tennisTools.currentLosers

    #Select list depending on gender
    if gender == 'f':
        statsFile = worldFile + 'playerStates\FEMALE_PLAYER_STATS.csv'
    elif gender == 'm':
        statsFile = worldFile + 'playerStates\MALE_PLAYER_STATS.csv'
    #Copy file to list
    with open(statsFile, "r") as readStats:
        thesePlayers = csv.reader(readStats, delimiter =',', quotechar='|' )
        for players in thesePlayers:
            statsList.append(players)

    #print(statsList[1])
    #print(statsList[5])
    one = 1
    #Total wins, TotalLosses
    for i in range(len(statsList)):
        for j in range(len(currentWinners)):
            if currentWinners[j] == statsList[i][0]:
                totalWins = int(statsList[i][1])
                statsList[i].insert(1, totalWins + one)
                statsList[i].pop(2)
            elif currentLosers[j] == statsList[i][0]:
                totalLosses = int(statsList[i][2])
                statsList[i].insert(2, totalLosses + one)
                statsList[i].pop(3)

    print('From Stats: \n')
    #print(statsList)
    for player in statsList:
        print(player)


    with open(statsFile, "w", newline='') as writeStatsBack:
        writeStats = csv.writer(writeStatsBack, delimiter =',', quotechar='|')
        for players in range(len(statsList)):
            writeStats.writerow(statsList[players])



    #print(tennisTools.currentWinners)

    #name,TotalWins,TotalLosses,Total2-margin,Total1-margin,WinPercentage
##    zero = 0
##    for player in range(len(statsList)):
##        statsList[player].insert(1,zero)
##        statsList[player].insert(2,zero)
##        statsList[player].insert(3,zero)
##        statsList[player].insert(4,zero)
##
##    with open(statsFile, "w") as writeStats:
##        writeList = csv.writer(writeStats, delimiter =',', quotechar='|' )
##        for players in range(len(statsList)):
##            writeList.writerow(statsList[players])
##
##    print(statsList)

#playerStatistics('m')

#2 Win percentage

#3 Player with most winners

#4Player with most losses.
