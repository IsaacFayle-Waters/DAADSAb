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
    currentWinnersScoreMargin = tennisTools.currentWinnersScoreMargin

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
    #Total wins, TotalLosses, Win Margin-1, win margin-2
    for i in range(len(statsList)):
        for j in range(len(currentWinners)):
            #if currentWinnersScoreMargin[j] == one:
            #    oneMargin = int(statsList[i][2])
            #    statsList[i].insert(3, oneMargin + one)
            #    statsList[i].pop(4)
            if currentWinners[j] == statsList[i][0]:
                totalWins = int(statsList[i][1])
                oneMargin = int(statsList[i][3])
                twoMargin = int(statsList[i][4])
                statsList[i].insert(1, totalWins + one)
                statsList[i].pop(2)

                if currentWinnersScoreMargin[j] == one:
                    #oneMargin = int(statsList[i][2])
                    statsList[i].insert(3, oneMargin + one)
                    statsList[i].pop(4)
                elif currentWinnersScoreMargin[j] == (one + one):
                    statsList[i].insert(4, twoMargin + one)
                    statsList[i].pop(5)

            elif currentLosers[j] == statsList[i][0]:
                totalLosses = int(statsList[i][2])
                statsList[i].insert(2, totalLosses + one)
                statsList[i].pop(3)


    print('From Stats: \n')
    #temp until menu function created.
    #zero = 0
    print('Name ','Wins ','Losses ','1-set ', '2-set', '3-set', '%-Won')
    for count in range(len(statsList)):
        #print(player[0])
        threeSet = int(statsList[count][1]) - (int(statsList[count][3]) + int(statsList[count][4]))
        #(win / (win + lose)) * 100
        if statsList[count][1] == 0:
            percentage = 0
        else:
            percentage = (float(statsList[count][1]) / (float(statsList[count][1]) + float(statsList[count][2]))) * 100
        #percentage =
        print(statsList[count][0],'   ',statsList[count][1],'   ',statsList[count][2],'   ',statsList[count][3],'   ',statsList[count][4],'   ',threeSet,'   ', percentage)


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
